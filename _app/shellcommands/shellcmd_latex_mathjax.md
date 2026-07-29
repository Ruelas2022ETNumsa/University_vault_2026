---
title: "Shell Commands — latex_to_mathjax"
galaxy_body: beacon
scope: vault
author: [usuario, claude]
audience: [usuario, claude]
related_notes:
  - "[[shellcmd_scripting_guide]]"
  - "[[shellcmd_config_script]]"
  - "[[shellcmd_config_gral]]"
  - "[[tsk_anki]]"
tags: [beacon, obsidian, shell-commands, anki, latex, infraestructura, automatizacion]
date_created: 2026-07-28
date_updated: 2026-07-28
status: activo
---

# Shell Commands — latex_to_mathjax

> Script de conversion bidireccional LaTeX <-> MathJax para el flujo Obsidian -> Anki (Opcion A — Marginalia).
> Trabaja en conjunto con el plugin **Cornell Marginalia** y el addon **AnkiConnect**.

---

## 1. Proposito

Obsidian usa `$...$` y `$$...$$` para renderizar LaTeX. Anki usa `\(...\)` y `\[...\]` (MathJax). Este script convierte entre ambos formatos directamente sobre el archivo `.md` activo, usando una bandera en el YAML para recordar el estado actual y un contador de exports para auditoria.

---

## 2. Archivo del script

```
.obsidian/scripts/python/latex_to_mathjax/main.py
```

---

## 3. Flujo completo

```
[archivo .md con $LaTeX$]
        |
        v Script (L->M)
[archivo con \(MathJax\)]  <-- latex_converted: true
        |
        v Ribbon: Cornell Marginalia sync
[tarjetas en Anki con IDs ^anki-XXXXXXXXXXXXX]
        |
        v Script (M->L)
[archivo con $LaTeX$ restaurado, IDs borrados]  <-- latex_converted: false | anki_exports: export_N
```

---

## 4. Logica del script (toggle)

El script lee `latex_converted` en el YAML y actua segun el estado:

| Estado `latex_converted` | Accion | Resultado |
|---|---|---|
| ausente / `false` | L->M: convierte `$...$` a `\(...\)` y `$$...$$` a `\[...\]` | Setea `latex_converted: true` |
| `true` | M->L: revierte `\(...\)` a `$...$` y `\[...\]` a `$$...$$`, borra IDs Anki | Setea `latex_converted: false`, incrementa `anki_exports` |

> Si la bandera no existe en el YAML, el script la crea automaticamente y asume estado `false` (LaTeX sin convertir).

---

## 5. Propiedades YAML gestionadas por el script

| Propiedad | Valores | Descripcion |
|---|---|---|
| `latex_converted` | `true` / `false` | Estado actual del archivo — `true` = listo para sync, `false` = Obsidian normal |
| `anki_exports` | `export_1`, `export_2`, ... | Contador de veces que el archivo fue exportado a Anki (se incrementa en cada M->L) |

---

## 6. Limpieza de IDs Anki

Al convertir M->L, el script borra automaticamente los IDs que Marginalia inyecta tras el sync:

```
;; ^anki-1785295229260 #tag %%   ->   ;; #tag %%
```

Patron: `^anki-` seguido de exactamente 13 digitos y un espacio.

> Advertencia: el espacio posterior al ID es el delimitador derecho — debe existir siempre (con o sin tag).

---

## 7. Restricciones

- No toca bloques de codigo (backtick inline ni triple backtick)
- No modifica el YAML frontmatter salvo `latex_converted` y `anki_exports`
- Si el archivo no tiene frontmatter YAML, el script crea la bandera al vuelo

---

## 8. Configuracion en Shell Commands

### Pestana General

| Campo | Valor |
|---|---|
| Alias | `latex->mathjax` |
| Confirmacion antes de ejecutar | OFF |
| stdin | vacio |

**Comando (Windows):**
```
"C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe" "{{vault_path}}\.obsidian\scripts\python\latex_to_mathjax\main.py" "{{file_path:absolute}}"
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

### Pestana Preactions

Ninguna — el script no requiere input del usuario.

### Pestana Events

| Campo | Valor |
|---|---|
| Availability in command palette | `Command palette & hotkeys` |
| Todos los eventos automaticos | OFF |

### Pestana Variables

| Variable | Si no esta disponible |
|---|---|
| `{{file_path}}` | `Cancel execution and show errors` |

---

## 9. Ribbon

Ambos botones agregados via **Commander**:

| Boton | Comando | Accion |
|---|---|---|
| `shell commands: execute: latex->mathjax` | Este script | Convierte L<->M segun bandera YAML |
| `cornell marginalia: sync flashcards to anki (current note)` | Cornell Marginalia | Exporta marginalia de la nota activa a Anki |

---

## 10. Flujo de uso paso a paso

1. Abrir el `.md` en Obsidian (con formulas `$LaTeX$`)
2. Click en ribbon **latex->mathjax** — convierte L->M, bandera `true`
3. Click en ribbon **Marginalia sync** — exporta tarjetas a Anki Desktop
4. Click en ribbon **latex->mathjax** — revierte M->L, borra IDs, incrementa `anki_exports`
5. Seguir editando normalmente en Obsidian

---

## 11. Plugins requeridos

| Plugin / Addon | Rol |
|---|---|
| Cornell Marginalia (Obsidian) | Renderiza marginalia y ejecuta el sync a Anki |
| AnkiConnect (Anki addon `2055492159`) | Recibe las tarjetas desde Obsidian via API local |
| Shell Commands (Obsidian) | Ejecuta el script Python desde Obsidian |
| Commander (Obsidian) | Agrega los botones al ribbon |

> Anki Desktop debe estar abierto y con AnkiConnect activo para que el sync funcione.

---

%%
# galaxy-links
[[tsk_anki]]
[[shellcmd_scripting_guide]]
[[shellcmd_config_script]]
%%
