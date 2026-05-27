# Note Convention — University Vault

> Full system documented in: [[galaxy-system]]
> ETN302 uses the legacy prefix system (below). All new subjects use the Galaxy System.

---

## LEGACY SYSTEM — ETN302 only

Prefixes for ETN302 files (do not apply to new subjects):

```
T     → Teoría principal de un subtema
W     → Whorled: propiedades/ventanas/resultados importantes
A     → Auxiliatura: archivo agrupador de una sesión
AA    → Auxiliatura Adicional: ejercicios individuales de aux.
E     → Ejercicio: imagen o ejercicio de clase
D     → Diagrama: índice de SVGs/imágenes del tema
TD    → Teoría-Diagrama: SVG que acompaña una nota T
WD    → Whorled-Diagrama: SVG de una propiedad W
AD    → Auxiliatura-Diagrama: SVG de ejercicio de aux.
TT    → Teoría de Tarea: ejercicios del libro/tarea
```

Numbering:
```
T2.21.302-1
│ │  │    └─ part number within subtopic
│ │  └────── subject code
│ └────────── subtopic (2.1 = topic 2, subtopic 1)
└──────────── type prefix
```

---

## GALAXY SYSTEM — All new subjects

### Folder structure

```
Semesters/
└── Sem_NN/
    └── ETNXXX/
        └── Partial_N/
            └── Topic_NN_descriptive-name/
                └── [notes]
```

### Body types and prefixes

| Prefix | Body        | Role                                                  |
| ------ | ----------- | ----------------------------------------------------- |
| `STAR` | ☀️ Star     | MOC — topic index, links all orbiting notes           |
| `PLN`  | 🪐 Planet   | Core theory — one concept per note                    |
| `MON`  | 🌙 Moon     | Property, formula, key result — orbits a Planet       |
| `CMT`  | ☄️ Comet    | Solved exercise — references multiple concepts        |
| `NBL`  | 🌫️ Nebula  | Session grouper — links Comets from one class session |
| `DWF`  | ⬛ Dwarf     | Summary — condensed review of a topic or partial      |
| `AST`  | 🪨 Asteroid | Reference material — book, PDF, external source       |
| `PHT`  | 💡 Photon   | Visual asset — Desmos graph, Excalidraw, image        |
| `BRG`  | 🌉 Bridge   | Cross-subject connection — links two galaxies         |

### Note naming pattern

```
[PREFIX]-[SUBJECT]-S[NN]-P[N]-T[NN]-[descriptive-name]-[part].md
```

Examples:
```
STAR-ETN806-S08-P2-T01-joint-probability-density.md
PLN-ETN806-S08-P2-T01-joint-pdf-definition.md
MON-ETN806-S08-P2-T01-marginal-density-formula.md
CMT-ETN806-S08-P2-T01-normalization-k-solved.md
AST-ETN806-S08-P2-T01-papoulis-ch6-excerpt.md
PHT-ETN806-S08-P2-T01-support-region-triangle.md
BRG-ETN806-ETN302-laplace-vs-probability.md
```

### Required YAML field per body

Every Galaxy note must include `galaxy_body` in its YAML:

```yaml
galaxy_body: star | planet | moon | comet | nebula | dwarf | asteroid | photon | bridge
```

See [[galaxy-system]] for full YAML templates per body type.

### Wikilink rules

- `STAR` lists all orbiting notes in YAML (`orbiting: [...]`)
- `PLN` links to its `STAR` and lists its `MON` notes
- `MON` links to the `PLN` it orbits (`orbits: [[PLN-...]]`)
- `CMT` lists all `PLN` and `MON` it uses (`concepts_used: [...]`)
- `PHT` always attaches to exactly one other note (`attached_to: [[...]]`)
- `BRG` links to one note in each of the two subjects it connects
