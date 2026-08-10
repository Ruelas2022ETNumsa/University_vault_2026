---
galaxy_body: ship
project: "Imagen a .md via base64 para lectura de Claude"
date: 2026-08-10
status: aborted
fleet:
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-10
**Retomar desde:** —
**Completado esta sesión:** Idea evaluada y descartada en conversación
**Próximo paso:** ninguno — aborted
**Preguntas de cierre:** —

---

## Resumen y objetivo

Crear un script Python que convierta una imagen PNG a base64 y la embeba en un archivo `.md`, para que Claude pueda "leerla" desde el vault sin necesidad de adjuntarla al chat — ahorrando tokens.

## Decisiones

| Fecha | Decisión | Motivo |
| ---------- | -------- | ------ |
| 2026-08-10 | Idea abortada | Base64 infla el tamaño un ~33%; Claude leyendo base64 crudo desde un .md consume más tokens que adjuntar la imagen directamente al chat |

> [!note]- Descartadas
> - **Script que genera descripción textual de la imagen:** Variante considerada donde el script analiza la imagen y produce un `.md` con descripción en texto plano. Potencialmente útil para imágenes recurrentes o de referencia fija, pero fuera del alcance del objetivo original.

---

## Planificación

El flujo propuesto era:
1. Script Python lee el PNG y lo convierte a base64
2. Embebe el base64 en un `.md` (ej. como bloque de código o data URI)
3. Claude lee el `.md` y procesa la imagen

**Por qué no funciona:** El sistema de adjuntos del chat maneja la imagen de forma más eficiente que leer base64 crudo desde texto. Adjuntar directamente es más liviano en tokens, no más pesado.

---

## Sugerencias

Una variante viable (no desarrollada): script que use una API de visión para generar una descripción textual de la imagen y la guarde como `.md`. Eso sí reduciría tokens en usos repetidos de la misma imagen.

---

## Flujo de pasos

No aplica — idea no ejecutada.

---

## Tareas

- [x] Evaluar si base64 en .md ahorra tokens vs adjuntar imagen
- [x] Descartar idea

---

## Preguntas abiertas

—

---

## Recursos

—
