##### Ej. Una masa m se mueve sin fricción sobre una barra rígida diagonal que forma 45° con la horizontal dentro de una caja cuadrada de lado H. El origen se ubica en la esquina inferior izquierda. La posición de la masa sobre la barra se describe por la distancia x medida a lo largo del eje horizontal desde el origen, de modo que y = H − x (restricción de la barra). Un resorte de constante k y longitud natural ℓ₀ conecta la masa con la esquina superior izquierda (punto fijo en coordenadas (0, H)). La longitud del resorte es r = √(x² + (H−x)²). El sistema opera en el plano z = 0. N = 1, q = x. Fuerzas: gravedad mg hacia abajo, resorte k(r−ℓ₀) a lo largo de r. Obtener la GDE para q = x usando fuerzas generalizadas (método no conservativo).

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=2, >=stealth]
  % Ejes coordenados
  \draw[->, thick, gray] (-0.2,0) -- (2.5,0) node[right] {$x$};
  \draw[->, thick, gray] (0,-0.2) -- (0,2.5) node[above] {$y$};
  
  % Caja cuadrada de lado H
  \draw[dashed, thick, black!60] (0,0) rectangle (2,2);
  \node[left] at (0,2) {$H$};
  \node[below] at (2,0) {$H$};
  \node[below left] at (0,0) {$O$};
  
  % Barra rígida y = H - x
  \draw[ultra thick, teal] (0,2) -- (2,0) node[midway, sloped, above] {$y = H - x$};
  
  % Masa m
  \filldraw[fill=orange, draw=black] (0.8,1.2) circle (0.12) node[above right=3pt] {$m(x,y)$};
  
  % Resorte desde (0,H) a la masa
  \draw[thick, black, double, double distance=1pt] (0,2) -- (0.8,1.2) node[midway, left=2pt] {$r$};
  
  % Fuerza de gravedad
  \draw[->, thick, orange] (0.8,1.2) -- (0.8,0.6) node[below] {$mg$};
  
\end{tikzpicture}
\end{document}
```

**Resolución**
Determinación de las componentes de fuerza sobre la masa, cálculo de la energía cinética y aplicación de la ecuación de Lagrange en la coordenada generalizada \\(x\\) para ambos casos posibles de interpretación geométrica de la longitud del resorte.

**Caso 1: Basado estrictamente en la geometría real (punto fijo en \\((0,H)\\) y longitud real \\(r = x\sqrt{2}\\))**

\\[
\begin{array}{rcl}
x & = & x \\[4pt]
y & = & H - x \\[4pt]
T & = & \frac{1}{2}m(\dot{x}^2 + \dot{y}^2) = m\dot{x}^2 \\[4pt]
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) - \frac{\partial T}{\partial x} & = & 2m\ddot{x} \\[4pt]
\vec{r} & = & x\mathbf{i} + (y-H)\mathbf{j} = x\mathbf{i} - x\mathbf{j} \\[4pt]
r & = & x\sqrt{2} \\[4pt]
\vec{F}_{res} & = & -k(x\sqrt{2}-\ell_0)\left(\frac{1}{\sqrt{2}}\mathbf{i} - \frac{1}{\sqrt{2}}\mathbf{j}\right) \\[4pt]
F_x & = & -k\left(x - \frac{\ell_0}{\sqrt{2}}\right) \\[4pt]
F_y & = & k\left(x - \frac{\ell_0}{\sqrt{2}}\right) - mg \\[4pt]
Q_x & = & F_x \frac{\partial x}{\partial x} + F_y \frac{\partial y}{\partial x} = F_x(1) + F_y(-1) \\[4pt]
Q_x & = & -2k\left(x - \frac{\ell_0}{\sqrt{2}}\right) + mg \\[4pt]
2m\ddot{x} & = & -2k\left(x - \frac{\ell_0}{\sqrt{2}}\right) + mg \\[4pt]
\therefore\quad \color{orange}{2m\ddot{x} + 2k\left(x - \frac{\ell_0}{\sqrt{2}}\right) - mg = 0}
\end{array}
\\]

**Caso 2: Utilizando la longitud explícita dada en el enunciado \\(r = \sqrt{x^2 + (H-x)^2}\\) (correspondiente a punto fijo en el origen \\((0,0)\\))**

\\[
\begin{array}{rcl}
x & = & x \\[4pt]
y & = & H - x \\[4pt]
T & = & m\dot{x}^2 \\[4pt]
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) - \frac{\partial T}{\partial x} & = & 2m\ddot{x} \\[4pt]
\vec{r} & = & x\mathbf{i} + y\mathbf{j} = x\mathbf{i} + (H-x)\mathbf{j} \\[4pt]
r & = & \sqrt{x^2 + (H-x)^2} \\[4pt]
F_x & = & -k(r-\ell_0)\frac{x}{r} \\[4pt]
F_y & = & -k(r-\ell_0)\frac{H-x}{r} - mg \\[4pt]
Q_x & = & F_x \frac{\partial x}{\partial x} + F_y \frac{\partial y}{\partial x} = F_x - F_y \\[4pt]
Q_x & = & -k(r-\ell_0)\frac{x - (H-x)}{r} + mg \\[4pt]
2m\ddot{x} & = & -k\left(1 - \frac{\ell_0}{r}\right)(2x - H) + mg \\[4pt]
\therefore\quad \color{orange}{2m\ddot{x} + k\left(1 - \frac{\ell_0}{r}\right)(2x - H) - mg = 0}
\end{array}
\\]