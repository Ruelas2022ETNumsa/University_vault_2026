---
galaxy_body: ship
project: "Marginalia Anki (Opcion A) — validacion completa con Script 2"
date: 2026-08-02
status: in-orbit
fleet: anki
---

## Handoff

**Ultima sesion:** 2026-08-02
**Retomar desde:** probar flujo completo Opcion A con Script 2 (latex_to_mathjax) en notas reales con LaTeX
**Completado esta sesion:** Script 2 implementado y documentado. Decision A vs B tomada — A como principal para planet/moon/comet.
**Proximo paso:** probar flujo A+Script2 en nota real con marginalia + LaTeX. Validar en AnkiDroid.
**Preguntas de cierre:** —

---

## Resumen y objetivo

Validar el flujo completo de Opcion A (Cornell Marginalia + Anki Advanced Sync) con el Script 2 (latex_to_mathjax) operativo. El unico bloqueador conocido era el LaTeX — el script lo resuelve. Confirmar que el flujo es fluido para uso real en notas galaxy.

---

## Decisiones

| Fecha | Decision | Motivo |
| ----- | -------- | ------ |
| 2026-08-02 | Opcion A como plugin principal para planet/moon/comet | Marginalia invisible, no interrumpe el contenido galaxy. Script 2 resuelve LaTeX |
| 2026-08-02 | Tag inline despues de `;;` como metodo preferido de deck mapping | Mas limpio que frontmatter para notas mixtas |
| 2026-07-28 | Script 2 implementado como toggle L->M / M->L | Convierte en el archivo, revierte despues del sync con bandera `latex_converted` en YAML |

> [!note]- Descartadas
> Addon Math Delimiters Replacer (codigo `401047458`) — conversion manual desde Anki, inviable para uso regular.
> Escribir LaTeX directo en formato MathJax `\(...\)` en Obsidian — rompe el renderizado nativo de Obsidian.

---

## Planificacion

Flujo definido para Opcion A con LaTeX:

```
Nota galaxy con $LaTeX$ en marginalia
        |
        v Script 2 (ribbon) — L->M: convierte $...$ a \(...\)
Nota con \(MathJax\) | latex_converted: true
        |
        v Ribbon: Cornell Marginalia sync
Tarjetas en Anki con IDs ^anki-XXXXXXXXXXXXX
        |
        v Script 2 (ribbon) — M->L: revierte, borra IDs, incrementa anki_exports
Nota restaurada con $LaTeX$ | latex_converted: false | anki_exports: export_N
```

**Restricciones:**
- Anki Desktop debe estar abierto para el sync
- Script 2 convierte todo el `.md` (excepto bloques de codigo y YAML) — no solo los bloques `%%>...%%`
- Script 2 requiere 2 clicks extra vs Opcion B (antes y despues del sync)
- Solo usar en notas planet/moon/comet — no en dwarf/formularios (esos van con Opcion B)

---

## Flujo de pasos

1. Abrir nota con marginalia + LaTeX en Obsidian
2. Verificar que Anki Desktop esta abierto con AnkiConnect activo
3. Click ribbon Script 2 — convierte L->M, bandera `latex_converted: true`
4. Click ribbon Marginalia sync — exporta tarjetas a Anki
5. Click ribbon Script 2 — revierte M->L, borra IDs, incrementa `anki_exports`
6. Verificar tarjetas en Anki Desktop — LaTeX debe renderizar
7. Sync Anki Desktop -> AnkiWeb -> AnkiDroid
8. Verificar LaTeX en AnkiDroid

---

## Tareas

- [x] Instalar y configurar Cornell Marginalia con Anki Advanced Sync
- [x] Configurar tag mapping (frontmatter e inline `;;`)
- [x] Probar sync basico (texto sin LaTeX)
- [x] Implementar Script 2 (latex_to_mathjax) — toggle L->M / M->L
- [x] Documentar Script 2 en `shellcmd_latex_mathjax.md`
- [x] Tomar decision A vs B — A como principal
- [ ] Probar flujo completo A + Script 2 en nota real con LaTeX
- [ ] Verificar renderizado LaTeX en Anki Desktop
- [ ] Verificar renderizado LaTeX en AnkiDroid
- [ ] Probar tag mapping inline `;;` con decks Galaxy reales
- [ ] Confirmar que `anki_exports` se incrementa correctamente en cada ciclo
- [ ] Documentar resultado final en `anki-opcionA-marginalia.md`
- [ ] Actualizar `anki_galaxy_guide.md` con estado final Opcion A

---

## Preguntas abiertas

Ninguna por el momento.

---

## Recursos

**Documentacion:**
- `_hangar/anki/anki-opcionA-marginalia.md` — guia completa Opcion A
- `_hangar/anki/opA_vs_opB.md` — comparativa y veredicto
- `_hangar/anki/anki_galaxy_guide.md` — guia maestra del sistema
- `_app/shellcommands/shellcmd_latex_mathjax.md` — documentacion Script 2

**Script:**
- `.obsidian/scripts/python/latex_to_mathjax/main.py` — Script 2

**Plugin:**
- Cornell Marginalia: https://github.com/Anna-Thomas/cornell-marginalia
- AnkiConnect addon: codigo `2055492159`
