---
galaxy_body: ship
project: "Integración etiqueta Figura a TABnote"
date: 2026-08-10
status: delivered
fleet:
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-10
**Retomar desde:** —
**Completado esta sesión:** Diseño completo e integración a `_TABnote-ref.md`
**Próximo paso:** ninguno — delivered
**Preguntas de cierre:** —

---

## Resumen y objetivo

Diseñar e integrar la convención de etiquetado de imágenes (`Figura T.N`) al sistema TABnote, compatible con el flujo IMA-SRC de NotebookLM.

## Decisiones

| Fecha | Decisión | Motivo |
| ---------- | -------- | ------ |
| 2026-08-10 | Delimitador: caja cerrada de 4 lados (cualquier color) | Más flexible que 2 líneas — funciona para media página o página completa |
| 2026-08-10 | Etiqueta `Figura T.N` dentro de la caja, primera línea | NLM lee etiqueta + contenido como unidad — no los separa |
| 2026-08-10 | Pie de descripción opcional, limpio, sin prefijo | Dentro de la caja ya es claro que pertenece a la figura |
| 2026-08-10 | Numeración T.N (tema.número) revisada a mano antes de exportar | Consistente con la convención de libros de ingeniería por capítulo |
| 2026-08-10 | Mapas mentales con corchetes del docente tratados como Figura | NBLM no los transcribe correctamente — mejor encerrarlos como imagen |
| 2026-08-10 | `IMA` eliminado | Reemplazado por `Figura` como señal para NLM — validado en prueba 1 |

> [!note]- Descartadas
> - **2 líneas grises horizontales:** descartadas porque no delimitan correctamente cuando la imagen ocupa solo media página.

---

## Planificación

Integrar al sistema TABnote existente una convención de figura que: (1) sea fácil de escribir a mano en Samsung Notes, (2) sea reconocida por NLM para entregar el bloque IMA-SRC, y (3) sea consistente con la terminología académica estándar de libros de ingeniería.

---

## Sugerencias

- Terminología académica universal: **Figura + número arábigo correlativo** — APA, IEEE, MLA, Chicago y normas en español convergen en esto.
- Prueba 1 validada en `Gemini_fuentes_pruebas.md`: NLM con prompt v2 detecta `Figura 4.4` y entrega número de página, etiqueta y pie correctamente.

---

## Flujo de pasos

1. Investigar terminología académica estándar para imágenes
2. Definir delimitador (caja vs líneas)
3. Definir posición de etiqueta (dentro/fuera, arriba/abajo)
4. Definir pie de figura (obligatorio/opcional, con prefijo/limpio)
5. Definir numeración (T.N por tema)
6. Integrar a `_TABnote-ref.md`

---

## Tareas

- [x] Investigar terminología académica
- [x] Decidir delimitador — caja cerrada
- [x] Decidir posición etiqueta — dentro, primera línea
- [x] Decidir pie — opcional, limpio
- [x] Decidir numeración — T.N revisada antes de exportar
- [x] Editar `_TABnote-ref.md` sección Imagen

---

## Preguntas abiertas

—

---

## Recursos

- `E:\University_vault_2026\_hangar\TPL_TAB\_TABnote-ref.md` — archivo editado
- `E:\University_vault_2026\_hangar\IMA_NBLM\Gemini_fuentes_pruebas.md` — validación NLM
