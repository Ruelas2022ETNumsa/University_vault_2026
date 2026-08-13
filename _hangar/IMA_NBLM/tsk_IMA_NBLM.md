---
galaxy_body: carrier
project: "IMA-SRC — localización y extracción de imágenes desde fuentes NBLM"
date: 2026-08-10
status: docking
fleet: ETN607
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-13 | hora inicio: 14:50
**Retomar desde:** Refinamiento de P1 v3 e integración en prompts de materia
**Completado esta sesión:**
- P1 v3 redactado en `IMA_NBLM_promtp.md` — campo `id` unifica etiqueta y pie, justificación reducida a 1 oración, reglas colapsadas
- Pruebas adicionales realizadas con PDF con etiqueta → flujo validado
- Confirmado: error de página +1 es tolerable cuando existe etiqueta como ancla
- Confirmado: diapositivas sin número de página ni etiqueta fallan — caso separado
- Dropship `IMA_NBLM-opc_slides.md` creado para normalizar caso diapositivas
- Foco del carrier acotado: P1 (NBLM) para PDF con/sin etiqueta — Gemini puede esperar

**Próximo paso:** Evaluar P1 v3 en prueba real y definir si se integra en `ETN607-transcription.md`
**Preguntas de cierre:** —

---

## Resumen y objetivo

NBLM no puede mostrar imágenes de libros ni de apuntes en su output `.md`. El objetivo es que NBLM señalice la ubicación exacta de una imagen relevante (fuente, página, figura), que Gemini+fuentes genere una descripción técnica y un contexto simplificado, y que Gemini simple dibuje la figura a partir de ambos. En paralelo, un script Python en Obsidian abrirá el PDF en la página exacta para extracción manual con PDF++.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-10 | Separar `IMA` (apuntes) de `IMA-SRC` (fuentes externas) | `IMA` ya funciona en ETN607; `IMA-SRC` es el caso nuevo |
| 2026-08-10 | Priorizar Ruta A (PDF++ semi-manual) como paso 1 | NBLM no da coordenadas de píxel; PDF++ ya integrado |
| 2026-08-10 | Flujo de 3 pasos: NBLM → Gemini+fuentes → Gemini imagen | Validado con prueba real — resultados buenos |
| 2026-08-10 | Separar Prompt 2 (descripción) de Prompt 2b (contexto) | Cada prompt tiene un rol distinto — mezclarlos obliga a Gemini+fuentes a hacer dos cosas a la vez |
| 2026-08-10 | Input de todos los prompts: Rx completo | Evita recortar manualmente — se pega toda la respuesta de NBLM |
| 2026-08-10 | Página en IMA-SRC = número impreso en el libro | NBLM entrega página impresa (207), no la del visor PDF (231) — el script debe contemplar el desfase |

> [!note]- Descartadas
> Ruta B (extracción automática con pymupdf) descartada como paso 1 — requiere coordenadas de región que NBLM no puede entregar. Queda como paso 2 si Ruta A resulta insuficiente.

---

## Planificación

**Capa 1 — NBLM señaliza:** prompt v2 activo. NBLM entrega explicación del concepto + bloque IMA-SRC con fuente, página impresa, etiqueta, pie y justificación.

**Capa 2 — Gemini describe y contextualiza:** Gemini+fuentes recibe Rx completo y ejecuta dos prompts separados — descripción técnica visual (P2) y contexto simplificado de 1 oración (P2b).

**Capa 3 — Gemini dibuja:** Gemini simple recibe Ry (descripción) + Rz (contexto) y genera la imagen con etiqueta de figura, estilo libro de texto, sin elementos extra.

**Capa 4 — Obsidian extrae (pendiente):** script Python `ima_src_opener` parsea el `.md`, detecta bloques IMA-SRC, abre el PDF en la página exacta vía URI Obsidian. Usuario recorta con PDF++ y pega.

---

## Flujo de pasos

1. Pregunta a NBLM con fuentes → entrega Rx (explicación + bloque IMA-SRC)
2. Gemini+fuentes con Prompt 2 + Rx → entrega Ry (descripción técnica visual)
3. Gemini+fuentes con Prompt 2b + Rx → entrega Rz (contexto simplificado, 1 oración)
4. Gemini simple con Ry + Rz → genera imagen con etiqueta de figura
5. *(pendiente)* Script `ima_src_opener` abre PDF en página exacta en Obsidian
6. *(pendiente)* Usuario recorta con PDF++ e inserta imagen en el `.md`
7. *(pendiente)* Agregar instrucción IMA-SRC al prompt ETN607-transcription.md
8. *(opcional v2)* Extracción automática con pymupdf si flujo manual es lento

---

## Tareas

- [x] Probar NBLM: localización de figura con libro + página + etiqueta → ✅ Figura 4.4, Apostol p.207
- [x] Definir formato IMA-SRC → ✅ v2 activo con campo `justificación`
- [x] Redactar prompts del flujo (P1v2, P2, P2b, P3) → ✅ en `IMA_NBLM_promtp.md`
- [x] Validar flujo completo con prueba real → ✅ imagen generada correcta
- [x] Documentar pruebas → ✅ `Gemini_fuentes_pruebas.md` + dropship `IMA_NBLM-prueba_p1.md`
- [ ] Probar Prompt 2b — validar Rz como contexto vs. Rx directo en Gemini simple
- [ ] Redactar instrucción IMA-SRC para prompt ETN607-transcription.md
- [ ] Crear script `ima_src_opener/main.py`
- [ ] Registrar script en Shell Commands
- [ ] Test de flujo completo en ETN607

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | ---- | ------ | ----------- |
| `tsk_IMA_NBLM.md` | carrier | docking | Este archivo — tareas activas |
| `logbook.md` | logbook | — | README histórico del proyecto |
| `Gemini_fuentes_pruebas.md` | logbook | — | Documentación extendida de pruebas |
| `IMA_NBLM_promtp.md` | dropship | activo | Prompts P1v1, P1v2, P2, P2b, P3 |
| `IMA_NBLM-prueba_p1.md` | dropship | evaluado | Prueba fase 1 — flujo NBLM→Gemini+f→Gemini→imagen |
| `IMA_NBLM-opc_slides.md` | dropship | activo | Caso especial diapositivas — pendiente normalización |

---

## Preguntas abiertas

- ¿El Prompt 2b mejora el resultado de Gemini simple respecto a usar Rx directo como contexto? → pendiente prueba
- ¿Cómo manejar el desfase página PDF vs. página impresa en `ima_src_opener`? → NBLM da página impresa; script debe mapearlo
- ¿El prompt IMA-SRC final va en las instrucciones del cuaderno NBLM o como primer mensaje del usuario?
- La recta tangente en P no aparece en el dibujo generado — ¿vale la pena una instrucción adicional en P3 o se acepta como limitación?

---

## Recursos

- Prompts IMA-SRC: `E:\University_vault_2026\_hangar\IMA_NBLM\IMA_NBLM_promtp.md`
- Documentación de pruebas: `E:\University_vault_2026\_hangar\IMA_NBLM\Gemini_fuentes_pruebas.md`
- Prompt activo ETN607: `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\ETN607-transcription.md`
- Guía PDF++: `E:\University_vault_2026\_app\_appnotes\PDF_PP-guide.md`
- Shell Commands config: `E:\University_vault_2026\_app\shellcommands\shellcmd_config_script.md`
- Scripts Python: `{{vault_path}}\.obsidian\scripts\python\`