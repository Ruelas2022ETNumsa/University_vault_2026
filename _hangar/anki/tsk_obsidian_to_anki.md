---
galaxy_body: ship
project: "Obsidian to Anki — documentacion y pruebas completas"
date: 2026-08-02
status: in-orbit
fleet: anki
---

## Handoff

**Ultima sesion:** 2026-08-02
**Retomar desde:** Opcion A (Cornell Marginalia) y Opcion C (Image Occlusion) — documentar y probar flujos restantes
**Completado esta sesion:** Opcion C — `occlusion_actions/main.py` completo y probado (B/S/Z). Documentacion `shellcmd_occlusion_actions.md` creada. Script `image_occlusion_reset` marcado como legacy.
**Proximo paso:** Revisar y documentar Opcion A (latex_to_mathjax + Cornell Marginalia). Luego Opcion C restante (Flashcards — no activado aun).
**Preguntas de cierre:** —

---

## Resumen y objetivo

Documentar, probar y dejar operativas las tres opciones de exportacion Obsidian -> Anki (A, B, C). La Opcion B (Obsidian_to_Anki plugin directo) ya esta operativa y documentada. Opciones A y C requieren revision y pruebas completas.

---

## Decisiones

| Fecha | Decision | Motivo |
| ----- | -------- | ------ |
| 2026-08-02 | `occlusion_actions/main.py` reemplaza `image_occlusion_reset/main.py` | Script nuevo mas flexible — acciones B/S/Z en lugar de logica de conservar carpeta mas reciente |
| 2026-08-02 | Template crea archivos `.md` en lugar de `.excalidraw` | `{{title}}` devuelve nombre limpio sin extension — evita problemas en legacy y busqueda de archivo fuente |
| 2026-08-02 | Accion S bloquea si ninguna carpeta fue exportada a Anki | Legacy solo tiene sentido con cartas que ya existen en Anki |

> [!note]- Descartadas
> Template con extension `.excalidraw` — descartado porque `{{title}}` devuelve `nombre.excalidraw` con extension incluida, rompiendo el flujo del script.

---

## Planificacion

Tres opciones de exportacion Obsidian -> Anki, cada una con su flujo y herramientas propias:

- **Opcion A** — Cornell Marginalia + latex_to_mathjax: marginalia en archivos `.md` con formulas LaTeX
- **Opcion B** — Obsidian_to_Anki plugin directo: exportacion directa desde notas `.md`
- **Opcion C** — Excalidraw Image Occlusion: cartas visuales desde excalidraws

Restriccion: plugin Flashcards no activado — probar con precaucion cuando se active por posibles conflictos con Image Occlusion.

---

## Flujo de pasos

1. Revisar y probar Opcion A completa (latex_to_mathjax + Cornell Marginalia)
2. Documentar Opcion A si no esta documentada
3. Revisar Opcion C — Flashcards (activar con precaucion y probar)
4. Documentar Opcion C — Flashcards
5. Integrar buffer `Obsidian_to_anki.md` a documentacion definitiva

---

## Tareas

- [x] Opcion B — flujo completo documentado y probado
- [x] Opcion C — Image Occlusion: script `occlusion_actions/main.py` creado y probado (B/S/Z)
- [x] Opcion C — documentacion `shellcmd_occlusion_actions.md` creada
- [x] Opcion C — template `tpl-Anki_excalidraw.md` funcional
- [x] Script `image_occlusion_reset` marcado como legacy
- [ ] Opcion A — revisar flujo completo y probar
- [ ] Opcion A — documentar si falta
- [ ] Opcion C — Flashcards: activar, probar compatibilidad con Image Occlusion
- [ ] Opcion C — Flashcards: documentar flujo
- [ ] Integrar `Obsidian_to_anki.md` a documentacion definitiva del vault

---

## Preguntas abiertas

- Plugin Flashcards: ¿genera conflictos con Image Occlusion al activarse?

---

## Recursos

**Scripts:**
- `.obsidian/scripts/python/occlusion_actions/main.py` — gestion de carpetas Image Occlusion
- `.obsidian/scripts/python/image_occlusion_reset/main.py` — script legacy (no usar)
- `.obsidian/scripts/python/latex_to_mathjax/main.py` — conversion LaTeX <-> MathJax

**Documentacion shell commands:**
- `_app/shellcommands/shellcmd_occlusion_actions.md`
- `_app/shellcommands/shellcmd_latex_mathjax.md`

**Buffer de documentacion:**
- `_hangar/anki/Obsidian_to_anki.md`

**Templates:**
- `_templates/tpl-Anki_excalidraw.md`
- `_templates/tpl-excalidraw_occlusion.md`
