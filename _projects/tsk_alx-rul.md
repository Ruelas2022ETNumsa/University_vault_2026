---
project: "Cornell Marginalia → Galaxy"
date: 2026-07-20
status: creciente
---

# tsk — Revisión e integración de Cornell Marginalia

---

## Handoff

**Última sesión:** 2026-07-25
**Retomar desde:** Board completo — todos los botones documentados. Próximo foco: EXP-10 (drag & drop a Canvas/Excalidraw), EXP-12 (navegación por teclado), y pendientes de S7 (PDF mode, active recall, overlay).
**Completado esta sesión:**
- Board CS — 7 botones documentados: Copy to clipboard, Export to markdown, Export to canvas, Zen doodle mode (SuperDoodle), Clear board, Import skeleton, Auto-add copied text.
- Flujo E — actualizado con pasos reales probados.
- EXP-08 y EXP-09 marcados como completos.
**Próximo paso:** EXP-10 drag & drop desde Explorer a Canvas/Excalidraw, o continuar con S7 filtros PDF pendientes.

---

## Resumen y objetivo

Revisar cada herramienta del plugin Cornell Marginalia una por una, probarla en Obsidian, y decidir si se integra a Galaxy y cómo. Nada se documenta como parte del sistema sin haberlo probado antes.

comentario: en la linea 770 de main.js se cambia los colores de superdoodle esto para una sesion corta para cambiar los colores y valores default

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

- [x] **Campo `dest:`** — convención definida: `_inbox/ETNXXX-inbox.md` por materia, `inbox.md` genérico. Autocompletado probado.
- [x] **Botón `ZK`** — ZK ON crea nota en `Zettelkasten/`, ZK OFF appendea a `dest:`. Probado.
- [x] **Botón `clear`** — limpia clipboard y memoria del campo dest. Sin decisión pendiente.
- [x] **Botón `doodle`** — cubierto por A10 (OCD).

### Sección 4 — Tabs

- [x] **`current`** — probado. Muestra marginalia del archivo activo agrupadas por tag. ✅ integrar al flujo de repaso.
- [x] **`vault`** — probado. Escanea todo el vault respetando exclusiones. ✅ útil para repaso global pre-parcial.
- [x] **`threads`** — probado en A9. Muestra árbol jerárquico de stitches y grupos por `#tag`. ✅
- [ ] **`board`** — pendiente completar: Import skeleton, Export to markdown, Auto-add copied text.

### Sección 5 — Acciones

- [x] **`stitch`** — probado en A9. Flujo de dos pasos, sintaxis clásica y semántica verificadas. ✅
- [x] **`group`** — pendiente. Probar agrupación de marginalia repetidas.
- [x] **Recargar** — sin decisión pendiente.

### Sección 7 — Filtros de tag

- [x] **Filtros `!` `?` `X-` `V-` `C-` `F-` `R-` `T-`** — probados. Funcionan correctamente. ✅ usar para repaso selectivo por tipo.
- [x] **Reloj (Recientes)** — probar. ¿Muestra las últimas marginalia escritas? Útil para retomar sesión.
- [ ] **Libro cerrado (Direct PDF mode)** — probar con PDF abierto en Obsidian. Relevante si se usan PDFs en Galaxy.
- [x] **Mazo de cartas (flashcards `;;`)** — probar junto con A7 y A8. Muestra solo marginalia con blur.
- [ ] **Cerebro (Active recall PDF)** — probar en PDF. Oculta resaltados para repasar sin ver las respuestas.
- [ ] **Globo (Overlay mode)** — probar. Muestra marginalia superpuestas sobre el PDF.

### Sección 8 — Navegación por teclado

- [ ] **`H` (hover X-Ray)** — probar previsualización de contexto sin abrir el archivo. Ver EXP-12.
- [ ] **`Spacebar` (seleccionar para stitch)** — probar mass stitch con `Alt+S`. Ver EXP-03.
- [ ] **`Shift+↓/↑` (mass pinning)** — probar pinear múltiples notas al Board rápidamente.
- [ ] **`Ctrl+Enter` (saltar a fuente)** — probado implícitamente con click. Verificar con teclado.

### Board

- [x] **Export full tree to Board** — probado en A9. Árbol exportado con título editable (doble click). ✅
- [ ] **Import skeleton** — pendiente.
- [ ] **Export to markdown** — pendiente.
- [ ] **Export to canvas** — pendiente.
- [ ] **Auto-add copied text** — pendiente.
- [x] **Zen doodle mode** — cubierto por A10 (SuperDoodle). ✅

---

## BLOQUE A (7-12) — Configuración del plugin (Settings)

Recorrer sección por sección. Para cada setting: entender, decidir valor Galaxy, documentar.

- [x] **A7. Active Recall — Blur** — ícono 👁️, sintaxis `;;`. Probar en Live Preview y Reading View. Probar Blur Explanatory Marginalias.
- [x] **A8. Flashcard Generator** — comando "Flashcards Generation". Uso principal en supernova y comet. Commander con ícono layers-2.
- [x] **A9. Margin Threads** — Stitch y agrupación por `#tag` probados. Árbol en tab Threads verificado. Hover Peek = tooltip en v4.9.0. Graph View conectado. Export to Board probado.
- [x] **A10. Doodle Engine** — comando "Draw a Doodle". Probar guardar boceto → inyección automática en nota. Probar Super Doodle si se activa.
- [x] **A11. Omni-Capture** — `Alt+C` enfoca input del Explorer. ZK ON/OFF probados. Clipboard texto e imagen probados. Convención `_inbox/` definida.
- [x] **A12. PDF Export** — flujo Prepare → Better Export PDF → Restore. Limitación: bloques cornell no exportan correctamente.

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

- [x] **Omni-Capture Default Folder** — `_inbox/inbox.md` (genérico) o `_inbox/ETNXXX-inbox.md` (por materia). Decidido.
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

## Sesión main.js — Bugs pendientes de parcheo

> Análisis realizado 2026-07-23. Parches a aplicar en sesión dedicada sobre `main.js`.
> Backup disponible: `main.js.bk` en `.obsidian/plugins/cornell-marginalia/`

### BUG-01 — `;;` visible en Reading View

**Síntoma:** En Reading View el marcador `;;` aparece visible dentro del texto de la marginalia. En Live Preview no ocurre.

**Causa:** El post-processor de Reading View (`registerMarkdownPostProcessor`, línea ~14160) hace `replace(";;", "")` solo sobre `tempContent` usado para el visual anchor (puntito de color). El texto real `finalNoteText` que se pasa a `MarkdownRenderer.render` nunca tiene el `;;` removido.

**Fix:** Agregar strip de `;;` sobre `finalNoteText` antes del render. Buscar en `main.js`:
```
let finalRenderText = finalNoteText;
```
Agregar inmediatamente después:
```js
if (finalRenderText.includes("  ;;")) finalRenderText = finalRenderText.replace(/\s*;;\s*/g, "").trim();
```

### BUG-02 — Nombre timestamp del archivo ZK (no usa slug)

> [!warning] Fix pendiente — sesión dedicada
> Los archivos ZK se crean con nombre timestamp (`YYYYMMDDHHmmss`) porque el plugin genera el archivo antes de que el template de Templater corra — el slug llega tarde y no puede usarse para nombrar el archivo en el momento de creación.
> **Solución:** script externo que lee el slug/title del frontmatter de cada archivo en `Zettelkasten/` y los renombra en lote. No resoluble desde `tpl-zk.md` ni desde `main.js` sin modificación mayor. Resolver en sesión dedicada — ver **Pendientes técnicos**.
> **observación:** se debe revisar el template tpl-zk.md para que no sea cargado (mejorarlo acorde al script).

**Síntoma:** Los archivos creados en `Zettelkasten/` reciben nombre de timestamp (`YYYYMMDDHHmmss`) en lugar del slug ingresado por el usuario.

**Causa:** Línea ~286 en `main.js`:
```js
const zkId = window.moment().format("YYYYMMDDHHmmss");
finalDestName = cleanDestName !== "Marginalia Inbox" ? `${zkId} - ${cleanDestName}` : zkId;
```
El archivo se crea con el timestamp antes de que el template se ejecute — el slug llega tarde.

**Fix propuesto:** Reemplazar el timestamp por el slug cuando esté disponible. El slug se obtiene del prompt de Templater pero el plugin no lo recibe. Opciones a evaluar en sesión:
- Usar `cleanDestName` directamente como nombre si no es `"Marginalia Inbox"`
- Exponer el slug como variable al plugin antes de crear el archivo

**Intentos en `tpl-zk.md`:** Se probaron polling + openFile + rename — no funcionaron porque el template se ejecuta después de que el archivo ya fue creado con timestamp.

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
| 2026-07-23 | A7 blur funciona en ambos modos con botón 👁️ activo | Probado en 6 casos en void.md |
| 2026-07-23 | Bug visual `;;` en Reading View — pendiente revisión de `main.js` | No configurable desde Settings; se mantiene por ahora |
| 2026-07-23 | A10 documentado — OCD y SuperDoodle son motores distintos | Flujos y destinos de guardado diferentes |
| 2026-07-23 | `tpl-zk.md` modificado — rename por polling + openFile | Evita renombrar el archivo activo (void) |
| 2026-07-23 | Nombre ZK timestamp no resoluble desde template | El archivo se crea antes de que el template corra — fix requiere `main.js` |
| 2026-07-23 | A8: una marginalia por línea en callouts | Dos marginalia en la misma línea contaminan las tarjetas generadas — convención, no bug |
| 2026-07-23 | A8: Flashcards Generation siempre post-Restore | Durante el Prepare el texto tiene IDs temporales que contaminan las tarjetas |
| 2026-07-23 | A8: comet es caso de uso propio, no solo herencia | Fórmulas clave y pasos de examen se anotan con `;;` directamente en el comet |
| 2026-07-23 | A12: bloques cornell no exportan correctamente | Choque entre Cornell Notes y Cornell Marginalia en el motor de print — limitación conocida |
| 2026-07-23 | A12: convención export = solo marginalia inline | Evitar bloques `cornell` y `marginalia` anidado en notas destinadas a PDF |
| 2026-07-23 | A11: `Alt+C` enfoca input del Explorer, no abre modal flotante | README del plugin desactualizado — comportamiento real en v4.9.0 |
| 2026-07-23 | A11: ZK OFF appendea como `%%> %%` inline, no texto plano | El contenido queda listo para ser procesado por el plugin |
| 2026-07-23 | A11: `_inbox/` como carpeta de captura rápida Galaxy | Una nota por materia activa + `inbox.md` genérico. Excluida del scanner del Explorer |
| 2026-07-23 | Screenshots y doodles → `_assets/` sin excepción | No van al inbox — destinos distintos por tipo de contenido |
| 2026-07-23 | Script de renombre ZK (timestamp → slug) — pendiente | Requiere script externo; `tpl-zk.md` no puede resolverlo |
| 2026-07-23 | A9: `#tag` en marginalia crea grupo en Threads automáticamente | No requiere Stitch — agrupación por tag es el mecanismo principal para Galaxy |
| 2026-07-23 | A9: `UNTAGGED` no renombrable desde Settings ni data.json | El plugin lo regenera — usar siempre `#tag` o etiqueta semántica |
| 2026-07-23 | A9: Hover Peek es tooltip en v4.9.0, no popup de preview | README desactualizado — comportamiento real verificado |
| 2026-07-23 | A9: nomenclatura kebab-case para grupos Galaxy | `#transformadas-integrales`, `#circuitos-rc`, etc. |
| 2026-07-25 | tag-class = nombre oficial para prefijo de color de marginalia (`!`, `?`, `X-`…) | Evitar confusión con tag-group |
| 2026-07-25 | tag-group = nombre oficial para agrupador de Threads (`#nombre`) | Evitar confusión con tag-class |
| 2026-07-25 | Stitch deshacer (`Ctrl+Shift+Z`): padre limpio, hilo conserva `^id` | Comportamiento verificado en ambos flujos (modal y drag & drop) |
| 2026-07-25 | Drag & drop S8→S8 como alternativa a stitch sin ventana emergente | No pide tipo de conexión; válido desde tab `vault` |
| 2026-07-25 | Group ordena por línea y agrupa por contenido exacto, independiente de tag-class e id | Comportamiento verificado en casos 3 y 4 |
| 2026-07-25 | Export full tree to board pierde jerarquía padre-hilo — todas las notas al mismo nivel | Board no refleja indentación de threads |
| 2026-07-25 | Indent en board hasta ~15 niveles confirmados | Límite superior no determinado |

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

- ~~¿Cómo se integra A6 (Explorer) con el flujo de repaso de parcial en Galaxy?~~ — pendiente de cerrar al completar A6.
- ~~¿Se usará Margin Threads (A9) activamente?~~ — sí, con `#tag` agrupador como mecanismo principal.
- ~~¿Omni-Capture reemplaza algún flujo existente del vault o es adicional?~~ — Es adicional. Captura rápida hacia `_inbox/`, no reemplaza ningún flujo existente.

---

## Pendientes técnicos

- [ ] **Script renombre ZK** — agarrar slug/title de archivos timestamp en `Zettelkasten/` y renombrarlos. Hacer en sesión dedicada.

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
- `E:\University_vault_2026\_templates\tpl-zk.md` — template ZK modificado esta sesión
- `E:\University_vault_2026\.obsidian\plugins\cornell-marginalia\main.js` — plugin (con backup `main.js.bk`)
- `E:\University_vault_2026\_inbox\inbox.md` — captura rápida genérica
