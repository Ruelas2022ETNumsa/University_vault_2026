---
title: "Shell Commands — start_snippet"
galaxy_body: beacon
scope: vault
author: [usuario, claude]
audience: [usuario, claude]
related_notes:
  - "[[shellcmd_config_script]]"
  - "[[shellcmd_config_gral]]"
tags: [beacon, obsidian, shell-commands, claude, infraestructura, automatizacion]
date_created: 2026-07-31
date_updated: 2026-08-02
status: activo
---

# Shell Commands — start_snippet

> Script que copia al portapapeles el snippet de inicio de sesión de Claude con la hora actual y el nombre del worker activo (archivo abierto en Obsidian). Elimina la necesidad de escribir manualmente el comando de inicio cada vez que se abre una sesión.

---

## 1. Propósito

Al iniciar una sesión de Claude, se necesita enviar siempre el mismo mensaje base indicando qué archivo leer vía MCP Filesystem. Este script genera ese mensaje con la hora actual (HH:MM) y el nombre del worker activo (`{{title}}` del archivo abierto) y lo deja listo en el portapapeles para pegar directamente en Claude.

---

## 2. Archivo del script

```
.obsidian/scripts/python/start_snippet/main.py
```

---

## 3. Output esperado al pegar

```
Usá el MCP Filesystem y leé E:\University_vault_2026\_skills\_start.md
Hora de inicio: 14:35
trabajás como: nombre_worker
```

---

## 4. Lógica del script

1. Lee la hora actual con `datetime.now()` formateada como `HH:MM`.
2. Recibe `{{title}}` como argumento (`sys.argv[1]`) — el nombre del archivo abierto en Obsidian.
3. Arma el string con el mensaje base + hora + worker.
4. Lo pasa a `Set-Clipboard` vía `subprocess` (PowerShell).

> [!warning] Caracteres especiales
> El `Set-Clipboard -Value '...'` usa comillas simples. Si el nombre del worker contiene apóstrofes u otros caracteres especiales, puede fallar. Evaluar escape o Here-String para una v3.

---

## 5. Configuración en Shell Commands

### Pestaña General

| Campo | Valor |
|---|---|
| Alias | `Start — copiar snippet` |
| Confirmación antes de ejecutar | OFF |
| stdin | vacío |

**Comando (Windows):**
```
python "{{vault_path}}\.obsidian\scripts\python\start_snippet\main.py" "{{title}}"
```

### Pestaña Variables

| Variable | Comportamiento si no disponible |
|---|---|
| `{{title}}` | `Execute with value:` → campo vacío |

### Pestaña Environments

| Campo | Valor |
|---|---|
| Terminal de Windows | `PowerShell 5` |

### Pestaña Output

| Canal | Valor |
|---|---|
| stdout | `Ignore` |
| stderr | `Notification balloon` |

### Pestaña Preactions

Ninguna — el script no requiere input del usuario.

### Pestaña Events

| Campo | Valor |
|---|---|
| Availability in command palette | `Command palette & hotkeys` |
| Todos los eventos automáticos | OFF |

---

## 6. Ribbon

Botón agregado via **Commander**:

| Botón | Ícono | Comando |
|---|---|---|
| `Start — copiar snippet` | `play-circle` | `shell commands: execute: Start — copiar snippet` |

---

## 7. Flujo de uso

1. Click en ribbon **Start** (o `Ctrl+P` → `Start — copiar snippet`).
2. Pegar directamente en Claude (`Ctrl+V`).
3. Claude lee `_start.md` vía MCP y arranca la sesión.

---

## 8. Plugins requeridos

| Plugin | Rol |
|---|---|
| Shell Commands (Obsidian) | Ejecuta el script Python desde Obsidian |
| Commander (Obsidian) | Agrega el botón al ribbon |

---

%%
# galaxy-links
[[shellcmd_config_script]]
%%
