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
date_updated: 2026-06-24
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

El vault es un **cerebro digital para ingeniería**. Las notas Galaxy capturan el conocimiento procesado — teoría, ejercicios, fórmulas, conexiones. Pero el conocimiento tiene fuentes: libros, apuntes del docente, prácticas oficiales. Esas fuentes llegan como PDF.

El Sistema PDF resuelve dos preguntas:
- **¿Dónde viven los PDFs físicos?** → En `_PDF/`, organizados por materia.
- **¿Cómo se conectan al grafo Galaxy?** → A través de notas `.md` generadas con PDF++ o Annotator, guardadas en `Semesters/`.

Los PDFs son archivos fuente — no se renombran, no se tocan. Las notas `.md` son los nodos activos del cerebro.

---

## Estructura de `_PDF/` — estado real en disco

```
_PDF/
├── PDF-601/                    ← materia (nombre descriptivo, no sigla ETN)
│   ├── Memorias de catedra/    ← subcarpeta interna: apuntes del docente por parcial
│   ├── Manuales/               ← subcarpeta interna: material técnico
│   ├── Gpt/                    ← subcarpeta interna: otros
│   ├── Thomas L. Floyd - Digital fundamentals, 11th ed.pdf    ← libro-guía (raíz de materia)
│   ├── Tocci, Widmer, Moss - Sistemas digitales, 10ma Ed.pdf  ← libro-guía (raíz de materia)
│   └── ...
├── PDF-903/                    ← otra materia
│   ├── 903_LIBRO_ING/          ← subcarpeta interna
│   ├── ING_PDF/
│   ├── intel/
│   ├── img903/
│   ├── Kip R. Irvine -7ed- Assembly Language for x86 Processors.pdf  ← libro-guía
│   └── ...
├── PDF-921/
├── PDF-Electrónica analógica/
├── PDF-Microprocesadores/
├── PDF-telefonia/
└── [PDFs sueltos en raíz]      ← archivos legacy sin carpeta asignada — no mover salvo indicación
```

### Convención de carpetas de materia

- Formato: `PDF-nombre` donde `nombre` es el nombre descriptivo de la materia (no la sigla ETN).
- Ejemplo: `PDF-601`, `PDF-telefonia`, `PDF-Electrónica analógica`.
- Una carpeta por materia. No crear subcarpetas nuevas salvo que el docente entregue material separado por parcial — en ese caso la subcarpeta refleja esa división (ej. `Memorias de catedra/`).
- Para materias nuevas: crear `PDF-nombre` siguiendo el mismo patrón.

### Tipos de contenido dentro de cada carpeta de materia

| Tipo | Ubicación dentro de `PDF-nombre/` | Descripción |
|------|-----------------------------------|-------------|
| **Libros-guía** | Raíz de `PDF-nombre/` | Libros de referencia general de la materia. Se mantienen con su nombre original (largo, con autor y edición). |
| **Material del docente** | Subcarpeta interna (`Memorias de catedra/`, etc.) | Apuntes, slides o prácticas entregadas por el docente. Pueden estar separadas por parcial si el docente las entrega así. |

> Los nombres de los PDFs físicos **no se tocan**. Los libros tienen nombres largos con autor y edición — eso está bien. La identidad del archivo en el grafo la da la nota `.md`, no el nombre del PDF.

---

## Notas `.md` generadas desde PDF++ y Annotator

Estas notas son el producto de trabajar con un PDF en Obsidian. Son nodos activos del grafo Galaxy — llevan YAML, wikilinks y el contenido anotado o extraído.

### Convención de nombres

La convención Galaxy se aplica **solo a las notas `.md`**, no a los PDFs físicos:

```
ETNXXX-TNN-PDF-nombre-descriptivo.md
```

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `ETNXXX` | Sigla de la materia | `ETN806` |
| `TNN` | Número de tema o subtema que se está anotando | `T01`, `T03` |
| `nombre-descriptivo` | Slug corto descriptivo del contenido, en español o inglés con guiones | `apuntes-pdf-conjunta`, `slides-independencia` |

Usar `T00` para notas de referencia general no atadas a un tema (libros-guía, formularios, prácticas completas).

**Ejemplos de nombres de nota:**
```
ETN806-T01-PDF-apuntes-pdf-conjunta.md
ETN806-T02-PDF-slides-independencia.md
ETN806-T00-PDF-practica2-enunciados.md
ETN601-T00-PDF-floyd-fundamentos-digitales.md
ETN903-T03-PDF-irvine-modos-direccionamiento.md
```

### Ubicación en el vault

Las notas `.md` van dentro de `Semesters/`, en la carpeta del parcial correspondiente — **sin subcarpeta de Topic**:

```
Semesters/Sem_NN/ETNXXX/Partial_N/ETNXXX-TNN-PDF-nombre-descriptivo.md
```

**Ejemplos:**
```
Semesters/Sem_08/ETN806/Partial_2/ETN806-T01-PDF-apuntes-pdf-conjunta.md
Semesters/Sem_09/ETN901/Partial_1/ETN901-T00-PDF-libro-referencia-cap3.md
```

> Las notas de PDF no tienen `Topic_NN/` porque una sola nota puede cruzar varios temas del parcial (un capítulo de libro, unas slides del docente). Si el contenido es muy específico de un tema, igualmente va en `Partial_N/` sin Topic.

### `galaxy_body` según el tipo de nota

| Contenido de la nota | `galaxy_body` | Cuándo |
|---|---|---|
| Anotaciones, citas, extracción de texto de un PDF | `asteroid` | Trabajando con PDF++ o Annotator sobre libro, apunte o práctica |
| Recorte de región de un PDF (imagen) | `photon` | Usando la herramienta de recorte de PDF++ — la imagen va a `_assets/` |

Una misma sesión de trabajo puede generar una nota `asteroid` (texto extraído) y uno o más `photon` (recortes de figuras o ecuaciones). Son notas separadas.

---

## YAML de las notas PDF

### Para `asteroid` (anotaciones y texto extraído)

```yaml
---
title: "Floyd — Cap. 3: Compuertas lógicas"
galaxy_body: asteroid
subject: ETN601
semester: 6
partial: 1
topic: 3
source_type: pdf-libro
source_title: "Digital Fundamentals, 11th ed."
source_author: "Thomas L. Floyd"
source_chapter: "3"
pdf_file: "Thomas L. Floyd - Digital fundamentals, 11th ed.pdf"
related_planets:
  - "[[ETN601-T03-compuertas-logicas]]"
tags: [ETN601, galaxy-asteroid, pdf, T03, P1]
date_created: YYYY-MM-DD
status: en-proceso
---
```

> `pdf_file` contiene el **nombre exacto del PDF físico** tal como aparece en disco — nombre largo con autor y edición. No se inventa un nombre corto. PDF++ usa este campo para abrir el archivo directamente.

### Para `photon` (recorte de región PDF)

```yaml
---
title: "Figura: tabla de verdad AND-OR"
galaxy_body: photon
photon_type: pdf-crop
subject: ETN601
semester: 6
partial: 1
topic: 3
source_pdf: "Thomas L. Floyd - Digital fundamentals, 11th ed.pdf"
source_page: 87
attached_to: "[[ETN601-T03-compuertas-logicas]]"
tags: [ETN601, galaxy-photon, pdf-crop, T03]
date_created: YYYY-MM-DD
---
```

---

## Tipos de PDF por `source_type`

| Valor | Descripción | Ejemplo |
|-------|-------------|--------|
| `pdf-libro` | Libro-guía de la materia | Floyd, Irvine, Tanenbaum |
| `pdf-apuntes` | Apuntes o slides del docente | Memorias de cátedra |
| `pdf-practica` | Enunciados oficiales de práctica o examen | Práctica 2 ETN806 |
| `pdf-formulario` | Formulario oficial de la materia | Formulario P2 |
| `pdf-paper` | Artículo académico o paper | Paper de referencia |

---

## Flujo de trabajo: de PDF a nodo del cerebro

### Con PDF++ (texto seleccionable)

```
1. Abres el PDF en Obsidian desde su carpeta _PDF/PDF-nombre/
        ↓
2. Seleccionas texto → PDF++ copia el callout [!PDF] con link a página exacta
        ↓
3. Creas la nota .md con la convención Galaxy:
   ETNXXX-TNN-nombre-descriptivo.md
   en Semesters/Sem_NN/ETNXXX/Partial_N/
        ↓
4. Pegas las citas en la nota → quedan conectadas al grafo
        ↓
5. Completas el YAML con source_title, source_author, pdf_file (nombre exacto del PDF)
        ↓
6. Agregas wikilinks al bloque %% para conectar con planets y stars del mismo tema
```

### Con Annotator (EPUBs o PDFs escaneados)

```
1. Creas la nota .md con el YAML mínimo incluyendo:
   annotation-target: _PDF/PDF-nombre/nombre-exacto-del-archivo.pdf
        ↓
2. Obsidian abre el PDF en modo Annotator al abrir la nota
        ↓
3. Anotas directamente sobre el PDF → las anotaciones se guardan en la nota .md
        ↓
4. Agregas YAML completo y wikilinks galaxy al terminar la sesión
```

---

## Plugins del sistema PDF

### PDF++

Lector y anotador principal. Las citas se copian como callouts `[!PDF]` con link a página exacta. Doble click en el highlight del PDF abre la nota correspondiente.

**Ajustes aplicados:**

| Ajuste | Valor | Dónde |
|--------|-------|-------|
| Default location for new attachments | `_PDF` | Obsidian Settings → Files and links |
| Dummy file folder path | `_PDF` | PDF++ Settings → Dummy PDF for external files |
| Copy format "Quote" | `> [!PDF] {{linkWithDisplay}}`<br>`> {{text}}` | PDF++ Settings → Copying → Copy formats |

**Cuándo usarlo:** PDFs con texto seleccionable — libros digitales, slides, prácticas. Es el flujo principal.

### Annotator

Lector estilo Hypothesis. Se activa nota por nota con el campo YAML `annotation-target`.

**Ajuste aplicado:**

| Ajuste | Valor | Dónde |
|--------|-------|-------|
| Custom default path | `_PDF` | Annotator Settings → Custom default path |

**Cuándo usarlo:** EPUBs, PDFs escaneados sin texto seleccionable, o cuando se prefiere anotar con comentarios largos.

### OmniSearch + Text Extractor

OmniSearch indexa todo el vault incluyendo PDFs. Requiere **Text Extractor** instalado y activo.

**Ajustes aplicados:**

| Ajuste | Valor | Dónde |
|--------|-------|-------|
| PDF content indexing | ✅ Activado | OmniSearch Settings |
| Images OCR indexing | ✅ Activado | OmniSearch Settings |
| Document content indexing | ❌ Desactivado | No se usan archivos Office |
| Images AI indexing | ❌ Desactivado | Innecesario |
| Index paths of unsupported files | ✅ Activado | Encuentra Excalidraw por nombre |
| Simpler search | ❌ Desactivado | Mantiene BM25 |
| Downranked folders | `_app`, `_templates`, `_assets` | Empuja infraestructura al fondo |

---

## Registro de decisiones de diseño

| Decisión | Razón |
|----------|-------|
| Los PDFs físicos no se renombran | Los libros tienen nombres canónicos con autor y edición — cambiarlos rompe la referencia. La identidad en el grafo la da la nota `.md`. |
| Notas PDF en `Partial_N/` sin `Topic_NN/` | Una nota de libro o apunte puede cruzar varios temas. Sin Topic evita forzar una clasificación incorrecta. |
| `pdf_file` contiene el nombre exacto del PDF | PDF++ necesita el nombre real del archivo para abrir el link. No se inventa un alias corto. |
| `asteroid` para anotaciones, `photon` para recortes | Son productos distintos: texto procesado vs imagen estática. Cada uno tiene su rol en el grafo. |
| Libros-guía en raíz de `PDF-nombre/` | Son referencias generales de la materia, no atadas a un parcial. Subcarpetas solo para material del docente dividido por parcial. |
| Carpetas `PDF-nombre` no `ETN-XXX` | Convención real heredada del vault anterior. Se mantiene para no romper links existentes. |
| `_PDF/` separado de `Semesters/` | Los PDFs son archivos fuente, no conocimiento procesado. Mismo principio que `_assets/`. |
| Recortes PDF++ → `_assets/` | Son imágenes, no fuentes. Se tratan como `photon` con `photon_type: pdf-crop`. |

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
[[_mindmap-system]]
[[_template-system]]
[[_ToDo-system]]
%%
