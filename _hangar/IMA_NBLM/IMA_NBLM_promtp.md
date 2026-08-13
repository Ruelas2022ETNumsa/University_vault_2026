# Prompt 1 — NBLM v3 ⬅ activo

```
Cuando expliques un concepto, si encontrás en las fuentes una imagen o figura que lo ilustre directamente, agregá al final:

IMA-SRC | fuente: [nombre del archivo] | página: [número impreso] | id: [etiqueta de figura si existe, o pie de figura si no] | posición: [dónde está en la página]
justificación: [por qué esta figura sirve para entender el concepto — 1 oración, sin describir lo que se ve]

Reglas:
- Solo citá si podés confirmar fuente + página + id. Si no, omití.
- Si hay etiqueta de figura (ej: Figura 4.4), usala como id. Si no hay, usá el pie de figura textual.
- Si tampoco hay pie, describí brevemente el visual como id (ej: "gráfico de barras en margen derecho").
- Podés citar más de una figura si son relevantes.
```

---

# Prompt 1 — NBLM v1 (legacy)

```
Cuando el usuario pida que expliques un concepto:

1. Explicá el concepto en máximo 2 oraciones.

2. Si encontrás una imagen, figura o gráfica en las fuentes que ilustre
   directamente el concepto, citala así:

   IMA-SRC | fuente: [nombre del libro] | página: [número impreso en el libro] | etiqueta de figura: [Figura X] | pie de figura: [texto completo del pie] | ubicación: [posición en la página]
   descripción relevante: [por qué esta imagen es útil para el concepto explicado — máximo 2 oraciones]

Condiciones:
- Solo citá si podés localizar la figura con certeza (fuente + página + etiqueta)
- El campo "etiqueta de figura" es prioritario sobre "ubicación"
- Si la imagen no tiene etiqueta clara, usá el pie de figura como referencia
- La "descripción relevante" debe conectar la imagen con la explicación dada
- Si no podés localizarla con certeza, omitila — no inventes
- Podés citar más de una figura si son relevantes
```

# Prompt 1 — NBLM v2

```
Cuando el usuario pida que expliques un concepto:

1. Explicá el concepto en máximo 2 oraciones.

2. Si encontrás una imagen, figura o gráfica en las fuentes que ilustre directamente el concepto, citala así:

   IMA-SRC | fuente: [nombre del archivo PDF] | página: [número impreso en el libro] | etiqueta de figura: [Figura X] | pie de figura: [texto completo del pie tal como aparece] | ubicación: [posición en la página]
   justificación: [por qué esta figura es útil para entender el concepto explicado — máximo 2 oraciones. No describas lo que se ve, explicá por qué sirve]

Condiciones:
- Solo citá si podés localizar la figura con certeza (fuente + página + etiqueta o pie)
- El campo "etiqueta de figura" es prioritario; si no existe, usá el pie de figura como referencia
- La "justificación" debe conectar la figura con las 2 oraciones de explicación — no describir visualmente la imagen
- Si no podés localizar la figura con certeza, omitila — no inventes
- Podés citar más de una figura si son relevantes
```

---

## Prompt 2 — Gemini+fuentes: descripción técnica para dibujo

Usar en Gemini con el cuaderno de NBLM cargado como fuente en la barra lateral.
Input: respuesta completa de NBLM (Rx).

```
Tengo esta respuesta de NotebookLM sobre un concepto:

[PEGAR RESPUESTA COMPLETA DE NBLM]

Buscá esa figura en el libro indicado, en la página indicada.
Describí únicamente lo que se ve en la imagen con el nivel de detalle necesario para que alguien pueda redibujarla sin verla:
- Qué elementos están presentes (puntos, curvas, rectas, ejes, triángulos, etc.)
- Posición relativa de cada elemento entre sí
- Etiquetas o nombres que aparecen sobre cada elemento (letras, variables, expresiones)
- Qué representa cada línea o punto según el pie de figura o la leyenda

Al final entregá únicamente:
Etiqueta de figura: [Figura X]
Pie de figura: [texto completo tal como aparece en el libro]

No agregues explicación del concepto. No agregues conclusiones. Solo descripción visual y los dos campos finales.
```

---

## Prompt 2b — Gemini+fuentes: contexto simplificado para dibujo

Usar en Gemini con el cuaderno de NBLM cargado, en el mismo chat o uno separado del Prompt 2.
Input: la respuesta completa de NBLM (las 2 oraciones de explicación + bloque IMA-SRC).

```
Tengo esta respuesta de NotebookLM sobre un concepto:

[PEGAR RESPUESTA COMPLETA DE NBLM]

A partir de eso, escribí una sola oración que describa:
- Qué representa geométrica o visualmente la figura citada
- Para qué nivel o contexto es (ej: Cálculo 1, análisis, álgebra)

Esa oración es para orientar el estilo de un dibujo — no para explicar el concepto.
No uses lenguaje formal ni definiciones. Solo describí qué es lo que se va a dibujar y en qué contexto.

Ejemplo de formato esperado:
"representación geométrica del cociente de diferencias y la recta tangente, para un apunte de Cálculo 1"
```

---

## Prompt 3 — Gemini (sin fuentes): generación del dibujo

Usar en Gemini estándar (sin cuaderno cargado).
Input: output del Prompt 2b (contexto) + output del Prompt 2 (descripción técnica).

```
Necesito que dibujes una figura matemática para un apunte universitario.

Contexto: [PEGAR OUTPUT DEL PROMPT 2b — 1 oración]

Descripción de la figura:
[PEGAR DESCRIPCIÓN COMPLETA DEL PROMPT 2]

Instrucciones para el dibujo:
- Estilo: diagrama matemático limpio, fondo blanco, líneas claras, sin decoración extra
- Incluí todas las etiquetas de puntos, líneas y ángulos mencionadas en la descripción
- En la parte superior de la imagen escribí únicamente: [ETIQUETA DE FIGURA — ej: Figura 4.4]
- No agregues pie de figura, descripción textual ni título adicional debajo de la imagen
- No agregues elementos que no estén en la descripción
```


