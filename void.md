##### Ej. a) $x^4 \geq 9x^2$





HIGHLIGHT_TEST







Desarrollo transcrito del manuscrito: ^[preuba: esto es una nota de pie]

$$\begin{array}{rcll} x^2(x^2-9) & \geq & 0 & (\text{transposición y factorización})\\
x^2(x-3)(x+3) & \geq & 0 & (\text{diferencia de cuadrados})\\
(x-0)^2(x-3)(x+3) & \geq & 0 & (\text{forma de puntos críticos}) \end{array}$$

Puntos críticos: $x=-3, 0, 3$. Prueba de signos: $I_1: x=-10 \rightarrow (+)(-)(-) \Rightarrow (+) \geq 0$ (Verdad). Debido al exponente par en $(x-0)^2$, el signo no se alterna al pasar por $0$.^[DEAR]

```desmos-graph
left=-6; right=6; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(-3, 0) | label: -3
(0, 0) | label: 0
(3, 0) | label: 3
x <= -3 | #94D2BD
x = 0 | #94D2BD
x >= 3 | #94D2BD
```

**Solución:** $C_s = ]-\infty, -3] \cup {0} \cup [3, \infty[$ $C_s = \mathbb{R} - ]-3, 0[ - ]0, 3[$ $C_s = {x / x \leq -3 \lor x=0 \lor x \geq 3}$

##### Ej. b) $\dfrac{2x}{x^2+2x-3} + \dfrac{2x+1}{3x^2+8x-3} \leq \dfrac{-1}{3x^2-4x+1}$

Desarrollo transcrito del manuscrito: $$\begin{array}{rcll} \dfrac{2x}{(x+3)(x-1)} + \dfrac{2x+1}{(3x-1)(x+3)} + \dfrac{1}{(3x-1)(x-1)} & \leq & 0 & (\text{factorización y transposición})\\
\dfrac{2x(3x-1) + (2x+1)(x-1) + (x+3)}{(x+3)(x-1)(3x-1)} & \leq & 0 & (\text{común denominador})\\
\dfrac{6x^2-2x + 2x^2-x-1 + x+3}{(x+3)(x-1)(3x-1)} & \leq & 0 & (\text{desarrollo})\\
\dfrac{8x^2-2x+2}{(x+3)(x-1)(3x-1)} & \leq & 0 & (\text{simplificación})\\
\dfrac{4x^2-x+1}{(x+3)(x-1)(3x-1)} & \leq & 0 & (\text{división entre 2}) \end{array}$$

Análisis del numerador $4x^2-x+1$: $D = (-1)^2 - 4(4)(1) = -15 < 0$. Como el discriminante es negativo y el coeficiente principal es positivo, la expresión es siempre positiva ($\in \mathbb{C}$ para raíces, siempre $(+)$ en $\mathbb{R}$).

Puntos críticos (denominador): $x=-3, 1/3, 1$. Prueba de signos en $x=0$: $\dfrac{(+)}{(+)(-)(-)} = \dfrac{(+)}{(+)} = (+) \leq 0$ (Falsedad).

```desmos-graph
left=-5; right=3; bottom=-1; top=1;
width=320; height=100;
---
y=0 | #005F73
(-3, 0) | open | label: -3
(0.333, 0) | open | label: 1/3
(1, 0) | open | label: 1
x < -3 | #94D2BD
0.333 < x < 1 | #94D2BD
```

**Solución:** $C_s = ]-\infty, -3[ \cup ]1/3, 1[$ $C_s = {x / x < -3 \lor 1/3 < x < 1}$

> [!summary] Resolución de inecuaciones no lineales mediante la determinación de puntos críticos, análisis de signos en intervalos y verificación de restricciones en el denominador.

> [!note] Complemento (Nivel B)
> 
> Para resolver inecuaciones racionales de la forma $P(x)/Q(x) > 0$ (o $\geq, <, \leq$), se deben seguir las reglas fundamentales de las desigualdades:
> 
> 1. **Puntos Críticos:** Son los valores de $x$ donde $P(x)=0$ (raíces del numerador) o $Q(x)=0$ (donde la expresión se indefine)., [13, A5]
> 2. **Factores Cuadráticos Irreducibles:** Si un factor cuadrático $ax^2 + bx + c$ tiene un discriminante $D < 0$, no cambia de signo en toda la recta real. Su signo será el mismo que el del coeficiente $a$.
> 3. **Intervalos:** Los puntos críticos dividen la recta real en intervalos donde la expresión mantiene un signo constante. Basta probar un valor dentro de cada intervalo para determinar si cumple la desigualdad. [13, A5-A6]
> 4. **Restricciones del Denominador:** Los valores que anulan a $Q(x)$ nunca pueden incluirse en el conjunto solución, independientemente de si la desigualdad es estricta o no., [13, A7]


