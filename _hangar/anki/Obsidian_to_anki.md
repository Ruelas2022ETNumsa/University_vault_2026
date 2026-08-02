---
title: "Obsidian to Anki — Image Occlusion: flujo y scripts"
scope: hangar
status: activo
date: 2026-08-02
---

# Obsidian to Anki — Image Occlusion: flujo y scripts

Buffer de documentacion del flujo Image Occlusion (Opcion C). Completo para la integracion actual (Excalidraw + Obsidian_to_Anki). Pendiente verificar compatibilidad con Opcion A (Cornell Marginalia) y plugin Flashcards.

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

## Parte 2 — Script: image-occlusion-reset (legacy) ✅

Script original. Conservado como referencia pero reemplazado por `occlusion_actions/main.py`.

**Ruta:** `.obsidian/scripts/python/image_occlusion_reset/main.py`

Logica: conservaba la carpeta mas reciente o sin ID, borraba las demas. Ya no se usa activamente.

---

## Parte 3 — Template `tpl-Anki_excalidraw.md` ✅

Template base para crear excalidraws de oclusión. Ubicado en `_templates/tpl-Anki_excalidraw.md`.

Al crear desde Templater pregunta el **nombre del archivo** y lo mueve automáticamente a `Excalidraw/Image-Occlusions/`. YAML mínimo sin `galaxy_body` — solo `excalidraw-plugin: parsed` y `tags: [excalidraw]`.

---

## Parte 4 — Deck y tag dinámicos al generar cartas ✅

El script `Image Occlusion.md` fue editado para preguntar **TARGET DECK** y **FILE TAGS** al momento de generar cartas (modos `hideOne` y `hideAll`). Los valores se inyectan en cada `.md` generado reemplazando las líneas correspondientes del template `tpl-excalidraw_occlusion.md`.

**Flujo actualizado — Paso 2 (completo):**

1. Presionar botón **Image Occlusion** en Excalidraw
2. Elegir modo (`Hide One` o `Hide All`)
3. Ingresar **TARGET DECK** (ej. `Galaxy::Anatomia`) — default: `Galaxy::General`
4. Ingresar **FILE TAGS** (ej. `Anatomia`) — default: `Obsidian_to_Ankipru`
5. Seleccionar template → `tpl-excalidraw_occlusion.md`
6. Se generan las cartas con deck y tag correctos

**Archivos modificados:**
- `Excalidraw/Scripts/Downloaded/Image Occlusion.md` — prompts de deck/tag + replace en template
- `_templates/tpl-excalidraw_occlusion.md` — agregada línea `FILE TAGS: Obsidian_to_Ankipru`

---

## Parte 5 — Script: occlusion_actions 🔧 (en desarrollo)

Nuevo script Python que reemplaza `image_occlusion_reset`. Gestiona tres acciones sobre las carpetas de Image Occlusion de un excalidraw dado.

**Ruta:** `.obsidian/scripts/python/occlusion_actions/main.py`
**BKs:** `mainv2.py.bk`, `mainv3.py.bk`, `mainv4.py.bk`

### Acciones

| Accion | Descripcion |
|---|---|
| **B** | Borrar: elimina todas las carpetas `nombre__timestamp`, borra notas en Anki, elimina decks vacios, limpia tags huerfanos |
| **S** | Legacy: archiva carpetas exportadas (con ID) a `_legacy/nombre/`. Bloquea si ninguna fue exportada. Avisa si algunas no tienen ID. |
| **Z** | Revisar: restaura todo el contenido de `_legacy/nombre/` a `Image-Occlusions/` |
| otro | Cancelar: sale sin tocar nada |

### Configuracion Shell Commands

| Campo | Valor |
|---|---|
| Alias | `Occlusion Actions` |
| Comando | `& "C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe" "E:\University_vault_2026\.obsidian\scripts\python\occlusion_actions\main.py" "{{_excalidraw_name}}" "{{vault_path}}" "{{_occlusion_action}}"` |
| Shell | PowerShell 5 |
| stdout | Notification balloon |
| stderr | Notification balloon |
| Output mode | Wait until finished |

**Prompt (Preactions) — Occlusion Actions:**
- Campo 1: label `Excalidraw` | Variable `{{_excalidraw_name}}` | Default `{{title}}` | Required ON
- Campo 2: label `Accion — B=Borrar S=Legacy Z=Revisar otro=Cancelar` | Variable `{{_occlusion_action}}` | Default `B` | Required ON

### Estado de pruebas

| Accion | Estado | Notas |
|---|---|---|
| B | ✅ Funcional | Borra carpetas, notas Anki, decks vacios, tags huerfanos |
| S | 🔧 Parcial | Mueve carpetas con ID OK — archivo fuente .excalidraw no se mueve |
| Z | ✅ Funcional | Restaura desde legacy correctamente |

### Pendientes fix S

1. Carpeta legacy no debe incluir extension en su nombre (`nombre/` no `nombre.excalidraw/`)
2. Archivo fuente `.excalidraw.md` no se mueve a legacy — ajustar `find_excalidraw_file`
3. `{{title}}` incluye `.excalidraw` cuando el archivo activo tiene esa extension — stripear en script

---

## Pendientes

- [ ] Verificar compatibilidad con Opcion A (Cornell Marginalia) al tener ambos activos
- [ ] Verificar compatibilidad con plugin Flashcards al activarlo
- [ ] Integrar a documentacion definitiva del vault cuando esten resueltas las 2 opciones anteriores
