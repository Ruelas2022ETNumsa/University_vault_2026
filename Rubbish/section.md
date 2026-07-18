--- _app\_config\_galaxy-system.md ---
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

```markdown
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
```

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

> Al fusionar, solo el archivo final lleva las conexiones al grafo. Ver [[_TABnote-system]] para el ciclo de vida completo.

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
