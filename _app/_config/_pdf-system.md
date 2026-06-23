---
title: "Sistema PDF — University Vault"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[_note-system]]"
  - "[[_mindmap-system]]"
  - "[[_template-system]]"
  - "[[_ToDo-system]]"
tags: [beacon, pdf, infraestructura]
date_created: 2026-05-28
date_updated: 2026-05-30
status: activo
---

# Sistema PDF — University Vault

> Sistema base: [[_galaxy-system]]
> Convención de notas: [[_note-system]]
> Sistema Mindmap: [[_mindmap-system]]
> Sistema de Plantillas: [[_template-system]]
> Pendientes: [[_ToDo-system]]

---

## Objetivo

El vault es un **cerebro digital para ingeniería**. Las notas Galaxy capturan el conocimiento procesado — teoría, ejercicios, fórmulas, conexiones. Pero el conocimiento tiene fuentes: apuntes del profesor, libros, prácticas oficiales, papers. Esas fuentes llegan como PDF.

El Sistema PDF resuelve una pregunta concreta: **¿dónde viven los PDFs y cómo se conectan al grafo Galaxy?**

La respuesta tiene dos piezas:
- Los archivos PDF físicos viven en `_PDF/` — ordenados por materia, sin contaminar el contenido académico.
- La conexión al grafo se hace a través de notas `asteroid` en `Semesters/` — que son las que llevan YAML, wikilinks y el texto extraído o anotado.

Un PDF sin nota `asteroid` es un archivo mudo. Una nota `asteroid` con `pdf_file` es un nodo activo del cerebro.

---

## Lugar de los PDFs en el mapa del vault

```
University_Vault_2026/
│
├── Semesters/                  ← contenido académico procesado (notas Galaxy)
├── MOC/                        ← índices por materia
├── _app/                       ← infraestructura del vault
│   └── _config/
│       ├── _galaxy-system.md
│       ├── _pdf-system.md      ← este archivo
│       └── ...
├── _assets/                    ← imágenes exportadas (.png, .svg, .jpeg)
├── _templates/                 ← plantillas de notas
│
└── _PDF/                       ← ★ archivos PDF físicos
    ├── ETN806/
    ├── ETN302/
    └── ETNXXX/
```

`_PDF/` sigue la misma lógica que `_assets/`: es un almacén de archivos fuente, no de notas. Una carpeta por materia, sin sub-carpetas de parcial ni de tema — la organización semántica la llevan los nombres de archivo y las notas `asteroid`.

---

## Convención de nombres para PDFs

Mismo patrón del Sistema Galaxy, sin `.md`:

```
ETNXXX-TNN-nombre-descriptivo.pdf
```

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `ETNXXX` | Sigla de la materia | `ETN806` |
| `TNN` | Número de tema | `T01`, `T03` |
| `nombre-descriptivo` | Slug corto en inglés, con guiones | `joint-pdf-slides` |

Usar `T00` para material de parcial completo o referencias generales (libros, formularios oficiales).

### Ejemplos

```
_PDF/ETN806/ETN806-T01-apuntes-pdf-conjunta.pdf
_PDF/ETN806/ETN806-T02-slides-independence.pdf
_PDF/ETN806/ETN806-T00-practica2-enunciados-oficial.pdf
_PDF/ETN806/ETN806-T00-libro-papoulis-cap6.pdf
_PDF/ETN302/ETN302-T05-laplace-apuntes.pdf
```

---

## La nota `asteroid` como puente al grafo

Un PDF solo es útil si está conectado al grafo. La conexión se hace con una nota de tipo `asteroid` ubicada en la carpeta de tema correspondiente dentro de `Semesters/`.

La nota `asteroid` es el nodo activo: tiene YAML, tiene wikilinks, tiene el texto extraído o las citas copiadas con PDF++. El PDF es el archivo fuente al que apunta.

### YAML extendido para `asteroid` con PDF

```yaml
---
title: "Papoulis — Cap. 6: Variables aleatorias conjuntas"
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
  - "[[ETN806-T01-marginal-density-formula]]"
tags: [ETN806, galaxy-asteroid, referencia, pdf, T01, P2]
date_created: YYYY-MM-DD
status: en-proceso
---
```

El campo `pdf_file` enlaza directamente al archivo en `_PDF/`. PDF++ detecta ese link y permite abrir el PDF con un click desde la nota.

### Cuerpo de la nota `asteroid` con citas PDF++

Cuando copias texto desde PDF++ (con el formato Quote configurado), se pega así:

```markdown
## Notas del capítulo

> [!PDF] [[ETN806-T00-libro-papoulis-cap6.pdf#page=142&selection=...|(Papoulis, p.142)]]
> La densidad conjunta f(x,y) queda definida sobre la región de soporte donde la integral doble normaliza a 1.

> [!PDF] [[ETN806-T00-libro-papoulis-cap6.pdf#page=145&selection=...|(Papoulis, p.145)]]
> La densidad marginal se obtiene integrando sobre toda la variable que se elimina.
```

Cada callout `[!PDF]` es un link a la página exacta del PDF. Doble click sobre el highlight en el PDF lleva de vuelta a esta nota.

---

## Flujo de trabajo: de PDF a nodo del cerebro

```
1. Consigues un PDF (apunte, libro, práctica oficial)
        ↓
2. Lo renombras con la convención Galaxy
   ETN806-T01-apuntes-pdf-conjunta.pdf
        ↓
3. Lo guardas en _PDF/ETN806/
        ↓
4. Creas una nota asteroid en la carpeta de tema:
   Semesters/Sem_08/ETN806/Partial_2/Topic_01_.../
   ETN806-T01-apuntes-pdf-conjunta.md
        ↓
5. Abres el PDF en Obsidian (PDF++ lo muestra integrado)
        ↓
6. Seleccionas texto → PDF++ copia el link con el callout [!PDF]
        ↓
7. Pegas en la nota asteroid → queda conectado al grafo
        ↓
8. Agregas wikilinks al bloque %% para conectar con planets y stars
```

---

## Plugins del sistema PDF

### PDF++

Lector y anotador principal. Las citas se copian como callouts `[!PDF]` con link a página exacta. Doble click en el highlight del PDF abre la nota `asteroid` correspondiente.

**Ajustes aplicados:**

| Ajuste | Valor | Dónde |
|--------|-------|-------|
| Default location for new attachments | In the folder specified below → `_pdf` | Obsidian Settings → Files and links |
| Dummy file folder path | `_pdf` | PDF++ Settings → Dummy PDF for external files |
| Copy format "Quote" | `> [!PDF] {{linkWithDisplay}}`<br>`> {{text}}` | PDF++ Settings → Copying → Copy formats |

**Cuándo usarlo:** PDFs con texto seleccionable — apuntes, slides, prácticas, libros digitales. Es el 90% del flujo diario.

---

### Annotator

Lector de anotaciones estilo Hypothesis. No tiene configuración global — se activa nota por nota con un campo en el YAML:

```yaml
annotation-target: _PDF/ETN806/ETN806-T01-apuntes-pdf-conjunta.pdf
```

**Ajuste aplicado:**

| Ajuste | Valor | Dónde |
|--------|-------|-------|
| Custom default path | `_pdf` | Annotator Settings → Custom default path |

**Cuándo usarlo:**
- EPUBs — Annotator es la única opción para libros `.epub`
- PDFs escaneados sin texto seleccionable
- Si se prefiere anotar con comentarios largos en estilo Hypothesis

---

### OmniSearch + Text Extractor

OmniSearch indexa todo el vault incluyendo PDFs. **Requiere el plugin compañero "Text Extractor"** instalado y activo para poder leer el contenido de PDFs e imágenes.

**Ajustes aplicados:**

| Ajuste | Valor | Dónde |
|--------|-------|-------|
| PDF content indexing | ✅ Activado | OmniSearch Settings |
| Images OCR indexing | ✅ Activado | OmniSearch Settings |
| Document content indexing | ❌ Desactivado | No se usan archivos Office |
| Images AI indexing | ❌ Desactivado | Requiere plugin extra innecesario |
| Index paths of unsupported files | ✅ Activado | Encuentra Canvas y Excalidraw por nombre |
| Simpler search | ❌ Desactivado | Mantiene el algoritmo BM25 con pesos configurados |
| Downranked folders | `_app`, `_templates`, `_assets` | Empuja infraestructura al fondo de resultados |

**Plugins requeridos:** Text Extractor (Community Plugins — mismo autor que OmniSearch).

---

## Tipos de PDF por `source_type`

| Valor | Descripción | Ejemplo |
|-------|-------------|---------|
| `pdf-apuntes` | Apuntes del profesor o diapositivas | Slides de clase ETN806 |
| `pdf-libro` | Capítulo o sección de libro | Papoulis Cap. 6 |
| `pdf-practica` | Enunciados oficiales de práctica o examen | Práctica 2 ETN806 |
| `pdf-paper` | Artículo académico o paper | Paper de referencia |
| `pdf-formulario` | Formulario oficial de la materia | Formulario P2 ETN806 |

---

## Conexión con los tipos de cuerpo Galaxy

| PDF contiene | Nota que se crea | `galaxy_body` |
|---|---|---|
| Apuntes de un tema específico | Nota de extracción del tema | `asteroid` |
| Libro o capítulo de referencia | Nota de referencia bibliográfica | `asteroid` |
| Enunciados de práctica o examen | Nota de enunciados | `asteroid` |
| Ejercicio resuelto en PDF | Nota de ejercicio resuelto | `comet` (con `pdf_file`) |

Un `comet` puede tener `pdf_file` si el ejercicio resuelto viene de un PDF oficial. En ese caso el `comet` apunta al PDF y a los `planets` de los conceptos usados.

---

## Registro de decisiones de diseño

| Decisión                                      | Razón                                                                                                                                                                                                  |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `_PDF/` separado de `Semesters/`              | Los PDFs son archivos fuente, no conocimiento procesado. Mismo principio que `_assets/`.                                                                                                               |
| Una carpeta por materia, sin sub-carpetas     | La organización semántica la llevan los nombres y las notas `asteroid`. Sub-carpetas serían redundancia.                                                                                               |
| La nota `asteroid` como único puente          | El grafo Galaxy no conecta archivos PDF directamente — conecta notas. El `asteroid` es el nodo que traduce el PDF al lenguaje del grafo.                                                               |
| Callout `[!PDF]` para citas                   | Visible, identificable, con link a página exacta. Consistente con el sistema de callouts de Obsidian.                                                                                                  |
| Mismo patrón de nombres que Galaxy            | Sin excepciones al sistema. Un archivo en `_PDF/` y su nota en `Semesters/` tienen el mismo nombre base — solo cambia la extensión.                                                                    |
| `source_type` como campo YAML                 | Permite filtrar con DataView: todos los libros, todas las prácticas, todos los papers de una materia.                                                                                                  |
| PDF++ para texto, Annotator para EPUBs        | Cada plugin tiene su dominio. PDF++ es nativo a Obsidian. Annotator cubre lo que PDF++ no soporta.                                                                                                     |
| Text Extractor como dependencia de OmniSearch | Sin él OmniSearch solo busca en notas markdown. Con él el cerebro busca en todas las fuentes.                                                                                                          |
| Recortes de región PDF++ → `_assets/`         | Las imágenes generadas al recortar una región de un PDF van al destino global de attachments (`_assets/`), no a `_PDF/`. Son visuals, no fuentes. Se tratan como `photon` con `photon_type: pdf-crop`. |

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
[[_mindmap-system]]
[[_template-system]]
[[_ToDo-system]]
%%
