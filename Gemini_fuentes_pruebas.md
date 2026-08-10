---
title: "Pruebas IMA-SRC — NBLM, Gemini+fuentes, Gemini"
date: 2026-08-10
project: IMA-SRC
status: documentado
---

# Pruebas IMA-SRC

Pruebas realizadas para evaluar la capacidad de NotebookLM (NBLM) y Gemini de localizar, describir y representar figuras de libros en PDF. El objetivo de fondo es alimentar el flujo IMA-SRC: que una IA señalice la ubicación exacta de una figura para que luego un script la extraiga e inserte en el `.md` de Obsidian.

El prompt usado en todas las pruebas con NBLM: `E:\University_vault_2026\IMA_NBLM_promtp.md`
Fuente usada: *Apostol vol 1 2ed-Calculus-1to7.pdf* — cuaderno de Cálculo 1 en NBLM.

---

## Prueba 1 — NBLM con prompt IMA-SRC

**Consulta enviada:** "explica la derivada"

**Resultado:** NBLM entregó la explicación del concepto en dos oraciones y generó tres bloques IMA-SRC correctamente formateados, citando figuras de Apostol y Piskunov con fuente, página, etiqueta de figura, ubicación y descripción relevante.

**Observaciones:**

- El prompt funcionó correctamente: NBLM respetó el formato IMA-SRC y las condiciones de citado.
- NBLM entrega el **número de página impreso en el libro**, no el número de página del visor PDF. Ejemplo: entrega `página: 207` (impreso en Apostol) cuando el visor PDF marca la página 231. Esto implica un desfase que el script `ima_src_opener` deberá contemplar.
- La etiqueta de figura ("Figura 4.4") fue identificada y usada correctamente como campo prioritario.
- El pie de figura fue incluido con el texto completo tal como aparece en el libro.
- La descripción relevante conectó la imagen con el concepto explicado en las dos oraciones previas.

**Conclusión:** NBLM localiza figuras de libros con precisión suficiente para el flujo IMA-SRC. El formato v1 del prompt es viable.

---

## Prueba 2 — Gemini con fuentes de NBLM (Gemini+fuentes)

**Contexto:** Dentro de Gemini, en la barra lateral izquierda se pueden acceder a los cuadernos de NBLM. Al seleccionar uno, Gemini puede consultarlo. Las fuentes están disponibles pero Gemini no las lee hasta que se le solicita explícitamente.

**Consulta enviada:**
> "Tengo en este cuaderno el libro 'Apostol vol 1 Calculus'. ¿Puedes ver la Figura 4.4 de la página 207 (página del PDF)? Descríbela con detalle y dime qué se ve en ella."

**Resultado:** Gemini entregó una descripción detallada y estructurada de la Figura 4.4, identificando ejes, puntos P y Q, recta secante, triángulo rectángulo auxiliar, y la interpretación geométrica del cociente de diferencias. Además generó espontáneamente un bloque IMA-SRC con la terminología correcta.

**Observaciones:**

- La descripción fue más detallada que la entregada por NBLM para la misma figura.
- Gemini adoptó el formato IMA-SRC sin que se le instruyera explícitamente — posiblemente por contexto del cuaderno.
- **Gemini+fuentes no puede generar imágenes** — al intentarlo devuelve error 1152 (límite de función no disponible). Esta es una limitación real de la modalidad.
- La descripción entregada por Gemini+fuentes resultó suficientemente precisa para usarla como insumo en la prueba siguiente.

**Conclusión:** Gemini+fuentes es útil para obtener descripciones detalladas de figuras. No reemplaza a NBLM como señalizador dentro del flujo IMA-SRC, pero puede complementar la descripción cuando se necesita mayor detalle.

---

## Prueba 3 — Gemini sin fuentes (solo descripción)

**Contexto:** Se tomó la descripción generada por Gemini+fuentes en la prueba anterior y se llevó a Gemini estándar (sin acceso a las fuentes del cuaderno) para pedirle que dibujara la figura a partir de esa descripción.

**Consulta enviada:** Se le proporcionó la descripción completa de la Figura 4.4 obtenida en la prueba 2 y se le pidió que la dibujara.

**Resultado:** Gemini generó la figura correctamente a partir de la descripción — ejes, curva, puntos, recta secante y triángulo rectángulo visibles y bien ubicados.

**Observaciones y mejoras identificadas para el prompt de descripción:**

- No agregar descripción textual debajo de la imagen generada — ya se cuenta con una.
- Incluir solo la etiqueta de figura ("Figura 4.4") en la parte superior de la imagen generada.
- El pie de figura fue incorporado correctamente gracias al nivel de detalle en la descripción de Gemini+fuentes.
- Los detalles internos de la figura (nombres de líneas, puntos, ángulos) fueron representados correctamente.

**Conclusión:** Gemini puede generar representaciones visuales útiles de figuras matemáticas a partir de descripciones textuales suficientemente detalladas. La calidad del dibujo depende directamente de la calidad de la descripción IMA-SRC.

---

## Resumen de resultados

| IA | Ve figuras en PDF | Describe con detalle | Genera imagen | Entrega bloque IMA-SRC |
|----|:-:|:-:|:-:|:-:|
| NBLM | ✅ | Parcial | ❌ | ✅ (con prompt) |
| Gemini+fuentes | ✅ | ✅ | ❌ (error 1152) | ✅ (espontáneo) |
| Gemini (sin fuentes) | ❌ | — | ✅ | — |

---

## Pendientes

- Definir si el campo `página` en IMA-SRC documenta la página impresa o la del visor PDF — actualmente NBLM entrega la impresa; el script `ima_src_opener` debe contemplar el desfase.
- Mejorar el prompt de descripción para que Gemini no agregue texto redundante al generar imágenes (solo etiqueta de figura en la parte superior).
