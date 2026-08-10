---
galaxy_body: ship
project: "IMA-SRC — localización y extracción de imágenes desde fuentes NBLM"
date: 2026-08-10
status: docked
fleet: ETN607
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

**Última sesión:** 2026-08-10 | hora inicio: 12:52
**Retomar desde:** Diseño del prompt IMA-SRC — mejoras y consolidación
**Completado esta sesión:**
- Prueba NBLM con cuaderno de Cálculo 1 (Apostol vol 1)
- Confirmado: NBLM ve e interpreta imágenes en PDFs
- Confirmado: NBLM usa nº de página del PDF (no el impreso en el libro)
- Confirmado: NBLM referencia figuras por su nombre en el libro (ej: "Figura 4.4") — más útil que posición
- Formato IMA-SRC v1 probado con Figura 4.4 (derivada, Apostol p.207) — resultado correcto
- Decisión: mantener campo `ubicación` + agregar campo `referencia` como prioritario
- Prompt de prueba creado en `E:\University_vault_2026\IMA_NBLM_promtp.md`
- Pendiente registrado: numerar imágenes propias en apuntes tipo "Figura X" para que NBLM las referencie igual que libros
**Próximo paso:** Mejorar prompt IMA-SRC (análisis y sugerencias activos — no editar aún)
**Preguntas de cierre:** —

---

## Resumen y objetivo

NBLM no puede mostrar imágenes de libros ni de apuntes en su output `.md`. El objetivo es que NBLM señalice explícitamente en el `.md` la ubicación exacta de una imagen relevante (fuente, página, nº figura), y que un mecanismo en Obsidian (PDF++ + script Python vía Shell Commands) la extraiga e inserte en su lugar.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-10 | Separar `IMA` (apuntes) de `IMA-SRC` (fuentes externas) | `IMA` ya funciona en el prompt ETN607; `IMA-SRC` es el caso nuevo |
| 2026-08-10 | Priorizar Ruta A (PDF++ semi-manual) como paso 1 | NBLM no da coordenadas de píxel; PDF++ ya está integrado en el vault |

> [!note]- Descartadas
> Ruta B (extracción automática con pymupdf) descartada como paso 1 — requiere coordenadas de región que NBLM no puede entregar con precisión. Queda como paso 2 si Ruta A resulta insuficiente.

---

## Planificación

El problema tiene dos capas independientes:

**Capa 1 — NBLM señaliza:** ajustar el prompt de transcripción para que, cuando detecte una imagen relevante en una fuente, emita un bloque `IMA-SRC` estandarizado con: archivo fuente, página, nº de figura y descripción. Formato a definir según prueba (ver Preguntas abiertas). Restricción: mínimo de caracteres en el prompt.

**Capa 2 — Obsidian extrae:** script Python (Shell Commands) que parsea el `.md`, detecta bloques `IMA-SRC`, y abre el PDF en la página exacta en Obsidian vía URI `obsidian://`. El usuario recorta con PDF++ y pega. En una v2 posible: extracción automática con pymupdf si se consiguen coordenadas.

Restricciones clave:
- NBLM solo señaliza si puede localizar la figura con certeza — si no, omite (ya establecido en prompt)
- El formato `IMA-SRC` debe ser parseable por script y económico en caracteres
- No romper el flujo `IMA` existente para imágenes de apuntes

---

## Sugerencias
%%
Se puebla cuando el usuario dispara la búsqueda con la palabra "web".
%%

---

## Flujo de pasos

1. Probar en NBLM si localiza figuras de libros con precisión suficiente (libro + página + nº figura)
2. Según resultado: definir formato `IMA-SRC` (comentario `%% %%` vs texto visible)
3. Agregar instrucción `IMA-SRC` al prompt `ETN607-transcription.md`
4. Crear script Python `ima_src_opener` en `.obsidian/scripts/python/` — lee `.md`, detecta bloques `IMA-SRC`, abre PDF en página exacta vía URI Obsidian
5. Registrar script en Shell Commands (PowerShell 5, alias: `IMA — abrir fuente en página`)
6. Probar flujo completo: NBLM genera bloque → script abre PDF → PDF++ recorta → imagen insertada
7. (Opcional v2) Script automático con pymupdf si el flujo manual es lento

---

## Tareas

- [x] Probar NBLM: pedir que localice una figura con libro + página + nº figura → ✅ funciona (Apostol, Figura 4.4, p.207)
- [x] Definir formato `IMA-SRC` según resultado de la prueba → ✅ v1 definido y probado
- [ ] Redactar instrucción `IMA-SRC` para el prompt (mínimo caracteres)
- [ ] Crear script `ima_src_opener/main.py`
- [ ] Registrar en Shell Commands
- [ ] Test de flujo completo en ETN607

---

## Preguntas abiertas

- ~~¿NBLM localiza figuras de libros con precisión real?~~ → ✅ confirmado viable
- ~~¿Formato `IMA-SRC`: comentario o texto visible?~~ → pendiente decidir al consolidar prompt final
- ¿Cómo manejar el desfase página PDF vs página impresa en el script `ima_src_opener`? → NBLM da página PDF; script debe usar ese número directo
- ¿El prompt final va en las instrucciones del cuaderno o como primer mensaje del usuario?

---

## Recursos

- Prompt activo ETN607: `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\ETN607-transcription.md`
- Prompt IMA-SRC v1 (prueba): `E:\University_vault_2026\IMA_NBLM_promtp.md`
- Guía PDF++: `E:\University_vault_2026\_app\_appnotes\PDF_PP-guide.md`
- Shell Commands config: `E:\University_vault_2026\_app\shellcommands\shellcmd_config_script.md`
- Scripts Python: `{{vault_path}}\.obsidian\scripts\python\`
- Plugin: PDF++ (ya configurado en vault)
