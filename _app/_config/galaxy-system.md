# Galaxy System — University Vault

> This vault is a **digital brain for engineering**. Every note has a precise location, a clean name, and YAML that defines its role and connections.
> Full convention summary: [[convencion-notas]]

---

## Core Idea

The vault is organized as a **universe of galaxies**. Each subject is a galaxy. Knowledge inside each galaxy is structured in orbital layers — from the central index (Star) outward to theory, properties, exercises, references, and visuals.

The galaxy metaphor lives **entirely in the YAML** of each note, not in folder names or file names. Folders give physical location. File names give identity. YAML gives role, orbit, and connections. Obsidian `[[wikilinks]]` are the gravitational threads.

> **ETN302 is legacy.** It stays unchanged. Galaxy System applies to all new subjects.

---

## Vault Folder Map

```
University_Vault_2026/
│
├── Semesters/                  ← all academic content lives here
│   └── Sem_NN/                 ← one folder per semester (Sem_03, Sem_08...)
│       └── ETNXXX/             ← one folder per subject
│           ├── Partial_1/      ← one folder per partial exam period
│           │   └── Topic_NN_descriptive-name/   ← one folder per topic
│           │       └── [notes]
│           ├── Partial_2/
│           └── Partial_3/
│
├── MOC/                        ← Map of Content notes — universe-level index
│                                  one MOC per subject, links all its Stars
│
├── _app/                       ← vault infrastructure (not academic content)
│   ├── _config/                ← system config files
│   │   ├── galaxy-system.md    ← this file
│   │   ├── convencion-notas.md ← naming convention summary
│   │   ├── TagsRoute.md        ← tag routing reference
│   │   ├── claude.md           ← Claude behavior config
│   │   ├── patch-obsidian.bat  ← obsidian patch scripts
│   │   └── patch-obsidian.ps1
│   │
│   ├── _appnotes/              ← guides for tools used inside the vault
│   │   ├── desmos_guide.md     ← unified Desmos guide (User + NotebookLM + Claude)
│   │   ├── tags_notes.md       ← tag system documentation
│   │   └── ...
│   │
│   ├── Canvas/                 ← Obsidian Canvas files (.canvas)
│   │                              visual maps of subject structure
│   ├── Excalidraw/             ← Excalidraw source files (.excalidraw)
│   │                              raw drawing files before export
│   ├── scripts/                ← automation scripts for vault maintenance
│   │   └── tag_routs_scripts/
│   │
│   ├── solve/                  ← known issues and solutions
│   │   └── git_solve.md        ← git conflict and sync solutions
│   │
│   └── TagsRoutes/             ← tag routing configuration files
│
├── _assets/                    ← all exported visual files
│                                  .png, .svg, .jpeg exported from Desmos,
│                                  Excalidraw, or inserted images.
│                                  Named to match their source note.
│
├── _templates/                 ← Obsidian note templates
│                                  one template per galaxy body type.
│                                  contextogen.md lives here too.
│
└── borrar/                     ← staging folder for files pending deletion
                                   review before permanent removal
```

---

## Note Naming Convention

### Pattern

```
ETNXXX-TNN-descriptive-name.md
```

| Field | Description | Example |
|-------|-------------|---------|
| `ETNXXX` | Subject code | `ETN806` |
| `TNN` | Topic number, zero-padded | `T01`, `T03` |
| `descriptive-name` | Short English slug, hyphenated | `joint-pdf-definition` |

### Examples

```
ETN806-T01-joint-pdf-definition.md
ETN806-T01-marginal-density-formula.md
ETN806-T01-normalization-k-solved.md
ETN806-T01-support-region-triangle.md
ETN806-T02-independence-statistical-test.md
ETN806-T02-variance-sum-covariance.md
ETN806-T00-formulario-partial2.md          ← T00 for partial-wide reference notes
ETN806-T00-practica2-enunciados.md
```

> Semester and partial are **not** in the file name — they are already encoded in the folder path and in the YAML. No redundancy.

> For Bridge notes connecting two subjects: `ETN806-ETN302-laplace-vs-probability.md`

---

## Galaxy Body Types

The `galaxy_body` YAML field defines the note's role. Nine types:

| `galaxy_body` | Symbol | Role |
|---------------|--------|------|
| `star` | ☀️ | MOC for one topic. Links all orbiting notes. One per topic folder. |
| `planet` | 🪐 | Core theory note. One concept per note. |
| `moon` | 🌙 | Property, formula, or key result. Always orbits a Planet. |
| `comet` | ☄️ | Solved exercise. References the concepts it used. |
| `nebula` | 🌫️ | Session grouper. Links Comets from one class or auxiliary session. |
| `dwarf` | ⬛ | Summary. Condensed review of a topic or partial. |
| `asteroid` | 🪨 | External reference. Book excerpt, PDF note, paper. |
| `photon` | 💡 | Visual asset. Desmos graph, Excalidraw, image. Attached to one note. |
| `bridge` | 🌉 | Cross-subject connection. Links concepts from two different subjects. |

---

## YAML Templates

### star
```yaml
---
title: "ETN806 — P2 — T01: Joint Probability Density"
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
status: active
---
```

### planet
```yaml
---
title: "Joint PDF — Definition and Support Region"
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
tags: [ETN806, galaxy-planet, P2, T01, joint-pdf]
date_created: YYYY-MM-DD
status: complete
---
```

### moon
```yaml
---
title: "Marginal Density — Formula"
galaxy_body: moon
subject: ETN806
semester: 8
partial: 2
topic: 1
orbits: "[[ETN806-T01-joint-pdf-definition]]"
tags: [ETN806, galaxy-moon, P2, T01, marginal]
date_created: YYYY-MM-DD
---
```

### comet
```yaml
---
title: "ETN806 — P2 — Normalization k: Solved"
galaxy_body: comet
subject: ETN806
semester: 8
partial: 2
topic: 1
source: "exam"
concepts_used:
  - "[[ETN806-T01-joint-pdf-definition]]"
  - "[[ETN806-T01-marginal-density-formula]]"
status: reviewed
tags: [ETN806, galaxy-comet, P2, T01, exercise]
date_created: YYYY-MM-DD
---
```

### nebula
```yaml
---
title: "ETN806 — Auxiliary Session 2026-05-20"
galaxy_body: nebula
subject: ETN806
semester: 8
partial: 2
session_date: 2026-05-20
comets:
  - "[[ETN806-T01-normalization-k-solved]]"
  - "[[ETN806-T02-independence-statistical-test]]"
tags: [ETN806, galaxy-nebula, P2, session]
---
```

### dwarf
```yaml
---
title: "ETN806 — P2 Summary"
galaxy_body: dwarf
subject: ETN806
semester: 8
partial: 2
covers:
  - "[[ETN806-T01-star]]"
  - "[[ETN806-T02-star]]"
tags: [ETN806, galaxy-dwarf, P2, summary]
date_created: YYYY-MM-DD
---
```

### asteroid
```yaml
---
title: "Papoulis — Ch6: Random Variables"
galaxy_body: asteroid
subject: ETN806
semester: 8
partial: 2
source_type: book
source_title: "Probability, Random Variables and Stochastic Processes"
source_author: "Papoulis"
source_chapter: "6"
related_planets:
  - "[[ETN806-T01-joint-pdf-definition]]"
tags: [ETN806, galaxy-asteroid, reference]
---
```

### photon
```yaml
---
title: "Support Region — Triangular Domain"
galaxy_body: photon
photon_type: desmos
attached_to: "[[ETN806-T01-normalization-k-solved]]"
subject: ETN806
tags: [ETN806, galaxy-photon, visual, desmos]
---
```

### bridge
```yaml
---
title: "Bridge: Laplace Transform (ETN302) ↔ Probability Generating Functions (ETN806)"
galaxy_body: bridge
subjects: [ETN806, ETN302]
semesters: [8, 3]
connects:
  - "[[ETN806-T03-generating-functions]]"
  - "[[ETN302-T05-laplace-transform]]"
tags: [galaxy-bridge, ETN806, ETN302]
---
```

---

## Wikilink Rules

- Every **Star** lists all orbiting notes in YAML (`orbiting: [...]`) and links them inline in its body.
- Every **Planet** links back to its Star and lists its Moons in YAML.
- Every **Moon** declares which Planet it orbits (`orbits: [[...]]`).
- Every **Comet** lists all Planets and Moons it used (`concepts_used: [...]`).
- Every **Nebula** lists all Comets from that session.
- Every **Photon** attaches to exactly one other note (`attached_to: [[...]]`).
- Every **Bridge** links to exactly one note per subject.

---

## TODO List

### Phase 0 — Foundation ✅
- [x] Define Galaxy System concept and body types
- [x] Define folder structure and naming convention
- [x] Define YAML templates per body type
- [x] Write galaxy-system.md
- [x] Update convencion-notas.md
- [ ] Create note templates in `_templates/` for each body type (9 templates)

### Phase 1 — ETN806 organization
- [ ] Create folder structure: `Semesters/Sem_08/ETN806/Partial_2/Topic_NN.../`
- [ ] Move existing ETN806 files into correct topic folders
- [ ] Add Galaxy YAML to existing `ETN806-2P-E*.md` files → galaxy_body: comet
- [ ] Add Galaxy YAML to Formulario → galaxy_body: moon (cluster)
- [ ] Add Galaxy YAML to Practica enunciados → galaxy_body: asteroid
- [ ] Add Galaxy YAML to Resuelto Referencia → galaxy_body: comet
- [ ] Create STAR note for each Partial 2 topic
- [ ] Create PLN notes for core concepts
- [ ] Create subject MOC in `MOC/` folder

### Phase 2 — New subjects
- [ ] Apply Galaxy System from day one to any new subject
- [ ] Use `_templates/` note templates for each body type
- [ ] Update `contextogen.md` to include galaxy_body field in generated contexts

### Phase 3 — Cross-galaxy
- [ ] Identify shared concepts between subjects
- [ ] Create Bridge notes
- [ ] Create universe-level MOC in `MOC/` linking all subject Stars

### Phase 4 — DataView (optional)
- [ ] Install DataView plugin
- [ ] Query: all Comets by subject and partial
- [ ] Query: all pending reviews
- [ ] Query: all Bridge notes
- [ ] Dashboard note per subject

---

## Design Decisions

| Decision | Reason |
|----------|--------|
| Galaxy in YAML, not in file name | File names stay clean and short. YAML carries all semantic data. |
| No semester/partial in file name | Already encoded in folder path. No redundancy. |
| Descriptive English slugs | Readable in search without memorizing codes. Avoids accent encoding issues. |
| T00 for partial-wide notes | Formularios and practice sheets belong to a partial, not a specific topic. |
| ETN302 stays legacy | Renaming would break hundreds of internal wikilinks. |
| Zero-padded topic numbers | File explorer sorts correctly: `T01` before `T10`. |
| Photons always attached | A visual has no meaning without the note it illustrates. |
| Bridge as explicit note | Cross-subject insight is itself valuable knowledge worth capturing. |
| `borrar/` staging folder | Safer than permanent deletion — review before removing. |
