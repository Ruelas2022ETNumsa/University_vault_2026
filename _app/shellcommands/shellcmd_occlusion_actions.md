---
title: "Shell Commands — occlusion_actions"
galaxy_body: beacon
scope: vault
author: [usuario, claude]
audience: [usuario, claude]
related_notes:
  - "[[shellcmd_scripting_guide]]"
  - "[[shellcmd_config_script]]"
  - "[[shellcmd_config_gral]]"
  - "[[tsk_anki]]"
tags: [beacon, obsidian, shell-commands, anki, excalidraw, image-occlusion, infraestructura, automatizacion]
date_created: 2026-08-02
date_updated: 2026-08-02
status: activo
---

# Shell Commands — occlusion_actions

> Script de gestion de carpetas Image Occlusion para el flujo Obsidian -> Anki (Opcion C — Excalidraw).
> Trabaja en conjunto con el plugin **Excalidraw**, el script **Image Occlusion** y el addon **AnkiConnect**.

---

## 1. Proposito

Al editar un excalidraw y regenerar cartas de occlusion, se acumulan carpetas timestamp en `Excalidraw/Image-Occlusions/`. Este script permite gestionar esas carpetas mediante tres acciones: borrar limpiamente (eliminando tambien las notas en Anki), archivar en legacy, o restaurar desde legacy.

---

## 2. Archivo del script

```
.obsidian/scripts/python/occlusion_actions/main.py
```

**Backups disponibles:** `mainv2.py.bk`, `mainv3.py.bk`, `mainv4.py.bk`, `mainv5.py.bk`

---

## 3. Flujo completo

```
[excalidraw editado con carpetas timestamp acumuladas]
        |
        +-- B --> Borra carpetas + notas Anki + decks vacios + tags huerfanos
        |
        +-- S --> Archiva carpetas exportadas (con ID) + archivo fuente a _legacy/nombre/
        |                  (bloquea si ninguna fue exportada a Anki)
        |
        +-- Z --> Restaura todo el contenido de _legacy/nombre/ a Image-Occlusions/
        |
        +-- otro --> Cancela sin tocar nada
```

---

## 4. Acciones disponibles

| Accion | Descripcion | Toca Anki |
|---|---|---|
| **B** | Borra todas las carpetas `nombre__timestamp`, elimina notas en Anki, borra decks vacios, limpia tags huerfanos | Si — Anki debe estar abierto |
| **S** | Archiva carpetas con ID + archivo fuente `.md` a `_legacy/nombre/`. Carpetas sin ID se omiten con aviso | No |
| **Z** | Restaura contenido de `_legacy/nombre/` a `Image-Occlusions/` | No |
| otro | Sale sin modificar nada | No |

> Acepta mayusculas y minusculas (b/B, s/S, z/Z).

---

## 5. Logica de accion B

1. Recorre todas las carpetas `nombre__timestamp` en `Image-Occlusions/`
2. Extrae IDs, TARGET DECK y FILE TAGS de cada carpeta
3. Si hay IDs — verifica que Anki este abierto. Si no responde, detiene todo sin borrar nada
4. Borra notas en Anki via `deleteNotes`
5. Borra carpetas del vault
6. Por cada deck registrado — si quedo vacio, lo borra con `deleteDecks`
7. Limpia tags huerfanos con `clearUnusedTags`
8. Muestra resumen: carpetas, cartas, decks y tags borrados

---

## 6. Logica de accion S (Legacy)

1. Recorre todas las carpetas `nombre__timestamp`
2. Clasifica: con IDs (exportadas) y sin IDs (no exportadas)
3. Si ninguna tiene ID — bloquea con mensaje `aun no fue exportado a Anki`
4. Mueve carpetas con ID a `_legacy/nombre/` — sobreescribe si ya existe
5. Busca archivo fuente (`nombre.md` o `nombre.excalidraw.md`) en `Image-Occlusions/`, fallback en `Excalidraw/`
6. Mueve archivo fuente a `_legacy/nombre/`
7. Muestra resumen — avisa si habia carpetas sin ID omitidas

**Estructura resultante:**
```
Image-Occlusions/_legacy/nombre/
    nombre__2026-08-01 19.36.09/
    nombre__2026-08-02 10.00.00/
    nombre.md
```

---

## 7. Logica de accion Z (Revisar)

1. Verifica que exista `_legacy/nombre/`
2. Si no existe — avisa y cancela
3. Mueve todo el contenido de `_legacy/nombre/` a `Image-Occlusions/`
4. Elimina la carpeta legacy si quedo vacia

---

## 8. Edge cases probados

| Caso | Comportamiento |
|---|---|
| Nombre incorrecto (B/S/Z) | Error: "no se encontraron carpetas para X" — no toca nada |
| Anki cerrado (B con IDs) | Error: "Anki no esta abierto" — no borra nada |
| Carpetas sin ID (S) | Bloquea si todas sin ID. Omite las sin ID si hay mezcla, avisa en mensaje |
| Mezcla con/sin ID (S) | Archiva solo las exportadas, avisa las omitidas |
| Nombre inexistente en legacy (Z) | Error: "Archivo no encontrado en legacy" |
| Carpeta ya existente en legacy (S) | Sobreescribe sin error |
| B sin IDs (carpetas no exportadas) | Borra carpetas del vault sin llamar a Anki |

---

## 9. Configuracion en Shell Commands

### Pestana General

| Campo | Valor |
|---|---|
| Alias | `Occlusion Actions` |
| Confirmacion antes de ejecutar | OFF |
| stdin | vacio |

**Comando (Windows):**
```
& "C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe" "E:\University_vault_2026\.obsidian\scripts\python\occlusion_actions\main.py" "{{_excalidraw_name}}" "{{vault_path}}" "{{_occlusion_action}}"
```

> Reemplazar `USUARIO` con el nombre de usuario real del sistema.

### Pestana Environments

| Campo | Valor |
|---|---|
| Windows shell command | (mismo comando que arriba) |
| Terminal de Windows | `PowerShell 5` |

### Pestana Output

| Canal | Valor |
|---|---|
| stdout | `Notification balloon` |
| stderr | `Notification balloon` |
| Output handling mode | `Wait until finished` |
| Show notification when executing | `Do not show` |

### Pestana Preactions — Prompt: Occlusion Actions

| Campo | Valor |
|---|---|
| Titulo | `Occlusion Actions` |
| Descripcion | `Archivo: {{title}}` |
| Preview shell command | OFF |
| Execute button text | `Execute` |

**Campo 1 — Excalidraw:**

| | |
|---|---|
| Field label | `Excalidraw` |
| Default value | `{{title}}` |
| Target variable | `{{_excalidraw_name}}` |
| Is required | ON |

**Campo 2 — Accion:**

| | |
|---|---|
| Field label | `Accion — B=Borrar  S=Legacy  Z=Revisar  otro=Cancelar` |
| Default value | `B` |
| Target variable | `{{_occlusion_action}}` |
| Is required | ON |

### Pestana Variables

| Variable | Si no esta disponible |
|---|---|
| `{{_excalidraw_name}}` | `Cancel execution and show errors` |
| `{{_occlusion_action}}` | `Cancel execution silently` |

---

## 10. Ribbon

Boton agregado via **Commander**:

| Boton | Comando |
|---|---|
| (icono elegido) | `shell commands: execute: Occlusion Actions` |

---

## 11. Plugins requeridos

| Plugin / Addon | Rol |
|---|---|
| Excalidraw (Obsidian) | Crea y edita los archivos de occlusion |
| Excalidraw Script: Image Occlusion | Genera las carpetas timestamp y cartas desde el excalidraw |
| Obsidian_to_Anki (Obsidian) | Exporta las cartas generadas a Anki y agrega IDs |
| AnkiConnect (Anki addon `2055492159`) | Recibe operaciones de borrado desde el script via API local |
| Shell Commands (Obsidian) | Ejecuta el script Python desde Obsidian |
| Commander (Obsidian) | Agrega el boton al ribbon |

> Anki Desktop debe estar abierto y con AnkiConnect activo para la accion B con cartas exportadas.

---

## 12. Nota sobre plugins adicionales

El flujo actual solo tiene activos **Excalidraw** y **Obsidian_to_Anki**. El plugin **Flashcards** no esta activo — se desconoce si su activacion genera conflictos con el flujo de Image Occlusion. Probar con precaucion cuando se active.

---

## 13. Template de creacion

Los excalidraws de occlusion se crean desde `_templates/tpl-Anki_excalidraw.md`. El template solicita el nombre del archivo y lo mueve automaticamente a `Excalidraw/Image-Occlusions/`.

> [!warning] Archivo creado como `.md` — no como `.excalidraw`
> El template crea el archivo con extension `.md` de forma intencional. Si se creara con extension `.excalidraw`, Obsidian devolveria el titulo como `nombre.excalidraw` (con extension incluida), lo que genera una carpeta legacy con nombre incorrecto y rompe la busqueda del archivo fuente en el script.
> 
> Los archivos `.md` creados por este template son **completamente funcionales como excalidraw** — Obsidian los reconoce y renderiza igual gracias al YAML `excalidraw-plugin: parsed`.

---

%%
# galaxy-links
[[tsk_anki]]
[[shellcmd_scripting_guide]]
[[shellcmd_config_script]]
%%
