---
title: "Sistema Mindmap — Excalidraw + Mindmap Builder"
galaxy_body: beacon
scope: vault
tool: excalidraw
audience: [usuario, claude]
tags: [beacon, excalidraw, mindmap, infraestructura]
date_created: 2026-05-28
status: activo
---

# Sistema Mindmap — University Vault

> Sistema Galaxy: [[_galaxy-system]]
> Sistema de Plantillas: [[_template-system]]
> Convención de notas: [[_note-system]]

Este documento define cómo se usa Excalidraw dentro del Sistema Galaxy. Excalidraw reemplaza completamente a Canvas de Obsidian.

---

## Idea central

Cada materia tiene mapas mentales visuales que representan su estructura galaxy. Estos mapas viven en Excalidraw usando el script **Mindmap Builder**, que permite construir mapas estructurados con auto-layout y atajos de teclado. Los archivos `.excalidraw` se guardan como `.md` en Obsidian y participan del grafo del vault como cualquier otra nota.

---

## Dos tipos de archivo Excalidraw

| `galaxy_body` | Símbolo | Herramienta | Uso | Carpeta |
|---|---|---|---|---|
| `constellation` | 🌌 | Excalidraw + Mindmap Builder | Mapa mental estructural de una materia, parcial o tema | `_app/Excalidraw/Constellations/` |
| `observatory` | 🔭 | Excalidraw sin Mindmap Builder | Dibujo técnico libre: regiones, esquemas, diagramas | `_app/Excalidraw/Observatory/` |

**Regla:** si vas a construir un mapa mental galaxy → `constellation`. Si vas a dibujar libremente sin estructura de mapa → `observatory`.

---

## Estructura de carpetas

```
_app/
└── Excalidraw/
    ├── Constellations/     ← galaxy_body: constellation
    │   └── ETNXXX-PN-nombre-descriptivo.excalidraw
    └── Observatory/        ← galaxy_body: observatory
        └── ETNXXX-PN-nombre-descriptivo.excalidraw
```

Templater crea las carpetas automáticamente si no existen al momento de crear el archivo.

---

## Convención de nombres

### Patrón

```
ETNXXX-PN-nombre-descriptivo.excalidraw
```

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `ETNXXX` | Sigla de la materia | `ETN806` |
| `PN` | Número de parcial | `P1`, `P2`, `P3` |
| `nombre-descriptivo` | Slug corto en inglés, con guiones | `joint-density`, `integration-region` |

> El número de tema (`TNN`) se omite del nombre cuando el mapa cubre un parcial completo. Si el mapa cubre un solo tema, se puede incluir: `ETN806-P2-T01-joint-density.excalidraw`.

### Ejemplos

```
ETN806-P2-joint-density.excalidraw           ← constellation, cubre parcial completo
ETN806-P2-T01-joint-density.excalidraw       ← constellation, cubre solo el tema 1
ETN806-P2-integration-region.excalidraw      ← observatory, dibujo técnico
```

---

## Granularidad de los mapas

| Nivel | Cuándo usarlo | Ejemplo de nombre |
|-------|--------------|-------------------|
| Parcial completo | Temas cortos o relacionados que caben en un mapa | `ETN806-P2-galaxy-map` |
| Tema específico | Temas muy extensos que merecen su propio mapa | `ETN806-P2-T01-joint-density` |

No hay regla fija — la decisión se toma según la cantidad de nodos. Si el mapa se vuelve difícil de leer, dividir por tema.

---

## Plantillas YAML

### constellation

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: constellation
subject: ETN806
semester: 8
partial: 2
topic:                        # vacío = cubre el parcial completo; llenar si es un tema específico
scope: partial                # partial | topic
tools: [excalidraw, mindmap-builder]
tags: [ETN806, galaxy-constellation, P2]
date_created: YYYY-MM-DD
status: activo
---
```

> Al crear con `tpl-constellation.md`, Templater pide el nombre del archivo y mueve el archivo a `_app/Excalidraw/Constellations/` automáticamente. Los campos de materia, semestre y parcial se completan a mano después de la creación.

Bloque de wikilinks al final:

```markdown
%%
galaxy-links
[[ETN806-T01-star]]
[[ETN806-T02-star]]
[[ETN806-T03-star]]
%%
```

---

### observatory

```yaml
---
title: "<% tp.file.title %>"
galaxy_body: observatory
subject: ETN806
semester: 8
partial: 2
topic: 1
attached_to: "[[ETN806-T01-normalization-k-solved]]"
tags: [ETN806, galaxy-observatory, P2, T01]
date_created: YYYY-MM-DD
---
```

> Al crear con `tpl-observatory.md`, Templater pide el nombre del archivo y mueve el archivo a `_app/Excalidraw/Observatory/` automáticamente.

```markdown
%%
galaxy-links
[[ETN806-T01-normalization-k-solved]]
%%
```

---

## Script Mindmap Builder

### Qué es

Mindmap Builder es un script de la librería de la comunidad de Excalidraw (autor: Zsolt Viczian). Se descarga desde el Script Store dentro de Excalidraw en Obsidian. Es completamente gratuito.

### Qué ofrece

- Auto-layout: los nodos se reorganizan automáticamente al crecer el mapa
- Atajos de teclado para crear nodos sin usar el ratón
- Agrupación recursiva de ramas
- Coloreo automático por nivel de profundidad
- Panel lateral persistente como interfaz de control (se puede desanclar como modal flotante)
- Compatible con wikilinks de Obsidian dentro de los nodos

### Instalación

1. Abrir cualquier archivo `.excalidraw` en Obsidian
2. En la barra de Excalidraw → ícono de scripts (pergamino) → **Script Store**
3. Buscar **Mindmap Builder** → instalar
4. El script queda disponible en la paleta de comandos: `Excalidraw: Run Mindmap Builder`

### Uso básico

| Acción | Atajo |
|--------|-------|
| Activar/desactivar Mindmap Builder | Ejecutar script desde paleta |
| Nuevo nodo hijo | `Enter` sobre nodo seleccionado |
| Nuevo nodo hermano | `Tab` |
| Eliminar nodo | `Delete` / `Backspace` |
| Expandir/colapsar rama | Click en el indicador del nodo |
| Forzar re-layout | Botón en el panel lateral |

> Para el manual completo del script: https://www.visual-thinking-workshop.com/mindmap

---

## Relación con el grafo de Obsidian

Los archivos `.excalidraw` se almacenan como `.md` en Obsidian. Esto significa que:

- Aparecen en el grafo del vault como nodos
- Soportan YAML (el motor de DataView los puede consultar)
- Los `[[wikilinks]]` dentro del cuerpo del archivo generan conexiones en el grafo
- Los wikilinks dentro de bloques `%%` son invisibles en modo lectura pero visibles en el grafo

Un `constellation` de ETN806 que enlaza sus stars aparecerá en el grafo como un nodo central conectado a todos los temas del parcial — exactamente la representación visual de la galaxia.

---

## Plugins instalados y configurados

| Plugin | Tipo | Función | Estado |
|--------|------|---------|--------|
| Excalidraw | Community | Motor principal de dibujo y mapas | ✅ Instalado |
| Templater | Community | Creación dinámica de archivos con YAML preconfigurado y movimiento automático a carpeta correcta | ✅ Instalado y configurado |
| Commander | Community | Botón en ribbon para abrir el selector de plantillas | ✅ Instalado y configurado |

> Canvas de Obsidian: **desactivado** — reemplazado por este sistema.

---

## Flujo de creación de un mapa

```
Clic en el botón del ribbon (selector de plantillas)
        ↓
Elegir tpl-constellation o tpl-observatory
        ↓
Templater pide: nombre del archivo
        ↓
Templater crea el archivo con YAML precargado
y lo mueve automáticamente a Constellations/ u Observatory/
(crea la carpeta si no existe)
        ↓
Se abre el archivo en Excalidraw
        ↓
Activar Mindmap Builder desde paleta (Ctrl+P) — solo para constellation
        ↓
Construir el mapa: star al centro → planets → moons/comets
        ↓
Al terminar: completar campos YAML (subject, semester, partial, topic)
y agregar wikilinks en bloque %% al final del archivo
```

---

## Registro de decisiones de diseño

| Decisión | Razón |
|----------|-------|
| Excalidraw reemplaza Canvas | Canvas es rígido, no integra con el grafo y tiene pocas opciones de personalización. Excalidraw con Mindmap Builder ofrece auto-layout, atajos de teclado, y sus archivos participan del grafo como notas `.md`. |
| Dos carpetas separadas (Constellations / Observatory) | Uso distinto, frecuencia distinta. Constellations es el 80% del uso — tenerla como carpeta por defecto reduce fricción. Observatory es para casos específicos de dibujo técnico. |
| Un solo botón en ribbon para todas las plantillas | Abre el selector de Templater con todas las plantillas disponibles. Evita saturar el ribbon con un botón por tipo de cuerpo galaxy. |
| constellation y observatory usan ruta fija, no dinámica | A diferencia de las plantillas de Semesters/ (Opción B), estas dos plantillas siempre van a la misma carpeta. Templater mueve el archivo automáticamente sin necesidad de preguntar materia ni semestre. |
| Nombre sin número de tema por defecto | Un mapa cubre normalmente un parcial completo. El tema se agrega al nombre solo cuando el mapa es específico de un tema extenso. |
| `photon` no incluye Excalidraw | Con `constellation` y `observatory` dedicados, `photon` queda exclusivamente para Desmos e imágenes exportadas. |

%%
galaxy-links
[[_galaxy-system]]
[[_template-system]]
[[_note-system]]
%%
