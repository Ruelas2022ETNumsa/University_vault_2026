---
title: "Shell Commands Guide — Configuracion del plugin"
galaxy_body: beacon
scope: vault
author: [usuario, claude]
audience: [usuario, claude]
related_notes:
  - "[[plugin_guide]]"
  - "[[script_guide]]"
tags: [beacon, obsidian, shell-commands, infraestructura, automatizacion]
date_created: 2026-07-11
date_updated: 2026-07-11
status: borrador
---

# Shell Commands Guide — Configuracion del plugin

> Borrador. Documenta la configuracion de Shell Commands para los scripts activos del vault.
> Para el detalle de cada script ver: [[script_guide]].
> Para contexto general del plugin ver: [[plugin_guide]].

---

## Indice

- [[#1. Configuracion general del plugin]]
- [[#2. Custom Variables]]
- [[#3. Comandos configurados]]
  - [[#3.1 NotebookLM Fix]]
  - [[#3.2 Sync NotebookLM Google Drive]]
  - [[#3.3 Section Extract]]
  - [[#3.4 Section Reintegrate]]

---

## 1. Configuracion general del plugin

| Campo | Valor | Nota |
|---|---|---|
| Shell (Windows) | PowerShell | default |
| Working directory | (vacio) | raiz del vault |
| Preview variables in command palette | ON/OFF | pendiente confirmar |
| Show autocomplete menu | ON/OFF | pendiente confirmar |

> Pendiente: completar con captura cuando se genere la guia definitiva.

---

## 2. Custom Variables

Creadas en Settings -> Shell Commands -> pestana Variables -> seccion Custom variables.

| Variable | Descripcion | Usado en |
|---|---|---|
| `{{_section_heading}}` | Heading exacto a extraer, ej: `## Titulo` | Section Extract |
| `{{_section_source}}` | Ruta absoluta del archivo fuente | Section Extract |

---

## 3. Comandos configurados

Cada comando se configura desde Settings -> Shell Commands -> boton **New command**.
La configuracion detallada se accede via el engranaje de cada comando.
Las pestanas disponibles por comando son: General, Preactions, Output, Environments, Events, Variables.

---

### 3.1 NotebookLM Fix

**Pestana General**

| Campo | Valor |
|---|---|
| Alias | `NotebookLM Fix — nota activa` |
| Comando | `"C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe" "{{vault_path}}\.obsidian\scripts\python\notebooklm_fix\src\main.py" "{{file_path:relative}}" "{{vault_path}}"` |

**Pestana Output**

| Canal | Valor |
|---|---|
| stdout | Notification balloon |
| stderr | Error balloon |

**Ribbon:** agregado via Commander. Icono: pendiente documentar.

---

### 3.2 Sync NotebookLM Google Drive

**Pestana General**

| Campo | Valor |
|---|---|
| Alias | `Sync NotebookLM -> Google Drive` |
| Comando | `rclone sync "E:\University_vault_2026\_app\notebooklm" gdrive:NotebookLM_sources --verbose` |

**Pestana Output**

| Canal | Valor |
|---|---|
| stdout | Notification balloon |
| stderr | Error balloon |

**Ribbon:** agregado via Commander. Icono: `upload-cloud`.

> Detalle completo de rclone: [[Rclone_guide]]

---

### 3.3 Section Extract

**Pestana General**

| Campo | Valor |
|---|---|
| Alias | `Section Extract` |
| Comando | `"C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe" "{{vault_path}}\.obsidian\scripts\python\section_extract\src\main.py" "{{file_path:relative}}" "{{vault_path}}" "{{_section_heading}}" "{{_section_source}}"` |

**Pestana Preactions — Prompt configurado**

| Campo | Valor |
|---|---|
| Titulo del prompt | `Section Extract` |
| Descripcion | (vacio) |
| Preview shell command | OFF |
| Execute button text | `Extraer` |

Campos del prompt:

| # | Label | Target variable | Tipo | Required |
|---|---|---|---|---|
| 1 | `Seccion (## Titulo)` | `{{_section_heading}}` | Single line text | ON |
| 2 | `Ruta del archivo` | `{{_section_source}}` | Single line text | ON |

**Pestana Output**

| Canal | Valor |
|---|---|
| stdout | Notification balloon |
| stderr | Error balloon |

**Ribbon:** agregado via Commander. Icono: `scissors`.

---

### 3.4 Section Reintegrate

**Pestana General**

| Campo | Valor |
|---|---|
| Alias | `Section Reintegrate` |
| Comando | `"C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe" "{{vault_path}}\.obsidian\scripts\python\section_reintegrate\src\main.py" "{{file_path:relative}}" "{{vault_path}}"` |

**Pestana Preactions:** ninguna — el script lee la metadata desde `section.json` automaticamente.

**Pestana Output**

| Canal | Valor |
|---|---|
| stdout | Notification balloon |
| stderr | Error balloon |

**Ribbon:** agregado via Commander. Icono: `file-input`.


---

%%
# galaxy-links
%%