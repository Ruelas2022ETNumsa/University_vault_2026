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

## Parte 2 — Script 3: image-occlusion-reset ✅

Script Python que borra carpetas antiguas de Image Occlusion y sus notas en Anki, para permitir re-exportar un excalidraw editado.

**Ruta:** `.obsidian/scripts/python/image_occlusion_reset/main.py`

### Flujo de uso

1. Tener **Anki Desktop abierto** con AnkiConnect activo
2. Correr el comando desde `Ctrl+P` → `image-occlusion-reset`
3. El prompt muestra el nombre del archivo activo prellenado (ej. `Prueba_anki.excalidraw`) — editar si no es el correcto
4. Presionar **Execute**
5. El script borra las carpetas antiguas del vault y sus notas en Anki
6. Notificación de confirmación con resumen

> En Anki el borrado puede no verse en la vista principal hasta reiniciar — desde el Explorador de Anki el cambio es inmediato.

### Lógica de selección — qué carpeta conservar

El script busca en `Excalidraw/Image-Occlusions/` todas las carpetas con el nombre base ingresado.

| Caso | Condición | Acción |
|---|---|---|
| **A** | Alguna carpeta tiene `.md` sin `<!--ID:-->` | Esa es la nueva (no exportada) — se conserva. Se borran todas las demás |
| **B** | Todas las carpetas tienen ID (todas exportadas) | Se conserva la más reciente por timestamp. Se borran todas las demás |
| **Una sola carpeta** | Solo existe una carpeta | No borra nada — avisa al usuario |

### Edge cases probados

| Caso | Comportamiento |
|---|---|
| 2 carpetas: una con ID, otra sin ID | Conserva la sin ID (Caso A) ✅ |
| 2 carpetas: ambas con ID | Conserva la más reciente (Caso B) ✅ |
| 1 sola carpeta | Avisa "nada que borrar", no toca nada ✅ |
| Nombre incorrecto | Error claro: "no se encontraron carpetas para X" ✅ |
| Anki cerrado | Error claro: "Anki no esta abierto... localhost:8765" — no borra carpetas ✅ |
| Archivo no-excalidraw abierto | Prompt muestra nombre incorrecto — editable antes de ejecutar ✅ |

### Configuración Shell Commands

| Campo | Valor |
|---|---|
| Alias | `image-occlusion-reset` |
| Comando | `& "C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe" "E:\University_vault_2026\.obsidian\scripts\python\image_occlusion_reset\main.py" "{{_excalidraw_name}}" "{{vault_path}}"` |
| Shell | PowerShell 5 |
| stdout | Notification balloon |
| stderr | Notification balloon |
| Output mode | Wait until finished |

**Prompt (Preactions):**
- Título: `Image Occlusion Reset`
- Descripción: `Nombre del excalidraw a procesar. Edita si el archivo activo no es el correcto.`
- Campo label: `Excalidraw` | Variable: `{{_excalidraw_name}}` | Default: `{{title}}`
- Is required: ON

---

## Parte 3 — Template `tpl-Anki_excalidraw.md` (pendiente)

Crear template base en `Excalidraw/Image-Occlusions/` para excalidraws de oclusión.
Basado en `Excalidraw/template/Template.excalidraw.md` con YAML mínimo sin `galaxy_body`.
Primer tarea de la próxima sesión.
