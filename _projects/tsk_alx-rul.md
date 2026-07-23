---
project: "Cornell Marginalia → Galaxy"
date: 2026-07-20
status: creciente
---

# tsk — Revisión e integración de Cornell Marginalia

---

## Handoff

**Última sesión:** 2026-07-22
**Retomar desde:** `_marginalia_system.md` A6 — documentar en sistema y continuar con A7
**Completado esta sesión:** A1, A2, A3, A4, A5 documentados en `_marginalia_system.md`. Creados `_marginalia_system.md`, `marginalia_explorer_guide.md.md`. Tags Galaxy definidos (8 tags con RGB). Reglas de uso A3/A4 establecidas. A6 probado parcialmente (current + vault).
**Próximo paso:** Documentar A6 en `_marginalia_system.md` → continuar con A7 (Blur)
**Preguntas de cierre:** —

---

## Resumen y objetivo

Revisar cada herramienta del plugin Cornell Marginalia una por una, probarla en Obsidian, y decidir si se integra a Galaxy y cómo. Nada se documenta como parte del sistema sin haberlo probado antes.

---

## BLOQUE A(1-6) — Herramientas del plugin (funcionalidades)

Recorrer en orden. Probar antes de decidir.

- [x] **A1. Sintaxis core** —\%%> \%% y \%%< \%% inline. Probar en Live Preview y Reading View. Verificar comportamiento con y sin parche.
- [x] **A2. Semantic Highlighting** — prefijos `?` `!` `X-` `V-`. Probar los 4 colores. Evaluar si los 4 cubren los casos de ingeniería o hacen falta más.
- [x] **A3. Grouping Method A** — callout `[!cornell]`. Probar con párrafo + lista y con párrafo + imagen. Solo Reading View.
- [x] **A4. Grouping Method B** — bloque ` ```marginalia `. Probar composición compleja. Probar que la nota va ANTES del texto (BUENA NOTA CORNELL). Evaluar cuándo usar A vs B.
- [x] **A5. Imágenes en el margen** — \%%> img:[[...]] \%%. Probar con una imagen real del vault. Probar el zoom hover.
- [ ] **A6. Marginalia Explorer** — sidebar, tabs Current / Vault / Threads / Board. Probar Click-to-Scroll, filtro por color, hover X-Ray con tecla H, drag a Canvas o Excalidraw.

---

## BLOQUE A6 — Marginalia Explorer (detalle de uso)

> Referencia completa de la UI: `[[marginalia_explorer_guide]]`
> Este bloque registra qué probar y decidir para cada componente del Explorer.

### Sección 2 — Omni-Capture

- [ ] **Campo `dest:`** — definir destino Galaxy para capturas rápidas. Opciones: `_inbox/`, `Rubbish/`, parcial activo. Decidir convención.
- [ ] **Botón `ZK`** — probar creación de nota atómica. ¿Se usa ZK mode en Galaxy o se appendea siempre al destino?
- [ ] **Botón `clear`** — sin decisión pendiente, funciona como limpieza de contexto.
- [ ] **Botón `doodle`** — probar flujo completo: dibujar → attach → guardar. Ver EXP-06 en `marginalia_explorer_guide`.

### Sección 4 — Tabs

- [x] **`current`** — probado. Muestra marginalia del archivo activo agrupadas por tag. ✅ integrar al flujo de repaso.
- [x] **`vault`** — probado. Escanea todo el vault respetando exclusiones. ✅ útil para repaso global pre-parcial.
- [ ] **`threads`** — pendiente. Solo tiene contenido si se usa Stitch (A9). Probar junto con A9.
- [ ] **`board`** — pendiente. Probar pinear notas, organizar, exportar. Ver EXP-08 y EXP-09.

### Sección 5 — Acciones

- [ ] **`stitch`** — probar conexión entre dos marginalia de archivos distintos. Ver EXP-03. Decidir si se usa en Galaxy.
- [ ] **`group`** — probar agrupación de marginalia repetidas. ¿Es útil en flujo de estudio?
- [ ] **Recargar** — sin decisión pendiente, usar cuando el Explorer no refleje cambios recientes.

### Sección 7 — Filtros de tag

- [x] **Filtros `!` `?` `X-` `V-` `C-` `F-` `R-` `T-`** — probados. Funcionan correctamente. ✅ usar para repaso selectivo por tipo.
- [ ] **Reloj (Recientes)** — probar. ¿Muestra las últimas marginalia escritas? Útil para retomar sesión.
- [ ] **Libro cerrado (Direct PDF mode)** — probar con PDF abierto en Obsidian. Relevante si se usan PDFs en Galaxy.
- [ ] **Mazo de cartas (flashcards `;;`)** — probar junto con A7 y A8. Muestra solo marginalia con blur.
- [ ] **Cerebro (Active recall PDF)** — probar en PDF. Oculta resaltados para repasar sin ver las respuestas.
- [ ] **Globo (Overlay mode)** — probar. Muestra marginalia superpuestas sobre el PDF.

### Sección 8 — Navegación por teclado

- [ ] **`H` (hover X-Ray)** — probar previsualización de contexto sin abrir el archivo. Ver EXP-12.
- [ ] **`Spacebar` (seleccionar para stitch)** — probar mass stitch con `Alt+S`. Ver EXP-03.
- [ ] **`Shift+↓/↑` (mass pinning)** — probar pinear múltiples notas al Board rápidamente.
- [ ] **`Ctrl+Enter` (saltar a fuente)** — probado implícitamente con click. Verificar con teclado.

### Board

- [ ] **Import skeleton** — probar importar estructura desde nota activa. ¿Compatible con formato Galaxy?
- [ ] **Export to markdown** — probar exportación. Verificar que el archivo generado sigue convenciones Galaxy.
- [ ] **Export to canvas** — probar. Verificar Block ID links y compatibilidad con Excalidraw/Constellation.
- [ ] **Auto-add copied text** — probar modo automático. ¿Interfiere con el clipboard en flujo normal de estudio?
- [ ] **Zen doodle mode** — probar dentro del Board. Relación con A10.

---

## BLOQUE A (7-12) — Configuración del plugin (Settings)

Recorrer sección por sección. Para cada setting: entender, decidir valor Galaxy, documentar.

- [ ] **A7. Active Recall — Blur** — ícono 👁️, sintaxis `;;`. Probar en Live Preview y Reading View. Probar Blur Explanatory Marginalias.
- [ ] **A8. Flashcard Generator** — comando "Flashcards Generation". Probar que genera sección al final. Evaluar relación con `supernova`, `planet`, `comet`.
- [ ] **A9. Margin Threads** — Stitch, Drag & Drop, Mass Stitch. Probar conexión entre dos notas distintas. Ver árbol en tab Threads. Probar Hover Peek (botón 🔗).
- [ ] **A10. Doodle Engine** — comando "Draw a Doodle". Probar guardar boceto → inyección automática en nota. Probar Super Doodle si se activa.
- [ ] **A11. Omni-Capture** — modal `Alt+C`. Probar captura de texto, imagen del portapapeles, doodle integrado. Definir carpeta destino en Galaxy.
- [ ] **A12. PDF Export** — flujo Prepare → Export → Restore. Probar con Method B. Verificar que Restore devuelve el archivo limpio.

---

## BLOQUE B — Configuración del plugin (Settings)

Recorrer sección por sección. Para cada setting: entender, decidir valor Galaxy, documentar.

### B1. Appearance & Rendering

- [ ] **Responsive Marginalia (Auto-Collapse)** `[1/0]=1` — ¿dejar ON? Probar con sidebar abierto.
- [ ] **Responsive Threshold (px)** `[slider]=850` — ¿ajustar según layout habitual del vault?
- [ ] **Adaptive Width (Theme Compatibility)** `[1/0]=1` — ¿el tema del vault necesita esto?
- [ ] **Margin Alignment** `[Left/Right]=left` — ¿left es el correcto para Galaxy? Probar ambos.
- [ ] **Margin Width (%)** `[slider]=30` — ¿30% es cómodo? Probar 20%, 25%, 30%.
- [ ] **Margin Distance (Offset)** `[slider]=15` — ajuste visual fino. Probar en nota real.
- [ ] **Font Size** `[text=0.85em]` — ¿dejar default o ajustar?
- [ ] **Font Family** `[text=inherit]` — ¿inherit es correcto con el tema activo?
- [ ] **Enable in Reading View** `[1/0]=1` — ON obligatorio para PDF Export y revisión de supernova.
- [ ] **Extract Highlights** `[1/0]=1` — ¿se quiere que `==texto==` aparezca en el Explorer? Evaluar ruido vs utilidad.
- [ ] **Blur Explanatory Marginalias** `[1/0]=1` — ¿ON si se usa flujo de flashcards?

### B2. Color Tags

- [ ] Revisar los 4 tags default (`!` `?` `X-` `V-`). ¿Alcanzan para ingeniería? ¿Falta alguno (ej. `#` para fórmula clave, `~` para relación con otra materia)?

### B3. Structural Box Colors

- [ ] ¿Se usa Margin Threads activamente? Si no se decide usar Threads, esta sección es irrelevante.

### B4. Task Management

- [ ] **Auto-Delete Completed Tasks** — ¿riesgo de borrado accidental? ¿Conviene en Galaxy?
- [ ] **TaskNotes HTTP API Integration** — ¿se usa TaskNotes en el vault? Si no, desactivar.

### B5. File & Output Management

- [ ] **Omni-Capture Default Folder** — ¿dónde van las capturas rápidas en Galaxy? Opciones: `Rubbish/`, nueva carpeta `_inbox/`, o directo al parcial activo.
- [ ] **Omni-Capture Template** — ¿el template default es suficiente o necesita YAML Galaxy?
- [ ] **Zettelkasten Folder** — solo relevante si se activan Margin Threads. ¿Carpeta en Galaxy o ignorar?
- [ ] **Zettelkasten Template Path** — ídem anterior.
- [ ] **Doodles Folder** `[text=Marginalia Attachments]` — ¿mover a `_assets/doodles`? Decidir convención.
- [ ] **Evidence Boards Folder** — ¿se usan Evidence Boards? Si no, irrelevante.
- [ ] **Pinboards Folder / Template** — ¿se usa Pinboard activamente? Decidir.
- [ ] **Clean Exports (Remove Tags / Block IDs)** — ¿ON para exportaciones limpias?
- [ ] **Drag & Drop Template** — revisar formato default. ¿Compatible con sintaxis Galaxy?

### B6. Advanced & Exclusions

- [ ] **Show Syntax in Source Mode** `[1/0]=1` — dejar ON (standard).
- [ ] **Ignored Folders** `[text=Templates]` — ¿agregar `_app,_templates,_PDF,Excalidraw,_skills,_projects`? Decidir lista Galaxy.
- [ ] **Ignored Folders for Highlights** `[text=Excalidraw]` — ¿suficiente o agregar más?
- [ ] **Ignored Highlight Texts** — ¿el texto de Excalidraw ya está? ¿Falta algún boilerplate del vault?
- [ ] **Semantic Stitching UI** `[1/0]=1` — solo relevante si se activan Threads.

### B7. Addons & Modules

- [ ] **Gamification & User Profile** — probar o descartar directo.
- [ ] **Custom Explorer Background** — cosmético, probar o ignorar.
- [ ] **Time Machine & Rhizome** — canvas cronológico. ¿Útil para revisión de parcial?
- [ ] **Pdf Doodle & Harvest** — dibujar sobre PDFs en Obsidian. ¿Interacción con PDF++?
- [ ] **Super Doodle** — extensión del Doodle Engine. Probar junto con A10.
- [ ] **Blurting Mode (1-3-7)** — repetición espaciada desde el Explorer. ¿Reemplaza algo o complementa?
- [ ] **Margidoro Engine** — Pomodoro + marginalia. Probar si se usa Pomodoro.
- [ ] **Anki Advanced Sync** — sync con Anki. ¿Se usa Anki? Si no, descartar.
- [ ] **Zoom & Pan Doodles** `[1/0]=1` — ya ON. Probar con imagen real en margen.
- [ ] **Dashboard: Smart Study** — panel de estudio. ¿Duplica algo del vault?
- [ ] **Cornell Board** — canvas libre desde marginalia. ¿Compite con Excalidraw/Constellation?

---

## Decisiones

| Fecha | Decisión | Motivo |
|---|---|---|
| 2026-07-22 | A3 se usa solo para múltiples marginalia e imágenes | No renderiza bien contenido simple |
| 2026-07-22 | A4 es el método principal para todo lo demás | Mejor renderizado y control |
| 2026-07-22 | A4 no soporta `img:[[...]]` — usar A3 para imágenes | Falla de renderizado confirmada |
| 2026-07-22 | Bloque cornell interno solo compatible con A4 | A3 dentro de ::cue/::note no renderiza |
| 2026-07-22 | 8 tags Galaxy definidos: `!` `?` `X-` `V-` `C-` `F-` `R-` `T-` | Cubren todos los casos de ingenieria |
| 2026-07-22 | `T-` exclusivo de supernova, no hereda | Archivos derivados deben quedar limpios |
| 2026-07-22 | Colores basados en paleta Galaxy con valores RGB | Reemplazan defaults del plugin |
| 2026-07-22 | Múltiples marginalia en A4 requieren salto de línea | Sin salto se apilan o desalinean |
| 2026-07-22 | Regla del punto final en listas con A4 | El último ítem necesita ancla de alineación |
| 2026-07-22 | `marginalia_explorer_guide.md` creado como beacon en `_appnotes/` | UI demasiado detallada para `_marginalia_system` |

> [!note]- Descartadas
> A3 como método general — no agrupa visualmente el contenido como se esperaba.

---

## Planificación

Revisión secuencial de A1–A12 y Bloque B. Para cada ítem: discutir, probar en `void.md`, documentar en `_marginalia_system.md`. Nada entra al sistema sin prueba previa. `void.md` se limpia entre pruebas; archivo de archivo separado si se necesita.

---

## Flujo de pasos

1. Probar ítem en `void.md`
2. Anotar qué se probó, qué se notó, y dónde se usa en Galaxy
3. Documentar en `_marginalia_system.md` (sección correspondiente)
4. Marcar como `[x]` en el Bloque A o B del tsk
5. Limpiar `void.md` antes del próximo ítem

---

## Preguntas abiertas

- ¿Cómo se integra A6 (Explorer) con el flujo de repaso de parcial en Galaxy?
- ¿Se usará Margin Threads (A9) activamente o es demasiado complejo para el flujo actual?
- ¿Omni-Capture reemplaza algún flujo existente del vault o es adicional?

---

## Recursos

**Plugin:**
- Repositorio: https://github.com/latazadehomero/cornell-marginalia
- Versión: v4.9.0

**Archivos del vault:**
- `E:\University_vault_2026\_app\_config\_marginalia_system.md` — integración Galaxy
- `E:\University_vault_2026\_app\_appnotes\Marginalia_guide.md` — guía técnica del plugin
- `E:\University_vault_2026\_app\_appnotes\marginalia_explorer_guide.md.md` — UI del Explorer
- `E:\University_vault_2026\_app\_appnotes\cornell_guide.md` — integración Cornell Notes
- `E:\University_vault_2026\void.md` — archivo de prueba (se limpia entre pruebas)
