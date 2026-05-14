# ==============================================================================
# patch-obsidian.ps1
# Patcher para el plugin Tags Routes de Obsidian
# Version: 2.0 | Compatible con Tags Routes v1.2.3+
# Uso: Ejecutar despues de actualizar el plugin en Obsidian (con Obsidian cerrado)
# ==============================================================================

$vaultRoot     = "E:\University_vault_2026"
$mainJsPath    = "$vaultRoot\.obsidian\plugins\tags-routes\main.js"
$manifestPath  = "$vaultRoot\.obsidian\plugins\tags-routes\manifest.json"
$dataJsonPath  = "$vaultRoot\.obsidian\plugins\tags-routes\data.json"
$oldDir        = "$vaultRoot\TagsRoutes"
$newDir        = "$vaultRoot\_app\TagsRoutes"
$patchLogPath  = "$newDir\patch-log.txt"

$oldPattern          = 'var programDirectory = "TagsRoutes";'
$newPattern          = 'var programDirectory = "_app/TagsRoutes";'
$oldSnapshot         = 'snapShotFolder: "graph-screenshot"'
$newSnapshot         = 'snapShotFolder: "_app/TagsRoutes/graph-screenshot"'
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

# Variables de resumen para el log final
$logNotes = @()

# ------------------------------------------------------------------------------
# PASO 0: Verificar que Obsidian este cerrado
# ------------------------------------------------------------------------------
Write-Info "Verificando que Obsidian este cerrado..."

$obsidianProcess = Get-Process Obsidian -ErrorAction SilentlyContinue
if ($obsidianProcess) {
    Write-Fail "Obsidian esta abierto. Cierra Obsidian antes de ejecutar el patcher."
    exit 1
}
Write-Ok "Obsidian no esta en ejecucion."

# ------------------------------------------------------------------------------
# PASO 1: Verificar que main.js existe
# ------------------------------------------------------------------------------
Write-Info "Verificando archivos del plugin..."

if (-not (Test-Path $mainJsPath)) {
    Write-Fail "No se encontro main.js en: $mainJsPath"
    Write-Fail "Verifica que el plugin este instalado correctamente."
    exit 1
}
Write-Ok "main.js encontrado."

# ------------------------------------------------------------------------------
# PASO 2: Leer version del plugin desde manifest.json
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
# PASO 3: Backup versionado de main.js
# ------------------------------------------------------------------------------
Write-Info "Creando backup de main.js..."

$backupPath = "$mainJsPath.$pluginVersion.bak"
if (Test-Path $backupPath) {
    Write-Skip "Backup ya existe para v$pluginVersion : $(Split-Path $backupPath -Leaf)"
} else {
    try {
        Copy-Item $mainJsPath $backupPath -Force
        Write-Ok "Backup creado: $(Split-Path $backupPath -Leaf)"
        $logNotes += "Backup: $(Split-Path $backupPath -Leaf)"
    } catch {
        Write-Warn "No se pudo crear el backup: $_"
    }
}

# ------------------------------------------------------------------------------
# PASO 4: Parchear programDirectory en main.js
# ------------------------------------------------------------------------------
Write-Info "Verificando parche de programDirectory en main.js..."

$content = Get-Content $mainJsPath -Raw -Encoding UTF8

if ($content -notmatch [regex]::Escape($oldPattern)) {
    if ($content -match [regex]::Escape($newPattern)) {
        Write-Skip "programDirectory ya esta parcheado."
        $logNotes += "programDirectory: ya parcheado"
    } else {
        Write-Fail "No se encontro el patron de programDirectory en main.js."
        Write-Fail "El plugin puede haber cambiado su estructura interna en v$pluginVersion."
        Write-Fail "Revisa manualmente: $mainJsPath"
        exit 1
    }
} else {
    $content = $content -replace [regex]::Escape($oldPattern), $newPattern
    Set-Content -Path $mainJsPath -Value $content -Encoding UTF8
    Write-Ok "main.js parcheado (programDirectory)."
    $logNotes += "programDirectory: parcheado"
}

# ------------------------------------------------------------------------------
# PASO 5: Parchear snapShotFolder (defaults) en main.js
# ------------------------------------------------------------------------------
Write-Info "Verificando parche de snapShotFolder en main.js..."

$content = Get-Content $mainJsPath -Raw -Encoding UTF8

if ($content -notmatch [regex]::Escape($oldSnapshot)) {
    if ($content -match [regex]::Escape($newSnapshot)) {
        Write-Skip "snapShotFolder ya esta parcheado."
        $logNotes += "snapShotFolder (main.js): ya parcheado"
    } else {
        Write-Warn "No se encontro el patron de snapShotFolder en main.js."
        Write-Warn "El campo puede haberse renombrado en v$pluginVersion. Revisa manualmente."
        $logNotes += "snapShotFolder (main.js): patron no encontrado - revision manual requerida"
    }
} else {
    $content = $content -replace [regex]::Escape($oldSnapshot), $newSnapshot
    Set-Content -Path $mainJsPath -Value $content -Encoding UTF8
    Write-Ok "main.js parcheado (snapShotFolder)."
    $logNotes += "snapShotFolder (main.js): parcheado"
}

# ------------------------------------------------------------------------------
# PASO 6: Parchear snapShotFolder en data.json
# ------------------------------------------------------------------------------
Write-Info "Verificando snapShotFolder en data.json..."

if (-not (Test-Path $dataJsonPath)) {
    Write-Warn "data.json no encontrado. Se omite este parche."
    $logNotes += "snapShotFolder (data.json): archivo no encontrado"
} else {
    try {
        $dataJson = Get-Content $dataJsonPath -Raw -Encoding UTF8 | ConvertFrom-Json

        if ($null -eq $dataJson.snapShotFolder) {
            Write-Warn "Campo 'snapShotFolder' no existe en data.json. Se omite."
            $logNotes += "snapShotFolder (data.json): campo no existe"
        } elseif ($dataJson.snapShotFolder -eq $dataJsonSnapshotNew) {
            Write-Skip "snapShotFolder en data.json ya es correcto."
            $logNotes += "snapShotFolder (data.json): ya parcheado"
        } else {
            $old = $dataJson.snapShotFolder
            $dataJson.snapShotFolder = $dataJsonSnapshotNew
            $dataJson | ConvertTo-Json -Depth 10 | Set-Content -Path $dataJsonPath -Encoding UTF8
            Write-Ok "data.json parcheado: '$old' -> '$dataJsonSnapshotNew'"
            $logNotes += "snapShotFolder (data.json): '$old' -> '$dataJsonSnapshotNew'"
        }
    } catch {
        Write-Warn "Error al procesar data.json: $_"
        $logNotes += "snapShotFolder (data.json): error - $_"
    }
}

# ------------------------------------------------------------------------------
# PASO 7: Crear carpeta destino _app/TagsRoutes si no existe
# ------------------------------------------------------------------------------
Write-Info "Verificando carpeta destino..."

if (-not (Test-Path $newDir)) {
    New-Item -ItemType Directory -Path $newDir -Force | Out-Null
    Write-Ok "Carpeta creada: $newDir"
} else {
    Write-Skip "Carpeta destino ya existe: $newDir"
}

# ------------------------------------------------------------------------------
# PASO 8: Migrar contenido desde TagsRoutes/ raiz (solo si existe)
# ------------------------------------------------------------------------------
Write-Info "Verificando carpeta vieja en raiz del vault..."

$migratedCount = 0

if (Test-Path $oldDir) {
    Write-Info "Migrando contenido desde $oldDir hacia $newDir ..."

    $items = Get-ChildItem -Path $oldDir -Recurse -Force

    if ($items.Count -eq 0) {
        Write-Skip "La carpeta vieja existe pero esta vacia."
        Remove-Item -Path $oldDir -Recurse -Force
        Write-Ok "Carpeta vieja eliminada (estaba vacia): $oldDir"
    } else {
        # Crear subcarpetas en destino
        $items | Where-Object { $_.PSIsContainer } | ForEach-Object {
            $relativePath = $_.FullName.Substring($oldDir.Length)
            $targetPath   = "$newDir$relativePath"
            if (-not (Test-Path $targetPath)) {
                New-Item -ItemType Directory -Path $targetPath -Force | Out-Null
            }
        }

        # Mover archivos
        $items | Where-Object { -not $_.PSIsContainer } | ForEach-Object {
            $relativePath = $_.FullName.Substring($oldDir.Length)
            $targetPath   = "$newDir$relativePath"
            $targetDir    = Split-Path $targetPath -Parent
            if (-not (Test-Path $targetDir)) {
                New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
            }
            Move-Item -Path $_.FullName -Destination $targetPath -Force
            Write-Ok "Movido: $relativePath"
            $migratedCount++
        }

        Remove-Item -Path $oldDir -Recurse -Force
        Write-Ok "Carpeta vieja eliminada: $oldDir"
    }

    $logNotes += "Migracion: $migratedCount archivos movidos desde TagsRoutes/"

} else {
    Write-Skip "No existe carpeta 'TagsRoutes' en la raiz. Nada que migrar."
    $logNotes += "Migracion: no requerida"
}

# ------------------------------------------------------------------------------
# PASO 9: Escribir log del parche
# ------------------------------------------------------------------------------
Write-Info "Registrando parche en log..."

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$logLines  = @("[$timestamp] Plugin v$pluginVersion") `
           + ($logNotes | ForEach-Object { "  - $_" }) `
           + @("")

try {
    Add-Content -Path $patchLogPath -Value ($logLines -join "`n") -Encoding UTF8
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