---
galaxy_body: dropship
carrier: "[[_hangar/IMA_NBLM/tsk_IMA_NBLM.md]]"
scope: prueba
status: evaluado
date: 2026-08-10
---

## Proposito

Documenta la prueba de la fase 1 del carrier IMA_NBLM — validación del flujo completo NBLM → Gemini+fuentes → Gemini imagen usando la Figura 4.4 de Apostol (derivada, Cálculo 1) como caso de prueba.

---

## Contenido

### Flujo probado

```
NBLM (Prompt 1 v2)
  → Rx: explicación del concepto + bloque IMA-SRC
      ↓
Gemini+fuentes (Prompt 2)
  → input: Rx completo
  → Ry: descripción técnica visual detallada
      ↓
Gemini+fuentes (Prompt 2b) — pendiente validación formal
  → input: Rx completo
  → Rz: contexto simplificado, 1 oración
      ↓
Gemini simple (Prompt 3)
  → input: Rx completo (usado como contexto) + Ry
  → output: imagen generada con etiqueta de figura
```

---

### Paso 1 — NBLM

**Consulta:** "explica la derivada"

**Rx entregado:**
> La derivada es una función que representa la razón de cambio instantánea de una variable respecto a otra, calculada formalmente como el límite del cociente de diferencias cuando el incremento de la variable independiente tiende a cero. Geométricamente, este valor equivale a la pendiente de la recta tangente a la curva de la función en un punto determinado.
>
> IMA-SRC | fuente: Apostol vol 1 2ed-Calculus-1to7.pdf | página: 207 | etiqueta de figura: Figura 4.4 | pie de figura: Interpretación geométrica del cociente de diferencia como tangente de un ángulo | ubicación: Parte central de la página
> justificación: Esta figura es de gran utilidad ya que permite visualizar de manera directa cómo el cociente de diferencias representa la pendiente de una recta secante, conectando de forma intuitiva este concepto geométrico con el proceso de límite que define a la derivada.

**Resultado:** ✅ Prompt v2 funcionó — `justificación` conecta la figura con la explicación sin describir visualmente la imagen.

**Nota:** NBLM entrega página impresa en el libro (207), no la del visor PDF (231). Desfase confirmado.

---

### Paso 2 — Gemini+fuentes (descripción)

**Input:** Rx completo
**Prompt usado:** P2

**Ry entregado:** descripción detallada de Figura 4.4 — ejes cartesianos, curva f, puntos P y Q, recta secante, triángulo rectángulo auxiliar con catetos h y f(x+h)−f(x), ángulo α, etiquetas de variables.

**Resultado:** ✅ descripción suficientemente precisa para redibujar la figura sin verla.

---

### Paso 3 — Gemini simple (imagen)

**Input:** Rx completo como contexto + Ry (descripción de Gemini+fuentes)
**Nota sobre el contexto:** se usó Rx completo pegado tal cual, sin reducir. Funcionó correctamente — el Prompt 3 debe permitir esto sin requerir que el usuario redacte un contexto simplificado. El Prompt 2b (Rz) queda pendiente de validación formal como alternativa más limpia.

**Resultado:** ✅ imagen generada correcta y didácticamente útil.

**Análisis comparativo — original (Apostol p.207) vs. generado:**

| Elemento | Original | Gemini |
|---|:-:|:-:|
| Curva f | ✅ | ✅ |
| Puntos P y Q sobre la curva | ✅ | ✅ |
| Recta secante PQ | ✅ | ✅ |
| Triángulo rectángulo con h y f(x+h)−f(x) | ✅ | ✅ |
| Ángulo α en P | ✅ | ✅ |
| Etiquetas x y x+h en eje horizontal | ✅ | ✅ |
| Ejes cartesianos completos (x, y) | ❌ | ✅ agregado |
| f(x) y f(x+h) en eje y con líneas punteadas | ❌ | ✅ agregado |
| α marcado también en el origen | ❌ | ✅ agregado |
| Recta tangente en P diferenciada | ✅ | ❌ omitida |
| Etiqueta "Figura 4.4" en la imagen | — | ✅ |

**Sobre elementos agregados:** matemáticamente correctos — f(x) y f(x+h) son las ordenadas de P y Q, marcarlos en el eje y es convención estándar. Mejoran la legibilidad para un apunte de estudio.

**Única omisión relevante:** recta tangente en P no aparece. Limitación conocida del flujo — no se corrige en el prompt porque los prompts deben ser generales.

---

### Veredicto

✅ Flujo validado — produce imágenes correctas y útiles para apuntes de Cálculo 1.
⏳ Pendiente: validar Prompt 2b (Rz) como contexto vs. Rx directo en Gemini simple.