Hallar las ecuaciones de movimiento de la Tierra alrededor del Sol
(estático) en función de las variables $x$ y $y$.


```tikz
\begin{tikzpicture}[>=stealth, scale=1.2]

% Orbita de la Tierra
\draw[dashed, thick, gray]
(0,2) circle (1.5);

% Sol
\draw[thick, orange]
(-0.45,2)
arc (180:540:0.45);

% Tierra
\fill[teal]
(1.05,3.05) circle (5pt);

% Centro
\fill[orange]
(-0.45,2) circle (2pt);

% Radio r
\draw[thick, orange]
(-0.45,2) -- (1.05,3.05);

% Etiqueta r
\node[red] at (0.25,2.75) {$r$};

% Fuerza gravitacional G
\draw[->, ultra thick, red]
(1.05,3.05) -- (0.82,2.82);

\node[red] at (0.55,2.98) {$G$};

% Linea horizontal de referencia
\draw[dashed, gray]
(-0.45,2) -- (2.0,2);

% Angulo theta
\draw[teal]
(-0.10,2) arc (0:35:0.35);

\node[teal] at (0.28,2.18) {$\theta$};

% Etiqueta Tierra
\node[teal] at (1.25,3.22) {$m$};

% Etiqueta Sol
\node[orange] at (-0.45,1.35) {Sol};

% Fuerza gravitacional
\node[teal] at (2.25,3.15)
{$F=\dfrac{GMm}{r^2}$};

\end{tikzpicture}
```



$$
\vec{v}=
\begin{cases}
\dot{x}\\
\dot{y}
\end{cases}
$$



$$
T=\frac{1}{2}m\left(\dot{x}^{2}+\dot{y}^{2}\right)
$$



$$
x=r\cos\theta
$$



$$
y=r\sen\theta
$$



$$
r=\sqrt{x^{2}+y^{2}}
$$



$$
\frac{d}{dt}
\left(
\frac{\partial T}{\partial \dot{x}}
\right)
-
\frac{\partial T}{\partial x}
=
F_x
$$



$$
m\ddot{x}
=
-\frac{GMm}{r^{2}}\cos\theta
$$



$$
\ddot{x}
=
-\frac{GM}{r^{2}}\cos\theta
$$



$$
\cos\theta=\frac{x}{r}
$$



$$
\boxed{
\ddot{x}
=
-\frac{GM}{r^{3}}x
}
$$



$$
\boxed{
\ddot{x}
=
-\frac{GM}{\left(\sqrt{x^{2}+y^{2}}\right)^{3}}x
}
$$



$$
\frac{d}{dt}
\left(
\frac{\partial T}{\partial \dot{y}}
\right)
-
\frac{\partial T}{\partial y}
=
F_y
$$



$$
m\ddot{y}
=
-\frac{GMm}{r^{2}}\sen\theta
$$



$$
\ddot{y}
=
-\frac{GM}{r^{2}}\sen\theta
$$



$$
\sen\theta=\frac{y}{r}
$$



$$
\boxed{
\ddot{y}
=
-\frac{GM}{r^{3}}y
}
$$



$$
\boxed{
\begin{aligned}
\ddot{x}
&=
-\frac{GM}{\left(\sqrt{x^{2}+y^{2}}\right)^{3}}x
\[6pt]
\ddot{y}
&=
-\frac{GM}{\left(\sqrt{x^{2}+y^{2}}\right)^{3}}y
\end{aligned}
}
$$

