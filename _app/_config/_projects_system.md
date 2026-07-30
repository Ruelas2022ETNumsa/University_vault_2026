---
title: Sistema de Proyectos — University Vault
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
related_notes:
  - "[[_galaxy-system]]"
tags:
  - beacon
  - galaxy
  - infraestructura
  - proyectos
date_created: 2026-07-30
date_updated: 2026-07-30
status: activo
---

# Sistema de Proyectos — University Vault

---

## Visión general

El sistema de proyectos organiza todo trabajo activo, pausado o archivado dentro del vault. Vive en `_hangar/` y se integra con el sistema galaxy a través de un subtipo de `galaxy_body` específico para proyectos.

Los proyectos tienen ciclo de vida completo: nacen como `blueprint`, se ejecutan como `ship` o `carrier`, y al completarse se archivan en `_legacy/` o en `_relics/` de su materia.

---

## Estructura de carpetas

```mermaid
---
config:
    treeView:
        rowIndent: 20
        paddingX: 8
        paddingY: 4
        lineThickness: 1
    themeVariables:
        treeView:
            labelFontSize: '12px'
            labelColor: '#7c6f9f'
            lineColor: '#b0a8c8'
            descriptionColor: '#9fb8a8'
            highlightBg: 'rgba(180, 160, 210, 0.15)'
            highlightStroke: '#c4aee0'
---
treeView-beta
_hangar/
  dock/
    logbook.md              ← índice de dock, dirigido a Claude
    tsk_*.md                ← ships en espera
  [carpeta-carrier]/        ← una por cada proyecto extenso
    logbook.md              ← índice del carrier, dirigido a Claude
    [alias]-config.md       ← configuración general del proyecto
    [alias]-opc_X-[dist].md ← documentación de opciones/pruebas
    tsk_[alias].md          ← carrier activo
  _legacy/                  ← archivo de proyectos completados
  alx-rul.md                ← operator
  alxgml.md                 ← operator
  alxhot.md                 ← operator
  alxrul.md                 ← operator
  emergn.md                 ← operator
  krajo.md                  ← operator
  standb.md                 ← operator
  tsk_tpl.md                ← plantilla base de proyectos
  _ideas_*.md               ← blueprints de futuros proyectos
```

**Archivo académico:** `semesters/[MATERIA]/_relics/` — proyectos universitarios completados.

---

## Subtipo galaxy_body — proyectos

Estos `galaxy_body` son un subtipo del sistema galaxy, específicos para proyectos. No se agregan a la tabla principal de `_galaxy-system.md`.

| `galaxy_body` | Qué es | Dónde vive |
|---|---|---|
| `operator` | Worker — procesa ships activos, uno a la vez | `_hangar/` raíz |
| `ship` | Proyecto simple, un solo archivo | `dock/` o cargado en operator |
| `carrier` | Proyecto extenso con carpeta propia y múltiples archivos | `_hangar/[carpeta]/` |
| `dropship` | Documentación interna de un carrier (opciones, pruebas, config) | dentro de carpeta carrier |
| `logbook` | Índice/README de una carpeta, dirigido a Claude | `dock/`, carpetas carrier |
| `blueprint` | Idea de futuro proyecto | `_hangar/` raíz como `_ideas_*.md` |
| `void` | Nota efímera sin yaml | carpeta pendiente de diseño |

---

## Estados

### Ship y Carrier

| `status` | Significado |
|---|---|
| `docked` | almacenado en `dock/`, esperando operator disponible |
| `in-orbit` | fue trabajado en operator, pausado sin dependencia externa |
| `delayed` | bloqueado por dependencia externa — ver campo `blocked_by:` |
| `docking` | activo dentro de su carpeta carrier, en proceso |
| `aborted` | proyecto no viable, descartado |
| `delivered` | terminado y documentado, listo para archivar |

### Operator

| `status` | Significado |
|---|---|
| `free` | disponible |
| `busy` | cargado con un ship activo |

### Dropship

| `status` | Significado |
|---|---|
| `activo` | en evaluación o uso |
| `evaluado` | prueba completada, veredicto registrado |
| `descartado` | opción descartada, motivo en el archivo |

### Blueprint

| `status` | Significado |
|---|---|
| `idea` | anotado, sin evaluar |
| `evaluando` | en análisis |
| `aprobado` | aprobado para convertirse en ship o carrier |

---

## Campos YAML por tipo

### Ship
```yaml
galaxy_body: ship
project: ""
date: 
status: docked
fleet:           # opcional — materia o contexto al que pertenece
blocked_by:      # opcional — solo si status: delayed
```

### Carrier (tsk_ dentro de su carpeta)
```yaml
galaxy_body: carrier
project: ""
date: 
status: docking
fleet:           # opcional
blocked_by:      # opcional
```

### Dropship
```yaml
galaxy_body: dropship
carrier: "[[ruta/tsk_carrier.md]]"
scope: config | opcion-A | opcion-B | prueba
status: activo
date: 
```

### Logbook
```yaml
galaxy_body: logbook
scope: dock | [nombre-carpeta-carrier]
date_updated: 
```

### Operator
```yaml
project: ""
date: 
status: free
alias: w1        # w1 a w7
```

### Blueprint
```yaml
galaxy_body: blueprint
status: idea
priority: alta | media | baja
date: 
```

---

## Flujo de vida de un proyecto

```
blueprint (_ideas_*.md)
    ↓ aprobado
ship (dock/) o carrier (_hangar/carpeta/)
    ↓ se asigna a operator
operator lo carga (status: busy)
    ↓
¿se bloquea?
  NO → se completa → status: delivered
  SÍ → se copia a dock/ como ship → status: delayed
       operator queda free
       blocked_by: apunta a la dependencia
       dependencia (carrier) indica en logbook qué desbloquea al terminar
    ↓ dependencia termina
ship vuelve a operator
    ↓ se completa → status: delivered
    ↓
se archiva en _hangar/_legacy/
o en semesters/[MATERIA]/_relics/ si es académico
```

**Sesión larga sin terminar:** contenido del operator se copia a `dock/` como ship con `status: in-orbit`. Operator queda `free`. Mismo mecanismo que bloqueo por dependencia.

---

## Convenciones de nombres

| Tipo | Convención | Ejemplo |
|---|---|---|
| Ship en dock | `tsk_[descripcion].md` | `tsk_pdf_marginalia_pp.md` |
| Carrier (tsk) | `tsk_[alias].md` | `tsk_anki.md` |
| Dropship config | `[alias]-config.md` | `anki-config.md` |
| Dropship opción | `[alias]-opc_[X]-[distintivo].md` | `anki-opc_A-marginalia.md` |
| Logbook | `logbook.md` | `logbook.md` |
| Operator | `[nombre].md` (sin tsk_) | `alx-rul.md` |
| Blueprint | `_ideas_[N]_[tema].md` | `_ideas_0_shellcmd.md` |

---

## Integración con _galaxy-system.md

- Los `galaxy_body` de proyectos son un **subtipo** — no aparecen en la tabla principal de galaxy.
- El campo `fleet:` conecta cualquier proyecto con su materia o contexto sin mover el archivo.
- Los workshops universitarios se integran con este sistema via `fleet:` — documentación pendiente en sesión dedicada.

---

## Pendientes

- [ ] Diseño de carpeta para `void` — opciones: `drift/`, `nebula/`, `debris/`, `static/`
- [ ] Integración formal con workshops (4 tipos actuales + tareas docente + prácticas auxiliar)
- [ ] Evaluar `tpl-w-project.md` — definir o eliminar
- [ ] Crear templates: `tpl-ship.md`, `tpl-carrier.md`, `tpl-dropship.md`, `tpl-logbook.md`, `tpl-blueprint.md`
