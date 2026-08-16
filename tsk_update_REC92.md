---
galaxy_body: ship
project: "update REC92 — migración a estructura workshop + secciones"
date: 2026-08-16
status: docked
fleet: REC92
---

## Handoff

**Última sesión:** 2026-08-16 — alx_hot
**Retomar desde:** sección ## Tareas — primer ítem pendiente
**Completado esta sesión:** diseño completo de estructura, YAMLs definidos, ship creado
**Próximo paso:** crear `tsk_REC92.md` en `REC92/`
**Preguntas de cierre:** —

---

## Resumen y objetivo

Migrar la carpeta REC92 desde su estructura actual (8 archivos planos sin galaxy_body) al esquema diseñado: un hub de proyecto (`tsk_REC92.md`, workshop), 7 hubs de sección (`s1`–`s7`, workshop) y subcarpetas `_ctx/` y `_prompts/`. No se edita ningún contenido — solo se reorganiza y se agregan YAMLs.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-16 | No usar carrier — usar workshop | REC92 es producción lineal, no exploración de variantes. Carrier agrega overhead innecesario para un proyecto de 2-3 semanas |
| 2026-08-16 | No usar 4 archivos por sección (_p/_n/_c/_x) — usar 1 archivo con 4 bloques | 36 archivos satélite vs 7 hubs. Claude puede leer toda la sección en un solo read_file |
| 2026-08-16 | `rec_perplexity.md` se conserva | No es redundante — es el backup de edición del `rec_perplexity_informe.md` según el usuario |
| 2026-08-16 | Archivos en `_ctx/` y `_prompts/` sin `galaxy_body` | Son archivos operativos, no notas del vault. Igual que los skills de Claude |
| 2026-08-16 | `phase_p/n/c/x` como campos YAML en cada sección | Tracker integrado en la nota — reemplaza la tabla separada de `REC92_tsk_informe.md` |

> [!note]- Descartadas
> - Carrier puro — los dropships modelan variantes/opciones, no outputs de producción por fase
> - `tpl-w-project.md` sin modificar — no tiene campos para secciones ni tracker de fases
> - `galaxy_body: blueprint` para archivos operativos — son archivos de trabajo, no ideas de proyecto

---

## Planificación

La carpeta REC92 tiene 7 archivos útiles (el duplicado `rec_perplexity 1.md` ya fue borrado por el usuario). La migración no toca el contenido — solo reorganiza y agrega estructura.

Restricciones:
- No editar contenido académico existente
- No romper el flujo de producción (Perplexity → NotebookLM → ChatGPT → Claude) ya documentado en `REC92_tsk_informe.md`
- El backup `E:\bk\REC92_bk` ya fue acordado — el usuario lo hace manualmente (sin acceso de Claude a esa ruta)

---

## Estructura objetivo

```
REC92/
├── tsk_REC92.md                  ← galaxy_body: workshop (hub del proyecto)
├── _ctx/
│   ├── contexto.md               ← sin galaxy_body (contenido de REC92_tsk.md)
│   ├── flujo.md                  ← sin galaxy_body (contenido de REC92_tsk_informe.md)
│   └── informe_apa.md            ← sin galaxy_body (renombrado de rec_informe_apa.md)
├── _prompts/
│   ├── plex_informe.md           ← sin galaxy_body (renombrado de rec_perplexity_informe.md)
│   ├── plex_datos.md             ← sin galaxy_body (renombrado de rec_perplexity_complemento.md)
│   ├── plex_bk.md                ← sin galaxy_body (renombrado de rec_perplexity.md — backup)
│   └── otras_ia.md               ← sin galaxy_body (renombrado de rec_otrasia.md)
└── _s/
    ├── s1_intro.md               ← galaxy_body: workshop (hub s1)
    ├── s2_marco.md               ← galaxy_body: workshop (hub s2)
    ├── s3_recursos.md            ← galaxy_body: workshop (hub s3)
    ├── s4_laguna.md              ← galaxy_body: workshop (hub s4)
    ├── s5_comparativa.md         ← galaxy_body: workshop (hub s5)
    ├── s6_impacto.md             ← galaxy_body: workshop (hub s6)
    └── s7_conclusiones.md        ← galaxy_body: workshop (hub s7)
```

---

## YAMLs definidos

### tsk_REC92.md
```yaml
---
title: "tsk_REC92 — Energía Geotérmica en Bolivia"
galaxy_body: workshop
subject: REC92
semester: 9
partial: 2
tags: [REC92, workshop, proyecto, P2]
date_created: 2026-08-16
date_updated: 2026-08-16
status: activo
phase: 1
sections:
  - "[[REC92/_s/s1_intro]]"
  - "[[REC92/_s/s2_marco]]"
  - "[[REC92/_s/s3_recursos]]"
  - "[[REC92/_s/s4_laguna]]"
  - "[[REC92/_s/s5_comparativa]]"
  - "[[REC92/_s/s6_impacto]]"
  - "[[REC92/_s/s7_conclusiones]]"
ctx:
  - "[[REC92/_ctx/contexto]]"
  - "[[REC92/_ctx/flujo]]"
  - "[[REC92/_ctx/informe_apa]]"
---
```

### s1_intro.md … s7_conclusiones.md (estructura común)
```yaml
---
title: "REC92 — s# Nombre"
galaxy_body: workshop
subject: REC92
semester: 9
partial: 2
tags: [REC92, workshop, P2]
date_updated: 2026-08-16
status: pendiente
section_num: #
section: nombre
hub: "[[REC92/tsk_REC92]]"
phase_p: ⬜
phase_n: ⬜
phase_c: ⬜
phase_x: ⬜
---
```

### Archivos en _ctx/ y _prompts/
```yaml
---
title: "REC92 — nombre descriptivo"
scope: REC92
date_updated: 2026-08-16
---
```

---

## Flujo de pasos

1. Crear carpetas `_ctx/`, `_prompts/`, `_s/` dentro de `REC92/`
2. Crear `tsk_REC92.md` con su YAML y estructura completa
3. Mover y renombrar archivos existentes a sus nuevas rutas:
   - `REC92_tsk.md` → `_ctx/contexto.md`
   - `REC92_tsk_informe.md` → `_ctx/flujo.md`
   - `rec_informe_apa.md` → `_ctx/informe_apa.md`
   - `rec_perplexity_informe.md` → `_prompts/plex_informe.md`
   - `rec_perplexity_complemento.md` → `_prompts/plex_datos.md`
   - `rec_perplexity.md` → `_prompts/plex_bk.md`
   - `rec_otrasia.md` → `_prompts/otras_ia.md`
4. Agregar YAML mínimo (`title`, `scope`, `date_updated`) a cada archivo movido
5. Crear los 7 archivos `s#_nombre.md` en `_s/` con su YAML y estructura de bloques
6. Verificar que no queden archivos huérfanos en la raíz de `REC92/`
7. Marcar ship como `delivered` y moverlo a `_hangar/_legacy/`

---

## Tareas

- [ ] Crear carpetas `_ctx/`, `_prompts/`, `_s/`
- [ ] Crear `tsk_REC92.md`
- [ ] Mover `REC92_tsk.md` → `_ctx/contexto.md` + agregar YAML mínimo
- [ ] Mover `REC92_tsk_informe.md` → `_ctx/flujo.md` + agregar YAML mínimo
- [ ] Mover `rec_informe_apa.md` → `_ctx/informe_apa.md` + agregar YAML mínimo
- [ ] Mover `rec_perplexity_informe.md` → `_prompts/plex_informe.md` + agregar YAML mínimo
- [ ] Mover `rec_perplexity_complemento.md` → `_prompts/plex_datos.md` + agregar YAML mínimo
- [ ] Mover `rec_perplexity.md` → `_prompts/plex_bk.md` + agregar YAML mínimo
- [ ] Mover `rec_otrasia.md` → `_prompts/otras_ia.md` + agregar YAML mínimo
- [ ] Crear `_s/s1_intro.md`
- [ ] Crear `_s/s2_marco.md`
- [ ] Crear `_s/s3_recursos.md`
- [ ] Crear `_s/s4_laguna.md`
- [ ] Crear `_s/s5_comparativa.md`
- [ ] Crear `_s/s6_impacto.md`
- [ ] Crear `_s/s7_conclusiones.md`
- [ ] Verificar estructura final con list_directory
- [ ] Marcar ship `delivered` → mover a `_hangar/_legacy/`

---

## Preguntas abiertas

- ¿El YAML mínimo de los archivos en `_ctx/` y `_prompts/` incluye `date_updated` o solo `title` y `scope`?
- ¿Los archivos `s#` necesitan bloque `%%` con galaxy-links desde el inicio, o se agrega cuando haya contenido real?

---

## Recursos

- `E:\University_vault_2026\REC92\` — carpeta origen
- `E:\bk\REC92_bk\` — backup manual del usuario (sin acceso de Claude)
- `E:\University_vault_2026\_hangar\template\tpl_ship.md` — plantilla usada
- `E:\University_vault_2026\_app\_config\_galaxy-system.md` — sistema galaxy
- `E:\University_vault_2026\_app\_config\_projects_system.md` — sistema de proyectos
