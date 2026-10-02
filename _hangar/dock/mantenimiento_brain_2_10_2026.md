---
galaxy_body: ship
project: "mantenimiento_brain_2_10_2026"
date: 2026-10-02
status: docked
fleet:
blocked_by:
---
%%
galaxy_body: ship → carrier si el proyecto escala (necesita carpeta propia y archivos extra)

status:
- docked: en dock/, esperando operator
- in-orbit: fue trabajado, pausado sin dependencia externa
- delayed: bloqueado por dependencia externa — ver blocked_by
- delivered: terminado y documentado, listo para archivar
- aborted: proyecto no viable, descartado
%%

## Handoff
%%
Sobreescribir con edit_file al cerrar cada sesión.
Es lo primero que Claude lee al retomar — debe ser suficiente para arrancar sin re-explicar.
%%

**Última sesión:** 2026-10-02 — discusión y registro de la tarea (sin ediciones al vault salvo este archivo)
**Retomar desde:** `_app/_config/_galaxy-system.md` — secciones "El grafo de Obsidian y los wikilinks" y "Registro de decisiones de diseño"
**Completado esta sesión:** Revisión de `_galaxy-system.md`; se identificaron 4 puntos de mantenimiento y se acordó posponerlos.
**Próximo paso:** Cuando haya tiempo (fuera de época de clases en vivo), empezar por el punto 3 (inconsistencias de nombres), que es lo más barato de corregir.
**Preguntas de cierre:** ¿El grafo de Obsidian detecta enlaces dentro de propiedades YAML en esta versión? ¿DataView puede leer enlaces dentro de bloques `%%`?

---

## Resumen y objetivo
Tarea de mantenimiento diferida del cerebro digital (Sistema Galaxy). Reúne 4 puntos detectados el 2026-10-02: redefinir el rol del YAML frente a los `galaxy-links`, simplificar el uso del sistema en materias en vivo, corregir inconsistencias de nombres y rutas, y evaluar el tamaño del archivo detallado `_galaxy-system.md`. Ninguno es crítico; se resuelven cuando haya tiempo de mantenimiento.

## Decisiones

| Fecha      | Decisión                                                                                                                      | Motivo                                                                                                                  |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 2026-10-02 | Los `%%galaxy-links%%` se mantienen como capa de conexión para archivos dentro del sistema galaxy                             | Usan ruta completa (sin ambigüedad) y alimentan el grafo de Obsidian. El YAML tenía el problema de la ruta.             |
| 2026-10-02 | El YAML se rediseñará para enlaces fuera del sistema galaxy (ej. imágenes, recursos externos); diseño aún sin definir         | Evita mantener la misma conexión en dos lugares.                                                                        |
| 2026-10-02 | En materias en vivo se usa solo `supernova`; la disección en planet/moon/comet se hace en materias pasadas                    | En el cuatrimestre no hay tiempo para estructurar todo. Una supernova basta para estudiar y consultar con IA.           |
| 2026-10-02 | Las inconsistencias de nombres no son críticas y se corrigen con el tiempo                                                    | No rompen el funcionamiento mientras se sepa cuál es el archivo correcto.                                               |
| 2026-10-02 | `_galaxy-system.md` se mantiene largo y detallado; no es el archivo de carga                                                  | El archivo de carga es el resumido, así que el tamaño no cuesta tokens en cada sesión.                                  |

> [!note]- Descartadas
> Mantener la doble capa YAML + `%%` sincronizada para las mismas relaciones — descartado como diseño ideal por el costo de mantenimiento y el riesgo de desincronización.

---

## Planificación
Enfoque: tarea de bajo costo y sin urgencia. Se hace en periodo sin clases en vivo. Orden sugerido: 3 → 1 → 2 → 4.

Restricciones:
- No editar nada hasta tener tiempo de mantenimiento y backup (`nombre 1.md`).
- ETN302 sigue siendo legacy: no renombrar (rompería wikilinks).

**Los 4 puntos:**

1. **YAML vs galaxy-links.** Los `galaxy-links` quedan para archivos dentro del sistema galaxy. El YAML pasa a usarse para enlaces fuera del sistema (imágenes, recursos externos), con diseño por definir. Verificar antes: si el grafo de Obsidian detecta enlaces en propiedades YAML, y si DataView puede leer enlaces dentro de `%%`. Si no puede, conservar en el YAML un mínimo de campos de relación (aunque sin ruta) para no perder filtros.
2. **Materias en vivo solo con supernova.** Para materias en curso, un único archivo supernova basta. Riesgo: sin conexiones no hay cruces entre materias. Mitigación: mantener `subtopics` bien puestos en el YAML; si se acerca un parcial, diseccionar solo los temas más difíciles.
3. **Inconsistencias de nombres y rutas.** Slugs con barra baja (convención) vs guiones (ejemplos YAML); `_pdf-system` vs `_pdf_pp-system`; `_TABnote-system` vs `_TAB_note-system`; workers en `_hangar\bay\` (`_start.md`) vs raíz de `_hangar` (`_galaxy-system.md`); plantillas `tsk_tpl.md` vs `tpl_worker.md` / `tpl_ship.md` / `tpl_carrier.md`; el listado real de `_hangar` (anki, bay, blueprint, IMA_NBLM, pdfpp_embed_nblm, template, TPL_TAB, _legacy) no coincide con el mapa de carpetas.
4. **Tamaño de `_galaxy-system.md`.** Es largo, pero es el detallado, no el de carga. Opción a futuro: dividir en conceptos (corto) y plantillas YAML. No urgente.

---

## Sugerencias
%%
Se puebla cuando el usuario dispara la búsqueda con la palabra "web".
%%

---

## Flujo de pasos
1. Hacer backup de `_galaxy-system.md` y de los archivos que se vayan a tocar.
2. Punto 3: listar y corregir inconsistencias de nombres y rutas (decidir cuál es la forma oficial de cada una).
3. Punto 1: probar con una nota de prueba si el grafo detecta enlaces en YAML y si DataView lee enlaces dentro de `%%`; luego definir el rol final del YAML.
4. Punto 2: documentar la regla "materia en vivo = solo supernova" en el sistema y en las plantillas.
5. Punto 4: decidir si se divide `_galaxy-system.md`.
6. Registrar decisiones en la tabla y actualizar `_galaxy-system.md`.

---

## Tareas

- [ ] Punto 1 — Probar grafo con enlaces YAML y DataView con enlaces dentro de `%%`
- [ ] Punto 1 — Definir el nuevo rol del YAML (enlaces fuera del sistema galaxy)
- [ ] Punto 2 — Documentar la regla "materia en vivo = solo supernova"
- [ ] Punto 3 — Unificar slugs (barra baja vs guiones) en convención y ejemplos
- [ ] Punto 3 — Corregir nombres `_pdf-system` / `_pdf_pp-system` y `_TABnote-system` / `_TAB_note-system`
- [ ] Punto 3 — Alinear ubicación de workers (`bay\` vs raíz de `_hangar`) y nombres de plantillas
- [ ] Punto 3 — Actualizar el mapa de carpetas de `_hangar` con la estructura real
- [ ] Punto 4 — Decidir si se divide `_galaxy-system.md`

---

## Preguntas abiertas
- ¿El grafo de Obsidian detecta enlaces dentro de propiedades YAML en la versión instalada?
- ¿DataView puede leer enlaces dentro de bloques `%%`?
- ¿Qué se usará exactamente el YAML para enlaces externos (imágenes, PDFs, otros)?
- ¿El sistema de proyectos (`_hangar`) se simplifica también durante el cuatrimestre?

---

## Recursos
- `_app/_config/_galaxy-system.md` — archivo detallado del sistema
- `_app/_config/_projects_system.md` — sistema de proyectos
- `_app/_config/_template-system.md` — plantillas
- `_hangar/template/tpl_ship.md` — plantilla de este ship
- `_skills/_claude-plan.md` — skill de planificación
