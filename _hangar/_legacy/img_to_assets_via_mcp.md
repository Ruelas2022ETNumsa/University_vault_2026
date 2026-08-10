---
galaxy_body: ship
project: "Pegar imágenes en assets vía MCP"
date: 2026-08-10
status: aborted
fleet:
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-10
**Retomar desde:** —
**Completado esta sesión:** Investigación completa, idea descartada
**Próximo paso:** ninguno — aborted
**Preguntas de cierre:** —

---

## Resumen y objetivo

Que Claude reciba una imagen adjunta en el chat y la guarde automáticamente en `assets\` del vault usando el MCP Filesystem, sin intervención manual.

## Decisiones

| Fecha | Decisión | Motivo |
| ---------- | -------- | ------ |
| 2026-08-10 | Idea abortada | El MCP Filesystem `write_file` solo soporta texto; no puede escribir binarios (PNG, JPG) sin corromperlos |

> [!note]- Descartadas
> - **Script Python via Shell Commands (Obsidian):** Se consideró un script que moviera imágenes de una carpeta `inbox\` a `assets\`. Descartado porque Obsidian ya maneja esto nativamente (drag & drop → assets, auto-renombrado con plugin).
> - **MCP Google Drive como intermediario:** Se investigó subir la imagen a Drive con `base64_content` y luego bajarla al vault. Descartado por bug activo: el `create_file` del Drive MCP trunca payloads base64 mayores a ~10K caracteres, inutilizable para imágenes reales.

---

## Planificación

El flujo buscado era:
1. Usuario adjunta imagen en el chat
2. Claude la recibe como base64 internamente
3. Claude escribe el binario en `assets\` vía `write_file`

**Restricción que lo bloquea:** `write_file` del MCP Filesystem estándar maneja solo contenido de texto (UTF-8). Escribir base64 decodificado como binario no está soportado en la implementación actual del servidor.

---

## Sugerencias

- Existe un MCP custom (`gdrive-upload-mcp`) que separa plano de control y datos, subiendo bytes directamente por HTTP sin pasar por JSON-RPC. Requiere montar servidor propio — no viable para este caso.
- El MCP Filesystem oficial tiene soporte de *lectura* de imágenes (retorna base64), pero no escritura binaria.

---

## Flujo de pasos

No aplica — idea no ejecutada.

---

## Tareas

- [x] Investigar si `write_file` del MCP Filesystem soporta binarios
- [x] Investigar alternativa vía MCP Google Drive
- [x] Descartar idea

---

## Preguntas abiertas

—

---

## Recursos

- MCP Filesystem oficial: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- Bug Drive MCP binarios: https://github.com/anthropics/claude-code/issues/50358
