---
title: "LaTeX — Guía de referencia rápida"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[_ToDo-system]]"
  - "[[obsidian_guide]]"
tags: [beacon, latex, matematicas, infraestructura]
date_created: 2026-05-30
date_updated: 2026-05-30
status: activo
---

# LaTeX — Guía de referencia rápida

> Sistema Galaxy: [[_galaxy-system]]
> Pendientes: [[_ToDo-system]]
> Sintaxis Obsidian: [[obsidian_guide]]

Guía de referencia de sintaxis LaTeX para uso en Obsidian (MathJax). Cubre los entornos, comandos y colores más usados en las materias del vault. Todo va dentro de `$...$` (inline) o `$$...$$` (display).

---

## Índice
- [[#1. Modos matemáticos]]
- [[#2. Fracciones]]
- [[#3. Subíndices y superíndices]]
- [[#4. Integrales y diferenciales — Cálculo 1]]
- [[#5. Límites y sumatorias]]
- [[#6. Derivadas]]
- [[#7. Cancelaciones y anulaciones visuales]]
- [[#8. Sistemas y llaves — bloques condicionales]]
- [[#9. Alineación de ecuaciones — array y align]]
- [[#10. Matrices]]
- [[#11. Tablas con array]]
- [[#12. Álgebra lineal]]
- [[#13. Electrónica y circuitos eléctricos]]
- [[#14. Colores]]
- [[#15. Quick LaTeX — atajos activos]]
- [[#16. Completr — autocompletado LaTeX]]

---

## 1. Modos matemáticos

```latex
$f(x) = x^2$                  % inline — dentro del texto
$$f(x) = x^2$$                % display — centrado en línea propia
```

En Obsidian con Quick LaTeX: escribir `$` abre automáticamente `$$` y posiciona el cursor dentro. Para display, escribir `$$` en una línea vacía.

---

## 2. Fracciones

```latex
\frac{numerador}{denominador}
\cfrac{numerador}{denominador}   % fracción grande — mejor en fracciones anidadas
\dfrac{numerador}{denominador}   % fuerza tamaño display aunque esté inline
```

**Ejemplos:**
```latex
\frac{2x^3+7}{5x^2+2y+5}

\cfrac{2x^y+8xy}{5x^2+2yz^2+17z}

\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}
```

> Quick LaTeX: escribir `a/b` dentro de un bloque math y presionar espacio expande a `\frac{a}{b}`.

---

## 3. Subíndices y superíndices

```latex
x_i          % subíndice simple
x_{i+1}      % subíndice compuesto — siempre con llaves si tiene más de un carácter
x^2          % superíndice simple
x^{n+1}      % superíndice compuesto
x_i^2        % ambos
a_{(i,j)}    % subíndice con paréntesis — estilo del vault
```

**Ejemplos de uso en matrices y sucesiones:**
```latex
a_{(0,0)} \quad a_{(1,4)} \quad a_{(2,5)}

f_{(i-2)} + f_{(i-1)}
```

---

## 4. Integrales y diferenciales — Cálculo 1

### Integral indefinida

```latex
\int f(x)\,dx
\int x^n\,dx = \frac{x^{n+1}}{n+1} + C
```

### Integral definida

```latex
\int_a^b f(x)\,dx
\int_0^1 x^2\,dx = \frac{1}{3}
```

### Integrales dobles y triples

```latex
\iint_D f(x,y)\,dx\,dy
\iiint_V f(x,y,z)\,dV
```

### Regla de la cadena e integración por partes

```latex
\int u\,dv = uv - \int v\,du

\int f(g(x))g'(x)\,dx = F(g(x)) + C
```

### Sustitución trigonométrica — referencia

```latex
\int \frac{dx}{\sqrt{a^2 - x^2}} = \arcsin\!\left(\frac{x}{a}\right) + C

\int \frac{dx}{a^2 + x^2} = \frac{1}{a}\arctan\!\left(\frac{x}{a}\right) + C

\int \sec^2(x)\,dx = \tan(x) + C
```

### Diferenciales comunes

```latex
dy = f'(x)\,dx
\Delta y \approx dy \quad \text{para } \Delta x \text{ pequeño}
```

### Notación de evaluación

```latex
\left. F(x) \right|_a^b = F(b) - F(a)
```

---

## 5. Límites y sumatorias

```latex
\lim_{x \to a} f(x)
\lim_{x \to \infty} \frac{1}{x} = 0
\lim_{h \to 0} \frac{f(x+h) - f(x)}{h}   % definición de derivada
```

```latex
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
\sum_{i=0}^{\infty} r^i = \frac{1}{1-r}, \quad |r| < 1
\prod_{i=1}^{n} x_i
```

---

## 6. Derivadas

### Notación de Leibniz

```latex
\frac{dy}{dx}
\frac{d^2y}{dx^2}
\frac{d^n y}{dx^n}
\frac{\partial f}{\partial x}
\frac{\partial^2 f}{\partial x \partial y}
```

### Notación prima

```latex
f'(x) \quad f''(x) \quad f^{(n)}(x)
```

### Reglas básicas

```latex
\frac{d}{dx}[x^n] = nx^{n-1}
\frac{d}{dx}[e^x] = e^x
\frac{d}{dx}[\ln x] = \frac{1}{x}
\frac{d}{dx}[\sin x] = \cos x
\frac{d}{dx}[\cos x] = -\sin x
\frac{d}{dx}[\tan x] = \sec^2 x
```

---

## 7. Cancelaciones y anulaciones visuales

Requieren el paquete `cancel` — disponible en MathJax/Obsidian.

```latex
\cancel{x}         % línea diagonal \
\bcancel{x}        % línea diagonal /
\xcancel{x}        % X sobre el término
\cancelto{a}{b}    % flecha hacia a cancelando b
```

### Con colores — patrón del vault

```latex
% cancelto con colores: flecha en naranja, destino en Orange, origen en Gray
{\color{orange}\cancelto{{\color{Orange} a }}{{\color{Gray} b }}}

% bcancel con color
{\color{orange}\bcancel{{\color{gray} x }}}

% subrayado con valor límite debajo
\underset{{\color{Orange} 0 }}{\underline{{\color{Gray} x }}}
```

**Ejemplo combinado — simplificación con cancelaciones:**
```latex
{\color{orange}\cancelto{{\color{Orange} 1 }}{{\color{Gray} \frac{x}{x} }}}
+ {\color{orange}\bcancel{{\color{gray} 2x }}}
+ \underset{{\color{Orange} 0 }}{\underline{{\color{Gray} C }}}
```

---

## 8. Sistemas y llaves — bloques condicionales

### Sistema con llave izquierda (función por casos)

```latex
f_i = \left\{ \begin{array}{lccl}
  si & i = 0 & \longrightarrow & 0 \\
  si & i = 1 & \longrightarrow & 1 \\
  si & i > 1 & \longrightarrow & f_{(i-2)} + f_{(i-1)}
\end{array} \right.
```

El `.` después de `\right` es obligatorio cuando no hay símbolo de cierre — indica que no se dibuja nada a la derecha.

### Sistema con llave derecha (agrupación)

```latex
\left. \begin{matrix}
  \frac{2x^3+7}{5x^2+2y+5} \cdot 4 = 2 \\
  \frac{2x^y+8xy}{5x^2+2yz^2+17z} = 43
\end{matrix} \right\}
```

### Con `\cfrac` para fracciones grandes en sistemas

```latex
\left. \begin{matrix}
  \cfrac{2x^3+7}{5x^2+2y+5} \cdot 4 = 2 \\
  \cfrac{2x^y+8xy}{5x^2+2yz^2+17z} = 43
\end{matrix} \right\}
```

### Símbolo `cases` — alternativa más compacta

```latex
f(x) = \begin{cases}
  x^2     & \text{si } x \geq 0 \\
  -x      & \text{si } x < 0
\end{cases}
```

---

## 9. Alineación de ecuaciones — array y align

### array con columnas explícitas

```latex
\begin{array}{rcl}
  f(n) & = & (n+1)^3 \\
       & = & n^3 + 3n^2 + 3n + 1
\end{array}
```

Los especificadores de columna: `r` derecha, `c` centro, `l` izquierda. El `&` separa columnas, `\\` termina la fila.

### align — alineación en el símbolo `=`

```latex
\begin{align}
  f(n) &= (n+1)^3 \\
       &= n^3 + 3n^2 + 3n + 1
\end{align}
```

> En MathJax/Obsidian, `align` numera las ecuaciones. Para evitar el número usar `align*` — aunque en Obsidian la numeración no siempre aparece visualmente.

### aligned — dentro de display math

```latex
$$
\begin{aligned}
  f(n) &= (n+1)^3 \\
       &= n^3 + 3n^2 + 3n + 1
\end{aligned}
$$
```

---

## 10. Matrices

Todos los entornos de matriz van dentro de `$$...$$`.

### Sin delimitadores

```latex
\begin{matrix}
  a_{(2,3)} & a_{(2,4)} & a_{(2,5)} \\
  a_{(3,3)} & a_{(3,4)} & a_{(3,5)} \\
  a_{(5,3)} & a_{(5,4)} & a_{(5,5)}
\end{matrix}
```

### Pequeña — smallmatrix (inline)

```latex
$\begin{smallmatrix}
  a_{(0,0)} & a_{(1,4)} & a_{(2,5)} \\
  a_{(0,1)} & a_{(1,4)} & a_{(2,5)} \\
  a_{(0,2)} & a_{(1,4)} & a_{(2,5)}
\end{smallmatrix}$
```

### Con paréntesis — pmatrix

```latex
\begin{pmatrix}
  a_{(3,4)} & a_{(3,5)} \\
  a_{(5,4)} & a_{(5,5)}
\end{pmatrix}
```

### Con corchetes — bmatrix

```latex
\begin{bmatrix}
  a & b \\
  c & d
\end{bmatrix}
```

### Con barras — determinante — vmatrix

```latex
\begin{vmatrix}
  a_{(3,4)} & a_{(3,5)} \\
  a_{(5,4)} & a_{(5,5)}
\end{vmatrix}
```

### Con doble barra — norma — Vmatrix

```latex
\begin{Vmatrix}
  a_{(3,4)} & a_{(3,5)} \\
  a_{(5,4)} & a_{(5,5)}
\end{Vmatrix}
```

### Resumen de delimitadores

| Entorno | Delimitador | Uso típico |
|---------|------------|-----------|
| `matrix` | ninguno | base sin decorar |
| `smallmatrix` | ninguno | inline en texto |
| `pmatrix` | `( )` | matrices de transformación |
| `bmatrix` | `[ ]` | vectores, sistemas |
| `vmatrix` | `\| \|` | determinantes |
| `Vmatrix` | `‖ ‖` | normas |

---

## 11. Tablas con array

### Alineación de columnas — referencia

```latex
\begin{array}{crl}
  c & r & l \\
  \text{center} & \text{right} & \text{left}
\end{array}
```

### Con bordes — `|` y `\hline`

```latex
\begin{array}{|l|c|r|}
  \hline
  l & c & r \\
  \text{left} & \text{center} & \text{right} \\
  \hline
\end{array}
```

### Con doble línea vertical — tablas de verdad

```latex
\begin{array}{|c|c||c|}
  \hline
  a & b & a \lor b \\
  \hline
  0 & 0 & 0 \\
  0 & 1 & 1 \\
  1 & 0 & 1 \\
  1 & 1 & 1 \\
  \hline
\end{array}
```

El `||` crea una línea doble vertical entre columnas — útil para separar inputs de output en tablas de verdad (Álgebra).

---

## 12. Álgebra lineal

### Sistemas de ecuaciones

```latex
\begin{cases}
  2x + 3y - z  = 4 \\
  x  - y  + 2z = 1 \\
  3x + y  + z  = 7
\end{cases}
```

### Matriz aumentada

```latex
\left[\begin{array}{ccc|c}
  2 &  3 & -1 & 4 \\
  1 & -1 &  2 & 1 \\
  3 &  1 &  1 & 7
\end{array}\right]
```

### Determinante 2×2 y 3×3

```latex
\det(A) = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc

\det(A) = \begin{vmatrix}
  a & b & c \\
  d & e & f \\
  g & h & i
\end{vmatrix}
= a(ei-fh) - b(di-fg) + c(dh-eg)
```

### Transpuesta, inversa, norma

```latex
A^T \qquad A^{-1} \qquad \|v\| \qquad \|A\|

A^T A = I \implies A^{-1} = A^T   % matriz ortogonal
```

### Valores y vectores propios

```latex
Av = \lambda v

\det(A - \lambda I) = 0   % ecuación característica
```

### Producto punto y vectorial

```latex
\vec{u} \cdot \vec{v} = \|u\|\|v\|\cos\theta

\vec{u} \times \vec{v} = \begin{vmatrix}
  \hat{i} & \hat{j} & \hat{k} \\
  u_1 & u_2 & u_3 \\
  v_1 & v_2 & v_3
\end{vmatrix}
```

### Transformación lineal

```latex
T: \mathbb{R}^n \to \mathbb{R}^m \qquad T(\vec{v}) = A\vec{v}
```

---

## 13. Electrónica y circuitos eléctricos

### Ley de Ohm y potencia

```latex
V = IR \qquad P = VI = I^2R = \frac{V^2}{R}
```

### Resistencias en serie y paralelo

```latex
R_{eq} = R_1 + R_2 + \cdots + R_n   % serie

\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots + \frac{1}{R_n}   % paralelo

R_{eq} = \frac{R_1 R_2}{R_1 + R_2}   % dos en paralelo
```

### Capacitores e inductores

```latex
V_C = \frac{1}{C}\int i\,dt \qquad i_C = C\frac{dV}{dt}

V_L = L\frac{di}{dt} \qquad i_L = \frac{1}{L}\int V\,dt
```

### Impedancia — dominio fasorial

```latex
Z_R = R \qquad Z_C = \frac{1}{j\omega C} \qquad Z_L = j\omega L

Z_{total} = R + j\!\left(\omega L - \frac{1}{\omega C}\right)
```

### Divisor de voltaje y corriente

```latex
V_x = V_s \cdot \frac{R_x}{R_1 + R_2}   % divisor de voltaje

I_x = I_s \cdot \frac{R_{total}}{R_x}    % divisor de corriente
```

### Leyes de Kirchhoff

```latex
\sum_{k} V_k = 0   % KVL: suma de voltajes en malla = 0

\sum_{k} I_k = 0   % KCL: suma de corrientes en nodo = 0
```

### Respuesta transitoria RC

```latex
v(t) = V_f + (V_0 - V_f)\,e^{-t/\tau} \qquad \tau = RC

i(t) = \frac{V_0}{R}\,e^{-t/\tau}
```

### Frecuencia de resonancia y función de transferencia

```latex
\omega_0 = \frac{1}{\sqrt{LC}} \qquad f_0 = \frac{1}{2\pi\sqrt{LC}}

H(j\omega) = \frac{V_{out}}{V_{in}} = \frac{Z_{out}}{Z_{in}}
```

### Semiconductores — transistor BJT

```latex
I_C = \beta I_B \qquad I_E = I_C + I_B = (\beta + 1)I_B

V_{CE} = V_{CC} - I_C R_C
```

---

## 14. Colores

Los colores se aplican con `{\color{Nombre} expresión}`. Funcionan dentro de bloques math y con `\mbox{}` para texto.

### Sintaxis

```latex
{\color{Orange} x^2 + 1}              % color a una expresión
{\color{Red} \frac{a}{b}}             % color a una fracción
\color{Blue} \text{toda la línea}     % sin llaves — afecta hasta el final
```

### Paleta — azules y verdes

```latex
{\color{NavyBlue}\mbox{NavyBlue}}
{\color{MidnightBlue}\mbox{MidnightBlue}}
{\color{TealBlue}\mbox{TealBlue}}
{\color{Aquamarine}\mbox{Aquamarine}}
{\color{BlueGreen}\mbox{BlueGreen}}
{\color{Emerald}\mbox{Emerald}}
{\color{JungleGreen}\mbox{JungleGreen}}
{\color{SeaGreen}\mbox{SeaGreen}}
{\color{PineGreen}\mbox{PineGreen}}
```

### Paleta — naranjas y amarillos

```latex
{\color{Apricot}\mbox{Apricot}}
{\color{Melon}\mbox{Melon}}
{\color{Tan}\mbox{Tan}}
{\color{Peach}\mbox{Peach}}
{\color{Goldenrod}\mbox{Goldenrod}}
{\color{Dandelion}\mbox{Dandelion}}
{\color{YellowOrange}\mbox{YellowOrange}}
{\color{BurntOrange}\mbox{BurntOrange}}
```

### Paleta — rojos y marrones

```latex
{\color{Bittersweet}\mbox{Bittersweet}}
{\color{RawSienna}\mbox{RawSienna}}
{\color{BrickRed}\mbox{BrickRed}}
{\color{Mahogany}\mbox{Mahogany}}
{\color{Sepia}\mbox{Sepia}}
{\color{Maroon}\mbox{Maroon}}
{\color{RedViolet}\mbox{RedViolet}}
```

### Paleta — básicos

```latex
{\color{Black}\mbox{Black}}
{\color{Red}\mbox{Red}}
{\color{Orange}\mbox{Orange}}
{\color{Blue}\mbox{Blue}}
{\color{Green}\mbox{Green}}
{\color{Gray}\mbox{Gray}}
{\color{White}\mbox{White}}
```

### Patrón de colores del vault — cancelaciones

El patrón establecido en el vault para simplificaciones con cancelación visual:

| Rol | Color | Uso |
|-----|-------|-----|
| Flecha / operador visual | `orange` (minúscula) | el `\cancelto`, `\bcancel` exterior |
| Valor destino / resultado | `Orange` (mayúscula) | lo que queda después de simplificar |
| Término que se cancela | `Gray` | el término original que desaparece |

```latex
% Patrón completo — término b se cancela hacia a
{\color{orange}\cancelto{{\color{Orange} a }}{{\color{Gray} b }}}

% Término que se tacha con /
{\color{orange}\bcancel{{\color{gray} x }}}

% Término que vale 0 — subrayado con 0 debajo
\underset{{\color{Orange} 0 }}{\underline{{\color{Gray} x }}}
```

---

## 15. Quick LaTeX — atajos activos

Quick LaTeX funciona automáticamente dentro de bloques `$...$` y `$$...$$`. Todos los atajos se pueden activar/desactivar en Settings → Quick LaTeX.

| Lo que escribes | Resultado | Condición |
|-----------------|-----------|-----------|
| `$` al inicio | `$$` con cursor dentro | fuera de math |
| `(` dentro de math | `()` con cursor dentro | auto-close |
| `[` dentro de math | `[]` con cursor dentro | auto-close |
| `{` dentro de math | `{}` con cursor dentro | auto-close |
| `a/b` + espacio | `\frac{a}{b}` | dentro de math |
| Tab | salta al siguiente `{}` | dentro de math con llaves |
| `\sum` + espacio | expande con `_{}^{}` | dentro de math |
| `\int` + espacio | expande con `_{}^{}` | dentro de math |
| `\begin{align}` | inserta bloque completo | dentro de `$$` |

> Para personalizar shorthands propios (ej. `ddt` → `\frac{d}{dt}`): Settings → Quick LaTeX → Custom shorthands.

---

## 16. Completr — autocompletado LaTeX

Completr sugiere comandos LaTeX mientras escribes. El trigger por defecto es `\` — al escribir `\fr` aparece la sugerencia `\frac{}{}`. Navegar con flechas `↑↓`, aceptar con `Tab` o `Enter`.

### Comandos que Completr completa automáticamente

```latex
\frac    → \frac{}{} con cursor en primer {}
\sqrt    → \sqrt{}
\sum     → \sum_{}^{}
\int     → \int_{}^{}
\lim     → \lim_{}
\begin   → sugiere entornos disponibles (matrix, align, cases, array...)
\color   → sugiere nombres de colores disponibles
\text    → \text{}
\mathbb  → \mathbb{} — para ℝ, ℤ, ℕ, ℂ
\vec     → \vec{}
\hat     → \hat{}
\bar     → \bar{}
```

### Letras griegas — completadas por Completr

```latex
\alpha   \beta    \gamma   \delta   \epsilon
\zeta    \eta     \theta   \iota    \kappa
\lambda  \mu      \nu      \xi      \pi
\rho     \sigma   \tau     \upsilon \phi
\chi     \psi     \omega

% Mayúsculas
\Gamma   \Delta   \Theta   \Lambda  \Xi
\Pi      \Sigma   \Upsilon \Phi     \Psi   \Omega
```

### Símbolos frecuentes en ingeniería

```latex
\infty          % ∞
\partial        % ∂
\nabla          % ∇
\approx         % ≈
\neq            % ≠
\leq  \geq      % ≤ ≥
\ll   \gg       % ≪ ≫
\cdot           % ·  producto
\times          % ×  producto vectorial / multiplicación
\div            % ÷
\pm             % ±
\mp             % ∓
\in   \notin    % ∈ ∉
\subset         % ⊂
\cup  \cap      % ∪ ∩
\mathbb{R}      % ℝ
\mathbb{Z}      % ℤ
\mathbb{C}      % ℂ
\implies        % ⟹
\iff            % ⟺
\therefore      % ∴
\because        % ∵
\forall         % ∀
\exists         % ∃
\longrightarrow % ⟶
\Longrightarrow % ⟹
```

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_ToDo-system.md]]
[[_app/_appnotes/obsidian_guide.md]]
%%
