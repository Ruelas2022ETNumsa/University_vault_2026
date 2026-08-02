---
galaxy_body: operator
project: "Template Anki Excalidraw"
date: 2026-08-01
status: busy
---

## Handoff

**Última sesión:** 2026-08-01
**Retomar desde:** pendiente de prueba de tag en Anki tras último ajuste
**Completado esta sesión:** `tpl-Anki_excalidraw.md` creado — template base excalidraw de oclusión con prompt de nombre. Script `Image Occlusion.md` editado — pregunta deck y tag al generar cartas. Template `tpl-excalidraw_occlusion.md` actualizado con línea `FILE TAGS`. Script `image_occlusion_reset` actualizado con ruta `Excalidraw/Image-Occlusions`.
**Próximo paso:** verificar que el tag llegue correctamente a Anki. Evaluar lógica de borrado para 1 sola carpeta en `image_occlusion_reset`.
**Preguntas de cierre:** —

---

## Ship activo

**Ship:** Verificar tag en Anki + evaluar borrado de carpeta única en `image_occlusion_reset`
**Origen:** flujo Image Occlusion — ajustes post-implementación
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
- [x] Crear `tpl-Anki_excalidraw.md` en `_templates/` con prompt de nombre y carpeta destino
- [x] Editar script `Image Occlusion.md` — agregar prompt de deck y tag al generar cartas
- [x] Editar `tpl-excalidraw_occlusion.md` — agregar línea `FILE TAGS`
- [ ] Verificar que el tag llegue correctamente a Anki
- [ ] Evaluar e implementar borrado de carpeta única en `image_occlusion_reset` (con prompt de confirmación)

---

## Recursos

- `E:\University_vault_2026\Excalidraw\template\Template.excalidraw.md` — base para el nuevo template
- `E:\University_vault_2026\_hangar\anki\Obsidian_to_anki.md` — documentación del flujo
