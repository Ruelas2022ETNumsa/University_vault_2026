---
galaxy_body: operator
project: "Template Anki Excalidraw"
date: 2026-08-01
status: busy
---

## Handoff

**Última sesión:** 2026-08-01
**Retomar desde:** crear `tpl-Anki_excalidraw.md` en `Excalidraw/Image-Occlusions/`
**Completado esta sesión:** Script 3 (`image_occlusion_reset`) — implementado, probado y documentado. Todos los edge cases verificados.
**Próximo paso:** crear template basado en `Template.excalidraw.md` con YAML mínimo sin galaxy_body y nombre `tpl-Anki_excalidraw.md`
**Preguntas de cierre:** —

---

## Ship activo

**Ship:** Crear `tpl-Anki_excalidraw.md`
**Origen:** flujo Image Occlusion — necesidad de template base para excalidraws de oclusión
**Bloqueado por:** —

---

## Tareas

- [x] Crear `.obsidian/scripts/python/image_occlusion_reset/main.py`
- [x] Probar Caso A — carpeta nueva sin ID + carpeta vieja con ID
- [x] Probar Caso B — todas las carpetas con ID
- [x] Probar edge: Anki cerrado
- [x] Probar edge: una sola carpeta
- [x] Configurar en Shell Commands con Prompt
- [x] Documentar en `Obsidian_to_anki.md` — Parte 2
- [x] Agregar botón al ribbon via Commander (opcional — baja prioridad)
- [ ] Crear `tpl-Anki_excalidraw.md` en `Excalidraw/Image-Occlusions/` basado en `Template.excalidraw.md` con YAML mínimo sin galaxy_body

---

## Recursos

- `E:\University_vault_2026\Excalidraw\template\Template.excalidraw.md` — base para el nuevo template
- `E:\University_vault_2026\_hangar\anki\Obsidian_to_anki.md` — documentación del flujo
