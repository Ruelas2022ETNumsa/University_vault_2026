---
skill: "Claude Start"
scope: "session-init"
activates: "Inicio de toda sesión"
requires: "Filesystem MCP — write_file, edit_file"
status: active
---

# _start

Leé este archivo y seguí el flujo exactamente.

---

## Verificación MCP

1. `write_file` → escribí `123` en `E:\University_vault_2026\Rubbish\section.md`
2. `edit_file` → borrá ese `123`
3. Si ambos pasan → continuá al paso siguiente
4. Si alguno falla → avisá cuál y detenete

**Si cualquier tool MCP falla en cualquier momento de la sesión:**
`"tool (write/edit) no disponible — revisá el MCP o permitís alternativas (y/n)"`
- `n` → esperás que el usuario reinicie el MCP y reintentás.
- `y` → buscás alternativa automáticamente.

---

## Selección de skill

Una vez verificado el MCP, respondé exactamente esto y esperá:

```
Skills disponibles:

1. work  — edición del vault
2. plan  — planificación de proyectos
3. setup — configuración técnica
4. boot  — trabajo completo del vault

Comandos:
/tokens  — hora en que se reestablecen los tokens
/worker  — worker activo en esta sesión
/name    — nombre de Claude en esta configuración
/close   — cierra la sesión
```

---

## Carga del skill

Según la opción elegida, leé el archivo correspondiente y ejecutá su flujo de inicio:

| Opción | Archivo a leer |
|--------|----------------|
| work   | `E:\University_vault_2026\_skills\_claude-work.md` |
| plan   | `E:\University_vault_2026\_skills\_claude-plan.md` |
| setup  | `E:\University_vault_2026\_skills\_claude-setup.md` |
| boot   | `E:\University_vault_2026\_skills\_claude-boot.md` |

---

## Control de tokens

La hora de inicio se indica en el mensaje de apertura como:
`Hora de inicio: HH:MM`

Cuando el usuario escriba **`/tokens`** , **`/token`** o diga "a qué hora se reestablecen lo tokens"→ respondé exactamente:
`Tokens se reestablecen a las HH:MM` (hora_inicio + 5 horas)

---
## Cierre de sesión

Cuando el usuario escriba **`/close`** o diga **"la sesión debe terminar, usa close"** →
leé `E:\University_vault_2026\_skills\_claude-close.md` y ejecutá su flujo de inicio.

---
## Worker de sesión

Tu nombre como IA es permanente y viene de la configuración de Claude — no cambia entre sesiones.

El archivo de worker a ejecutar se indica en el mensaje de apertura como:
`worker: nombre-worker`

Este nombre corresponde a un archivo `.md` ubicado en `E:\University_vault_2026\_hangar\bay\`. Trabajás con ese archivo pero tu identidad como IA no cambia.

Cuando el usuario escriba **`/worker`** → respondé exactamente:
`Worker activo: {nombre-worker}`

Cuando el usuario escriba **`/name`** → respondé exactamente:
`Nombre de configuración: {nombre de las instrucciones de Claude}`
