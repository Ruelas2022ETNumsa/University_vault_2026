---
title: "Obsidian to Anki — Image Occlusion: flujo y scripts"
scope: hangar
status: buffer
date: 2026-08-01
---

# Obsidian to Anki — Image Occlusion: flujo y scripts

Buffer de documentación del flujo Image Occlusion (Opción C).
Cuando esté completo se integra a `anki_galaxy_guide.md` y/o `anki-opcionC-obsidian-to-anki.md`.

---

## Parte 1 — Flujo completo de creación y exportación ✅

### Paso 1 — Crear el excalidraw

1. Presionar el botón ribbon de Excalidraw (izquierda) → se crea un nuevo archivo `.excalidraw.md`
2. Renombrar el archivo con un nombre descriptivo
3. Pegar la imagen que se quiere ocultar → se guarda automáticamente en `_assets/`

### Paso 2 — Crear las oclusiones

1. Dentro de la interfaz de Excalidraw, dibujar recuadros, flechas o figuras sobre los datos a ocultar
2. Presionar el botón **Image Occlusion** (ícono estrella ⭐ — agregado manualmente al ribbon de Excalidraw)
3. Se muestran 4 opciones:
   - `Add Card: Hide One, Guess One`
   - `Add Cards: Hide All, Guess One` ← **elegir esta**
   - `Delete Cards: Delete old cards (add DELETE marker)`
   - `Delete Cards: Delete old cards files and related images (Be cautious!!)`
4. Seleccionar opción 2 — **Add Cards: Hide All, Guess One**
5. Pide seleccionar un template → elegir `_templates/tpl-ex_occlusion.md`

### Paso 3 — Archivos generados

El script crea una carpeta en `Excalidraw/Image-Occlusions/` con el nombre del excalidraw + timestamp:

```
Excalidraw/Image-Occlusions/NombreArchivo.excalidraw__YYYY-MM-DD HH.MM.SS/
```

Por cada recuadro/figura de oclusión se generan:

| Archivo | Descripción |
|---|---|
| `TIMESTAMP.md` | Carta en formato START/END para Obsidian_to_Anki |
| `q-TIMESTAMP.png` | Imagen con el área tapada (frente de la carta — pregunta) |
| `a-TIMESTAMP.png` | Imagen completa revelada (reverso de la carta — respuesta) |
| `batch-marker.md` | Índice de todas las cartas generadas en esta sesión |

Ejemplo con 3 recuadros → se generan 3 cartas, 6 PNG, 3 `.md` + 1 `batch-marker.md`.

**Estructura de cada `TIMESTAMP.md` (antes de exportar):**

```
TARGET DECK: Galaxy::General
START
Image Occlusion Enhanced
ID (hidden): TIMESTAMP
Header: 
Image: ![[/Excalidraw/Image-Occlusions/Carpeta/a-TIMESTAMP.png]]
Question Mask: ![[/Excalidraw/Image-Occlusions/Carpeta/q-TIMESTAMP.png]]
Footer: 
Remarks: [[Excalidraw/NombreArchivo.excalidraw.md|✏️ Editar fuente]]
Sources: [[Excalidraw/Image-Occlusions/Carpeta/batch-marker.md|📋 Batch]]
Extra 1: 
Extra 2: 
Answer Mask: 
Original Mask: 
END
```

### Paso 4 — Exportar a Anki

1. Abrir **Anki Desktop** (obligatorio — AnkiConnect debe estar activo)
2. Presionar el botón ribbon de **Obsidian_to_Anki** en Obsidian
3. Se muestran 3 notificaciones en secuencia:
   - `Scanning vault, check console for details`
   - `Successfully connected to Anki! This could take a few minutes - please don't close Anki until the plugin is finished`
   - `All done! Saving file hashes and added media now...` (en menos de 2 segundos)
4. Las cartas aparecen en Anki con tipo **Image Occlusion Enhanced**

**Efecto en los archivos:** el plugin inserta un `<!--ID: NNNNNNNNNNNNN-->` justo antes de `END` en cada `TIMESTAMP.md` (excepto `batch-marker.md`):

```
...
Original Mask: 
<!--ID: 1785614213095-->
END
```

Este ID vincula la carta en Obsidian con la nota en Anki. El plugin lo usa para actualizar en lugar de duplicar en syncs futuros.

---

## Parte 2 — Script 3: reset de oclusiones (pendiente)

> Documentar después de definir el flujo de re-exportación.

---

## Parte 3 — Integración con anki_galaxy_guide.md (pendiente)

> Integrar cuando el flujo completo esté probado y validado.
