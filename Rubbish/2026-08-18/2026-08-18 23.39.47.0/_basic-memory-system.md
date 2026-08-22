---
title: "Sistema Basic Memory — MCP para el vault"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
tags: [beacon, infraestructura, mcp, basic-memory, configuracion]
date_created: 2026-06-07
date_updated: 2026-06-25
status: activo
---

# Sistema Basic Memory — MCP para el vault

> Sistema Galaxy: [[_galaxy-system]]

Basic Memory es el servidor MCP que conecta este vault con Claude Desktop, dándole memoria persistente y búsqueda semántica entre sesiones. Todo vive localmente — sin cuentas externas, sin nube.

---

## Qué hace Basic Memory

| Herramienta | Función |
|-------------|---------|
| `write_note` | Crea o actualiza un archivo `.md` en el vault |
| `read_note` | Lee una nota por título o permalink |
| `search_notes` | Busca por significado semántico |
| `edit_note` | Modifica una nota existente |
| `delete_note` | Elimina una nota |
| `recent_activity` | Muestra qué cambió recientemente |

La diferencia clave con Filesystem: Basic Memory entiende el **significado** del contenido. Buscar "temas del parcial 1 de ETN806" devuelve las notas relevantes aunque esas palabras exactas no estén en el nombre del archivo.

---

## Diferencia con Filesystem MCP

| | Filesystem | Basic Memory |
|---|---|---|
| Búsqueda | Por nombre exacto | Por significado semántico |
| Memoria entre sesiones | No | Sí — indexa y recuerda |
| Acceso | Carpetas configuradas | Solo `BASIC_MEMORY_PROJECT_PATH` |
| Para qué sirve | Manipular archivos | Segundo cerebro de Claude |

Ambos conviven — Filesystem para operaciones de archivo, Basic Memory para búsqueda inteligente y memoria.

---

## Configuración instalada

**Ruta del vault indexado:** `E:\University_vault_2026`

**Archivo de configuración de Claude Desktop:**
`C:\Users\USUARIO\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json`

**Entrada en el config:**
```json
"basic-memory": {
  "command": "C:\\Users\\USUARIO\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\basic-memory.exe",
  "args": ["mcp"],
  "env": {
    "BASIC_MEMORY_PROJECT_PATH": "E:\\University_vault_2026"
  }
}
```

> **Nota:** La configuración anterior usaba `uvx.exe` de Python 3.11 para lanzar basic-memory. Fue reemplazada el 2026-06-09 por una instalación directa — ver sección de bug resuelto más abajo.

**Dependencias instaladas:**

| Herramienta | Versión | Instalación |
|-------------|---------|-------------|
| Python | 3.13.3 | python.org (reemplaza a 3.11.8 para este propósito) |
| basic-memory | 0.21.6 | `py -3.13 -m pip install basic-memory` |
| uv / uvx | 0.11.19 | instalado previamente, ya no usado para basic-memory |

> **Nota:** Claude Desktop se instala desde `claude.ai/download` pero Windows lo ejecuta desde la ruta de Microsoft Store (`Packages\Claude_pzs8sxrjxfjjc`). El config JSON debe estar en esa ruta — no en `AppData\Roaming\Claude`.

---

## Problemas encontrados en instalación (2026-06-07)

| Problema | Causa | Solución |
|----------|-------|----------|
| `pip install basic-memory` falla | Nombre incorrecto del paquete | Instalar `uv` y usar `uvx` |
| Carpeta `%APPDATA%\Claude` no existe | Claude Desktop Store usa ruta diferente | Usar `%LOCALAPPDATA%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude` |
| Error JSON "bad escaped character" | Barras `\` sin escapar en el JSON | Usar doble barra `\\` en todas las rutas |
| Basic Memory aparece como "Failed" | Config usaba `uv run` en lugar de `uvx` | Cambiar command a `uvx.exe` con args `["basic-memory", "mcp"]` |
| Antivirus bloquea escritura de Basic Memory | uvx descarga paquetes al primer uso | Dar permisos al antivirus para el vault |

---

## Escalabilidad

Basic Memory usa SQLite + embeddings vectoriales locales. No hay límite de software — el techo es RAM y disco local. Referencia real: un vault de ~17,000 archivos genera un índice SQLite de ~83 MB con búsquedas de ~23ms. Para un vault universitario que crece durante años, el rendimiento se mantiene eficiente.

---

## Flujo universitario

```
Apuntes manuscritos (foto/PDF)
        ↓
   Claude Desktop — Vision
   [transcripción a Markdown]
        ↓
   Basic Memory write_note
   [guardado en vault con YAML galaxy]
        ↓
   Próxima sesión:
   search_notes("temas parcial 1 ETN806")
        ↓
   Claude lee las notas relevantes
   y ayuda a estudiar / resumir / ejercitar
```

---

## Alternativas consideradas

| Alternativa | Por qué no se eligió |
|-------------|---------------------|
| ButlerBrain | Contenido sube a servidores externos; plan gratuito con límites no publicados |
| Filesystem solo | Sin búsqueda semántica ni memoria entre sesiones |
| Plugin Obsidian Copilot | Requiere API key de pago para modelos avanzados |

---

## Nota: múltiples cuentas de Claude (2026-06-08)

Si Basic Memory aparece como `Could not attach` al cambiar de cuenta, verificar que en `claude_desktop_config.json` todos los UUIDs de `bypassPermissionsGateByAccount` estén en `true`. Con la instalación actual (Python 3.13 + ejecutable directo) esto se configura una sola vez y no requiere pasos adicionales.

---

## Bug resuelto: Basic Memory no iniciaba automáticamente al arranque (2026-06-09)

### Síntoma
Al reiniciar la PC y abrir Claude Desktop, Basic Memory fallaba al iniciar. El workaround era correr manualmente en PowerShell:
```powershell
& "C:\Users\USUARIO\AppData\Local\Programs\Python\Python311\Scripts\uvx.exe" basic-memory mcp
```
Luego reiniciar Claude Desktop para que conectara.

### Causa raíz
`uvx` gestiona su propio Python internamente (tenía Python 3.12 interno aunque el sistema tenía 3.11). Al arranque en frío, Claude Desktop invocaba `uvx` antes de que su entorno interno estuviera inicializado → falla silenciosa. Es una condición de carrera entre Claude Desktop y el caché de `uvx`.

**Detalle importante:** basic-memory requiere Python 3.12+. El sistema solo tenía 3.11.8 y 3.6 instalados oficialmente. `uvx` funcionaba porque descargó y gestionaba su propio Python 3.12 internamente — pero ese mecanismo era frágil al arranque.

### Lo que se intentó sin éxito
- Tarea programada en Windows para precalentar `uvx` al inicio de sesión — la tarea se creaba correctamente pero `basic-memory mcp --help` no terminaba limpiamente (código de error 267014, timeout).

### Solución aplicada
Instalar Python 3.13.3 oficialmente y `basic-memory` directamente con `pip`, eliminando `uvx` del flujo:

```powershell
# 1. Instalar Python 3.13.3 desde python.org (marcar "Add to PATH")
# 2. Instalar basic-memory
py -3.13 -m pip install basic-memory
```

Actualizar `claude_desktop_config.json` para apuntar al ejecutable directo:
```json
"basic-memory": {
  "command": "C:\\Users\\USUARIO\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\basic-memory.exe",
  "args": ["mcp"],
  "env": {
    "BASIC_MEMORY_PROJECT_PATH": "E:\\University_vault_2026"
  }
}
```

Sin `uvx`, sin caché interno, sin condición de carrera. Claude Desktop invoca el ejecutable directamente y arranca sin intervención manual.

### Estado
Resuelto. Basic Memory inicia automáticamente al abrir Claude Desktop tras reinicio de PC.

---

---

## Comportamiento en Autoruns / Administrador de tareas (2026-08-18)

> [!NOTE] ✅ Comportamiento verificado — no es malware
> Al revisar las apps de inicio con **Autoruns de Sysinternals**, Claude Desktop aparece con características que pueden parecer sospechosas pero son completamente normales:
>
> - **Nombre:** `\` (barra invertida) — sin nombre visible
> - **Publisher:** `(Not Verified)` — sin firma digital de Microsoft
> - **Image Path:** `\` en vez de la ruta completa del exe
> - **No abre ubicación** al hacer clic derecho → "Abrir ubicación del archivo"
>
> **Por qué ocurre esto:** Claude Desktop se registra en el inicio de Windows con el parámetro `--startup` para arrancar minimizado. La entrada real en el registro es:
> ```
> "C:\Users\Alxnd\AppData\Local\AnthropicClaude\claude.exe" --startup
> ```
> El nombre `\` y la falta de verificación son artefactos de cómo Claude Desktop se registra — no tiene firma Authenticode de Microsoft porque es una app Electron de terceros. Es el mismo comportamiento en todas las PCs/laptops donde Claude Desktop está instalado.
>
> **El mismo proceso aparece en la laptop** con ícono de hoja blanca y sin poder abrir ubicación — mismo motivo, misma app, comportamiento idéntico.
>
> **Confirmado limpio con:** Autoruns (Sysinternals) · Malwarebytes · Windows Defender · SFC /scannow · análisis manual de rutas

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
%%
