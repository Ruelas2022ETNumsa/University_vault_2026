---
title: "Pruebas IMA-SRC — NBLM, Gemini+fuentes, Gemini"
date: 2026-08-10
project: IMA-SRC
status: documentado
---

# Pruebas IMA-SRC

Pruebas realizadas para evaluar la capacidad de NotebookLM (NBLM) y Gemini de localizar, describir y representar figuras de libros en PDF. El objetivo de fondo es alimentar el flujo IMA-SRC: que una IA señalice la ubicación exacta de una figura para que luego un script la extraiga e inserte en el `.md` de Obsidian.

El prompt usado en todas las pruebas con NBLM: `E:\University_vault_2026\_hangar\IMA_NBLM\IMA_NBLM_promtp.md`
Fuente usada: *Apostol vol 1 2ed-Calculus-1to7.pdf* — cuaderno de Cálculo 1 en NBLM.

---

## Prueba 1 — NBLM con prompt IMA-SRC v2

**Consulta enviada:** "explica la derivada"

**Respuesta de NBLM:**
> La derivada es una función que representa la razón de cambio instantánea de una variable respecto a otra, calculada formalmente como el límite del cociente de diferencias cuando el incremento de la variable independiente tiende a cero. Geométricamente, este valor equivale a la pendiente de la recta tangente a la curva de la función en un punto determinado.
>
> IMA-SRC | fuente: Apostol vol 1 2ed-Calculus-1to7.pdf | página: 207 | etiqueta de figura: Figura 4.4 | pie de figura: Interpretación geométrica del cociente de diferencia como tangente de un ángulo | ubicación: Parte central de la página
> justificación: Esta figura es de gran utilidad ya que permite visualizar de manera directa cómo el cociente de diferencias representa la pendiente de una recta secante, conectando de forma intuitiva este concepto geométrico con el proceso de límite que define a la derivada.

**Observaciones:**

- El prompt v2 funcionó correctamente: la `justificación` conecta la figura con la explicación sin describir visualmente la imagen — diferencia clave respecto a la v1.
- NBLM entrega el **número de página impreso en el libro** (207), no el del visor PDF (231). Desfase confirmado — el script `ima_src_opener` deberá contemplarlo.
- La etiqueta de figura y el pie de figura fueron identificados y entregados correctamente.

**Conclusión:** NBLM con prompt v2 localiza y justifica figuras con precisión suficiente para alimentar el paso siguiente. El campo `justificación` cumple su rol sin invadir la descripción visual.

---

## Prueba 2 — Gemini+fuentes: descripción técnica

**Contexto:** Se pasó el bloque IMA-SRC completo entregado por NBLM. Gemini tenía el cuaderno de Cálculo 1 cargado en la barra lateral.

**Input entregado:**
> IMA-SRC | fuente: Apostol vol 1 2ed-Calculus-1to7.pdf | página: 207 | etiqueta de figura: Figura 4.4 | pie de figura: Interpretación geométrica del cociente de diferencia como tangente de un ángulo | ubicación: Parte central de la página — justificación: [...]

**Resultado:** Gemini entregó una descripción detallada y estructurada de la Figura 4.4 — ejes, puntos P y Q, recta secante, triángulo rectángulo auxiliar, etiquetas de variables, ángulo α — con nivel de detalle suficiente para redibujar la figura sin verla.

**Observaciones:**

- La descripción fue más detallada que la entregada por NBLM en pruebas anteriores con el prompt v1.
- **Gemini+fuentes no puede generar imágenes** — error 1152 (limitación real de la modalidad con fuentes cargadas).
- La descripción resultó directamente utilizable como input para el paso 3.

**Conclusión:** Gemini+fuentes cumple su rol en el flujo: convierte una referencia IMA-SRC en una descripción técnica visual precisa. No necesita contexto adicional más allá del bloque IMA-SRC.

---

## Prueba 3 — Gemini sin fuentes: generación del dibujo

**Contexto entregado:** La respuesta completa de NBLM (las 2 oraciones de explicación + bloque IMA-SRC) pegada tal cual, sin reducción ni reescritura, más la descripción de Gemini+fuentes.

**Resultado:** Gemini generó una figura correcta y didácticamente sólida. Ver imágenes adjuntas: original del libro (Apostol p.207) y versión generada por Gemini.

**Análisis comparativo — original vs. generado:**

| Elemento | Original Apostol | Gemini generado |
|---|---|---|
| Curva f | ✅ | ✅ |
| Puntos P y Q sobre la curva | ✅ | ✅ |
| Recta secante PQ | ✅ | ✅ |
| Triángulo rectángulo con h y f(x+h)−f(x) | ✅ | ✅ |
| Ángulo α en P | ✅ | ✅ |
| Etiquetas x y x+h en eje horizontal | ✅ | ✅ |
| Ejes cartesianos completos (x, y) | ❌ no tiene | ✅ agregado |
| f(x) y f(x+h) marcados en eje y | ❌ no tiene | ✅ agregado |
| Líneas punteadas desde P y Q al eje y | ❌ no tiene | ✅ agregado |
| α también marcado en el origen | ❌ no tiene | ✅ agregado |
| Recta tangente en P diferenciada | ✅ (punteada) | ❌ omitida |
| Etiqueta "Figura 4.4" en la imagen | — | ✅ correcto |

**Sobre los elementos agregados por Gemini:** los ejes, las marcas de f(x) y f(x+h) en el eje y, y las líneas punteadas son matemáticamente correctos — f(x) y f(x+h) son las ordenadas de P y Q y marcarlos es convención estándar en libros de Cálculo. Hacen la figura más legible para un apunte de estudio. No son errores.

**Única omisión relevante:** la recta tangente en P (diferenciada de la secante) no fue dibujada. Es el elemento que conecta visualmente con la definición de derivada como pendiente de la tangente. No se corrige en el prompt porque los prompts deben ser generales — queda como limitación conocida del flujo.

**Sobre el contexto del paso 3:** se usó la respuesta completa de NBLM pegada tal cual (sin reducir ni reescribir). Funcionó correctamente. El prompt debe permitir esto — no debe requerir que el usuario redacte un contexto simplificado.

**Conclusión:** el flujo de 3 pasos produce resultados buenos con imágenes correctas y didácticamente útiles. El dibujo generado es una representación válida para la consulta "explica la derivada" en el contexto de Cálculo 1.

---

## Resumen del flujo validado

```
NBLM (prompt v2)
  → respuesta + bloque IMA-SRC
      ↓
Gemini+fuentes
  → input: bloque IMA-SRC completo
  → output: descripción técnica visual
      ↓
Gemini simple
  → input: respuesta NBLM completa (pegada tal cual) + descripción de Gemini+fuentes
  → output: imagen generada con etiqueta de figura
```

---

## Tabla de capacidades

| IA | Ve figuras en PDF | Describe con detalle | Genera imagen | Entrega bloque IMA-SRC |
|----|:-:|:-:|:-:|:-:|
| NBLM | ✅ | Justificación | ❌ | ✅ (con prompt v2) |
| Gemini+fuentes | ✅ | ✅ técnica | ❌ (error 1152) | ✅ (espontáneo) |
| Gemini (sin fuentes) | ❌ | — | ✅ | — |

---

## Pendientes

- El campo `página` en IMA-SRC es el número impreso en el libro — el script `ima_src_opener` debe contemplar el desfase respecto al visor PDF.
- La recta tangente en P no aparece en el dibujo generado — limitación conocida, no se corrige en el prompt.
- Evaluar si el contexto completo de NBLM en el paso 3 puede simplificarse automáticamente (por Gemini+fuentes u otro medio) sin perder calidad en el dibujo.

---

## Pruebas P1 v3 — 2026-08-13

### PDF con etiqueta de figura

**Resultado:** ✅ flujo validado. NBLM localiza correctamente fuente, página y etiqueta.

**Observación — error de página +1:** En al menos un caso NBLM entregó el número de página de la página siguiente (p+1). Causa probable: el número impreso está en el encabezado superior y NBLM lo asocia a la página siguiente. **Veredicto:** tolerable — cuando existe etiqueta de figura, la localización sigue siendo confiable. La etiqueta es el ancla real; la página es referencia de apoyo.

**PDF con páginas inclinadas / fotos con rayones:** procesados sin errores graves. NBLM los trata como cualquier PDF.

### PDF sin etiqueta

**Resultado:** sin errores graves en las pruebas realizadas. Sin casos de PDF sin etiqueta disponibles para prueba exhaustiva — la mayoría de los PDF del vault tiene etiqueta.

### Diapositivas (sin número de página ni etiqueta)

**Resultado:** ❌ fallo. NBLM entregó número de página incorrecto al no tener ancla (ni etiqueta ni número impreso). El bloque IMA-SRC resultante no es confiable para localizar la imagen.

**Conclusión:** diapositivas sin identificadores son un caso distinto. Requieren normalización separada — ver `IMA_NBLM-opc_slides.md`.

### Veredicto general P1 v3

Validada para PDF con etiqueta. Es el caso principal de uso real y cubre la mayoría del vault. Diapositivas quedan como caso pendiente separado.
