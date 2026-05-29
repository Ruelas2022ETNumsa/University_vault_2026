# Sistema Galaxy — University Vault

> Resumen de convención: [[convencion-notas]]
> Sistema PDF: [[_pdf-system]]
> Sistema Mindmap: [[_mindmap-system]]
> Sistema de Plantillas: [[_template-system]]
> Este baúl es un **cerebro digital para ingeniería**. Cada nota tiene una ubicación precisa, un nombre limpio y un YAML que define su rol y sus conexiones.

---

## Idea central

El baúl está organizado como un **universo de galaxias**. Cada materia es una galaxia. El conocimiento dentro de cada galaxia se estructura en capas orbitales — desde el índice central (star) hacia afuera: teoría, propiedades, ejercicios, referencias y visuales.

La metáfora de la galaxia vive **únicamente en el YAML** de cada nota — no en los nombres de carpetas ni en los nombres de archivo. Las carpetas dan ubicación física. El nombre del archivo da identidad. El YAML da rol, órbita y conexiones. Los `[[wikilinks]]` de Obsidian son los hilos gravitacionales, y los bloques `%%comentados%%` los hacen visibles en el grafo sin aparecer en el modo de lectura.

> **ETN302 es legacy.** Se queda como está. El Sistema Galaxy aplica a todas las materias nuevas.

---

## Mapa de carpetas del baúl

```
University_Vault_2026/
│
├── Semesters/                  ← todo el contenido académico vive aquí
│   └── Sem_NN/                 ← una carpeta por semestre (Sem_03, Sem_08...)
│       └── ETNXXX/             ← una carpeta por materia
│           ├── Partial_1/      ← una carpeta por parcial
│           │   └── Topic_NN_nombre-descriptivo/   ← una carpeta por tema
│           │       └── [notas]
│           ├── Partial_2/
│           └── Partial_3/
│
├── MOC/                        ← notas de índice a nivel de materia
│                                  una MOC por materia, enlaza todas sus Stars
│
├── _app/                       ← infraestructura del baúl (no es contenido académico)
│   ├── _config/                ← archivos de configuración del sistema
│   │   ├── _galaxy-system.md   ← este archivo
│   │   ├── _pdf-system.md      ← sistema de integración de PDFs
│   │   ├── _mindmap-system.md  ← sistema Excalidraw + Mindmap Builder
│   │   ├── _template-system.md ← sistema de plantillas Templater
│   │   ├── convencion-notas.md ← resumen de convención de nombres
│   │   ├── TagsRoute.md        ← referencia del sistema de tags
│   │   ├── _claude-sync.md     ← configuración de comportamiento de Claude
│   │   └── tagroute_parche/
│   │
│   ├── _appnotes/              ← guías de herramientas usadas dentro del baúl
│   │   ├── desmos_guide.md     ← guía unificada Desmos (Usuario + NotebookLM + Claude)
│   │   ├── tags_notes.md       ← documentación del sistema de tags
│   │   └── ...
│   │
│   ├── Excalidraw/             ← archivos fuente de Excalidraw (.excalidraw)
│   │   ├── Constellations/     ← mapas mentales galaxy (Excalidraw + Mindmap Builder)
│   │   │                          galaxy_body: constellation — uno por parcial o tema
│   │   └── Observatory/        ← dibujos técnicos libres sin Mindmap Builder
│   │                              galaxy_body: observatory
│   ├── scripts/                ← scripts de automatización para mantenimiento del baúl
│   │   └── tag_routs_scripts/
│   │
│   ├── solve/                  ← problemas conocidos y sus soluciones
│   │   └── git_solve.md        ← soluciones a conflictos de git y sincronización
│   │
│   └── TagsRoutes/             ← archivos de configuración de rutas de tags
│
├── _assets/                    ← todos los archivos visuales exportados
│                                  .png, .svg, .jpeg exportados desde Desmos,
│                                  Excalidraw, o imágenes insertadas.
│                                  Se nombran igual que la nota fuente.
│
├── _pdf/                       ← archivos PDF físicos — ver [[_pdf-system]]
│   ├── ETN806/                    una carpeta por materia, sin sub-carpetas
│   ├── ETN302/                    la organización semántica la llevan los nombres
│   └── ETNXXX/                    y las notas asteroid en Semesters/
│
├── _templates/                 ← plantillas de notas de Obsidian — ver [[_template-system]]
│   ├── tpl-star.md             ← una plantilla por tipo de cuerpo galaxy
│   ├── tpl-planet.md
│   ├── tpl-moon.md
│   ├── tpl-comet.md
│   ├── tpl-nebula.md
│   ├── tpl-dwarf.md
│   ├── tpl-asteroid.md
│   ├── tpl-photon.md
│   ├── tpl-bridge.md
│   ├── tpl-constellation.md    ← Excalidraw + Mindmap Builder
│   ├── tpl-observatory.md      ← Excalidraw dibujo libre
│   ├── contextogen.md          ← generador de contexto para Claude
│   └── alt-B/                  ← respaldo
│       └── plantillas-A-respaldo.md  ← plantillas Opción A consolidadas (sin ruta dinámica)
│
└── borrar/                     ← carpeta de espera antes de eliminar archivos
                                   revisar antes de borrar permanentemente
```

---

## Convención de nombres de notas

### Patrón

```
ETNXXX-TNN-nombre-descriptivo.md
```

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `ETNXXX` | Sigla de la materia | `ETN806` |
| `TNN` | Número de tema con cero al frente | `T01`, `T03` |
| `nombre-descriptivo` | Slug corto en inglés, con guiones | `joint-pdf-definition` |

Usar `T00` para notas que pertenecen al parcial completo y no a un tema específico (formularios, enunciados de práctica, referencias generales).

Para notas Bridge que conectan dos materias: `ETN806-ETN302-nombre-del-puente.md`

### Ejemplos

```
ETN806-T01-joint-pdf-definition.md
ETN806-T01-marginal-density-formula.md
ETN806-T01-normalization-k-solved.md
ETN806-T01-support-region-triangle.md
ETN806-T02-independence-statistical-test.md
ETN806-T02-variance-sum-covariance.md
ETN806-T00-formulario-partial2.md
ETN806-T00-practica2-enunciados.md
ETN806-ETN302-laplace-vs-probability.md
```

> El semestre y el parcial **no van en el nombre** — ya están codificados en la ruta de carpeta y en el YAML. Sin redundancia.

---

## Tipos de cuerpo galaxy

El campo `galaxy_body` en el YAML define el rol de la nota. Once tipos:

| `galaxy_body` | Símbolo | Rol |
|---------------|---------|-----|
| `star` | ☀️ | MOC de un tema. Enlaza todas las notas en órbita. Una por carpeta de tema. |
| `planet` | 🪐 | Nota de teoría central. Un concepto por nota. |
| `moon` | 🌙 | Propiedad, fórmula o resultado clave. Siempre orbita un planet. |
| `comet` | ☄️ | Ejercicio resuelto. Referencia los conceptos que usó. |
| `nebula` | 🌫️ | Agrupador de sesión. Enlaza comets de una clase o auxiliatura. |
| `dwarf` | ⬛ | Resumen. Revisión condensada de un tema o parcial. |
| `asteroid` | 🪨 | Referencia externa. Extracto de libro, nota de PDF, paper. |
| `photon` | 💡 | Recurso visual. Gráfica Desmos o imagen exportada. Siempre adjunto a otra nota. |
| `constellation` | 🌌 | Mapa mental galaxy. Excalidraw + Mindmap Builder. Uno por parcial o tema. Vive en `_app/Excalidraw/Constellations/`. |
| `observatory` | 🔭 | Dibujo técnico libre en Excalidraw sin Mindmap Builder. Vive en `_app/Excalidraw/Observatory/`. |
| `bridge` | 🌉 | Conexión entre materias. Enlaza conceptos de dos galaxias distintas. |
| `beacon` | 📡 | Guía de infraestructura del vault. Herramientas, procesos, soluciones. Vive en `_app/`. |

---

## El grafo de Obsidian y los wikilinks

El grafo nativo de Obsidian **solo detecta `[[wikilinks]]` escritos en el cuerpo de la nota** — el YAML no genera conexiones visibles en el grafo. Para construir el grafo sin ensuciar el modo de lectura se usan **bloques de comentario `%%`**:

```markdown
%%
galaxy-links
[[ETN806-T01-joint-pdf-definition]]
[[ETN806-T01-marginal-density-formula]]
[[ETN806-T01-normalization-k-solved]]
%%
```

Los bloques `%%...%%` son **invisibles en modo lectura y preview**, pero el motor del grafo los detecta y dibuja las conexiones. Cada nota debe tener su bloque `%%` al final con todos sus enlaces galaxy.

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

Cuerpo de la nota — al final:
```markdown
%%
galaxy-links
[[ETN806-T01-joint-pdf-definition]]
[[ETN806-T01-marginal-density-formula]]
[[ETN806-T01-normalization-k-solved]]
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
galaxy-links
[[ETN806-T01-star]]
[[ETN806-T01-marginal-density-formula]]
[[ETN806-T01-normalization-k-solved]]
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
galaxy-links
[[ETN806-T01-joint-pdf-definition]]
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
galaxy-links
[[ETN806-T01-joint-pdf-definition]]
[[ETN806-T01-marginal-density-formula]]
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
galaxy-links
[[ETN806-T01-normalization-k-solved]]
[[ETN806-T02-independence-statistical-test]]
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
galaxy-links
[[ETN806-T01-star]]
[[ETN806-T02-star]]
%%
```

---

### asteroid

El `asteroid` con PDF tiene YAML extendido — ver [[_pdf-system]] para el detalle completo.

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
galaxy-links
[[ETN806-T01-joint-pdf-definition]]
%%
```

---

### photon
```yaml
---
title: "Región de soporte — Dominio triangular"
galaxy_body: photon
photon_type: desmos
attached_to: "[[ETN806-T01-normalization-k-solved]]"
subject: ETN806
tags: [ETN806, galaxy-photon, P2, T01]
date_created: YYYY-MM-DD
---
```

```markdown
%%
galaxy-links
[[ETN806-T01-normalization-k-solved]]
%%
```

> `photon` no incluye Excalidraw. Para Excalidraw usar `constellation` o `observatory`. Ver [[_mindmap-system]].

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
galaxy-links
[[ETN806-T01-star]]
[[ETN806-T02-star]]
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
galaxy-links
[[ETN806-T01-joint-pdf-definition]]
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
galaxy-links
[[ETN806-T03-generating-functions]]
[[ETN302-T05-laplace-transform]]
%%
```

---

## Lista de tareas

### Fase 0 — Fundación ✅
- [x] Definir concepto del Sistema Galaxy y tipos de cuerpo
- [x] Definir estructura de carpetas y convención de nombres
- [x] Definir plantillas YAML por tipo de cuerpo
- [x] Definir regla de wikilinks comentados `%%` para el grafo
- [x] Escribir `_galaxy-system.md`
- [x] Actualizar `convencion-notas.md`
- [x] Crear `_pdf/` y definir sistema PDF en `_pdf-system.md`
- [x] Configurar plugins PDF++ · Annotator · OmniSearch · Text Extractor
- [x] Definir tipos `constellation` y `observatory` para Excalidraw
- [x] Desactivar Canvas — reemplazado por Excalidraw + Mindmap Builder
- [x] Crear carpetas `_app/Excalidraw/Constellations/` y `_app/Excalidraw/Observatory/`
- [x] Documentar sistema Excalidraw en `_mindmap-system.md`
- [x] Crear `_template-system.md` con documentación completa de plantillas
- [x] Crear plantillas `tpl-constellation.md` y `tpl-observatory.md` en `_templates/`
- [x] Crear plantillas restantes en `_templates/` — star, planet, moon, comet, nebula, dwarf, asteroid, photon, bridge
- [x] Instalar y configurar Templater + Commander para creación rápida de archivos
- [x] Elegir Opción B como sistema oficial para `Semesters/` — plantillas con ruta dinámica
- [x] Corregir `tpl-constellation` y `tpl-observatory` para generar lienzos Excalidraw (YAML híbrido + bloque compressed-json)
- [ ] Configurar Excalidraw — ajustes del plugin pendientes (próxima sesión)

### Fase 1 — Organización ETN806
- [ ] Crear estructura de carpetas: `Semesters/Sem_08/ETN806/Partial_2/Topic_NN.../`
- [ ] Mover archivos ETN806 existentes a las carpetas de tema correctas
- [ ] Agregar YAML galaxy a los archivos `ETN806-2P-E*.md` existentes → `galaxy_body: comet`
- [ ] Agregar YAML galaxy al Formulario → `galaxy_body: moon`
- [ ] Agregar YAML galaxy a Práctica enunciados → `galaxy_body: asteroid`
- [ ] Agregar YAML galaxy a Resuelto Referencia → `galaxy_body: comet`
- [ ] Crear notas star para cada tema del Parcial 2
- [ ] Crear notas planet para los conceptos centrales
- [ ] Crear MOC de la materia en la carpeta `MOC/`
- [ ] Agregar bloques `%%` a todas las notas

### Fase 2 — Materias nuevas
- [ ] Aplicar el Sistema Galaxy desde el primer día a cualquier materia nueva
- [ ] Usar plantillas de `_templates/` para cada tipo de cuerpo
- [ ] Actualizar `contextogen.md` para incluir el campo `galaxy_body` en los contextos generados

### Fase 3 — Conexiones entre galaxias
- [ ] Identificar conceptos compartidos entre materias
- [ ] Crear notas bridge
- [ ] Crear MOC a nivel universo en `MOC/` que enlace todas las Stars de todas las materias

### Fase 4 — DataView (opcional)
- [ ] Instalar plugin DataView
- [ ] Consulta: todos los comets por materia y parcial
- [ ] Consulta: todas las notas pendientes de revisión
- [ ] Consulta: todos los bridges
- [ ] Nota de dashboard por materia usando DataView

---

## Registro de decisiones de diseño

| Decisión | Razón |
|----------|-------|
| `constellation` y `observatory` como tipos separados | Excalidraw tiene dos modos de uso distintos: mapa mental estructural (con Mindmap Builder) y dibujo técnico libre. Separarlos en tipos galaxy permite filtrarlos con DataView y distinguirlos en el grafo. |
| `photon` ya no incluye Excalidraw | Con `constellation` y `observatory` dedicados, `photon` queda limpio para Desmos e imágenes exportadas únicamente. |
| Canvas desactivado — reemplazado por Excalidraw + Mindmap Builder | Canvas es rígido y no integra con el grafo de Obsidian de forma útil. Excalidraw con Mindmap Builder ofrece auto-layout, atajos de teclado y los archivos `.excalidraw` participan del grafo como notas `.md`. |
| La galaxia vive en el YAML, no en el nombre del archivo | Los nombres se mantienen limpios y cortos. El YAML lleva todos los datos semánticos. |
| Semestre y parcial no van en el nombre del archivo | Ya están codificados en la ruta de carpeta. Sin redundancia. |
| Slugs descriptivos en inglés | Legibles en búsqueda sin memorizar códigos. Evita problemas de codificación con tildes. |
| T00 para notas de parcial completo | Formularios y enunciados pertenecen al parcial, no a un tema específico. |
| ETN302 se queda como legacy | Renombrar rompería cientos de wikilinks internos. |
| `beacon` como tipo de infraestructura | Las notas de `_app/` no son contenido académico — necesitan un tipo visual propio que las distinga en el grafo sin contaminar los tipos galaxy del contenido real. El nombre refleja su rol: señales de orientación del vault. |
| Números de tema con cero al frente | El explorador de archivos ordena correctamente: `T01` antes que `T10`. |
| Los photons siempre adjuntos | Un visual no tiene significado sin la nota que ilustra. |
| Bridge como nota explícita | La conexión entre materias es conocimiento valioso en sí mismo. |
| Wikilinks en bloque `%%` | Invisibles en lectura, visibles en el grafo. Grafo limpio sin ensuciar el contenido. |
| Dos capas de conexión (YAML + `%%`) | YAML para búsquedas y DataView. `%%` para visualización en el grafo. Cada una con su propósito. |
| `borrar/` como carpeta de espera | Más seguro que borrar directamente — revisar antes de eliminar permanentemente. |
| `_pdf/` como almacén separado de `Semesters/` | Los PDFs son fuentes, no conocimiento procesado. El `asteroid` es el puente al grafo. |
| PDF++ para texto, Annotator para EPUBs/escaneados | Cada plugin tiene su dominio sin solaparse. OmniSearch + Text Extractor cubren la búsqueda. |
| Opción B como sistema oficial para Semesters/ (2026-05-28) | Las plantillas B preguntan materia, semestre, parcial, tema y nombre, y mueven el archivo automáticamente. Elimina la necesidad de navegar manualmente a la carpeta destino. Las plantillas A quedan en `_templates/alt-B/plantillas-A-respaldo.md`. |
| YAML híbrido en constellation y observatory (2026-05-28) | El plugin de Excalidraw requiere `excalidraw-plugin: parsed` en el frontmatter para abrir el archivo como lienzo. Se unifica con los campos galaxy en un solo bloque YAML. Sin este campo el archivo se abre como nota de texto. |
| Extensión `.excalidraw.md` en lugar de `.excalidraw` | Mantener `.md` preserva compatibilidad con YAML, DataView y el grafo de Obsidian. Para usar en excalidraw.com se exporta con el comando del plugin. |

%%
galaxy-links
[[_template-system]]
[[_pdf-system]]
[[_mindmap-system]]
[[convencion-notas]]
%%
