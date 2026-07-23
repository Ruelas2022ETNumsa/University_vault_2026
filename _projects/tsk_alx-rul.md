---
project: "Cornell Marginalia → Galaxy"
date: 2026-07-20
status: activa
---

# tsk — Revisión e integración de Cornell Marginalia

> Objetivo: revisar cada herramienta del plugin una por una, probarla en Obsidian, y decidir si se integra a Galaxy y cómo. Nada se documenta en la guía como "parte del sistema" sin haberlo probado antes.

---

## Flujo de trabajo

Para cada ítem:
1. Discutir qué hace la herramienta / configuración
2. Probarla en Obsidian (cuando aplique)
3. Decidir: ✅ integrar / ❌ descartar / ⏸️ dejar pendiente
4. Si ✅ → definir cómo se usa en Galaxy y actualizar `Marginalia_guide.md`

---

## BLOQUE A — Herramientas del plugin (funcionalidades)

Recorrer en orden. Probar antes de decidir.

- [x] **A1. Sintaxis core** —\%%> \%% y \%%< \%% inline. Probar en Live Preview y Reading View. Verificar comportamiento con y sin parche.
- [x] **A2. Semantic Highlighting** — prefijos `?` `!` `X-` `V-`. Probar los 4 colores. Evaluar si los 4 cubren los casos de ingeniería o hacen falta más.
- [x] **A3. Grouping Method A** — callout `[!cornell]`. Probar con párrafo + lista y con párrafo + imagen. Solo Reading View.
- [x] **A4. Grouping Method B** — bloque ` ```marginalia `. Probar composición compleja. Probar que la nota va ANTES del texto (BUENA NOTA CORNELL). Evaluar cuándo usar A vs B.
- [x] **A5. Imágenes en el margen** — \%%> img:[[...]] \%%. Probar con una imagen real del vault. Probar el zoom hover.
- [ ] **A6. Marginalia Explorer** — sidebar, tabs Current / Vault / Threads / Board. Probar Click-to-Scroll, filtro por color, hover X-Ray con tecla H, drag a Canvas o Excalidraw.
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

## Decisiones tomadas

> Se irán registrando acá a medida que se avanza.

| Item | Decisión | Notas |
|------|----------|-------|
| — | — | — |

---

## Pendientes que surjan durante la revisión

> Anotaciones libres de cosas que aparezcan y requieran acción futura.

-
