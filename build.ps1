# Monta os três livros do sistema.
#
#   template/*.html  +  template/livro.css  +  bestiario/*.md  +  imagens/*.png
#       ->  livro-do-jogador.html  ·  bestiario.html  ·  grimorio.html
#
# As páginas precisam ser autossuficientes: nenhum arquivo externo é carregado,
# então as capas entram codificadas dentro do próprio HTML. Este script prepara
# as capas em .build/*.b64 e depois chama build_livros.py, que faz a montagem e
# a conversão dos markdown.
#
# Uso:  powershell -ExecutionPolicy Bypass -File build.ps1

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$raiz  = Split-Path -Parent $MyInvocation.MyCommand.Path
$build = Join-Path $raiz '.build'
New-Item -ItemType Directory -Force -Path $build | Out-Null

function Converter-Capa {
    param(
        [string] $Arquivo,      # nome do PNG em imagens/
        [string] $Saida,        # nome do .b64 em .build/
        [int]    $LarguraMax = 1100,
        [int]    $Qualidade  = 88
    )

    $caminho = Join-Path $raiz "imagens\$Arquivo"
    if (-not (Test-Path $caminho)) { throw "Capa não encontrada: $caminho" }

    $original = [System.Drawing.Image]::FromFile($caminho)
    try {
        $escala  = [Math]::Min(1.0, $LarguraMax / $original.Width)
        $largura = [int][Math]::Round($original.Width  * $escala)
        $altura  = [int][Math]::Round($original.Height * $escala)

        $bmp = New-Object System.Drawing.Bitmap($largura, $altura)
        try {
            $g = [System.Drawing.Graphics]::FromImage($bmp)
            try {
                $g.InterpolationMode = 'HighQualityBicubic'
                $g.SmoothingMode     = 'HighQuality'
                $g.PixelOffsetMode   = 'HighQuality'
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

            $destino = Join-Path $build "$Saida.b64"
            [System.IO.File]::WriteAllText($destino, "data:image/jpeg;base64,$b64",
                (New-Object System.Text.ASCIIEncoding))

            $kb = [Math]::Round($b64.Length / 1KB)
            Write-Output ("  {0,-22} {1,4} x {2,-5} -> {3,4} KB" -f $Arquivo, $largura, $altura, $kb)
        } finally { $bmp.Dispose() }
    } finally { $original.Dispose() }
}

function Gerar-Miniatura {
    param([string] $Arquivo, [string] $Saida, [int] $Largura = 520, [int] $Qualidade = 80)

    $original = [System.Drawing.Image]::FromFile((Join-Path $raiz "imagens\$Arquivo"))
    try {
        $escala = [Math]::Min(1.0, $Largura / $original.Width)
        $w = [int][Math]::Round($original.Width * $escala)
        $h = [int][Math]::Round($original.Height * $escala)
        $bmp = New-Object System.Drawing.Bitmap($w, $h)
        try {
            $g = [System.Drawing.Graphics]::FromImage($bmp)
            try {
                $g.InterpolationMode = 'HighQualityBicubic'
                $g.SmoothingMode     = 'HighQuality'
                $g.PixelOffsetMode   = 'HighQuality'
                $g.Clear([System.Drawing.Color]::White)
                $g.DrawImage($original, 0, 0, $w, $h)
            } finally { $g.Dispose() }

            $codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() |
                     Where-Object { $_.MimeType -eq 'image/jpeg' }
            $params = New-Object System.Drawing.Imaging.EncoderParameters(1)
            $params.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter(
                [System.Drawing.Imaging.Encoder]::Quality, [long]$Qualidade)

            $destino = Join-Path $raiz "imagens\$Saida"
            $bmp.Save($destino, $codec, $params)
            $kb = [Math]::Round((Get-Item $destino).Length / 1KB)
            Write-Output ("  {0,-22} {1,4} x {2,-5} -> {3,4} KB" -f $Saida, $w, $h, $kb)
        } finally { $bmp.Dispose() }
    } finally { $original.Dispose() }
}

Write-Output 'preparando capas para embutir:'
# Arte tonal comprime bem. Traço puro sobre branco precisa de qualidade maior
# para as linhas não sujarem. A capa do Grimório é a mais detalhada de todas, e
# por isso vai mais estreita — a 1100 px ela sozinha passava de 900 KB.
Converter-Capa -Arquivo 'capa.png'            -Saida 'capa'            -Qualidade 88
Converter-Capa -Arquivo 'contracapa.png'      -Saida 'contracapa'      -Qualidade 94
Converter-Capa -Arquivo 'capa-bestiario.png'  -Saida 'capa-bestiario'  -Qualidade 86
Converter-Capa -Arquivo 'capa-grimorio.png'   -Saida 'capa-grimorio' `
               -LarguraMax 950 -Qualidade 82

Write-Output ''
Write-Output 'gerando miniaturas para a estante do site:'
# O index.html não pode carregar os PNG originais: são 10 MB somados.
Gerar-Miniatura -Arquivo 'capa.png'           -Saida 'thumb-jogador.jpg'
Gerar-Miniatura -Arquivo 'capa-bestiario.png' -Saida 'thumb-bestiario.jpg'
Gerar-Miniatura -Arquivo 'capa-grimorio.png'  -Saida 'thumb-grimorio.jpg'

Write-Output ''
& python (Join-Path $raiz 'build_livros.py')
if ($LASTEXITCODE -ne 0) { throw "build_livros.py falhou com código $LASTEXITCODE" }
