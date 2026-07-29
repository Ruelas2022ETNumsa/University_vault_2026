---
project: "Anki Galaxy — Decisión de flujo definitivo + Script LaTeX Opción A"
date: 2026-07-28
status: creciente
---

comentario, las 3 son plugins utiles para distintas etapas, es necesario un anki_system para documentar que hara cada plugin.
## Handoff

**Última sesión:** 2026-07-28
**Retomar desde:** `tsk_anki.md` → sección Tareas → Tomar decisión final A o B
**Completado esta sesión:**
- Opción A (Marginalia Anki Sync) — probada ✅
- Opción B (Flashcards reuseman) — probada ✅
- Opción C (Obsidian_to_Anki Pseudonium) — instalada, configurada y probada ✅
- Flujo Image Occlusion Excalidraw → Opción C → Anki — funcional ✅
- Template `_templates/proex.md` — configurado para Image Occlusion Enhanced ✅
- `data.json` de Opción C — limpiado y optimizado ✅
- Documentación A, B, C creada
- `anki_galaxy_guide.md` actualizado con flujo definitivo provisional
- Script 2 (`latex_to_mathjax`) — implementado, probado y documentado ✅
  - Toggle L->M / M->L con bandera `latex_converted` en YAML
  - Contador `anki_exports` (export_1, export_2, ...)
  - Limpieza automática de IDs `^anki-XXXXXXXXXXXXX` en M->L
  - Documentado en `shellcmd_latex_mathjax.md`
  - Botones ribbon configurados via Commander

**Próximo paso:** tomar decisión final — A o B como plugin principal de texto. Actualizar `anki_galaxy_guide.md` con decisión.

**Preguntas de cierre:**
- ¿Opción A con Script 2 es suficientemente fluida para ser el plugin principal de texto?
- ¿Coexisten A+B o se elige uno como principal?

---

## Resumen y objetivo

Decidir el flujo definitivo Anki Galaxy entre las opciones A (Marginalia), B (Flashcards reuseman) y C (Obsidian_to_Anki). La decisión depende de si el Script 2 resuelve el único problema de Opción A (LaTeX). C ya está definida como exclusiva para Image Occlusion.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-07-28 | Opción C = flujo Image Occlusion | Único plugin que soporta Image Occlusion Enhanced desde Excalidraw |
| 2026-07-28 | AnkiSync+ (RochaG07) descartado | Creaba decks pero no tarjetas — sin fix, sin mantenimiento |
| 2026-07-28 | Opción D descartada | Complejidad innecesaria — Opción B resuelve LaTeX sin scripts |
| 2026-07-28 | Script 3 (limpiar `<!--ID-->`) — pendiente | Necesario para re-exportar si se borran mazos manualmente en Anki |

> [!note]- Descartadas
> - **AnkiSync+ (RochaG07):** creaba mazos pero no tarjetas. Sin solución conocida, sin mantenimiento activo.
> - **Opción D (Obsidian-Anki-Sync debanjandhar12):** sintaxis de cloze en LaTeX muy compleja. Opción B resuelve el mismo problema de forma más limpia.
> - **TrillStones Image Occlusion:** genera 2 PNG separados — no compatible con Image Occlusion Enhanced. Reemplazado por script zsviczian.

---

## Planificación

El único bloqueador para decidir entre Opción A y B es el LaTeX en Opción A. Opción B lo resuelve nativamente con `$...$`. Opción A requiere conversión `$` → `\(...\)` dentro de bloques `%%> ... %%` antes del sync.

**Restricciones:**
- El script no debe modificar el `.md` permanentemente — debe revertir después del sync o trabajar sobre una copia temporal
- Solo debe tocar contenido dentro de bloques `%%> ... %%`
- Debe correr desde Obsidian (Shell Commands plugin) con un solo click

**Enfoque elegido:** script Python que lee el archivo, convierte `$...$` → `\(...\)` y `$$...$$` → `\[...\]` solo dentro de bloques `%%>...%%`, guarda una versión temporal, lanza el sync de Marginalia, y restaura el original. Alternativa más simple: script que convierte en memoria y no toca el archivo original, sino que genera un archivo temporal que Marginalia lee.

> [!error]- Enfoque descartado — addon Math Delimiters Replacer
> El addon `401047458` hace la conversión pero manualmente desde Anki Desktop (seleccionar texto → Alt+M). Inviable para uso regular con muchas notas.

---

## Consideraciones para decisión final

### Comparativa A vs B para texto y fórmulas

| Criterio | Opción A (Marginalia) | Opción B (Flashcards) |
|---|---|---|
| LaTeX `$...$` | ❌ requiere Script 2 | ✅ directo |
| Integración con flujo de estudio | ✅ nativa — misma sintaxis Marginalia | 🟡 sintaxis separada (`#card`) |
| Sintaxis en nota activa | ✅ no interrumpe la nota | 🟡 agrega tags `#card` visibles |
| Mantenimiento | ✅ activo (Cornell Marginalia) | ⚠️ inactivo desde Oct 2022 |
| Deck por tag | ✅ tag mapping inline y frontmatter | ✅ deck por carpeta automático |
| Cloze | 🟡 no nativo | ✅ con `==highlight==` |
| Reversed | 🟡 no nativo | ✅ con `#card-reverse` |
| Inline cards | 🟡 sintaxis `%%>;;%%` | ✅ con `::` |
| Riesgo de abandono | bajo | alto (sin updates en 2 años) |

### Escenarios de decisión

**Si Script 2 funciona bien:** Opción A como principal para notas con marginalia. Opción B para notas dedicadas exclusivamente a flashcards (sin marginalia). C para Image Occlusion.

**Si Script 2 es frágil o lento:** Opción B como principal para texto/fórmulas. A solo para marginalia sin LaTeX. C para Image Occlusion.

---

## Flujo de pasos — Script 2

1. Leer el `.md` en memoria
2. Encontrar todos los bloques `%%> ... %%`
3. Dentro de cada bloque, aplicar:
   - `$$...$$ ` → `\[...\]`
   - `$...$` → `\(...\)`
   - No tocar bloques de código `` ` `` ni wikilinks `[[]]`
4. Ejecutar sync de Marginalia sobre el contenido convertido
5. Restaurar el `.md` original (sin cambios en disco)

**Alternativa más simple — solo conversión en archivo temporal:**
1. Copiar el `.md` a un archivo `_tmp_sync.md`
2. Aplicar conversiones en el temporal
3. Abrir el temporal en Obsidian y ejecutar sync manual
4. Borrar el temporal

---

## Tareas

- [x] Instalar Anki Desktop + AnkiConnect + FSRS
- [x] Instalar AnkiDroid y vincular cuenta AnkiWeb
- [x] Probar Opción A (Marginalia Anki Sync)
- [x] Probar Opción B (Flashcards reuseman)
- [x] Instalar y configurar Opción C (Obsidian_to_Anki Pseudonium)
- [x] Configurar template `proex.md` para Image Occlusion Enhanced
- [x] Probar flujo completo Excalidraw → Image Occlusion → Anki
- [x] Limpiar y optimizar `data.json` de Opción C
- [x] Documentar A, B, C en archivos separados
- [x] Actualizar `anki_galaxy_guide.md`
- [x] **Implementar Script 2** — conversor `$` → MathJax para Opción A
- [x] Probar Script 2 con notas reales que tengan marginalia + fórmulas LaTeX
- [x] Evaluar fluidez del flujo A+Script2 vs B puro
- [ ] **Tomar decisión final** — A o B como plugin principal de texto
- [ ] Actualizar `anki_galaxy_guide.md` con decisión final
- [ ] Implementar Script 1 (conversor Marginalia → Flashcards) si se decide B como principal
- [ ] Implementar Script 3 (limpiar `<!--ID-->`) como Shell Command

---

## Preguntas abiertas

- ¿El Script 2 debe modificar el archivo temporalmente o trabajar con una copia?
- ¿Opción A y B coexisten o se elige una como estándar para texto?
- ¿Se necesita Script 1 (Marginalia → Flashcards) si se decide mantener ambas opciones?

---

## Recursos

### Archivos del vault
- `anki_galaxy_guide.md` — guía maestra del sistema
- `anki-opcionA-marginalia.md` — documentación Opción A
- `anki-opcionB-flashcards.md` — documentación Opción B
- `anki-opcionC-obsidian-to-anki.md` — documentación Opción C
- `_templates/proex.md` — template Image Occlusion para Opción C
- `.obsidian/plugins/obsidian-to-anki-plugin/data.json` — config Opción C

### Plugins de Obsidian
- Cornell Marginalia (Opción A): https://github.com/Anna-Thomas/cornell-marginalia
- Flashcards reuseman (Opción B): https://github.com/reuseman/flashcards-obsidian
- Obsidian_to_Anki (Opción C): https://github.com/ObsidianToAnki/Obsidian_to_Anki
- Excalidraw plugin: https://github.com/zsviczian/obsidian-excalidraw-plugin
- Script Image Occlusion zsviczian: https://github.com/zsviczian/obsidian-excalidraw-plugin/blob/master/ea-scripts/Image%20Occlusion.md
- Shell Commands plugin: https://github.com/Taitava/obsidian-shellcommands

### Anki
- AnkiConnect addon: código `2055492159` | https://github.com/FooSoft/anki-connect
- Image Occlusion Enhanced addon: código `1374772155`
- Math Delimiters Replacer: código `401047458` (solo Opción A, manual)
- AnkiWeb: https://ankiweb.net
- AnkiDroid: Play Store → "AnkiDroid Flashcards" (AnkiDroid Open Source Team)

### Referencia LaTeX — conversión MathJax
- Obsidian usa `$...$` y `$$...$$`
- Anki usa `\(...\)` y `\[...\]` (MathJax)
- La conversión es: `$expr$` → `\(expr\)` | `$$expr$$` → `\[expr\]`
- Aplicar solo dentro de bloques `%%> ... %%` de Marginalia
