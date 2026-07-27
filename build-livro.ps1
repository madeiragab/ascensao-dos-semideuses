# Monta o livro final embutindo as capas como data URI.
#
# A página publicada precisa ser autossuficiente — nenhum arquivo externo é
# carregado. Por isso as capas entram codificadas dentro do próprio HTML, e
# por isso existe esta etapa de montagem.
#
#   livro-do-jogador.template.html  +  imagens/*.png  ->  livro-do-jogador.html
#
# Uso:  powershell -File build-livro.ps1

Add-Type -AssemblyName System.Drawing

$raiz     = Split-Path -Parent $MyInvocation.MyCommand.Path
$template = Join-Path $raiz 'livro-do-jogador.template.html'
$saida    = Join-Path $raiz 'livro-do-jogador.html'

if (-not (Test-Path $template)) { throw "Template não encontrado: $template" }

function Converter-ParaDataUri {
    param(
        [string] $Caminho,
        [int]    $LarguraMax,
        [int]    $Qualidade
    )

    $original = [System.Drawing.Image]::FromFile($Caminho)
    try {
        $escala  = [Math]::Min(1.0, $LarguraMax / $original.Width)
        $largura = [int][Math]::Round($original.Width  * $escala)
        $altura  = [int][Math]::Round($original.Height * $escala)

        $bmp = New-Object System.Drawing.Bitmap($largura, $altura)
        try {
            $g = [System.Drawing.Graphics]::FromImage($bmp)
            try {
                $g.InterpolationMode  = 'HighQualityBicubic'
                $g.SmoothingMode      = 'HighQuality'
                $g.PixelOffsetMode    = 'HighQuality'
                # As capas são opacas; fundo branco evita halo em qualquer borda.
                $g.Clear([System.Drawing.Color]::White)
                $g.DrawImage($original, 0, 0, $largura, $altura)
            } finally { $g.Dispose() }

            $codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() |
                     Where-Object { $_.MimeType -eq 'image/jpeg' }
            $params = New-Object System.Drawing.Imaging.EncoderParameters(1)
            $params.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter(
                [System.Drawing.Imaging.Encoder]::Quality, [long]$Qualidade)

            $ms = New-Object System.IO.MemoryStream
            try {
                $bmp.Save($ms, $codec, $params)
                $b64 = [Convert]::ToBase64String($ms.ToArray())
            } finally { $ms.Dispose() }

            [PSCustomObject]@{
                DataUri = "data:image/jpeg;base64,$b64"
                KB      = [Math]::Round($b64.Length / 1KB)
                Dim     = "$largura x $altura"
            }
        } finally { $bmp.Dispose() }
    } finally { $original.Dispose() }
}

# A capa é arte tonal: comprime bem. A contracapa é traço puro sobre branco,
# então precisa de qualidade maior para as linhas não sujarem.
$capa        = Converter-ParaDataUri (Join-Path $raiz 'imagens\capa.png')        1100 88
$contracapa  = Converter-ParaDataUri (Join-Path $raiz 'imagens\contracapa.png') 1100 94

Write-Output "capa ......... $($capa.Dim)  ->  $($capa.KB) KB em base64"
Write-Output "contracapa ... $($contracapa.Dim)  ->  $($contracapa.KB) KB em base64"

$html = Get-Content $template -Raw -Encoding UTF8
$html = $html.Replace('{{CAPA}}',       $capa.DataUri)
$html = $html.Replace('{{CONTRACAPA}}', $contracapa.DataUri)

if ($html -match '\{\{[A-Z]+\}\}') { throw "Sobrou um marcador não substituído no template." }

# UTF-8 sem BOM: o HTML é lido por navegador e por ferramentas.
[System.IO.File]::WriteAllText($saida, $html, (New-Object System.Text.UTF8Encoding($false)))

$kb = [Math]::Round((Get-Item $saida).Length / 1KB)
Write-Output "livro ........ $saida  ($kb KB)"
