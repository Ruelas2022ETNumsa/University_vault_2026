##### Ej. Una masa m cuelga de un hilo inextensible de longitud inicial l enrollado en una rueda de radio R fija en el origen O. El sistema opera en el plano xy. La coordenada generalizada es θ. A medida que la rueda gira un ángulo θ, el hilo se desenvuelve y la longitud libre del hilo aumenta: d = l + θR. El punto de tangencia P se mueve sobre la rueda. Fuerzas: peso mg hacia abajo $+y$, tensión T a lo largo del hilo. Obtener la GDE para qr = θ mediante la ecuación alfa.

**Resolución**
Determinamos las velocidades cartesianas para formular la energía cinética y aplicamos la ecuación de Lagrange para obtener la ecuación de movimiento.


$$
\begin{array}{rcl}
x & = & R\cos\theta + (l + \theta R)\sin\theta \\
y & = & -R\sin\theta + (l + \theta R)\cos\theta \\
\dot{x} & = & -R\dot{\theta}\sin\theta + R\dot{\theta}\sin\theta + (l + \theta R)\dot{\theta}\cos\theta\ =\ (l + \theta R)\dot{\theta}\cos\theta \\
\dot{y} & = & -R\dot{\theta}\cos\theta + R\dot{\theta}\cos\theta - (l + \theta R)\dot{\theta}\sin\theta\ =\ -(l + \theta R)\dot{\theta}\sin\theta \\
v^2 & = & \dot{x}^2 + \dot{y}^2\ =\ (l+\theta R)^2\dot{\theta}^2(\cos^2\theta + \sin^2\theta)\ =\ (l+\theta R)^2\dot{\theta}^2 \\
T & = & \frac{1}{2}m v^2\ =\ \frac{1}{2}m(l+\theta R)^2\dot{\theta}^2 \\
\frac{\partial T}{\partial \dot{\theta}} & = & m(l+\theta R)^2\dot{\theta} \\
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) & = & m(l+\theta R)^2\ddot{\theta} + 2mR(l+\theta R)\dot{\theta}^2 \\
\frac{\partial T}{\partial \theta} & = & mR(l+\theta R)\dot{\theta}^2 \\
\text{L.I.} & = & \frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}}\right) - \frac{\partial T}{\partial \theta}\ =\ m(l+\theta R)^2\ddot{\theta} + mR(l+\theta R)\dot{\theta}^2 \\
\frac{\partial y}{\partial \theta} & = & -R\cos\theta + R\cos\theta - (l+\theta R)\sin\theta\ =\ -(l+\theta R)\sin\theta \\
Q_\theta & = & F_y \frac{\partial y}{\partial \theta}\ =\ -mg(l+\theta R)\sin\theta \\
\text{Ecuación }\alpha & \rightarrow & m(l+\theta R)^2\ddot{\theta} + mR(l+\theta R)\dot{\theta}^2\ =\ -mg(l+\theta R)\sin\theta \\
& \rightarrow & m(l+\theta R)\left[(l+\theta R)\ddot{\theta} + R\dot{\theta}^2\right]\ =\ -mg(l+\theta R)\sin\theta \\
\therefore\quad & & \color{orange}{(l + \theta R)\ddot{\theta} + R\dot{\theta}^2 + g\sin\theta\ =\ 0}
\end{array}
$$

