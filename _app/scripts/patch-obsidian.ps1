# ==============================================================================
# patch-obsidian.ps1
# Patcher para el plugin Tags Routes de Obsidian
# Version: 1.0 | Compatible con Tags Routes v1.2.3+
# Uso: Ejecutar despues de actualizar el plugin en Obsidian (con Obsidian cerrado)
# ==============================================================================

$vaultRoot     = "E:\University_vault_2026"
$mainJsPath    = "$vaultRoot\.obsidian\plugins\tags-routes\main.js"
$manifestPath  = "$vaultRoot\.obsidian\plugins\tags-routes\manifest.json"
$oldDir        = "$vaultRoot\TagsRoutes"
$newDir        = "$vaultRoot\_app\TagsRoutes"
$patchLogPath  = "$newDir\patch-log.txt"

$oldPattern    = 'var programDirectory = "TagsRoutes";'
$newPattern    = 'var programDirectory = "_app/TagsRoutes";'

$oldSnapshot   = 'snapShotFolder: "graph-screenshot"'
$newSnapshot   = 'snapShotFolder: "_app/TagsRoutes/graph-screenshot"'

$dataJsonPath  = "$vaultRoot\.obsidian\plugins\tags-routes\data.json"
$dataJsonSnapshotNew = "_app/TagsRoutes/graph-screenshot"

# Colores para output
function Write-Ok    { param($msg) Write-Host "[OK]    $msg" -ForegroundColor Green }
function Write-Skip  { param($msg) Write-Host "[SKIP]  $msg" -ForegroundColor Cyan }
function Write-Warn  { param($msg) Write-Host "[WARN]  $msg" -ForegroundColor Yellow }
function Write-Fail  { param($msg) Write-Host "[ERROR] $msg" -ForegroundColor Red }
function Write-Info  { param($msg) Write-Host "[INFO]  $msg" -ForegroundColor White }

Write-Host ""
Write-Host "======================================" -ForegroundColor Magenta
Write-Host "  Tags Routes Patcher - Obsidian      " -ForegroundColor Magenta
Write-Host "======================================" -ForegroundColor Magenta
Write-Host ""

# ------------------------------------------------------------------------------
# PASO 0: Verificar que main.js existe
# ------------------------------------------------------------------------------
Write-Info "Verificando archivos del plugin..."

if (-not (Test-Path $mainJsPath)) {
    Write-Fail "No se encontro main.js en: $mainJsPath"
    Write-Fail "Verifica que el plugin este instalado correctamente."
    exit 1
}
Write-Ok "main.js encontrado."

# ------------------------------------------------------------------------------
# PASO 1: Leer version del plugin desde manifest.json
# ------------------------------------------------------------------------------
$pluginVersion = "desconocida"
if (Test-Path $manifestPath) {
    try {
        $manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
        $pluginVersion = $manifest.version
        Write-Ok "Version del plugin: $pluginVersion"
    } catch {
        Write-Warn "No se pudo leer manifest.json. Se continua sin version."
    }
} else {
    Write-Warn "manifest.json no encontrado. Se continua sin version."
}

# ------------------------------------------------------------------------------
# PASO 2: Verificar si main.js ya esta parcheado
# ------------------------------------------------------------------------------
Write-Info "Verificando estado del parche en main.js..."

$content = Get-Content $mainJsPath -Raw -Encoding UTF8

if ($content -notmatch [regex]::Escape($oldPattern)) {
    if ($content -match [regex]::Escape($newPattern)) {
        Write-Skip "main.js ya esta parcheado con '_app/TagsRoutes'. No se requiere accion."
    } else {
        Write-Fail "No se encontro el patron esperado en main.js."
        Write-Fail "El plugin puede haber cambiado su estructura interna."
        Write-Fail "Revisa manualmente: $mainJsPath"
        exit 1
    }
} else {
    # Aplicar el parche de programDirectory
    Write-Info "Aplicando parche en main.js..."
    $patched = $content -replace [regex]::Escape($oldPattern), $newPattern
    Set-Content -Path $mainJsPath -Value $patched -Encoding UTF8 -NoNewline
    Write-Ok "main.js parcheado (programDirectory)."
}

# Parche secundario: snapshotDirectory en main.js
Write-Info "Verificando parche de snapshotDirectory en main.js..."
$content = Get-Content $mainJsPath -Raw -Encoding UTF8

if ($content -notmatch [regex]::Escape($oldSnapshot)) {
    if ($content -match [regex]::Escape($newSnapshot)) {
        Write-Skip "snapshotDirectory ya esta parcheado."
    } else {
        Write-Warn "No se encontro el patron de snapshotDirectory. Puede haber cambiado en una actualizacion."
    }
} else {
    $patched = $content -replace [regex]::Escape($oldSnapshot), $newSnapshot
    Set-Content -Path $mainJsPath -Value $patched -Encoding UTF8 -NoNewline
    Write-Ok "main.js parcheado (snapshotDirectory)."
}

# ------------------------------------------------------------------------------
# PASO 2b: Parchear snapShotFolder en data.json
# ------------------------------------------------------------------------------
Write-Info "Verificando snapShotFolder en data.json..."

if (-not (Test-Path $dataJsonPath)) {
    Write-Warn "data.json no encontrado. Se omite este parche."
} else {
    try {
        $dataRaw  = Get-Content $dataJsonPath -Raw -Encoding UTF8
        $dataJson = $dataRaw | ConvertFrom-Json

        if ($null -eq $dataJson.snapShotFolder) {
            Write-Warn "Campo 'snapShotFolder' no existe en data.json. Se omite."
        } elseif ($dataJson.snapShotFolder -eq $dataJsonSnapshotNew) {
            Write-Skip "snapShotFolder ya apunta a '$dataJsonSnapshotNew'."
        } else {
            $old = $dataJson.snapShotFolder
            $dataJson.snapShotFolder = $dataJsonSnapshotNew
            $dataJson | ConvertTo-Json -Depth 10 | Set-Content -Path $dataJsonPath -Encoding UTF8
            Write-Ok "data.json parcheado: '$old' -> '$dataJsonSnapshotNew'"
        }
    } catch {
        Write-Warn "Error al procesar data.json: $_"
    }
}

# ------------------------------------------------------------------------------
# PASO 3: Crear carpeta destino _app/TagsRoutes si no existe
# ------------------------------------------------------------------------------
Write-Info "Verificando carpeta destino..."

if (-not (Test-Path $newDir)) {
    New-Item -ItemType Directory -Path $newDir -Force | Out-Null
    Write-Ok "Carpeta creada: $newDir"
} else {
    Write-Skip "Carpeta destino ya existe: $newDir"
}

# ------------------------------------------------------------------------------
# PASO 4: Migrar contenido desde TagsRoutes/ raiz (solo si existe)
# ------------------------------------------------------------------------------
Write-Info "Verificando carpeta vieja en raiz del vault..."

if (Test-Path $oldDir) {
    Write-Info "Migrando contenido desde $oldDir hacia $newDir ..."
    
    $items = Get-ChildItem -Path $oldDir -Recurse -Force
    
    if ($items.Count -eq 0) {
        Write-Skip "La carpeta vieja existe pero esta vacia."
        Remove-Item -Path $oldDir -Recurse -Force
        Write-Ok "Carpeta vieja eliminada (estaba vacia): $oldDir"
    } else {
        # Primero crear todas las subcarpetas en destino
        $items | Where-Object { $_.PSIsContainer } | ForEach-Object {
            $relativePath = $_.FullName.Substring($oldDir.Length)
            $targetPath   = "$newDir$relativePath"
            if (-not (Test-Path $targetPath)) {
                New-Item -ItemType Directory -Path $targetPath -Force | Out-Null
            }
        }

        # Mover archivos (no copiar) — el original desaparece automaticamente
        $items | Where-Object { -not $_.PSIsContainer } | ForEach-Object {
            $relativePath = $_.FullName.Substring($oldDir.Length)
            $targetPath   = "$newDir$relativePath"
            $targetDir    = Split-Path $targetPath -Parent
            if (-not (Test-Path $targetDir)) {
                New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
            }
            Move-Item -Path $_.FullName -Destination $targetPath -Force
            Write-Ok "Movido: $relativePath"
        }

        # Con los archivos ya movidos, eliminar la carpeta vieja completa
        Remove-Item -Path $oldDir -Recurse -Force
        Write-Ok "Carpeta vieja eliminada: $oldDir"
    }

} else {
    Write-Skip "No existe carpeta 'TagsRoutes' en la raiz. Nada que migrar."
}

# ------------------------------------------------------------------------------
# PASO 5: Escribir log del parche
# ------------------------------------------------------------------------------
Write-Info "Registrando parche en log..."

$timestamp  = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$logEntry   = "[$timestamp] Parche aplicado | Plugin version: $pluginVersion | main.js: $mainJsPath"

try {
    Add-Content -Path $patchLogPath -Value $logEntry -Encoding UTF8
    Write-Ok "Log actualizado: $patchLogPath"
} catch {
    Write-Warn "No se pudo escribir el log: $_"
}

# ------------------------------------------------------------------------------
# FIN
# ------------------------------------------------------------------------------
Write-Host ""
Write-Host "======================================" -ForegroundColor Magenta
Write-Ok "Parche completado exitosamente."
Write-Host "Puedes abrir Obsidian ahora." -ForegroundColor White
Write-Host "======================================" -ForegroundColor Magenta
Write-Host ""