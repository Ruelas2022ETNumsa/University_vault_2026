---
title: Sistema Galaxy — University Vault
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
related_notes:
  - "[[_note-system]]"
  - "[[_pdf_pp-system]]"
  - "[[_mindmap-system]]"
  - "[[_template-system]]"
  - "[[_graph-system]]"
  - "[[_ToDo-system]]"
  - "[[_TAB_note-system]]"
  - "[[_notebooklm-system]]"
  - "[[claude_prompts]]"
  - "[[_claude-plan]]"
  - "[[_claude-work]]"
  - "[[_claude-boot]]"
  - "[[_claude-setup]]"
  - "[[_claude-close]]"
tags:
  - beacon
  - galaxy
  - infraestructura
date_created: 2026-05-28
date_updated: 2026-07-17
status: activo
---

# Sistema Galaxy — University Vault

> Convención de notas: [[_note-system]]
> Sistema PDF: [[_pdf_pp-system]]
> Sistema Mindmap: [[_mindmap-system]]
> Sistema de Plantillas: [[_template-system]]
> Pendientes: [[_ToDo-system]]

Este baúl es un **cerebro digital para ingeniería**. Cada nota tiene una ubicación precisa, un nombre limpio y un YAML que define su rol y sus conexiones.

---

## Idea central

El baúl está organizado como un **universo de galaxias**. Cada materia es una galaxia. El conocimiento dentro de cada galaxia se estructura en capas orbitales — desde el índice central (star) hacia afuera: teoría, propiedades, ejercicios, referencias y visuales.

La metáfora de la galaxia vive **únicamente en el YAML** de cada nota — no en los nombres de carpetas ni en los nombres de archivo. Las carpetas dan ubicación física. El nombre del archivo da identidad. El YAML da rol, órbita y conexiones. Los `[[wikilinks]]` de Obsidian son los hilos gravitacionales, y los bloques `%%comentados%%` los hacen visibles en el grafo sin aparecer en el modo de lectura.

> **ETN302 es legacy.** Se queda como está. El Sistema Galaxy aplica a todas las materias nuevas.

---

## Mapa de carpetas del baúl

```mermaid
---
config:
    treeView:
        rowIndent: 20
        paddingX: 8
        paddingY: 4
        lineThickness: 1
    themeVariables:
        treeView:
            labelFontSize: '30px'
            labelColor: '#7c6f9f'
            lineColor: '#b0a8c8'
            descriptionColor: '#9fb8a8'
            highlightBg: 'rgba(180, 160, 210, 0.15)'
            highlightStroke: '#c4aee0'
---
treeView-beta
    University_Vault_2026/
        Semesters/ ## todo el contenido académico vive aquí
            Sem_NN/ ## una carpeta por semestre (Sem_03, Sem_08...)
                ETNXXX/ ## una carpeta por materia
                    Partial_1/ ## una carpeta por parcial
                        Topic_NN_nombre-descriptivo/ ## una carpeta por tema
                            [notas]
                    Partial_2/
                    Partial_3/
        MOC/ ## notas de índice a nivel de materia — una MOC por materia, enlaza todas sus Stars
        _app/ ## infraestructura del baúl (no es contenido académico)
            notebooklm/ ## prompts y guías del sistema NotebookLM
                prompts/ ## instrucciones de comportamiento para NotebookLM
                    ETN806/
                        ETN806-P1.md ## prompt P1 Procesos Estocásticos
                        ETN806-P1-legacy.md ## histórico primer prompt P1
                        ETN806-P2.md ## prompt P2 Procesos Estocásticos
                        ETN806-P3.md ## prompt P3 Procesos Estocásticos
                    MAT101/
                        MAT101-study.md ## prompt estudio activo Cálculo 1
                        MAT101-transcription.md ## guía de transcripción cuaderno físico MAT101
                guides/ ## fuentes que se suben al notebook
                    ETN806/
                        ETN806-P3-colas_guide_s.md ## estructuras de colas con Mermaid
                        ETN806-P3-Tikz_markov_guide.md ## diagramas Markov con TikZ
                    MAT101/
                        MAT101_desmos.md ## sintaxis Desmos para Obsidian
                        MAT101_TikzJax.md ## sintaxis TikZJax para Obsidian
                        MAT101_latex.md ## notación LaTeX: cancelaciones, colores, cajas
                        MAT101_library.md ## criterio de fuentes, caps y páginas por tema
                general/ ## guías reutilizables independientes de la materia
                    obsidian_notation.md ## YAML, wikilinks, Cornell, callouts, bloques
                    tikzjax_guide-legacy.md ## sintaxis antigua y genérica de TikZJax (legacy)
                other/ ## archivos en desuso pendientes de revisión
                    MAT101-notebooklm-user_guide.md ## guía de uso personal Cálculo 1
            _config/ :::highlight
                _basic-memory-system.md ## MCP Basic Memory (memoria semántica)
                _claude-boot.md ## punto de entrada de Claude al vault
                _excalidraw-system.md ## configuración del plugin Excalidraw
                _galaxy-system.md ## este archivo — sistema completo: tipos, YAML, convenciones
                _graph-system.md ## Desmos / TikZJax (neutrino)
                _library-system.md ## protocolo de búsqueda y selección de libros
                _mindmap-system.md ## Excalidraw + Mindmap Builder
                _note-system.md ## convención de nombres de notas
                _notebooklm-system.md ## beacon del sistema NotebookLM (transcripción + estudio)
                _pdf-system.md ## sistema de integración de PDFs
                _sync-system.md ## sincronización GitHub + Mega
                _TABnote-system.md ## apuntes de tablet (Samsung Notes → supernova)
                _template-system.md ## sistema de plantillas Templater
                _claude-matter-boot.md ## generador de contexto para Claude
                _ToDo-system.md ## pendientes del sistema
            _appnotes/ ## guías de herramientas usadas dentro del baúl
                tags_notes.md ## documentación del sistema de tags
            scripts/ ## scripts de automatización para mantenimiento del baúl
                tag_routs_scripts/
            solve/ ## problemas conocidos y sus soluciones
                git_solve.md ## soluciones a conflictos de git y sincronización
        _assets/ ## archivos visuales exportados — .png .svg .jpeg desde Desmos, Excalidraw o imágenes insertadas — se nombran igual que la nota fuente
        Excalidraw/
            Constellations/ ## mapas mentales galaxy (Excalidraw + Mindmap Builder) — galaxy_body: constellation
		    Observatory/ ## dibujos técnicos libres sin Mindmap Builder — galaxy_body: observatory
        _PDF/ ## archivos PDF físicos — ver _pdf-system
            PDF-telefonia/ ## una carpeta por materia/tema en texto (no sigla ETNXXX)
            PDF-921/
            PDF-nombre/ ## la organización semántica la llevan los nombres y las notas asteroid en Semesters/
        _projects/ ## proyectos activos y backlog de ideas
            tsk_alias.md ## slots de proyecto — 5 slots activos + 1 standby + 1 emergencia
            tsk_tpl.md ## plantilla base para los slots
            _ideas.md ## backlog de ideas futuras (sin galaxy_body)
        _skills/ ## skills de sesión de Claude (work, plan, close, setup, boot) — cada archivo define el comportamiento de Claude para un tipo de tarea específica
        _templates/ ## plantillas de notas de Obsidian — ver _template-system
            tpl-supernova.md ## una plantilla por tipo de cuerpo galaxy
            tpl-star.md
            tpl-planet.md
            tpl-moon.md
            tpl-comet.md
            tpl-nebula.md
            tpl-dwarf.md
            tpl-asteroid.md
            tpl-photon.md
            tpl-bridge.md
            tpl-constellation.md ## Excalidraw + Mindmap Builder
            tpl-observatory.md ## Excalidraw dibujo libre
            tpl-w-initial.md ## workshop: inicio de materia
            tpl-w-transcription.md ## workshop: transcripción por parcial
            tpl-w-study.md ## workshop: estudio por parcial
            tpl-w-project.md ## workshop: proyecto académico puntual
            alt-B/ ## respaldo
                plantillas-A-respaldo.md ## plantillas Opción A consolidadas (sin ruta dinámica)
        borrar/ ## carpeta de espera antes de eliminar — revisar antes de borrar permanentemente
```

---

## Archivos sin galaxy_body

Estos archivos son operativos — no son notas del vault, no participan del grafo de Obsidian ni del sistema galaxy. Se agrupan aquí por convención.

### Skills de Claude

Instrucciones de comportamiento para Claude. Viven en `_skills/`.

| Archivo            | Rol                                           |
| ------------------ | --------------------------------------------- |
| `_claude-boot.md`  | Arranque de sesión — carga contexto del vault |
| `_claude-work.md`  | Sesión de edición de archivos                 |
| `_claude-plan.md`  | Planificación de proyectos (`_projects/`)     |
| `_claude-close.md` | Cierre de sesión — actualiza el `tsk_`        |
| `_claude-setup.md` | Configuración técnica (plugins, herramientas) |

### Proyectos del usuario

Slots de trabajo activo y backlog. Viven en `_projects/`. Temporales por naturaleza — al cerrar un proyecto se documenta y el slot queda libre.

| Archivo         | Rol                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------ |
| `tsk_alias.md`  | Slot de proyecto activo — 5 slots para proyectos en curso simultáneos                      |
| `tsk_standb.md` | Slot standby — desborde controlado, para un 6to proyecto cuando los 5 slots están ocupados |
| `tsk_emergn.md` | Slot de emergencia — proyecto urgente que no puede esperar a que se libere un slot activo  |
| `tsk_tpl.md`    | Plantilla base para los slots                                                              |
| `_ideas.md`     | Backlog de ideas futuras — sin ciclo de vida fijo                                          |

---

## Convención de nombres de notas

### Patrón

```
ETNXXX-TNN-nombre_descriptivo.md
```

| Campo                | Descripción                                    | Ejemplo                  |
| -------------------- | ---------------------------------------------- | ------------------------ |
| `ETNXXX`             | Sigla de la materia                            | `ETN806`                 |
| `TNN`                | Número de tema con cero al frente              | `T01`, `T03`             |
| `nombre_descriptivo` | Slug corto en español o ingles, con barra baja | `ejemplo_pdf_definicion` |

Usar `T00` para notas que pertenecen al parcial completo y no a un tema específico (formularios, enunciados de práctica, referencias generales).

Para notas Bridge que conectan dos materias: `ETN806-ETN302-nombre_del_puente.md`

### Ejemplos

```
ETN806-T01-joint_pdf_definition.md
ETN806-T01-marginal_density_formula.md
ETN806-T01-normalization_k_solved.md
ETN806-T01-support_region_triangle.md
ETN806-T02-independence_statistical_test.md
ETN806-T02-variance_sum_covariance.md
ETN806-T00-formulario_partial2.md
ETN806-T00-practica2_enunciados.md
ETN806-ETN302-laplace_vs_probability.md
```

> El semestre y el parcial **no van en el nombre** — ya están codificados en la ruta de carpeta y en el YAML. Sin redundancia.

---

## Tipos de cuerpo galaxy

El campo `galaxy_body` en el YAML define el rol de la nota. Catorce tipos:

| `galaxy_body`   | Símbolo | Rol                                                                                                                                                            |
| --------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `star`          | ☀️      | MOC de un tema. Enlaza todas las notas en órbita. Una por carpeta de tema.                                                                                     |
| `planet`        | 🪐      | Nota de teoría central. Un concepto por nota.                                                                                                                  |
| `moon`          | 🌙      | Propiedad, fórmula o resultado clave. Siempre orbita un planet.                                                                                                |
| `comet`         | ☄️      | Ejercicio resuelto. Referencia los conceptos que usó.                                                                                                          |
| `nebula`        | 🌫️     | Agrupador de sesión. Enlaza comets de una clase o auxiliatura.                                                                                                 |
| `dwarf`         | ⬛       | Resumen. Revisión condensada de un tema o parcial.                                                                                                             |
| `asteroid`      | 🪨      | Referencia externa. Extracto de libro, nota de PDF, paper.                                                                                                     |
| `photon`        | 💡      | Imagen estática pura. Archivo visual (.png, .jpg, .svg) pegado o arrastrado. Siempre adjunto a otra nota.                                                      |
| `neutrino`      | ⚛️      | Código que genera una imagen. Bloque Desmos o TikZJax embebido en un planet o comet. No es nota separada — vive dentro de la nota host. Ver [[_graph-system]]. |
| `constellation` | 🌌      | Mapa mental galaxy. Excalidraw + Mindmap Builder. Uno por parcial o tema. Vive en `Excalidraw/Constellations/`.                                           |
| `observatory`   | 🔭      | Dibujo técnico libre en Excalidraw sin Mindmap Builder. Vive en `Excalidraw/Observatory/`.                                                                |
| `bridge`        | 🌉      | Conexión entre materias. Enlaza conceptos de dos galaxias distintas.                                                                                           |
| `beacon`        | 📡      | Guía de infraestructura del vault. Herramientas, procesos, soluciones. Vive en `_app/`.                                                                        |
| `supernova`     | ✨       | Transcripción bruta de NotebookLM de apuntes de clase. Material en bruto pendiente de disección en notas galaxy. Ver [[_TAB_note-system]].                      |
| `workshop` | 🔧 | Tarea académica por materia. Seguimiento de transcripción, estudio o proyecto puntual dentro de una materia. Vive en `Semesters/`. Ver [[_template-system]]. |

---

## El grafo de Obsidian y los wikilinks

El grafo nativo de Obsidian **solo detecta `[[wikilinks]]` escritos en el cuerpo de la nota** — el YAML no genera conexiones visibles en el grafo. Para construir el grafo sin ensuciar el modo de lectura se usan **bloques de comentario `%%`**:

```markdown
%%
# galaxy-links
[[Semesters/Sem_01/MAT101/Partial_1/T00-numeros_reales/MAT101-T00-axiomas_cuerpo.md]]
[[Semesters/Sem_01/MAT101/Partial_1/T00-numeros_reales/MAT101-T00-axiomas_igualdad.md]]
[[Semesters/Sem_01/MAT101/Partial_1/T00-numeros_reales/MAT101-T00-teoremas_reales.md]]
## Links a notas pendientes de crear
[[Semesters/Sem_01/MAT101/Partial_1/T00-numeros_reales/no_existe.md]]
%%
```

Los bloques `%%...%%` son **invisibles en modo lectura y preview**, pero el motor del grafo los detecta y dibuja las conexiones. Cada nota debe tener su bloque `%%` al final con todos sus enlaces galaxy.

> Los wikilinks dentro del bloque `%%` pueden apuntar a archivos que aún no existen. Obsidian los muestra en el grafo como nodos sin contenido. Es una forma válida de planificar notas antes de crearlas — el link queda registrado en el grafo desde el momento en que se escribe.

### Regla: dos capas de conexión

| Capa | Herramienta | Propósito |
|------|------------|-----------|
| Metadatos | YAML (`orbiting`, `orbits`, `concepts_used`...) | Búsquedas, filtros, DataView |
| Grafo visual | `%%wikilinks comentados%%` | Visualización en modo grafo de Obsidian |

Ambas capas deben estar sincronizadas — si un enlace está en el YAML también debe estar en el bloque `%%`.

---

## Plantillas YAML por tipo de cuerpo

> Documentación completa de cada plantilla: [[_template-system]]
> Archivos físicos en `_templates/` — nombrados `tpl-[tipo].md`
> Las plantillas de `Semesters/` usan **Opción B**: Templater pregunta materia, semestre, parcial, tema y nombre, y mueve el archivo automáticamente a la ruta correcta.

> ⚠️ Los bloques `%%` en estos ejemplos usan rutas de archivos inexistentes como ilustración. En notas reales usar siempre ruta relativa completa desde la raíz del vault (`E:\University_vault_2026`). Ver formato en [El grafo de Obsidian y los wikilinks](#el-grafo-de-obsidian-y-los-wikilinks).

---

### star
```yaml
---
title: "ETN806 — P2 — T01: Densidad de probabilidad conjunta"
galaxy_body: star
subject: ETN806
semester: 8
partial: 2
topic: 1
topic_name: joint-probability-density
orbiting:
  - "[[ETN806-T01-joint-pdf-definition]]"
  - "[[ETN806-T01-marginal-density-formula]]"
  - "[[ETN806-T01-normalization-k-solved]]"
tags: [ETN806, galaxy-star, P2, T01]
date_created: YYYY-MM-DD
status: activo
---
```

```markdown
%%
# galaxy-links
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-planet-nombre.md]]
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-moon-nombre.md]]
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-comet-nombre.md]]
%%
```

---

### planet
```yaml
---
title: "PDF Conjunta — Definición y región de soporte"
galaxy_body: planet
subject: ETN806
semester: 8
partial: 2
topic: 1
star: "[[ETN806-T01-star]]"
moons:
  - "[[ETN806-T01-marginal-density-formula]]"
comets:
  - "[[ETN806-T01-normalization-k-solved]]"
tags: [ETN806, galaxy-planet, P2, T01]
date_created: YYYY-MM-DD
status: activo
---
```

```markdown
%%
# galaxy-links
[[MOC/ETNXXX-TNN-star.md]]
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-moon-nombre.md]]
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-comet-nombre.md]]
%%
```

> Al crear con `tpl-planet.md`, Templater precarga `subject`, `semester`, `partial` y los tags automáticamente.

---

### moon
```yaml
---
title: "Densidad marginal — Fórmula"
galaxy_body: moon
subject: ETN806
semester: 8
partial: 2
topic: 1
orbits: "[[ETN806-T01-joint-pdf-definition]]"
tags: [ETN806, galaxy-moon, P2, T01]
date_created: YYYY-MM-DD
---
```

```markdown
%%
# galaxy-links
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-planet-nombre.md]]
%%
```

---

### comet
```yaml
---
title: "ETN806 — P2 — Normalización k: Resuelto"
galaxy_body: comet
subject: ETN806
semester: 8
partial: 2
topic: 1
source: "examen"
concepts_used:
  - "[[ETN806-T01-joint-pdf-definition]]"
  - "[[ETN806-T01-marginal-density-formula]]"
status: pendiente
tags: [ETN806, galaxy-comet, P2, T01]
date_created: YYYY-MM-DD
---
```

```markdown
%%
# galaxy-links
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-planet-nombre.md]]
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-moon-nombre.md]]
%%
```

---

### nebula
```yaml
---
title: "ETN806 — Sesión de auxiliatura 2026-05-20"
galaxy_body: nebula
subject: ETN806
semester: 8
partial: 2
session_date: 2026-05-20
comets:
  - "[[ETN806-T01-normalization-k-solved]]"
  - "[[ETN806-T02-independence-statistical-test]]"
tags: [ETN806, galaxy-nebula, P2]
---
```

```markdown
%%
# galaxy-links
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-comet-nombre.md]]
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-comet-nombre2.md]]
%%
```

---

### dwarf
```yaml
---
title: "ETN806 — Resumen P2"
galaxy_body: dwarf
subject: ETN806
semester: 8
partial: 2
covers:
  - "[[ETN806-T01-star]]"
  - "[[ETN806-T02-star]]"
tags: [ETN806, galaxy-dwarf, P2]
date_created: YYYY-MM-DD
---
```

```markdown
%%
# galaxy-links
[[MOC/ETNXXX-T01-star.md]]
[[MOC/ETNXXX-T02-star.md]]
%%
```

---

### asteroid

El `asteroid` con PDF tiene YAML extendido — ver [[_pdf_pp-system]] para el detalle completo.

```yaml
---
title: "Papoulis — Cap. 6: Variables aleatorias"
galaxy_body: asteroid
subject: ETN806
semester: 8
partial: 2
topic: 1
source_type: pdf-libro
source_title: "Probability, Random Variables and Stochastic Processes"
source_author: "Papoulis"
source_chapter: "6"
pdf_file: "[[ETN806-T00-libro-papoulis-cap6.pdf]]"
related_planets:
  - "[[ETN806-T01-joint-pdf-definition]]"
tags: [ETN806, galaxy-asteroid, P2, T01]
date_created: YYYY-MM-DD
status: en-proceso
---
```

```markdown
%%
# galaxy-links
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-planet-nombre.md]]
%%
```

---

### photon

`photon` es una imagen estática pura — archivo visual (.png, .jpg, .svg) pegado o arrastrado. Sin código, sin lógica.

```yaml
---
title: "Región de soporte — captura"
galaxy_body: photon
photon_type: image
attached_to: "[[ETN806-T01-normalization-k-solved]]"
subject: ETN806
tags: [ETN806, galaxy-photon, P2, T01]
date_created: YYYY-MM-DD
---
```

```markdown
%%
# galaxy-links
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-nombre-adjunto.md]]
%%
```

`photon_type` válidos: `image` (png/jpg arrastrado) | `pdf-crop` (recorte de PDF++).

> Para código que genera imagen (Desmos, TikZJax) → `neutrino`. Ver [[_graph-system]].
> Para Excalidraw → `constellation` o `observatory`. Ver [[_mindmap-system]].

---

### neutrino

`neutrino` es código que genera una imagen. **No existe como nota separada** — vive embebido dentro de un `planet` o `comet` como bloque de código. El código es la fuente de verdad; la imagen es su output.

Herramientas soportadas:

| `neutrino_type` | Bloque de código | Caché |
|----------------|-----------------|-------|
| `desmos` | ` ```desmos-graph ` | `.cache/desmos/` — SVGs en disco, dentro del vault |
| `tikz` | ` ```tikz ` | IndexedDB de Electron — interno, no accesible como archivo |

Como `neutrino` no es nota separada, **no tiene YAML propio ni bloque `%%`**. La nota host (planet o comet) lleva el YAML y los wikilinks.

Ejemplo — bloque Desmos dentro de un planet:

`````markdown
## Región de soporte

```desmos-graph
left=-0.2; right=1.5; bottom=-0.2; top=2.5;
width=500; height=500;
---
y=x|0<=x<=1|RED
y=2-x|0<=x<=1|BLUE
y<2-x|y>x|x>=0|x<=1|#a5d8ff
```
```

Ejemplo — bloque TikZJax dentro de un comet:
```markdown
## Circuito equivalente

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
  \draw (0,0) to[R, l=$R_1$] (3,0);
\end{circuitikz}
\end{document}
```
```

> Documentación completa de cada herramienta: [[_graph-system]]

---

### constellation
```yaml
---
excalidraw-plugin: parsed
tags: [excalidraw, galaxy-constellation]
galaxy_body: constellation
title: "ETN806 — P2: Mapa galaxy Parcial 2"
subject: ETN806
semester: 8
partial: 2
topic:
scope: partial
tools: [excalidraw, mindmap-builder]
date_created: YYYY-MM-DD
status: activo
---
`````

```markdown
%%
# galaxy-links
[[MOC/ETNXXX-T01-star.md]]
[[MOC/ETNXXX-T02-star.md]]
%%
```

> `excalidraw-plugin: parsed` debe ir primero en el YAML — el plugin lo requiere para abrir el archivo como lienzo.
> `scope`: `partial` si cubre el parcial completo | `topic` si cubre un solo tema.

---

### observatory
```yaml
---
excalidraw-plugin: parsed
tags: [excalidraw, galaxy-observatory]
galaxy_body: observatory
title: "Diagrama: Región de integración doble"
subject: ETN806
semester: 8
partial: 2
topic: 1
attached_to: "[[ETN806-T01-joint-pdf-definition]]"
date_created: YYYY-MM-DD
---
```

```markdown
%%
# galaxy-links
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-nombre-adjunto.md]]
%%
```

> `excalidraw-plugin: parsed` debe ir primero en el YAML — el plugin lo requiere para abrir el archivo como lienzo.

---

### bridge
```yaml
---
title: "Bridge: Transformada de Laplace (ETN302) ↔ Funciones generadoras de probabilidad (ETN806)"
galaxy_body: bridge
subjects: [ETN806, ETN302]
semesters: [8, 3]
connects:
  - "[[ETN806-T03-generating-functions]]"
  - "[[ETN302-T05-laplace-transform]]"
tags: [galaxy-bridge, ETN806, ETN302]
date_created: YYYY-MM-DD
---
```

```markdown
%%
# galaxy-links
[[Semesters/Sem_NN/ETNXXX1/Partial_N/Topic_NN_nombre/ETNXXX1-TNN-planet-nombre.md]]
[[Semesters/Sem_NN/ETNXXX2/Partial_N/Topic_NN_nombre/ETNXXX2-TNN-planet-nombre.md]]
%%
```

---

> Tareas y pendientes: [[_ToDo-system]]

---

### supernova

Dos variantes según ciclo de vida — usar `tpl-supernova.md` (pregunta al inicio cuál es).

**Class individual** (`ETN901-class001-P1-jun15.md`):
```yaml
---
title: "ETN901-class001-P1-jun15"
galaxy_body: supernova
subject: ETN901
semester: 9
partial: 1
class_number: 001
class_date: YYYY-MM-DD
subtopics:
  - "1.1 Definicion"
  - "1.2 Propiedades"
related_planets: []
tags: [ETN901, galaxy-supernova, P1]
date_created: YYYY-MM-DD
status: en-proceso
---
```

> Las `class` individuales no necesitan bloque `%%` hasta tener `related_planets`.

**Supernova fusionada** (`ETN901-T1-densidad_probabilidad_conjunta-P1.md`):
```yaml
---
title: "ETN901-T1-densidad_probabilidad_conjunta-P1"
galaxy_body: supernova
subject: ETN901
semester: 9
partial: 1
topic: T1
topic_name: densidad_probabilidad_conjunta
class_parts:
  - "[[ETN901-class001-P1-jun15]]"
  - "[[ETN901-class002-P1-jun17]]"
related_planets:
  - "[[ETN901-T01-definicion-densidad]]"
tags: [ETN901, galaxy-supernova, P1]
date_created: YYYY-MM-DD
status: completo
---
```

```markdown
%%
# galaxy-links
[[Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/ETNXXX-TNN-planet-nombre.md]]
%%
```

> Al fusionar, solo el archivo final lleva las conexiones al grafo. Ver [[_TAB_note-system]] para el ciclo de vida completo.

---

### workshop

Cuatro variantes según el tipo de tarea académica. Usar la plantilla correspondiente en `_templates/`.

**tpl-w-initial** — inicio de materia:
```yaml
---
title: "tsk_ini_ETNXXX"
galaxy_body: workshop
subject: ETNXXX
semester: N
tags: [ETNXXX, workshop, inicio]
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
status: activo
---
```

**tpl-w-transcription** — transcripción por parcial:
```yaml
---
title: "tsk_trans_ETNXXX_PN"
galaxy_body: workshop
subject: ETNXXX
semester: N
partial: N
tags: [ETNXXX, workshop, transcripcion, PN]
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
status: activo
---
```

**tpl-w-study** — estudio por parcial:
```yaml
---
title: "tsk_study_ETNXXX_PN"
galaxy_body: workshop
subject: ETNXXX
semester: N
partial: N
tags: [ETNXXX, workshop, estudio, PN]
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
status: activo
---
```

**tpl-w-project** — proyecto académico puntual:
```yaml
---
title: "tsk_ETNXXX_nombre_proyecto"
galaxy_body: workshop
subject: ETNXXX
semester: N
partial: N
tags: [ETNXXX, workshop, proyecto, PN]
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
status: activo
---
```

```markdown
%%
# galaxy-links
## Links a notas pendientes de crear
%%
```

> Al crear con Templater, pregunta materia, semestre y parcial, y mueve el archivo automáticamente a `Semesters/Sem_NN/ETNXXX/` o `Semesters/Sem_NN/ETNXXX/Partial_N/` según el tipo. `galaxy_body: workshop` en todas las variantes. El bloque `%%` se puebla durante el trabajo.

---
## Registro de decisiones de diseño

| Decisión                                                          | Razón                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `constellation` y `observatory` como tipos separados              | Excalidraw tiene dos modos de uso distintos: mapa mental estructural (con Mindmap Builder) y dibujo técnico libre. Separarlos en tipos galaxy permite filtrarlos con DataView y distinguirlos en el grafo.                                                                                                                                                                                                                                                                                                     |
| `photon` = imagen estática únicamente (2026-05-30)                | Un archivo visual puro (.png, .jpg arrastrado o recorte PDF++) no tiene la misma naturaleza que código que genera una imagen. Mezclarlos en un solo tipo era un error conceptual.                                                                                                                                                                                                                                                                                                                              |
| `neutrino` como tipo separado (2026-05-30)                        | Desmos y TikZJax son código — tienen sintaxis, se editan, se versionan con Git. La imagen es solo su output. Un `neutrino` no es nota separada sino bloque embebido en la nota host. El nombre refleja su naturaleza: no se ve directamente pero genera un efecto visible.                                                                                                                                                                                                                                     |
| `neutrino` vive embebido, no como nota propia                     | Casi nunca justifica nota separada. Su contexto siempre es la teoría o el ejercicio que ilustra.                                                                                                                                                                                                                                                                                                                                                                                                               |
| `photon` ya no incluye Excalidraw ni código generador             | Con `constellation`, `observatory` y `neutrino` dedicados, `photon` queda exclusivamente para imágenes estáticas puras.                                                                                                                                                                                                                                                                                                                                                                                        |
| Canvas desactivado — reemplazado por Excalidraw + Mindmap Builder | Canvas es rígido y no integra con el grafo de Obsidian de forma útil. Excalidraw con Mindmap Builder ofrece auto-layout, atajos de teclado y los archivos `.excalidraw` participan del grafo como notas `.md`.                                                                                                                                                                                                                                                                                                 |
| La galaxia vive en el YAML, no en el nombre del archivo           | Los nombres se mantienen limpios y cortos. El YAML lleva todos los datos semánticos.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Semestre y parcial no van en el nombre del archivo                | Ya están codificados en la ruta de carpeta. Sin redundancia.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Slugs descriptivos en inglés                                      | Legibles en búsqueda sin memorizar códigos. Evita problemas de codificación con tildes.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| T00 para notas de parcial completo                                | Formularios y enunciados pertenecen al parcial, no a un tema específico.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ETN302 se queda como legacy                                       | Renombrar rompería cientos de wikilinks internos.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `beacon` como tipo de infraestructura                             | Las notas de `_app/` no son contenido académico — necesitan un tipo visual propio que las distinga en el grafo sin contaminar los tipos galaxy del contenido real. El nombre refleja su rol: señales de orientación del vault.                                                                                                                                                                                                                                                                                 |
| Números de tema con cero al frente                                | El explorador de archivos ordena correctamente: `T01` antes que `T10`.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Los photons siempre adjuntos                                      | Un visual no tiene significado sin la nota que ilustra.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Bridge como nota explícita                                        | La conexión entre materias es conocimiento valioso en sí mismo.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `borrar/` como carpeta de espera                                  | Más seguro que borrar directamente — revisar antes de eliminar permanentemente.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `_PDF/` como almacén separado de `Semesters/`                     | Los PDFs son fuentes, no conocimiento procesado. El `asteroid` es el puente al grafo.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PDF++ para texto, Annotator para EPUBs/escaneados                 | Cada plugin tiene su dominio sin solaparse. OmniSearch + Text Extractor cubren la búsqueda.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Opción B como sistema oficial para Semesters/ (2026-05-28)        | Las plantillas B preguntan materia, semestre, parcial, tema y nombre, y mueven el archivo automáticamente. Elimina la necesidad de navegar manualmente a la carpeta destino. Las plantillas A quedan en `_templates/alt-B/plantillas-A-respaldo.md`.                                                                                                                                                                                                                                                           |
| YAML híbrido en constellation y observatory (2026-05-28)          | El plugin de Excalidraw requiere `excalidraw-plugin: parsed` en el frontmatter para abrir el archivo como lienzo. Se unifica con los campos galaxy en un solo bloque YAML. Sin este campo el archivo se abre como nota de texto.                                                                                                                                                                                                                                                                               |
| Extensión `.excalidraw.md` en lugar de `.excalidraw`              | Mantener `.md` preserva compatibilidad con YAML, DataView y el grafo de Obsidian. Para usar en excalidraw.com se exporta con el comando del plugin.                                                                                                                                                                                                                                                                                                                                                            |
| `supernova` como tipo #14 (2026-06-24)                            | Las transcripciones de NotebookLM son producción propia, no fuentes externas — forzarlas en `asteroid` rompía el principio producción-propia vs fuente-externa. Material en bruto de alta energía que aún no se ha condensado en notas galaxy. Símbolo ✨. Dos variantes: `class` individual (por sesión, `status: en-proceso`) y fusionada (tema completo, `status: completo`). Slug en español con guion_bajo. Contador `classNNN` corrido por semestre. Ruta: raíz de `Partial_N/`. Ver [[_TAB_note-system]]. |
| Rutas relativas en `galaxy-links` (2026-07-17)                    | Los wikilinks del bloque `%%` usan ruta relativa desde la raíz del vault (`E:\University_vault_2026`). Ejemplo: `[[Semesters/Sem_09/ETN901/Partial_1/ETN901-T01-intro.md]]`. Esto permite a Claude leer cualquier archivo enlazado directamente sin ambigüedad. Links a archivos inexistentes son válidos — Obsidian los muestra como nodos sin contenido en el grafo y sirven para planificar notas antes de crearlas.                                                                                        |
| `_skills/` como carpeta sin `galaxy_body` (2026-07-17)            | Los skills son instrucciones de comportamiento para Claude, no notas del vault. Forzarles un `galaxy_body` sería ruido — no participan del grafo ni del sistema galaxy.                                                                                                                                                                                                                                                                                                                                        |
| `_tasks/` renombrada a `_projects/` (2026-07-18)                  | Nombre más descriptivo — la carpeta contiene proyectos activos y backlog de ideas, no tareas sueltas.                                                                                                                                                                                                                                                                                                                                                                                                          |
| `workshop` aprobado como tipo #15, símbolo 🔧 (2026-07-18)        | Necesidad de monitorear tareas académicas por materia sin mezclar con galaxy bodies de contenido. Cuatro variantes de plantilla según etapa: initial, transcription, study, project.                                                                                                                                                                                                                                                                                                                           |
| Archivos `tsk_` sin `galaxy_body` (2026-07-18)                    | Son slots de trabajo temporal — no son notas del vault ni participan del grafo. Forzarles un `galaxy_body` sería ruido. Al cerrar un proyecto se documenta y el slot queda libre. Su ubicacion esta en la ruta \_projects/ .                                                                                                                                                                                                                                                                                   |
| `_ideas.md` como backlog en `_projects/` (2026-07-18)             | Lista de ideas futuras que pueden convertirse en proyectos activos. Sin `galaxy_body`, sin ciclo de vida fijo. Escalable: `_ideas_2.md` si el primero se satura. Su ruta es \_projects/ .                                                                                                                                                                                                                                                                                                                      |

---

%%
# galaxy-links
[[_app/_config/_template-system.md]]
[[_pdf_pp-system]]
[[_app/_config/_mindmap-system.md]]
[[_app/_config/_note-system.md]]
[[_app/_config/_graph-system.md]]
[[_app/_config/_ToDo-system.md]]
[[_app/_config/_notebooklm-system.md]]

[[_app/_appnotes/claude_prompts]]
[[_claude-plan]]
[[_claude-work]]
[[_claude-boot]]
[[_claude-setup]]
[[_claude-close]]
%%
