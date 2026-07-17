---
title: Convención de Notas — University Vault
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
related_notes:
  - "[[_galaxy-system]]"
  - "[[_template-system]]"
  - "[[_mindmap-system]]"
  - "[[_pdf_pp-system]]"
  - "[[_TABnote-system]]"
  - "[[_ToDo-system]]"
tags:
  - beacon
  - convencion
  - infraestructura
date_created: 2026-05-28
date_updated: 2026-06-24
status: activo
---

# Convención de Notas — University Vault

> Sistema Galaxy: [[_galaxy-system]]
> Sistema de Plantillas: [[_template-system]]
> Sistema Mindmap: [[_mindmap-system]]
> Sistema PDF: [[_pdf_pp-system]]
> Pendientes: [[_ToDo-system]]

> ETN302 = sistema legacy (sin cambios). Todas las materias nuevas = Sistema Galaxy.

---

## LEGACY — Solo ETN302

```
T   → Teoría           W   → Whorled (propiedades)    A  → Sesión de auxiliatura
AA  → Ejercicio aux.   D   → Índice de diagramas       TD → Diagrama de teoría
WD  → Diagrama Whorled AD  → Diagrama de aux.          TT → Teoría de tarea
```

Numeración: `T2.21.302-1` → tipo | tema.subtema | materia | parte

---

## SISTEMA GALAXY — Materias nuevas

### La ruta de carpeta codifica la ubicación

```
Semesters/Sem_NN/ETNXXX/Partial_N/Topic_NN_nombre/[notas]
```

Semestre y parcial **no se repiten** en el nombre del archivo.

---

### Patrón de nombre de archivo

```
ETNXXX-TNN-nombre_descriptivo.md
```

| Campo                                                | Ejemplo                |
| ---------------------------------------------------- | ---------------------- |
| Sigla de la materia                                  | `ETN806`               |
| Número de tema (con cero)                            | `T01`, `T03`           |
| Slug descriptivo en español o inglés, con barra baja | `joint_pdf_definition` |

Usar `T00` para notas de parcial completo (formularios, enunciados, referencias generales).
Para notas Bridge entre dos materias: `ETN806-ETN302-nombre-del-puente.md`

**Ejemplos:**
```
ETN806-T01-joint_pdf_definition.md
ETN806-T01-marginal_density_formula.md
ETN806-T01-normalization_k_solved.md
ETN806-T00-formulario_partial2.md
ETN806-ETN302-laplace_vs_probability.md
```


---

### Caso especial: notas PDF (`asteroid` tipo PDF)

Las notas asteroid que referencian un PDF van directamente en `Partial_N/` (sin entrar a `Topic_NN/`) porque suelen ser referencias generales del parcial. Nombre igual al patrón estándar con `T00` o el tema que corresponda:

```
ETN806-T00-PDF-papoulis_cap6.md
ETN806-T01-PDF-apuntes_conjunta.md
```

---

### Caso especial: notas `supernova`

Dos variantes según el ciclo de vida. Ambas van en la raíz de `Partial_N/` (no dentro de `Topic_NN/`).

**Class individual** — una por sesión de clase, mientras el tema está en proceso:
```
ETNXXX-PN-classNNN-mesdía.md
```
- `classNNN` → contador corrido por semestre, no reinicia por parcial
- `PN` → número de parcial (ej. `P1`)
- `mesdía` → formato abreviado sin separador (ej. `jun15`, `ago03`)

Ejemplos:
```
ETN901-P1-class001-jun15.md
ETN901-P1-class002-jun17.md
ETN901-P1-class003-jun22.md
```

**Supernova fusionada** — cuando el tema está completo, se fusionan todas las class en un solo archivo:
```
ETNXXX-TNN-PNN-slug_del_tema.md
```
- `TNN` → número de tema (ej. `T01`, `T02`) — mismo sistema que el resto del vault
- `slug_del_tema` → nombre en español, guion_bajo entre palabras, sin tildes ni ñ
- `PN` → número de parcial

Ejemplos:
```
ETN901-T01-P1-densidad_probabilidad_conjunta.md
ETN901-T02-P1-variables_aleatorias_continuas.md
```

> Ver [[_TABnote-system]] para el ciclo de vida completo (class → fusionada → diseccionada en notas galaxy).

---

### Tipos de cuerpo galaxy (en el YAML)

| `galaxy_body` | Símbolo | Rol |
|---------------|---------|-----|
| `star` | ☀️ | MOC del tema — enlaza todas las notas en órbita |
| `planet` | 🪐 | Teoría central — un concepto por nota |
| `moon` | 🌙 | Propiedad o fórmula — orbita un planet |
| `comet` | ☄️ | Ejercicio resuelto — referencia los conceptos usados |
| `nebula` | 🌫️ | Agrupador de sesión — enlaza comets de una clase |
| `dwarf` | ⬛ | Resumen — revisión condensada de tema o parcial |
| `asteroid` | 🪨 | Referencia externa — libro, PDF, paper |
| `photon` | 💡 | Imagen estática pura — .png, .jpg arrastrado o recorte de PDF++ |
| `neutrino` | ⚛️ | Código que genera imagen — bloque Desmos o TikZJax, embebido en planet/comet. Sin nota propia. |
| `constellation` | 🌌 | Mapa mental galaxy — Excalidraw + Mindmap Builder |
| `observatory` | 🔭 | Dibujo técnico libre en Excalidraw |
| `beacon` | 📡 | Guía de infraestructura del vault — vive en `_app/` |
| `bridge` | 🌉 | Conexión entre materias |
| `supernova` | ✨ | Transcripción bruta de NotebookLM de apuntes de clase — ver [[_TABnote-system]] |

> `neutrino` no tiene nota propia ni YAML. La nota host (planet/comet) lo contiene.

YAML mínimo requerido para cualquier nota Galaxy:

```yaml
---
galaxy_body: [tipo]
subject: ETNXXX
semester: N
partial: N
topic: N
tags: [ETNXXX, galaxy-[tipo], PN, TNN]
---
```

Ver [[_galaxy-system]] para plantillas YAML completas por tipo.

---

### Conexiones: dos capas

| Capa | Herramienta | Propósito |
|------|-------------|-----------|
| Metadatos | YAML (`orbiting`, `orbits`, `concepts_used`...) | Búsquedas, filtros, DataView |
| Grafo visual | `%%wikilinks comentados%%` al final de la nota | Visualización en modo grafo de Obsidian |

El YAML **no genera conexiones** en el grafo nativo de Obsidian. Los `[[wikilinks]]` dentro de bloques `%%` sí lo hacen y son invisibles en modo lectura. Ambas capas deben estar sincronizadas.

```markdown
%%
# galaxy-links
[[MOC\MAT101-T00-star.md]]
[[Semesters\Sem_01\MAT101\Partial_1\T00-numeros_reales\MAT101-T00-valor_absoluto.md]]

## Links a notas pendientes de crear
[[Semesters/Sem_01/MAT101/Partial_1/T00-numeros_reales/no_existe.md]]
%%
```

---

## Sistema Cornell — layout y marginalia

El vault usa dos plugins complementarios para el formato de apuntes. Ver [[cornell_guide]] para sintaxis completa y uso.

| Plugin             | Bloque                        | Rol                                              |
| ------------------ | ----------------------------- | ------------------------------------------------ |
| Cornell Notes      | `````cornell` (5 backticks)   | Layout dos columnas: Claves \| Desarrollo        |
| Cornell Marginalia | ````marginalia` (4 backticks) | Anotaciones al margen, anidado dentro de cornell |

**Aplica en:** `supernova` · `planet` · `comet` · `dwarf`
**No aplica en:** `star` · `beacon` · `asteroid` · `photon` · `constellation` · `observatory`

---

## Carpetas del baúl

| Carpeta            | Función                                                            |
| ------------------ | ------------------------------------------------------------------ |
| `Semesters/`       | Todo el contenido académico                                        |
| `MOC/`             | Notas de índice por materia, enlazan todas sus stars               |
| `_app/_config/`    | Configuración del sistema: convención, galaxy system, tags         |
| `_app/_appnotes/`  | Guías de herramientas: Desmos, tags, etc.                          |
| `_app/Excalidraw/` | Archivos fuente de Excalidraw — `Constellations/` y `Observatory/` |
| `_app/scripts/`    | Scripts de automatización del baúl                                 |
| `_app/solve/`      | Problemas conocidos y soluciones (git, sync, etc.)                 |
| `.cache/desmos/`   | Caché SVG de Desmos — generado automáticamente por el plugin       |
| `_assets/`         | Imágenes exportadas: .png, .svg, .jpeg                             |
| `_templates/`      | Plantillas de notas — una por tipo de cuerpo galaxy                |
| `_PDF/`            | Archivos PDF físicos — una carpeta por materia                     |
| `_tabnotes_archivo/` | Snapshots PDF de cierre de parcial (apuntes manuscritos propios) — fuera de Git, ver [[_TABnote-system]] |
| `borrar/`          | Zona de espera antes de eliminar archivos permanentemente          |

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_template-system.md]]
[[_app/_config/_mindmap-system.md]]
[[_pdf_pp-system]]
[[_app/_config/_graph-system.md]]
[[_app/_config/_ToDo-system.md]]
%%
