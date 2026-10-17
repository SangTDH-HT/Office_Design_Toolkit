<#
.SYNOPSIS
  Cai skill cua repo Office_Design_Toolkit vao ~/.claude/skills (Claude Code, Windows).

.DESCRIPTION
  - skills\*                      -> ~/.claude/skills\<ten>  (bo qua skill da co, tru khi -Force)
  - vendor\ui-ux-pro-max-skill    -> ~/.claude/skills\ui-ux-pro-max, doi ${CLAUDE_PLUGIN_ROOT} sang duong dan that
  - -WithUupmExtras               -> them banner-design, brand, design, design-system, slides, ui-styling
  Ban cu bi ghi de duoc sao luu vao ~/.claude/skills-backup\<ngay-gio>\ (ngoai thu muc skills).
  frontend-design va ppt-master cai bang lenh /plugin (in ra o cuoi).

.EXAMPLE
  .\scripts\install.ps1 -WhatIf
  .\scripts\install.ps1
  .\scripts\install.ps1 -Force -WithUupmExtras
#>
[CmdletBinding()]
param(
    [switch]$Force,
    [switch]$WithUupmExtras,
    [switch]$WhatIf
)
$ErrorActionPreference = 'Stop'
$Repo = Split-Path -Parent $PSScriptRoot
$Dest = Join-Path $env:USERPROFILE '.claude\skills'
$Backup = Join-Path $env:USERPROFILE ('.claude\skills-backup\' + (Get-Date -Format 'yyyyMMdd-HHmm'))
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Install-Skill([string]$Source, [string]$Name) {
    $target = Join-Path $Dest $Name
    if (Test-Path $target) {
        if (-not $Force) { Write-Host ("  bo qua  {0} (da co, dung -Force de ghi de)" -f $Name); return $false }
        if ($WhatIf) { Write-Host ("  ghi de  {0} (sao luu -> {1})" -f $Name, $Backup); return $true }
        New-Item -ItemType Directory -Force -Path $Backup | Out-Null
        Move-Item -Path $target -Destination (Join-Path $Backup $Name)
    }
    if ($WhatIf) { Write-Host ("  cai     {0}" -f $Name); return $true }
    Copy-Item -Path $Source -Destination $target -Recurse
    Get-ChildItem -Path $target -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force
    Write-Host ("  da cai  {0}" -f $Name)
    return $true
}

Write-Host ("Dich: {0}" -f $Dest)
New-Item -ItemType Directory -Force -Path $Dest | Out-Null

Write-Host 'Skill cua Sang:'
Get-ChildItem -Path (Join-Path $Repo 'skills') -Directory | ForEach-Object {
    [void](Install-Skill $_.FullName $_.Name)
}

Write-Host 'ui-ux-pro-max (MIT, nextlevelbuilder):'
$uupm = Join-Path $Repo 'vendor\ui-ux-pro-max-skill\skills'
if (Install-Skill (Join-Path $uupm 'ui-ux-pro-max') 'ui-ux-pro-max') {
    if (-not $WhatIf) {
        $skillMd = Join-Path $Dest 'ui-ux-pro-max\SKILL.md'
        $abs = ($Dest -replace '\\', '/') + '/ui-ux-pro-max/'
        $text = [IO.File]::ReadAllText($skillMd, [Text.Encoding]::UTF8)
        $count = ([regex]::Matches($text, [regex]::Escape('${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/'))).Count
        $text = $text.Replace('${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max/', $abs)
        [IO.File]::WriteAllText($skillMd, $text, $Utf8NoBom)
        Write-Host ("  doi {0} duong dan script -> {1}" -f $count, $abs)
    }
}
if ($WithUupmExtras) {
    foreach ($n in 'banner-design', 'brand', 'design', 'design-system', 'slides', 'ui-styling') {
        [void](Install-Skill (Join-Path $uupm $n) $n)
    }
}

Write-Host ''
Write-Host 'Plugin - go trong Claude Code:'
Write-Host '  /plugin install frontend-design@claude-plugins-official'
Write-Host '  /plugin marketplace add hugohe3/ppt-master'
Write-Host '  /plugin install ppt-master@ppt-master'
Write-Host 'MCP Illustrator / Photoshop: xem mcp\README.md'
Write-Host 'Skill docx / xlsx / pptx / pdf: co san trong Claude (Anthropic), khong cai tu repo.'
