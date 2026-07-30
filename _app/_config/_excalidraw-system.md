---
title: Sistema Excalidraw — Configuración del plugin
galaxy_body: beacon
scope: vault
tool: excalidraw
audience:
  - usuario
  - claude
related_notes:
  - "[[_galaxy-system]]"
  - "[[_mindmap-system]]"
  - "[[_template-system]]"
  - "[[_note-system]]"
  - "[[_pdf_pp-system]]"
  - "[[_ToDo-system]]"
tags:
  - beacon
  - excalidraw
  - configuracion
  - infraestructura
date_created: 2026-05-28
date_updated: 2026-05-30
status: pausado
---

# Sistema Excalidraw — Configuración del plugin

> Sistema Galaxy: [[_galaxy-system]]
> Sistema Mindmap: [[_mindmap-system]]
> Sistema de Plantillas: [[_template-system]]
> Convención de notas: [[_note-system]]
> Sistema PDF: [[_pdf_pp-system]]
> Pendientes: [[_ToDo-system]]

Este documento registra la configuración aplicada al plugin `obsidian-excalidraw-plugin` (archivo `data.json`) para alinearla con el Sistema Galaxy. Es la referencia canónica para restaurar o migrar la configuración. 

---

## Versión del plugin

```
obsidian-excalidraw-plugin v2.23.7
Archivo de configuración: .obsidian/plugins/obsidian-excalidraw-plugin/data.json
```

---

## Rutas configuradas

| Campo en data.json | Valor | Razón |
|--------------------|-------|-------|
| `folder` | `Excalidraw` | Carpeta raíz donde viven Constellations/ y Observatory/ |
| `templateFilePath` | `Excalidraw/Template.excalidraw.md` | Plantilla base para nuevos lienzos creados desde el botón de Excalidraw |
| `scriptFolderPath` | `Excalidraw/Scripts` | Carpeta donde el Script Store instala Mindmap Builder y otros scripts |

> `fontAssetsPath` se deja en su valor por defecto — no se usan fuentes CJK en este vault.

---

## Configuración de carpetas (Settings → Excalidraw → Saving)

Excalidraw tiene su propia configuración de destino, independiente de la configuración global de Obsidian (Settings → Files & Links → `_assets`).

| Ajuste | Valor configurado | Razón |
|--------|-------------------|-------|
| Excalidraw folder | `Excalidraw` | Punto de aterrizaje para todos los archivos nuevos |
| Use Excalidraw folder when embedding | `ON` | Los dibujos embebidos desde el command palette caen en `Excalidraw`, no en `_assets` |
| Crop file folder | `Excalidraw/Observatory` | Las imágenes recortadas son dibujos técnicos puntuales → `observatory` |
| Image annotation file folder | `Excalidraw/Observatory` | Anotar una imagen es un dibujo libre → `observatory` |

> La carpeta global de attachments de Obsidian está configurada en `_assets`. Esto afecta imágenes arrastradas desde fuera del vault. Los recortes de PDF++ también van a `_assets/` — ver [[_pdf_pp-system]].

---

## Nombres de archivo por defecto

Estos valores aplican solo si se crea un lienzo desde el botón de Excalidraw **sin usar Templater**. En el flujo normal del Sistema Galaxy los archivos se crean desde Templater y nunca llegan a usar estos prefijos.

| Campo | Valor | Razón |
|-------|-------|-------|
| `drawingFilenamePrefix` | `RENOMBRAR-` | Señal visual de que el archivo necesita ser renombrado según la convención `ETNXXX-PN-nombre` |
| `drawingFilenameDateTime` | `DD-MM-YYYY HH.mm.ss` | Formato de fecha preferido del vault |

---

## Compresión y lectura en modo Markdown

| Campo | Valor | Razón |
|-------|-------|-------|
| `compress` | `true` | Requerido para que las plantillas de Templater generen el bloque `compressed-json` correctamente |
| `decompressForMDView` | `true` | Permite leer el cuerpo del archivo como texto en modo Markdown y que Claude lo pueda procesar |

> **Importante:** `compress: true` y `decompressForMDView: true` no son contradictorios. El archivo se guarda comprimido en disco pero se descomprime automáticamente al abrirlo en modo texto/lectura.

---

## Tema y apariencia

| Campo | Valor | Razón |
|-------|-------|-------|
| `matchTheme` | `true` | El lienzo sigue el tema claro/oscuro de Obsidian |
| `matchThemeAlways` | `true` | El tema se aplica siempre, no solo al abrir |
| `dynamicStyling` | `colorful` | Estilo visual por defecto para los elementos del lienzo |
| `previewMatchObsidianTheme` | `false` | Las previsualizaciones embebidas mantienen su propio color |

---

## Previsualizaciones embebidas

Cuando un `constellation` u `observatory` se embebe en una nota `.md` con `![[nombre.excalidraw]]`, estos valores controlan cómo se renderiza:

| Campo | Valor | Razón |
|-------|-------|-------|
| `displaySVGInPreview` | `true` | Muestra el lienzo como SVG en modo lectura de la nota que lo embebe |
| `previewImageType` | `SVG` | Formato de la imagen de preview — SVG es vectorial y se escala sin pérdida |
| `width` | `400` | Ancho por defecto del embed en píxeles |
| `displayExportedImageIfAvailable` | `false` | Siempre renderiza desde el archivo fuente, no desde un PNG exportado |

---

## Exportación

| Campo | Valor | Razón |
|-------|-------|-------|
| `pngExportScale` | `2` | Resolución 2× para exports a `_assets/` — legible en documentos e impresión |
| `exportWithTheme` | `true` | El PNG exportado respeta el tema activo |
| `exportWithBackground` | `true` | Incluye el fondo en el PNG exportado |
| `exportPaddingSVG` | `10` | Margen de 10px en exports SVG |
| `autoexportSVG` | `false` | No exporta SVG automáticamente al guardar — se hace manualmente cuando se necesita |
| `autoexportPNG` | `false` | Igual — export manual según necesidad |

> Los exports se guardan en `_assets/` con el mismo nombre que el archivo fuente. Convención: `ETN806-P2-joint-density.png`.

---

## Comportamiento de apertura y navegación

| Campo | Valor | Razón |
|-------|-------|-------|
| `zoomToFitOnOpen` | `true` | Al abrir un mapa encaja todo el contenido en pantalla automáticamente |
| `zoomToFitOnResize` | `false` | No re-encaja al redimensionar la ventana — evita saltos molestos |
| `openInAdjacentPane` | `true` | Abre el lienzo en un panel lateral, permite ver la nota fuente al mismo tiempo |
| `defaultMode` | `normal` | Modo de inicio: selección normal, no modo pluma |

---

## Autosave

| Campo | Valor |
|-------|-------|
| `autosave` | `true` |
| `autosaveIntervalDesktop` | `60000` (60 segundos) |
| `autosaveIntervalMobile` | `30000` (30 segundos) |

---

## Template base — `Excalidraw/template/Template.excalidraw.md`

El plugin usa este archivo como punto de partida cuando se crea un lienzo **desde el botón de Excalidraw** (no desde Templater). Contiene el YAML mínimo del Sistema Galaxy con campos vacíos para completar manualmente, más el bloque `compressed-json` de lienzo vacío.

```yaml
---
excalidraw-plugin: parsed
tags: [excalidraw]
galaxy_body: 
title: ""
subject: 
semester: 
partial: 
topic: 
date_created: 
status: activo
---
```

> Los campos `galaxy_body`, `subject`, `semester`, `partial` y `topic` se completan a mano según si el lienzo será `constellation` o `observatory`. Luego se debe mover el archivo a `Constellations/` u `Observatory/` manualmente, y agregar el bloque `%%` con los wikilinks galaxy.
>
> **Flujo preferido:** siempre usar Templater (`tpl-constellation` o `tpl-observatory`) — mueve el archivo automáticamente y precarga todos los campos.

---

## Configuración YAML requerida en archivos Excalidraw

Todo archivo `.excalidraw.md` en este vault **debe** comenzar con `excalidraw-plugin: parsed` como primer campo del YAML. Sin este campo el plugin abre el archivo como nota de texto en lugar de como lienzo.

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

> El campo `excalidraw-plugin: parsed` debe ir **siempre primero** en el YAML. El plugin lo requiere para reconocer el archivo como lienzo.

---

## Estructura de carpetas Excalidraw en el vault

```
Excalidraw/
    ├── Template.excalidraw.md    ← plantilla base para lienzos creados fuera de Templater
    ├── Scripts/                  ← scripts instalados desde el Script Store
    │   └── Mindmap Builder.md    ← script principal para constellations (instalar manualmente)
    ├── Constellations/           ← galaxy_body: constellation
    │   └── ETNXXX-PN-nombre-descriptivo.excalidraw.md
    └── Observatory/              ← galaxy_body: observatory
        └── ETNXXX-PN-nombre-descriptivo.excalidraw.md
```

---

## Cambios aplicados en esta sesión (2026-05-28)

Los siguientes valores fueron modificados respecto al estado inicial del plugin:

| Campo | Valor anterior | Valor nuevo | Quién |
|-------|---------------|-------------|-------|
| `templateFilePath` | `Excalidraw/template/Template.excalidraw` | `Excalidraw/Template.excalidraw.md` | usuario + claude |
| `scriptFolderPath` | `Excalidraw/Scripts` | `Excalidraw/Scripts` | usuario |
| `drawingFilenamePrefix` | `Drawing ` | `RENOMBRAR-` | usuario |
| `drawingFilenameDateTime` | `YYYY-MM-DD HH.mm.ss` | `DD-MM-YYYY HH.mm.ss` | usuario |
| `decompressForMDView` | `false` | `true` | claude |
| `displaySVGInPreview` | `false` | `true` | claude |
| `matchTheme` | `false` | `true` | claude |
| `matchThemeAlways` | `false` | `true` | claude |
| `pngExportScale` | `1` | `2` | claude |

### Archivos y carpetas creados

| Acción | Ruta |
|--------|------|
| Carpeta creada | `Excalidraw/Scripts/` |
| Archivo creado | `Excalidraw/Template.excalidraw.md` |
| Archivo creado | `_app/_config/_excalidraw-system.md` |

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_mindmap-system.md]]
[[_app/_config/_template-system.md]]
[[_app/_config/_note-system.md]]
[[_pdf_pp-system]]
[[_app/_config/_ToDo-system.md]]
%%
