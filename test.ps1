# Executa toda a regressão numérica do sistema sem dependências externas.
# Uso: powershell -ExecutionPolicy Bypass -File test.ps1

param([string] $Only = '')

$ErrorActionPreference = 'Stop'
$raiz = Split-Path -Parent $MyInvocation.MyCommand.Path
$testes = @(
    'defesas_passivas.py',
    'graus.py',
    'anteparo.py',
    'comparar.py',
    'dia_de_aventura.py',
    'kleos.py',
    'habilidades.py',
    'condicoes.py',
    'equilibrio.py',
    'tecnicas.py',
    'calibrar_kleos.py',
    'forja.py',
    'criaturas.py',
    'completo.py',
    'nevoa.py'
)

Write-Output 'regressão numérica:'
foreach ($teste in $testes) {
    if ($Only -and $teste -ne $Only) { continue }
    Write-Output ("  ... {0}" -f $teste)
    $caminho = Join-Path $raiz "sim\$teste"
    $saida = & python $caminho 2>&1
    if ($LASTEXITCODE -ne 0) {
        $saida | Write-Output
        throw "$teste falhou com código $LASTEXITCODE"
    }
    Write-Output ("  OK  {0}" -f $teste)
}

Write-Output 'todos os testes passaram'
