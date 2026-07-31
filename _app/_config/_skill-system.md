---
title: Sistema de Skills — University Vault
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
related_notes:
  - "[[_galaxy-system]]"
  - "[[_projects_system]]"
tags:
  - beacon
  - infraestructura
  - claude
  - skills
date_created: 2026-07-31
date_updated: 2026-07-31
status: activo
---

# Sistema de Skills — University Vault

Los skills son archivos de instrucciones de comportamiento para Claude. Viven en `_skills/` y se cargan bajo demanda al inicio de cada sesión. No tienen `galaxy_body` — no participan del grafo ni del sistema galaxy.

> Documentación del sistema galaxy: [[_galaxy-system]]
> Documentación del sistema de proyectos: [[_projects_system]]

---

## Estructura de la carpeta

```
_skills/
  _start.md          ← punto de entrada obligatorio de toda sesión
  _start 1.md        ← backup de _start.md
  _claude-work.md    ← edición del vault
  _claude-plan.md    ← planificación de proyectos
  _claude-setup.md   ← configuración técnica
  _claude-close.md   ← cierre de sesión
  _claude-boot.md    ← trabajo completo del vault (pendiente de documentar)
  _claude-boot 1.md  ← backup de _claude-boot.md
```

---

## Flujo de sesión

```
Usuario pega el prompt de inicio (generado por script Python)
    ↓
Claude lee _start.md
    ↓
Verificación MCP (write + edit sobre Rubbish/section.md)
    ↓
Menú de skills → usuario elige
    ↓
Claude lee el skill elegido y ejecuta su flujo
    ↓
Trabajo de la sesión
    ↓
Usuario dice "la sesión debe terminar, usa close"
    ↓
Claude lee _claude-close.md y ejecuta cierre
```

---

## Prompt de inicio

El usuario dispara cada sesión con un script Python que genera y copia al portapapeles un mensaje con este formato:

```
Usá el MCP Filesystem y leé E:\University_vault_2026\_skills\_start.md
Hora de inicio: HH:MM
```

La hora de inicio es capturada automáticamente por el script — Claude la usa para el control de tokens (`/tokens`).

---

## Skills disponibles

### _start

**Archivo:** `_skills/_start.md`
**Activa:** toda sesión — es el punto de entrada obligatorio
**Requiere:** Filesystem MCP — `write_file`, `edit_file`

Flujo fijo que Claude ejecuta al inicio de cualquier sesión:

1. **Verificación MCP** — escribe `123` en `Rubbish/section.md` y lo borra con `edit_file`. Si alguno falla avisa y se detiene.
2. **Menú de skills** — muestra las 4 opciones disponibles y espera elección.
3. **Carga del skill** — lee el archivo correspondiente y ejecuta su flujo.
4. **Control de tokens** — captura `Hora de inicio` del mensaje de apertura. Ante `/tokens` o `/token` responde: `Tokens se reestablecen a las HH:MM` (hora_inicio + 5h).
5. **Cierre** — ante `"la sesión debe terminar, usa close"` lee y ejecuta `_claude-close.md`.

**Manejo de fallos MCP (regla global):**
Ante cualquier fallo de tool durante la sesión:
`"tool (write/edit) no disponible — revisá el MCP o permitís alternativas (y/n)"`
- `n` → espera que el usuario reinicie el MCP y reintenta
- `y` → busca alternativa automáticamente

---

### _claude-work

**Archivo:** `_skills/_claude-work.md`
**Activa:** sesiones de edición del vault
**Requiere:** Filesystem MCP — `write_file`, `edit_file`

Modo de edición controlada. Claude actúa como asistente de edición con confirmación obligatoria antes de cualquier cambio.

**Reglas críticas:**
- `edit_file` es la única herramienta para modificar archivos existentes
- `write_file` solo para archivos vacíos y con pedido explícito en ese mensaje
- Antes de cualquier `write_file` → avisa `"cambios masivos, bk necesario"` y espera confirmación
- Lectura puntual con `read_text_file` + rango `[ini, fin]` — nunca leer archivo completo para ediciones intermedias
- Siempre `dryRun: true` primero, salvo que el usuario diga **"aplicar edit"**
- Si los cambios superan 5 bloques o 50 líneas → avisa `"cambios masivos, bk necesario"`
- `oldText` del `edit_file` debe ser cadena única y exacta del archivo

**Flujo de edición:**
- `"ver dryRun"` → muestra diff, espera confirmación
- `"aplicar edit"` → pasa directo a `dryRun: false`

**Convención de backups:** `nombre.md` → `nombre 1.md` → `nombre 2.md` (el usuario crea el bk manualmente)

**Señal de contexto extenso:** si la conversación lleva muchos intercambios o hay inconsistencias → avisa: `"Contexto extenso — recomiendo cerrar sesión con el prompt de cierre para evitar errores."`

---

### _claude-plan

**Archivo:** `_skills/_claude-plan.md`
**Activa:** sesiones de planificación de proyectos
**Requiere:** Filesystem MCP — `write_file`, `edit_file`

Modo de planificación para el sistema `_hangar/`. Claude lee operators y genera contenido de ships/carriers.

**Al iniciar:** lista `_hangar/` y responde `ok`.

**Operators disponibles:** `alx_hot.md`, `alx_gml.md`, `alx-rul.md`, `alxrul.md`, `emergn.md`, `krajo.md`, `standb.md`

**Flujo:**
1. Usuario indica qué operator usar
2. Claude lee el operator y verifica `status` en YAML
   - `free` → procede
   - `busy` → avisa y espera instrucción
3. Discute el enfoque antes de escribir nada
4. Si el usuario dice **"web"** → busca antecedentes, resume fuentes y propone enfoque
5. Acordado el enfoque, genera contenido completo siguiendo estructura de `tpl_worker.md`
6. Avisa `"cambios masivos, bk necesario"` y espera confirmación
7. Escribe con `write_file` en el operator indicado

**Reglas de lectura:** solo lectura — sin ediciones. El usuario provee ruta y línea final; Claude lee desde línea 1 hasta esa línea. Nunca leer archivo completo salvo indicación explícita.

---

### _claude-setup

**Archivo:** `_skills/_claude-setup.md`
**Activa:** configuraciones técnicas (plugin, herramienta, entorno)
**Requiere:** Filesystem MCP — opcional, solo si el vault está involucrado

Modo de asistencia técnica paso a paso. Diseñado para evitar que Claude asuma el entorno del usuario.

**Flujo:**
1. Preguntas mínimas sobre entorno (SO, versiones, rutas, estado previo) antes de mostrar cualquier paso
2. Muestra el flujo completo como lista numerada de títulos — solo el mapa, sin detalles
3. Espera que el usuario indique: `"paso X: [lo que ve o la duda]"`
4. Por cada paso: explica qué hacer y qué esperar → espera confirmación → si falla, diagnostica antes de avanzar
5. Si el usuario dice **"web"** → busca documentación oficial para ese paso específico

---

### _claude-close

**Archivo:** `_skills/_claude-close.md`
**Activa:** cierre de sesión — trigger: `"la sesión debe terminar, usa close"`
**Requiere:** Filesystem MCP — `write_file`, `edit_file`

Modo de cierre controlado. Claude actualiza el operator activo antes de terminar la sesión.

**Al iniciar:** el usuario provee la ruta del operator → Claude lo lee completo y responde `ok`.

**Tipos de cierre:**
- **Mínimo** → sobreescribe solo `## Handoff` con `edit_file`
- **Completo** → actualiza con `edit_file`: `## Handoff` + `## Tareas` + `## Decisiones` + `## Recursos`

**Estructura de `## Handoff`:**
```
**Última sesión:** YYYY-MM-DD
**Retomar desde:** [ruta + línea final sugerida]
**Completado esta sesión:**
**Próximo paso:**
**Preguntas de cierre:**
```

**Reglas de edición:**
- `edit_file` siempre — nunca `write_file` en el operator
- Siempre `dryRun: true` primero salvo `"aplicar edit"`
- Si los cambios son considerables → avisa `"cambios masivos, bk necesario"` y espera confirmación
- Nunca edita sin confirmación explícita

---

### _claude-boot

**Archivo:** `_skills/_claude-boot.md`
**Activa:** trabajo completo del vault
**Requiere:** Filesystem MCP — `write_file`, `edit_file`

> Pendiente de documentar — archivo extenso. Se documenta en sesión dedicada.

---

## Control de tokens

El límite de uso de Claude opera en una **ventana móvil de 5 horas** — no se resetea a medianoche. La hora de inicio de sesión se provee en el primer mensaje vía script Python.

**Trigger:** `/tokens` o `/token`
**Respuesta de Claude:** `Tokens se reestablecen a las HH:MM`

---

## Convención de backups (global)

Aplica a todos los skills que editan archivos:

| Versión | Nombre |
|---|---|
| Original | `nombre.md` |
| Backup 1 | `nombre 1.md` |
| Backup 2 | `nombre 2.md` |

El usuario crea el backup manualmente antes de confirmar cambios masivos. Claude avisa con `"cambios masivos, bk necesario"` y espera confirmación antes de proceder.

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_projects_system.md]]
[[_skills/_start.md]]
[[_skills/_claude-work.md]]
[[_skills/_claude-plan.md]]
[[_skills/_claude-setup.md]]
[[_skills/_claude-close.md]]
%%
