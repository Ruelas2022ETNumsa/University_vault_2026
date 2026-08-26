Subtema detectado: T2 — CONCEPTOS BÁSICOS II (Restricciones, energía cinética y ecuaciones de movimiento)

##### Ej. Una masa \(m\) desliza sin fricción sobre una barra diagonal que une el vértice inferior izquierdo \((0,0)\) con el vértice superior derecho \((L,L)\) de un cuadrado de lado \(L\). Un resorte de constante \(k\) y longitud natural \(\ell_0\) conecta la masa con el vértice inferior derecho \((L,0)\). Obtener la GDE para \(q = x\).

Una masa \(m\) desliza sin fricción sobre una barra diagonal que une el vértice inferior izquierdo \((0,0)\) con el vértice superior derecho \((L,L)\) de un cuadrado de lado \(L\). Un resorte de constante \(k\) y longitud natural \(\ell_0\) conecta la masa con el vértice inferior derecho \((L,0)\). Obtener la GDE para \(q = x\).

Este ejercicio es altamente similar en su estructura física y algebraica al ejercicio modelo **P1-E8-607** (pero con el resorte anclado en el vértice inferior derecho \((L,0)\) en lugar de \((0,H)\)).

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}
\draw[gray, dashed] (0,0) rectangle (4,4);
\draw[thick, teal] (0,0) -- (4,4) node[above right] {$(L,L)$};
\draw[fill=teal] (2.4,2.4) circle (0.15) node[above left, teal] {$m$};
\draw[decoration={coil,aspect=0.4,segment length=2.5mm,amplitude=3pt},decorate,orange,thick] (4,0) -- (2.4,2.4);
\draw[fill=orange] (4,0) circle (0.05) node[below right, orange] {$(L,0)$};
\draw[fill=gray] (0,0) circle (0.05) node[below left] {$(0,0)$};
\draw[->,thick,gray] (0,0) -- (4.5,0) node[right] {$x$};
\draw[->,thick,gray] (0,0) -- (0,4.5) node[above] {$y$};
\end{tikzpicture}
\end{document}
```

**Resolución**
Determinación de la GDE usando la ecuación de movimiento general (ecuación alfa) mediante la parametrización de la barra y la proyección de las fuerzas del resorte y de la gravedad.

**Paso 1 — Restricción geométrica y parametrización**
Puesto que la masa está obligada a deslizarse por la barra diagonal que une el origen \((0,0)\) con el punto \((L,L)\), la ecuación de restricción geométrica para su trayectoria es:
\[ y = x \]
Derivando respecto al tiempo, las velocidades cartesianas se acoplan (con \(z = 0\) y \(\dot{z} = 0\)) según:
\[ \dot{y} = \dot{x} \]

**Paso 2 — Energía cinética del sistema**
Sustituyendo la restricción de velocidad en la expresión de la energía cinética de una partícula libre en el plano:
\[ T = \frac{1}{2}m\left(\dot{x}^2 + \dot{y}^2\right) \]
\[ T = \frac{1}{2}m\left(\dot{x}^2 + \dot{x}^2\right) \]
\[ T = m\dot{x}^2 \]

**Paso 3 — Geometría y longitud del resorte**
El resorte conecta el vértice inferior derecho \(A(L,0)\) con la masa en la posición actual \(P(x,x)\). El vector de posición del resorte medido desde el punto fijo de anclaje hacia la masa es:
\[ \vec{r} = (x - L)\mathbf{i} + x\mathbf{j} \]
La longitud actual del resorte \(r = |\vec{r}|\) se calcula mediante el módulo del vector:
\[ r = \sqrt{(x - L)^2 + x^2} \]
\[ r = \sqrt{x^2 - 2Lx + L^2 + x^2} \]
\[ r = \sqrt{2x^2 - 2Lx + L^2} \]

**Paso 4 — Fuerzas activas sobre la masa**
Las fuerzas externas aplicadas sobre la masa \(m\) son la gravedad actuando verticalmente hacia abajo en \(-y\) y la fuerza restauradora elástica del resorte que tira de la masa hacia el vértice de anclaje \(A(L,0)\):
\[ F_x = -k(r-\ell_0)\frac{x-L}{r} \]
\[ F_y = -mg - k(r-\ell_0)\frac{x}{r} \]

**Paso 5 — Ecuación de movimiento general (Ecuación Alfa)**
Utilizamos la ecuación alfa para la única coordenada generalizada del sistema, \(q = x\):
\[ \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) - \frac{\partial T}{\partial x} = F_x\frac{\partial x}{\partial x} + F_y\frac{\partial y}{\partial x} \]
Calculando de forma independiente las derivadas de la energía cinética respecto a la coordenada y velocidad generalizada:
\[ \frac{\partial T}{\partial \dot{x}} = 2m\dot{x} \qquad\Rightarrow\qquad \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) = 2m\ddot{x} \]
\[ \frac{\partial T}{\partial x} = 0 \]
Las derivadas parciales de posición respecto a la coordenada generalizada son:
\[ \frac{\partial x}{\partial x} = 1 \qquad \frac{\partial y}{\partial x} = 1 \]

**Paso 6 — Proyección de fuerzas y acoplamiento algebraico**
Proyectamos las fuerzas activas del Paso 4 en la dirección de la coordenada generalizada utilizando las derivadas parciales de posición del Paso 5 para obtener la fuerza generalizada \(Q_x\):
\[ Q_x = \left[-k(r-\ell_0)\frac{x-L}{r}\right](1) + \left[-mg - k(r-\ell_0)\frac{x}{r}\right](1) \]
\[ Q_x = -k(r-\ell_0)\left[\frac{x-L}{r} + \frac{x}{r}\right] - mg \]
\[ Q_x = -k(r-\ell_0)\frac{2x-L}{r} - mg \]
\[ Q_x = -k\left(1 - \frac{\ell_0}{r}\right)(2x-L) - mg \]

**Resultado**
\[ 2m\ddot{x} + k\left(1 - \frac{\ell_0}{\sqrt{2x^2 - 2Lx + L^2}}\right)(2x-L) + mg = 0 \]