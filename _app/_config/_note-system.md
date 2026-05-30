---
title: "Convención de Notas — University Vault"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[_template-system]]"
  - "[[_mindmap-system]]"
  - "[[_pdf-system]]"
  - "[[_ToDo-system]]"
tags: [beacon, convencion, infraestructura]
date_created: 2026-05-28
date_updated: 2026-05-30
status: activo
---

# Convención de Notas — University Vault

> Sistema Galaxy: [[_galaxy-system]]
> Sistema de Plantillas: [[_template-system]]
> Sistema Mindmap: [[_mindmap-system]]
> Sistema PDF: [[_pdf-system]]
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
ETNXXX-TNN-nombre-descriptivo.md
```

| Campo | Ejemplo |
|-------|---------|
| Sigla de la materia | `ETN806` |
| Número de tema (con cero) | `T01`, `T03` |
| Slug descriptivo en inglés, con guiones | `joint-pdf-definition` |

Usar `T00` para notas de parcial completo (formularios, enunciados, referencias generales).
Para notas Bridge entre dos materias: `ETN806-ETN302-nombre-del-puente.md`

**Ejemplos:**
```
ETN806-T01-joint-pdf-definition.md
ETN806-T01-marginal-density-formula.md
ETN806-T01-normalization-k-solved.md
ETN806-T00-formulario-partial2.md
ETN806-ETN302-laplace-vs-probability.md
```

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
| `photon` | 💡 | Visual — Desmos, Excalidraw, imagen |
| `constellation` | 🌌 | Mapa mental galaxy — Excalidraw + Mindmap Builder |
| `observatory` | 🔭 | Dibujo técnico libre en Excalidraw |
| `beacon` | 📡 | Guía de infraestructura del vault — vive en `_app/` |
| `bridge` | 🌉 | Conexión entre materias |

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
galaxy-links
[[ETN806-T01-star]]
[[ETN806-T01-marginal-density-formula]]
%%
```

---

## Carpetas del baúl

| Carpeta | Función |
|---------|---------|
| `Semesters/` | Todo el contenido académico |
| `MOC/` | Notas de índice por materia, enlazan todas sus stars |
| `_app/_config/` | Configuración del sistema: convención, galaxy system, tags |
| `_app/_appnotes/` | Guías de herramientas: Desmos, tags, etc. |
| `_app/Excalidraw/` | Archivos fuente de Excalidraw — `Constellations/` y `Observatory/` |
| `_app/scripts/` | Scripts de automatización del baúl |
| `_app/solve/` | Problemas conocidos y soluciones (git, sync, etc.) |
| `_app/TagsRoutes/` | Archivos de configuración de rutas de tags |
| `_assets/` | Imágenes exportadas: .png, .svg, .jpeg |
| `_templates/` | Plantillas de notas — una por tipo de cuerpo galaxy |
| `_pdf/` | Archivos PDF físicos — una carpeta por materia |
| `borrar/` | Zona de espera antes de eliminar archivos permanentemente |

%%
galaxy-links
[[_galaxy-system]]
[[_template-system]]
[[_mindmap-system]]
[[_pdf-system]]
[[_ToDo-system]]
%%
