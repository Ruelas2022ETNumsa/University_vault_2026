# Note Convention — University Vault

> Full system: [[galaxy-system]]
> ETN302 = legacy system (unchanged). All new subjects = Galaxy System.

---

## LEGACY — ETN302 only

```
T   → Theory         W   → Whorled (properties)    A  → Auxiliary session
AA  → Aux exercise   D   → Diagram index            TD → Theory diagram
WD  → Whorled diag   AD  → Aux diagram              TT → Homework theory
```

Numbering: `T2.21.302-1` → type | topic.subtopic | subject | part

---

## GALAXY SYSTEM — New subjects

### Folder path encodes location

```
Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_name/[notes]
```

Semester and partial are **not** repeated in the file name.

---

### File name pattern

```
ETNXXX-TNN-descriptive-name.md
```

| Field | Example |
|-------|---------|
| Subject code | `ETN806` |
| Topic number (zero-padded) | `T01`, `T03` |
| Descriptive slug (English, hyphenated) | `joint-pdf-definition` |

Use `T00` for partial-wide notes (formularios, practice sheets, references).

**Examples:**
```
ETN806-T01-joint-pdf-definition.md
ETN806-T01-marginal-density-formula.md
ETN806-T01-normalization-k-solved.md
ETN806-T00-formulario-partial2.md
ETN806-ETN302-laplace-vs-probability.md   ← Bridge note
```

---

### Galaxy body types (in YAML)

| `galaxy_body` | Symbol | Role |
|---------------|--------|------|
| `star` | ☀️ | Topic MOC — links all orbiting notes |
| `planet` | 🪐 | Core theory — one concept per note |
| `moon` | 🌙 | Property or formula — orbits a planet |
| `comet` | ☄️ | Solved exercise — references concepts used |
| `nebula` | 🌫️ | Session grouper — links comets from one session |
| `dwarf` | ⬛ | Summary — condensed topic or partial review |
| `asteroid` | 🪨 | External reference — book, PDF, paper |
| `photon` | 💡 | Visual — Desmos, Excalidraw, image |
| `bridge` | 🌉 | Cross-subject connection |

Minimum required YAML for any Galaxy note:

```yaml
---
galaxy_body: [type]
subject: ETNXXX
semester: N
partial: N
topic: N
tags: [ETNXXX, galaxy-[type], PN, TNN]
---
```

See [[galaxy-system]] for full YAML templates and wikilink rules.

---

## Vault Folders

| Folder | Purpose |
|--------|---------|
| `Semesters/` | All academic content |
| `MOC/` | Subject-level index notes linking all Stars |
| `_app/_config/` | System config: convention, galaxy system, tag routes |
| `_app/_appnotes/` | Tool guides: Desmos, tags, etc. |
| `_app/Canvas/` | Obsidian Canvas visual maps |
| `_app/Excalidraw/` | Raw Excalidraw source files |
| `_app/scripts/` | Vault automation scripts |
| `_app/solve/` | Known issues and solutions (git, sync, etc.) |
| `_assets/` | Exported images: .png, .svg, .jpeg |
| `_templates/` | Note templates — one per galaxy body type |
| `borrar/` | Staging area for files pending deletion |
