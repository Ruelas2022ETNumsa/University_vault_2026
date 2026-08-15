---
proyecto: REC92 — Energía Geotérmica en Bolivia
archivo: REC92_tsk_informe.md
uso: plan de trabajo para la creación del informe final
estado: en_diseño
---

# REC92 — Plan de Creación del Informe

---

## Flujo de trabajo diseñado

El informe se construye en capas, usando cuatro herramientas con roles distintos y complementarios.

```
PERPLEXITY
  → búsqueda de fuentes confiables y datos actualizados
  → prompt puntual por sección + instrucción de listar fuentes
  → guardar resultado como _p.md por sección

NOTEBOOKLM
  → recibe los PDFs propios + fuentes que entregó Perplexity
  → se le hace la misma pregunta adaptada a sus documentos
  → es más confiable para referencias porque cita el texto exacto
  → guardar resultado como _n.md por sección

CHATGPT (Project configurado con prompt de redacción)
  → recibe _p y _n de la misma sección
  → genera borrador fluido en español académico
  → guardar resultado como _c.md por sección

CLAUDE
  → recibe los tres archivos: _p, _n y _c
  → criterio de generación del _x:
      - estructura y redacción: toma de _c
      - datos, cifras y referencias: toma de _n (fuente de verdad)
      - contexto adicional: toma de _p solo si _n no lo cubre
      - si hay contradicción entre _n y _c en un dato, gana _n siempre
  → genera _x — versión final lista para insertar en el informe APA
```

---

## Roles de cada herramienta

| Herramienta | Rol | Peso |
|-------------|-----|------|
| Perplexity | Buscador de fuentes y datos actualizados | Borrador de NotebookLM |
| NotebookLM | Validador de fuentes — trabaja con PDFs reales | Fuente de verdad |
| ChatGPT | Redactor de borrador fluido | Borrador de Claude |
| Claude | Redactor final con criterio definido | Versión final (_x) |

---

## Archivos del proyecto

| Archivo | Descripción |
|---------|-------------|
| `REC92_tsk.md` | Plan general de investigación y antecedentes |
| `REC92_tsk_informe.md` | Este archivo — plan de creación del informe |
| `rec_perplexity.md` | Prompts de complemento e investigación (datos, estado actual, comparativa) |
| `rec_perplexity_informe.md` | Prompts de Perplexity orientados a cada sección del informe |
| `rec_otrasia.md` | Prompts para ChatGPT y Gemini |
| `rec_perplexity_complemento.md` | Prompts para datos concretos: inversión, costos, papers, normativa, altitud |
| `rec_informe_apa.md` | Plantilla del informe con estructura APA |

---

## Distinción entre archivos de prompts

**`rec_perplexity.md`** — prompts de complemento
Orientados a obtener datos puntuales: estado actual del proyecto, inversión ejecutada, comparativa regional, papers recientes, normativa. Son de investigación general, no están atados a una sección específica del informe. Se usan para alimentar NotebookLM con fuentes confiables.

**`rec_perplexity_informe.md`** — prompts de informe (nuevo)
Orientados directamente a cada sección del informe APA. Cada prompt está diseñado para obtener contenido que va a una sección específica. Todos incluyen al final la instrucción de listar fuentes con autor, año y URL.

---

## Fases del trabajo

### FASE 1 — Obtención de fuentes confiables (ACTUAL)
Toda la atención está en Perplexity como primer paso.
- Ejecutar los prompts de `rec_perplexity_informe.md` sección por sección
- Para cada prompt: guardar la respuesta como `_p.md` con el nombre de la sección
- Recopilar todas las fuentes que liste Perplexity
- Filtrar cuáles son PDFs accesibles para cargar a NotebookLM

### FASE 2 — Carga y consulta en NotebookLM
- Cargar PDFs propios ya filtrados + fuentes obtenidas en Fase 1
- Ejecutar consultas por sección
- Guardar resultados como `_n.md`

### FASE 3 — Borrador con ChatGPT
- Para cada sección: pasar `_p` + `_n` a ChatGPT
- Guardar borrador como `_c.md`

### FASE 4 — Versión final con Claude
- Para cada sección: pasar `_p`, `_n` y `_c`
- Claude genera `_x.md` con criterio definido arriba
- El `_x` es el texto listo para insertar en `rec_informe_apa.md`

---

## Estado por sección

| Sección                            | Fase 1 _p | Fase 2 _n | Fase 3 _c | Fase 4 _x |
| ---------------------------------- | --------- | --------- | --------- | --------- |
| Resumen                            | ⬜         | ⬜         | ⬜         | ⬜         |
| 1. Introducción                    | ⬜         | ⬜         | ⬜         | ⬜         |
| 2. Marco Teórico                   | ⬜         | ⬜         | ⬜         | ⬜         |
| 3. Recursos geotérmicos en Bolivia | ⬜         | ⬜         | ⬜         | ⬜         |
| 4. Proyecto Laguna Colorada        | ⬜         | ⬜         | ⬜         | ⬜         |
| 5. Análisis comparativo regional   | ⬜         | ⬜         | ⬜         | ⬜         |
| 6. Impacto ingeniería y soberanía  | ⬜         | ⬜         | ⬜         | ⬜         |
| 7. Conclusiones                    | ⬜         | ⬜         | ⬜         | ⬜         |
| Referencias APA                    | ⬜         | ⬜         | ⬜         | ⬜         |

---

## Notas

- El Resumen se escribe último — cuando todas las secciones están completas
- Las Referencias se construyen acumulando las fuentes de cada _n a lo largo del proceso
- Los prompts de `rec_perplexity.md` (complemento) se ejecutan en paralelo a la Fase 1 para alimentar NotebookLM con material adicional
- Si una fuente de Perplexity no tiene PDF accesible, igual se anota para citarla en APA desde la URL
