---
title: "Sistema Basic Memory — MCP para el vault"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
tags: [beacon, infraestructura, mcp, basic-memory, configuracion]
date_created: 2026-06-07
date_updated: 2026-06-07
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
  "command": "C:\\Users\\USUARIO\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\uvx.exe",
  "args": ["basic-memory", "mcp"],
  "env": {
    "BASIC_MEMORY_PROJECT_PATH": "E:\\University_vault_2026"
  }
}
```

**Dependencias instaladas:**

| Herramienta | Versión | Instalación |
|-------------|---------|-------------|
| Python | 3.11.8 | python.org |
| uv / uvx | 0.11.19 | `pip install uv` |
| basic-memory | 3.3.1 | descargado por `uvx` automáticamente |
| fastmcp | 3.3.1 | dependencia de basic-memory |

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

%%
galaxy-links
[[_galaxy-system]]
%%
