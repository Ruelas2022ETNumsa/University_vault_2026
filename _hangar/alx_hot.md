---
galaxy_body: operator
project: "Template Anki Excalidraw"
date: 2026-08-01
status: busy
---

## Handoff

**Última sesión:** 2026-08-01
**Retomar desde:** rediseño completo de `image_occlusion_reset/main.py`
**Completado esta sesión:** `tpl-Anki_excalidraw.md` creado. Script `Image Occlusion.md` parcheado con prompts de deck y tag. Template `tpl-excalidraw_occlusion.md` actualizado con línea `FILE TAGS`. Flujo completo de Image Occlusion diseñado y documentado. Rediseño de `main.py` especificado y listo para implementar.
**Próximo paso:** implementar rediseño de `main.py` (ver worker abajo) + reconfigurar Shell Commands con nuevo argumento de acción.
**Preguntas de cierre:** —

---

## Ship activo

**Ship:** Rediseño `image_occlusion_reset/main.py` — acciones B/S/Z
**Origen:** flujo Image Occlusion — necesidad de borrar, archivar y restaurar tarjetas desde Obsidian
**Bloqueado por:** —

---

## Worker — `main.py` rediseño

**Existe `.bk` en:** `E:\University_vault_2026\.obsidian\scripts\python\image_occlusion_reset\main.py.bk`

**Nuevo argumento:** `sys.argv[3]` — acción ingresada via prompt de Shell Commands.

**Prompt Shell Commands a agregar:** `{{prompt:Acción — B=Borrar, S=Legacy, Z=Revisar, otro=Cancelar}}`

**Lógica por acción (acepta mayúsculas y minúsculas):**

`B/b` — Borrar todo sin distinción de cantidad de carpetas ni IDs:
- Borra notas de Anki via AnkiConnect
- Borra carpeta(s) `nombre__timestamp` del vault
- Mensaje: `"Tarjetas de 'nombre' eliminadas de Anki y vault"`

`S/s` — Legacy:
- Mueve carpeta(s) `nombre__timestamp` → `Excalidraw/Image-Occlusions/_legacy/nombre/`
- Busca `.excalidraw.md` en `Excalidraw/Image-Occlusions/` primero, fallback `Excalidraw/`
- Mueve `.excalidraw.md` → `Excalidraw/Image-Occlusions/_legacy/nombre/`
- No toca Anki
- Estructura resultante: `_legacy/nombre/nombre__timestamp/` + `_legacy/nombre/nombre.excalidraw.md`
- Mensaje: `"'nombre' archivado en legacy"`

`Z/z` — Revisar (ctrl+z de legacy):
- Verifica que exista `_legacy/nombre/` — si no existe: `"Archivo no encontrado"` + exit
- Mueve todo el contenido de `_legacy/nombre/` → `Excalidraw/Image-Occlusions/`
- Mensaje: `"'nombre' restaurado para revisión"`

otro — Cancelar:
- Sin cambios
- Mensaje: `"Operación cancelada"` + exit 0

**Eliminar:** bloqueo actual `if len(carpetas) == 1: sys.exit(0)`

**Reconfigurar Shell Commands:** agregar tercer argumento con el prompt de acción al comando existente.

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
- [ ] Implementar rediseño `main.py` — acciones B/S/Z (ver worker arriba)
- [ ] Reconfigurar Shell Commands — agregar tercer argumento de acción
- [ ] Verificar que el tag llegue correctamente a Anki

---

## Recursos

- `E:\University_vault_2026\Excalidraw\template\Template.excalidraw.md` — base para el nuevo template
- `E:\University_vault_2026\_hangar\anki\Obsidian_to_anki.md` — documentación del flujo
