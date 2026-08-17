---
galaxy_body: logbook
scope: pdfpp_embed_nblm
status: on-track
date_updated: 2026-08-16
---

## Visión general

Explorar si NotebookLM puede generar automáticamente un link embed de PDF++ que apunte a la página exacta donde se encuentra una figura, en lugar de solo entregar los metadatos de IMA-SRC para localización manual. El carrier es grande porque involucra pruebas en NotebookLM, configuración de PDF++, y una restricción no resuelta de numeración de páginas. El criterio de éxito es lograr que el usuario pegue el embed en una nota `.md` y PDF++ renderice la página del libro inline sin intervención adicional.

---

## Estado actual

**Salud:** on-track
**Resumen:** Idea definida y documentada. Sin pruebas realizadas aún.
**Último avance:** Definición del flujo completo y análisis de features de PDF++. Conversión de ship a carrier.
**Próximo hito:** Primera prueba de embed básico en Obsidian + primera prueba en NotebookLM con notebook duplicado.

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `pdfpp_embed_nblm.md` | tsk | — | archivo de trabajo activo |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `chronicle.md` | chronicle | — | registro cronológico de pruebas |
| `prompts.md` | dropship | activo | prompts de prueba para NotebookLM |

---

## Hitos

- 2026-08-16 — definición del flujo completo y análisis de PDF++ features. Carrier creado.

---

## Riesgos y dependencias

- **Numeración de páginas:** NotebookLM entrega el número impreso en el libro, no el número que el visor PDF cuenta. PDF++ usa el número del visor. El desfase puede variar por PDF (portada, índice, etc.). Sin resolver. Ver pendiente de script delta abajo.
- **[[]] vs ![[]]:** el embed `![[]]` renderiza la página inline en Obsidian pero es lento. `[[]]` abre el PDF en otra ventana al hacer click — más liviano para navegar. Confirmado en prueba: usar `[[]]` en los prompts.

## Pendientes futuros

- **Script delta de numeración:** calcular la diferencia entre el número de página impreso en el libro y el número real del visor PDF (delta = visor − impreso). Si el delta es consistente por archivo, se puede corregir automáticamente el embed. Evaluar si vale la pena según resultados de las pruebas.
- **PDFs en vault:** Los libros de ETN607 deben estar en `_PDF\ETN-607\` con nombres consistentes con lo que IMA-SRC reporta como `fuente`. Por el momento la carpeta está vacía.
- **Límite del prompt v3:** 9985/10000 chars — sin margen para agregar instrucciones al prompt existente. Decisión tomada: no se modifica el prompt v3, se prueba de forma separada.

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-16 | No modificar el prompt v3 — probar el embed de forma separada con notebook duplicado | El prompt ya está al límite de caracteres |
| 2026-08-16 | IMA-SRC sigue siendo el flujo principal — este carrier es una mejora opcional | Si el embed no funciona bien, IMA-SRC no se toca |
| 2026-08-16 | Pendiente a futuro: duplicar el notebook — uno para transcripción, otro para el embed y complementos | Buena idea registrada, no es prioridad actual |

> [!note]- Descartadas
> - Redibujo automático con Gemini — descartado por complejidad; pruebas en `_hangar/IMA_NBLM/`
