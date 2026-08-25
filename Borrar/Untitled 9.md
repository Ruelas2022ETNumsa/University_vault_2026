

##### Ej. Una masa $m$ se desliza sobre una semicircunferencia de radio $r$ con centro en $(r, 0)$, cuya ecuación es $(x - r)^2 + y^2 = r^2$. Una barra articulada en el origen $O$ conecta la masa, y lleva un resorte de constante $k$. La única coordenada generalizada es $x$. El sistema está en el plano $z = 0$. Obtener la GDE para $q_r = x$.

```tikz
\usepackage{tikz}
\begin{document}
\draw[->, thin, gray] (-0.5,0) -- (5,0) node[right] {$x$};
\draw[->, thin, gray] (0,-0.5) -- (0,3) node[above] {$y$};
\draw[thick, teal] (0,0) arc (180:0:2);
\draw[fill=teal] (2,0) circle (1.5pt) node[below] {$(r,0)$};
\draw[fill=teal] (0,0) circle (1.5pt) node[below left] {$O$};
\draw[thick, orange] (0,0) -- (3, 1.73) node[midway, above left] {$\lambda$};
\draw[fill=orange] (3, 1.73) circle (3pt) node[above right] {$m(x,y)$};
\end{document}
```

**Resolución**
Aplicar la formulación de Lagrange obteniendo la energía cinética, potencial y las derivadas respecto a la coordenada generalizada $x$.


$$
\begin{array}{rcl}
\lambda & = & \sqrt{x^2 + y^2} = \sqrt{x^2 + (2xr - x^2)} = \sqrt{2xr} \[8pt]
V(x) & = & mgy + \frac{1}{2}k(\lambda - \lambda_0)^2 = mg\sqrt{2xr - x^2} + \frac{1}{2}k(\sqrt{2xr} - \lambda_0)^2 \[8pt]
L(x, \dot{x}) & = & \frac{1}{2}m\dot{x}^2 \frac{r^2}{2xr - x^2} - mg\sqrt{2xr - x^2} - \frac{1}{2}k(\sqrt{2xr} - \lambda_0)^2 \[8pt]
\frac{\partial L}{\partial \dot{x}} & = & m\dot{x}\frac{r^2}{2xr-x^2} \[8pt]
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{x}}\right) & = & \frac{mr^2\ddot{x}}{2xr-x^2} - \frac{2mr^2(r-x)\dot{x}^2}{(2xr-x^2)^2} \[8pt]
\frac{\partial L}{\partial x} & = & \frac{\partial T}{\partial x} - \frac{\partial V}{\partial x} = -\frac{mr^2(r-x)\dot{x}^2}{(2xr-x^2)^2} - \left[\frac{mg(r-x)}{\sqrt{2xr-x^2}} + \frac{kr(\sqrt{2xr}-\lambda_0)}{\sqrt{2xr}}\right] \[8pt]
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{x}}\right) - \frac{\partial L}{\partial x} & = & 0 \[8pt]
\therefore\quad \color{orange}{\frac{r^2 \ddot{x}}{2xr - x^2} - \frac{r^2 (r-x)\dot{x}^2}{(2xr - x^2)^2} + \frac{g(r-x)}{\sqrt{2xr-x^2}} + \frac{k}{m}\left(r - \lambda_0 \sqrt{\frac{r}{2x}}\right) = 0}
\end{array}
$$

