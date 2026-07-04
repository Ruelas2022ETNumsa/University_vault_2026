---
cssclasses:
  - cornell-note
---

---
---
---

> [!title] Ejemplo 1 · Texto plano

> [!cue] ¿Qué es una derivada?

Medida instantánea del cambio de una función respecto a su variable.
Geométricamente es la pendiente de la recta tangente en un punto.

> [!cue] ¿Cuándo no existe?

Cuando hay una discontinuidad, un pico afilado o una asíntota vertical en ese punto.

> [!cue] Regla de la cadena

Si $h(x) = f(g(x))$, entonces $h'(x) = f'(g(x)) \cdot g'(x)$.
Se aplica cuando una función está compuesta dentro de otra.

> [!summary]
> La derivada mide la tasa de cambio instantánea; no existe en discontinuidades o picos, y la regla de la cadena la extiende a funciones compuestas.


---
---
---




> [!title] Ejemplo 2 · Listas

> [!cue] Tipos de discontinuidad
- **Evitable** — el límite existe pero $f(a)$ no coincide.
- **De salto** — los límites laterales son distintos.
- **Esencial** — el límite no existe (oscilación, asíntota).

> [!cue] Condiciones de diferenciabilidad
1. La función debe ser continua en el punto.
2. Los límites laterales de la derivada deben coincidir.
3. La tangente no puede ser vertical.

> [!cue] Reglas básicas
- Potencia: $(x^n)' = nx^{n-1}$
- Producto: $(uv)' = u'v + uv'$
- Cociente: $(u/v)' = (u'v - uv') / v^2$

> [!summary]
> Tres tipos de discontinuidad; diferenciabilidad requiere continuidad y límites laterales iguales; las reglas de potencia, producto y cociente cubren la mayoría de los casos.


---
---
---
---

> [!title] Ejemplo 3 · Fórmulas LaTeX

> [!cue] Definición formal

$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$

> [!cue] Derivadas trigonométricas

| Función | Derivada |
|---------|----------|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |

> [!cue] Integral como anti-derivada

Si $F'(x) = f(x)$, entonces:
$\int_a^b f(x)\,dx = F(b) - F(a)$

> [!summary]
> La derivada es un límite de cocientes incrementales; las trig tienen pares sen/cos; la integral definida se evalúa con la anti-derivada por el TFC.


---
---
---
---

> [!title] Ejemplo 4 · Página 2 en el mismo archivo

> [!cue] ¿Qué es una integral impropia?

Integral sobre un intervalo no acotado o con una discontinuidad en el intervalo.
Ejemplo: $\int_1^{\infty} \frac{1}{x^2}\,dx = 1$

> [!cue] Criterio de comparación

Si $0 \le f(x) \le g(x)$ y $\int g$ converge, entonces $\int f$ también converge.
Si $\int f$ diverge, entonces $\int g$ también diverge.

> [!summary]
> Las impropias se resuelven con límites; el criterio de comparación permite concluir convergencia sin calcular explícitamente.


---
---
---
---

> [!title] Ejemplo 5 · Modo Repaso (Review Mode)

> [!cue] ¿Qué 
> condición 
> necesaria
>  tiene 
> un extremo
>  local?

$f'(c) = 0$ o $f'(c)$ no existe (punto crítico).
⚠️ Es condición necesaria, no suficiente.

> [!cue] Prueba de la segunda derivada

- $f''(c) > 0$ → mínimo local
- $f''(c) < 0$ → máximo local
- $f''(c) = 0$ → inconcluyente (usar primera derivada)

> [!cue] Valores absolutos en intervalo cerrado

1. Hallar puntos críticos en $(a, b)$.
2. Evaluar $f$ en críticos y en extremos $a$, $b$.
3. El mayor valor es el máximo absoluto; el menor, el mínimo.

> [!summary]
> Los extremos ocurren en puntos crític
> os; la segunda derivada clasifica 
> si es suficientemente informativa; en cerrados siempre comparar con los 
> extremos del intervalo.
