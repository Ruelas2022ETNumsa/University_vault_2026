##### Ej. Una masa $m$ se desliza sobre una semicircunferencia de radio $r$ con centro en $(r,0)$, cuya ecuación es $(x-r)^2+y^2=r^2$. Una barra articulada en el origen $O$ conecta la masa y lleva un resorte de constante $k$ y longitud natural $r_0$. Única coordenada generalizada: $x$. Sistema en el plano $z=0$. Obtener la GDE para $q_r = x$.

_La semicircunferencia pasa por el origen — verificable con $x=0$: $(0-r)^2+0^2=r^2$ ✓. Esto no es casual: significa que cuando la masa está en $O$, el resorte tiene longitud cero._

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.2]
  \definecolor{azul}{RGB}{20,75,90}
  \definecolor{naranja}{RGB}{240,140,20}
  \draw[->, thick, azul] (-0.3,0) -- (7,0) node[right] {$x$};
  \draw[->, thick, azul] (0,-0.2) -- (0,4.2) node[above] {$y$};
  \node[below left] at (0,0) {$O$};
  \draw[very thick, azul] (0,0) arc (180:0:3);
  \fill (3,0) circle (2pt) node[below] {$(r,0)$};
  \coordinate (P) at (5.25,2.0);
  \draw[thick, naranja] (0,0) -- (P);
  \draw[thick, naranja]
    (3.40,1.30) -- (3.55,1.60) -- (3.65,1.25) -- (3.80,1.70)
    -- (3.90,1.35) -- (4.05,1.80) -- (4.15,1.45) -- (4.30,1.90) -- (4.40,1.55);
  \node[azul] at (3.70,2.10) {$k$};
  \filldraw[draw=naranja, fill=orange!20, thick]
    (5.05,2.05) -- (5.30,2.35) -- (5.65,2.10) -- (5.40,1.80) -- cycle;
  \node[azul] at (5.85,2.35) {$m$};
  \draw[thick, red] (3,0) -- (P);
  \node[red] at (4.55,0.75) {$R$};
  \draw[naranja, thick] (1.2,0) arc (0:21:1.2);
  \node[naranja] at (1.25,0.42) {$\theta$};
  \node[azul] at (2.4,1.45) {$r$};
\end{tikzpicture}
\end{document}
```

#### Ecuación de movimiento general — Lagrangiano

$$
\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot{x}}\right) - \frac{\partial L}{\partial x} = 0
\qquad \text{con} \quad L = T - V
$$

_Se usa el Lagrangiano en lugar de la ecuación alfa porque el resorte tiene energía potencial elástica — es más limpio incluirla en $V$ que proyectarla como fuerza generalizada._

---

#### Restricción geométrica

$$
(x-r)^2 + y^2 = r^2 \qquad \Rightarrow \qquad y = \sqrt{2xr - x^2}
$$

_Se toma la raíz positiva porque la masa circula por la semicircunferencia superior ($y \geq 0$)._

Derivando respecto al tiempo para obtener $\dot{y}$:

$$
\dot{y} = \frac{d}{dt}\sqrt{2xr-x^2} = \frac{(r-x)\dot{x}}{\sqrt{2xr-x^2}}
$$

_Esta es la velocidad vertical — no es independiente, está completamente determinada por $\dot{x}$ y la posición $x$. La restricción elimina $\dot{y}$ como grado de libertad._

---

#### Longitud de la barra

$$
r = \sqrt{x^2 + y^2} = \sqrt{x^2 + (2xr - x^2)} = \sqrt{2xr}
$$

_La simplificación $x^2 + y^2 = 2xr$ es exacta sobre la semicircunferencia — viene de expandir $(x-r)^2 + y^2 = r^2$. Físicamente: la longitud de la barra desde $O$ hasta cualquier punto de la curva depende solo de $x$._

---

#### Energía cinética $T$

$$
T = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2)
= \frac{1}{2}m\left(\dot{x}^2 + \frac{(r-x)^2\dot{x}^2}{2xr-x^2}\right)
= \frac{1}{2}m\dot{x}^2\cdot\frac{r^2}{2xr-x^2}
$$

_El factor $\frac{r^2}{2xr-x^2}$ actúa como una **masa efectiva** que depende de la posición — la curvatura de la trayectoria hace que moverse en $x$ arrastre automáticamente movimiento en $y$, y eso tiene un costo cinético que varía según dónde está la masa sobre la curva._

---

#### Energía potencial $V$

$$
V = \underbrace{mgy}_{\text{gravedad}} + \underbrace{\frac{1}{2}k(r - r_0)^2}_{\text{resorte}}
= mg\sqrt{2xr-x^2} + \frac{1}{2}k(\sqrt{2xr}-r_0)^2
$$

---

#### GDE para $q_r = x$

**Derivadas de $T$:**

$$
\frac{\partial T}{\partial \dot{x}} = m\dot{x}\cdot\frac{r^2}{2xr-x^2}
$$

$$
\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot{x}}\right)
= \frac{mr^2\ddot{x}}{2xr-x^2} - \frac{2mr^2(r-x)\dot{x}^2}{(2xr-x^2)^2}
$$

_El segundo término aparece porque la masa efectiva $\frac{r^2}{2xr-x^2}$ cambia con $x$, y $x$ cambia con el tiempo — regla del producto sobre $\dot{x}\cdot f(x)$._

$$
\frac{\partial T}{\partial x} = -\frac{mr^2(r-x)\dot{x}^2}{(2xr-x^2)^2}
$$

**Derivadas de $V$:**

$$
\frac{\partial V}{\partial x}
= \frac{mg(r-x)}{\sqrt{2xr-x^2}} + \frac{k r(\sqrt{2xr}-r_0)}{\sqrt{2xr}}
$$

_El primer término es la proyección de la gravedad sobre la dirección de movimiento permitida por la curva. El segundo es la fuerza elástica proyectada sobre $x$ — nótese que $\frac{\partial r}{\partial x} = \frac{r}{\sqrt{2xr}} = \sqrt{\frac{r}{2x}}$._

**Igualando $\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot{x}}\right) - \frac{\partial L}{\partial x} = 0$:**

$$
\color{orange}{\boxed{
\frac{r^2\ddot{x}}{2xr-x^2}
- \frac{r^2(r-x)\dot{x}^2}{(2xr-x^2)^2}
+ \frac{g(r-x)}{\sqrt{2xr-x^2}}
+ \frac{k}{m}\!\left(r - r_0\sqrt{\frac{r}{2x}}\right) = 0
}}
$$
