# 🌌 GALAXY SYSTEM — University Vault

---

## Core Idea

The vault is structured as a **universe of galaxies**. Each subject is a galaxy. Each galaxy has a gravitational center (the subject's MOC), orbiting bodies at different distances (topics, subtopics, notes), and bridges to other galaxies (cross-subject connections).

The galaxy metaphor is **not visual** — it lives in the YAML of each note as metadata that defines the note's role, orbit level, and connections. Obsidian's `[[wikilinks]]` are the gravitational threads between bodies.

The goal is a **digital brain for engineering**: every concept, exercise, property, and reference has a precise location, a descriptive name, and YAML that makes it searchable, filterable, and connectable.

> ETN302 stays as-is. The Galaxy System applies to new subjects going forward.

---

## The Universe — Folder Structure

```
University_Vault/
│
├── Semesters/
│   ├── Sem_03/
│   │   └── ETN302/          ← stays unchanged (legacy)
│   ├── Sem_08/
│   │   └── ETN806/
│   │       ├── Partial_1/
│   │       │   ├── Topic_01_[descriptive-name]/
│   │       │   │   ├── [notes...]
│   │       │   └── Topic_02_[descriptive-name]/
│   │       ├── Partial_2/
│   │       └── Partial_3/
│   └── Sem_NN/
│       └── ETNXXX/
│
├── _app/
│   ├── _config/       ← system files (this file lives here)
│   ├── _appnotes/     ← tool guides (desmos_guide, etc.)
│   └── _assets/       ← images, SVGs, exported files
│
└── _templates/        ← note templates by galaxy body type
```

### Folder naming rules

| Level | Pattern | Example |
|-------|---------|---------|
| Semester | `Sem_NN` | `Sem_08` |
| Subject | `ETNXXX` | `ETN806` |
| Partial | `Partial_N` | `Partial_2` |
| Topic | `Topic_NN_descriptive-name` | `Topic_03_joint-probability` |

Topics use zero-padded numbers (`01`, `02`...) so they sort correctly in the file explorer.

---

## Galaxy Bodies — Note Types

Every note inside a topic folder is a **galaxy body**. The body type determines the note's role, its name prefix, and its YAML.

| Body | Symbol | Role | Name prefix |
|------|--------|------|-------------|
| **Star** | ☀️ | MOC — gravitational center of a topic. Links to all bodies in orbit. | `STAR` |
| **Planet** | 🪐 | Core theory note. One concept per note. | `PLN` |
| **Moon** | 🌙 | Property, formula, or key result. Always orbits a Planet. | `MON` |
| **Comet** | ☄️ | Solved exercise. Passes through multiple concepts. | `CMT` |
| **Nebula** | 🌫️ | Session grouper (class session or auxiliary session). Links to its Comets. | `NBL` |
| **Dwarf** | ⬛ | Summary / condensed review of a topic or partial. | `DWF` |
| **Bridge** | 🌉 | Cross-subject connection note. Links concepts from two different galaxies. | `BRG` |
| **Asteroid** | 🪨 | Reference material — book excerpt, PDF note, external source. | `AST` |
| **Photon** | 💡 | Visual asset note — Desmos graph, Excalidraw, image. Always attached to another body. | `PHT` |

---

## Note Naming Convention

### Full pattern

```
[PREFIX]-[SUBJECT][SEM]-[PARTIAL]-[TOPIC]-[descriptive-name]-[part]
```

### Fields

| Field | Description | Example |
|-------|-------------|---------|
| `PREFIX` | Body type prefix | `PLN`, `CMT`, `MON` |
| `SUBJECT` | Subject code | `ETN806` |
| `SEM` | Semester number | `S08` |
| `PARTIAL` | Partial number | `P2` |
| `TOPIC` | Topic number (zero-padded) | `T03` |
| `descriptive-name` | Short descriptive slug | `joint-pdf-normalization` |
| `part` | Part number if note is split | `1`, `2` (omit if single) |

### Examples

```
STAR-ETN806-S08-P2-T01-joint-probability-density.md
PLN-ETN806-S08-P2-T01-joint-pdf-definition.md
MON-ETN806-S08-P2-T01-marginal-density-formula.md
CMT-ETN806-S08-P2-T01-normalization-k-solved.md
CMT-ETN806-S08-P2-T01-independence-verification-solved.md
NBL-ETN806-S08-P2-T01-session-aux-2026-05-20.md
DWF-ETN806-S08-P2-T01-summary.md
AST-ETN806-S08-P2-T01-papoulis-ch6-excerpt.md
PHT-ETN806-S08-P2-T01-support-region-triangle.md
BRG-ETN806-ETN302-S08-laplace-vs-probability.md
```

### Existing ETN806 files (already renamed)

The current `ETN806-2P-E*.md` files predate the Galaxy System. They map as:

| Current file | Galaxy body | Future equivalent pattern |
|---|---|---|
| `ETN806-2P-E1-...md` | Comet | `CMT-ETN806-S08-P2-T01-....md` |
| `ETN806-Formulario-2doP-...md` | Moon cluster | `MON-ETN806-S08-P2-formulario.md` |
| `ETN806-Practica2-Enunciados-...md` | Asteroid | `AST-ETN806-S08-P2-practica2-enunciados.md` |
| `ETN806-Resuelto-Referencia-...md` | Comet | `CMT-ETN806-S08-P2-T00-docente-referencia.md` |

> These files are **not renamed now**. This mapping is for future reference when the full migration happens.

---

## YAML Template per Body Type

### Star (MOC)
```yaml
---
title: "[Subject] — Partial N — Topic N: [Topic name]"
galaxy_body: star
subject: ETNXXX
semester: N
partial: N
topic: N
topic_name: "[descriptive topic name]"
orbiting:
  - "[[PLN-...]]"
  - "[[MON-...]]"
  - "[[CMT-...]]"
tags: [ETNXXX, galaxy-star, partial-N, topic-N]
date_created: YYYY-MM-DD
status: active
---
```

### Planet (theory)
```yaml
---
title: "[Concept name]"
galaxy_body: planet
subject: ETNXXX
semester: N
partial: N
topic: N
star: "[[STAR-...]]"
moons:
  - "[[MON-...]]"
comets:
  - "[[CMT-...]]"
tags: [ETNXXX, galaxy-planet, partial-N, topic-N, concept-slug]
date_created: YYYY-MM-DD
status: complete
---
```

### Moon (property / formula)
```yaml
---
title: "[Property or formula name]"
galaxy_body: moon
subject: ETNXXX
semester: N
partial: N
topic: N
orbits: "[[PLN-...]]"
tags: [ETNXXX, galaxy-moon, partial-N, topic-N]
date_created: YYYY-MM-DD
---
```

### Comet (solved exercise)
```yaml
---
title: "[Subject] — [Partial] — [Exercise description]"
galaxy_body: comet
subject: ETNXXX
semester: N
partial: N
topic: N
source: "[exam | practice | auxiliary | book]"
concepts_used:
  - "[[PLN-...]]"
  - "[[MON-...]]"
status: "[reviewed | pending]"
tags: [ETNXXX, galaxy-comet, partial-N, topic-N, exercise]
date_created: YYYY-MM-DD
---
```

### Nebula (session grouper)
```yaml
---
title: "[Subject] — Session [date or number]: [topic]"
galaxy_body: nebula
subject: ETNXXX
semester: N
partial: N
session_date: YYYY-MM-DD
comets:
  - "[[CMT-...]]"
tags: [ETNXXX, galaxy-nebula, partial-N, session]
---
```

### Dwarf (summary)
```yaml
---
title: "[Subject] — Summary: [Partial or Topic]"
galaxy_body: dwarf
subject: ETNXXX
semester: N
partial: N
covers:
  - "[[STAR-...]]"
  - "[[PLN-...]]"
tags: [ETNXXX, galaxy-dwarf, partial-N, summary]
date_created: YYYY-MM-DD
---
```

### Asteroid (reference material)
```yaml
---
title: "[Source title] — [Chapter or section]"
galaxy_body: asteroid
subject: ETNXXX
semester: N
partial: N
source_type: "[book | pdf | paper | video]"
source_title: ""
source_author: ""
source_chapter: ""
related_planets:
  - "[[PLN-...]]"
tags: [ETNXXX, galaxy-asteroid, reference]
---
```

### Bridge (cross-subject)
```yaml
---
title: "Bridge: [ConceptA] ([SubjectA]) ↔ [ConceptB] ([SubjectB])"
galaxy_body: bridge
subjects: [ETNXXX, ETNYYY]
semesters: [N, M]
connects:
  - "[[PLN-ETNXXX-...]]"
  - "[[PLN-ETNYYY-...]]"
tags: [galaxy-bridge, ETNXXX, ETNYYY]
---
```

### Photon (visual asset)
```yaml
---
title: "[Description of visual]"
galaxy_body: photon
photon_type: "[desmos | excalidraw | image]"
attached_to: "[[PLN-... or CMT-...]]"
subject: ETNXXX
tags: [ETNXXX, galaxy-photon, visual]
---
```

---

## The [[Wikilink]] Layer

The folder structure gives location. The YAML gives metadata. The `[[wikilinks]]` give **gravity** — the actual connections between bodies.

### Rules for linking

- Every **Planet** links to its **Star** (`star: [[STAR-...]]`) and lists its Moons.
- Every **Moon** links to the Planet it orbits (`orbits: [[PLN-...]]`).
- Every **Comet** lists the Planets and Moons it used (`concepts_used`).
- Every **Star** lists all bodies in its orbit (`orbiting: [...]`).
- Every **Bridge** links to a body in each of the two galaxies it connects.
- **Photons** always attach to exactly one other body (`attached_to`).

### Inside note body

Beyond YAML, use inline wikilinks naturally:

```markdown
The marginal density (see [[MON-ETN806-S08-P2-T01-marginal-density-formula]])
is obtained by integrating the joint PDF over the other variable.
```

---

## TODO List

### Phase 0 — Foundation (current)
- [x] Define Galaxy System concept
- [x] Define folder structure
- [x] Define body types and prefixes
- [x] Define naming convention
- [x] Define YAML templates per body type
- [x] Write this document
- [ ] Update `convencion-notas.md` with Galaxy System summary
- [ ] Create note templates in `_templates/` for each body type

### Phase 1 — ETN806 migration
- [ ] Reorganize ETN806 files into `Semesters/Sem_08/ETN806/Partial_2/`
- [ ] Create topic folders for Partial 2
- [ ] Add Galaxy YAML to existing `ETN806-2P-E*.md` files (Comets)
- [ ] Add Galaxy YAML to Formulario, Practica, Resuelto files
- [ ] Create STAR notes for each Partial 2 topic
- [ ] Create PLN notes for core concepts (joint PDF, marginals, independence, etc.)
- [ ] Create MON notes from the Formulario content
- [ ] Link everything with wikilinks

### Phase 2 — New subjects
- [ ] Apply Galaxy System from day one to any new subject
- [ ] Use `_templates/` note templates for each body type
- [ ] Update `contextogen.md` to reference Galaxy System for new subjects

### Phase 3 — Cross-galaxy
- [ ] Identify concepts shared between ETN806 and other subjects
- [ ] Create Bridge notes for cross-subject connections
- [ ] Build a Universe-level MOC (`0.Universe.md`) linking all galaxy Stars

### Phase 4 — DataView integration (optional)
- [ ] Install DataView plugin
- [ ] Build queries: all Comets by subject, all pending reviews, all Bridges
- [ ] Build dashboard note per subject using DataView

---

## Design Decisions Log

| Decision | Reason |
|----------|--------|
| Names in English | Consistent, searchable, no encoding issues with accents |
| Long descriptive names over short codes | Readable in search, no need to remember codes |
| Galaxy in YAML not in folder structure | Folders give location; YAML gives meaning. Separating concerns. |
| ETN302 stays as legacy | Renaming would break hundreds of internal links |
| Zero-padded topic numbers | File explorer sorts correctly (`Topic_01` before `Topic_10`) |
| Photons always attached | Visual assets have no meaning without the note they illustrate |
| Bridges as explicit notes | Cross-subject insight is valuable knowledge, not just a link |
