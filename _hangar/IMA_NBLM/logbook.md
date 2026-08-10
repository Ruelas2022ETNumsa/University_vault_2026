---
galaxy_body: logbook
scope: IMA_NBLM
status: on-track
date_updated: 2026-08-10
---

## Visión general

IMA-SRC es un flujo para que NBLM señalice figuras de libros en su output `.md` y que Gemini las describa y dibuje como imagen reutilizable en apuntes de Obsidian. Escala a carrier porque combina pruebas de IAs (NBLM, Gemini+fuentes, Gemini imagen), diseño de prompts, y desarrollo de un script Python de extracción — tres capas independientes con archivos propios. El criterio de éxito es un flujo completo: consulta en NBLM → imagen insertada en el `.md` de Obsidian con mínima intervención manual.

---

## Estado actual

**Salud:** on-track
**Resumen:** Flujo de 3 pasos (NBLM → Gemini+fuentes → Gemini imagen) definido y validado con prueba real. Prompts redactados y documentados. Pendiente validar Prompt 2b y desarrollar el script de extracción.
**Último avance:** Validación completa del flujo con Figura 4.4 (Apostol, derivada) — imagen generada correcta y didácticamente útil.
**Próximo hito:** Validar Prompt 2b (Rz) como contexto simplificado vs. Rx directo en Gemini simple.

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `tsk_IMA_NBLM.md` | tsk | — | archivo de trabajo activo |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `Gemini_fuentes_pruebas.md` | logbook | — | documentación extendida de pruebas |
| `IMA_NBLM_promtp.md` | dropship | activo | prompts P1v1, P1v2, P2, P2b, P3 |
| `IMA_NBLM-prueba_p1.md` | dropship | evaluado | prueba fase 1 — flujo NBLM→Gemini+f→Gemini→imagen |

---

## Hitos

- 2026-08-10 — Confirmado que NBLM localiza figuras de libros con precisión (fuente + página impresa + etiqueta)
- 2026-08-10 — Formato IMA-SRC v2 definido con campo `justificación`
- 2026-08-10 — Flujo de 3 pasos validado con prueba real — imagen generada correcta
- 2026-08-10 — Carrier creado — proyecto escalado desde ship

---

## Riesgos y dependencias

- Desfase página impresa vs. visor PDF — NBLM entrega página impresa (ej: 207), el visor marca otra (231). El script `ima_src_opener` debe contemplarlo.
- Gemini+fuentes no puede generar imágenes (error 1152) — limitación real de la modalidad, no resoluble en el flujo actual.
- La recta tangente en P no aparece en el dibujo generado por Gemini — limitación conocida, aceptada por ahora.

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-10 | Separar `IMA` (apuntes) de `IMA-SRC` (fuentes externas) | `IMA` ya funciona en ETN607; `IMA-SRC` es el caso nuevo |
| 2026-08-10 | Flujo de 3 pasos: NBLM → Gemini+fuentes → Gemini imagen | Validado con prueba real — cada IA hace lo que sabe hacer |
| 2026-08-10 | Separar Prompt 2 (descripción) de Prompt 2b (contexto) | Roles distintos — mezclarlos obliga a Gemini+fuentes a hacer dos cosas a la vez |
| 2026-08-10 | Input siempre Rx completo | Evita recortar manualmente — agiliza el flujo |
| 2026-08-10 | Página IMA-SRC = número impreso en el libro | NBLM entrega página impresa, no la del visor PDF |
| 2026-08-10 | Priorizar Ruta A (PDF++ semi-manual) como extracción paso 1 | NBLM no da coordenadas de píxel; PDF++ ya integrado en el vault |

> [!note]- Descartadas
> - Ruta B (extracción automática pymupdf) descartada como paso 1 — requiere coordenadas de región que NBLM no puede entregar. Queda como paso 2 opcional.