##### Ejercicio 7

Una masa $m$ cuelga de un hilo inextensible de longitud inicial $l$ enrollado en una rueda de radio $R$ fija en el origen $O$. El sistema opera en el plano $xy$ ($y$ positivo hacia abajo). La coordenada generalizada es $\theta$ — ángulo girado por la rueda. A medida que la rueda gira, el hilo se desenvuelve y la longitud libre aumenta: $d = l + \theta R$. Fuerzas: $F_x = 0$, $F_y = mg$, $F_z = 0$. Obtener la GDE para $q_r = \theta$.

_La restricción geométrica acopla el giro $\theta$ con la posición de la masa — no es un péndulo simple sino un sistema con longitud variable._

```tikz
\begin{tikzpicture}[
    >=stealth,
    line cap=round,
    line join=round,
    scale=1.15
]
\def\R{2.0}
\def\ang{35}

\coordinate (O) at (0,0);
\coordinate (P) at ({\R*cos(\ang)},{\R*sin(\ang)});
\coordinate (M) at ({\R*cos(\ang)+3.5*sin(\ang)},{\R*sin(\ang)-3.5*cos(\ang)});

% Circunferencia
\draw[thick] (O) circle (\R);

% Ejes
\draw[->,thick,red] (O) -- (4.0,0) node[right] {$x$};
\draw[->,thick,red] (O) -- (0,-3.2) node[below] {$y$};
\node[red,left] at (O) {$O$};

% Radio R
\draw[thick,teal] (O) -- (P) node[midway,above left] {$R$};

% Ángulo theta en el centro
\draw[->,teal,thick] (0.65,0) arc[start angle=0,end angle=\ang,radius=0.65];
\node[teal] at (0.72,0.25) {$\theta$};

% Hilo tangente P→M
\draw[very thick,black] (P) -- (M);

% Cota theta*R sobre el hilo
\draw[<->,blue,thick]
    ({\R*cos(\ang)+0.12},{\R*sin(\ang)+0.12})
    -- ({\R*cos(\ang)+1.75*sin(\ang)+0.12},{\R*sin(\ang)-1.75*cos(\ang)+0.12})
    node[midway,right] {$\theta R$};

% Línea auxiliar vertical desde P
\draw[dashed,orange,thick] (P) -- ({\R*cos(\ang)},-2.8);

% Cota l
\draw[<->,orange,thick]
    ({\R*cos(\ang)+0.18},0)
    -- ({\R*cos(\ang)+0.18},-2.35)
    node[midway,right] {$\ell$};

% Ángulo theta en P (respecto a vertical)
\draw[->,teal,thick]
    ({\R*cos(\ang)},{\R*sin(\ang)-0.65})
    arc[start angle=90,end angle={90-\ang},radius=0.65];
\node[teal] at ({\R*cos(\ang)+0.15},{\R*sin(\ang)-0.95}) {$\theta$};

% Etiqueta d
\node[orange] at (3.1,-0.3) {$d=\ell+\theta R$};

% Masa
\fill[orange] (M) circle (0.22);

% Peso mg
\draw[->,red,very thick] (M) -- ++(0,-1.0) node[below] {$mg$};

% Puntos de referencia
\fill[orange] (-1.85,0) circle (0.10);
\fill[orange] ({\R*cos(\ang)},-2.8) circle (0.10);

\end{tikzpicture}
```

#### Ecuación de movimiento general (ecuación alfa)

$$
\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot\theta}\right)
-
\frac{\partial T}{\partial \theta}
=
F_x\frac{\partial x}{\partial \theta}
+
F_y\frac{\partial y}{\partial \theta}
+
F_z\frac{\partial z}{\partial \theta}
$$

---

#### Datos del sistema

**Coordenadas cartesianas de la masa:**

$$
x = R\cos\theta + (l+\theta R)\sin\theta \qquad y = -R\sin\theta + (l+\theta R)\cos\theta
$$

**Velocidades** — aplicando regla del producto; los términos $\pm R\dot\theta\sin\theta$ y $\pm R\dot\theta\cos\theta$ se cancelan:

$$
\dot x = (l+\theta R)\dot\theta\cos\theta \qquad \dot y = -(l+\theta R)\dot\theta\sin\theta
$$

_Los términos cruzados se cancelan porque el punto de tangencia se mueve exactamente a la misma velocidad que el hilo se desenvuelve — por eso la velocidad de la masa depende solo de $d = l+\theta R$ y $\dot\theta$._

**Energía cinética:**

$$
v^2 = \dot x^2 + \dot y^2 = (l+\theta R)^2\dot\theta^2\underbrace{(\cos^2\theta+\sin^2\theta)}_{=\,1}
$$

$$
T = \frac{m}{2}(l+\theta R)^2\dot\theta^2
$$

---

#### GDE para $q_r = \theta$

**Lado izquierdo — derivadas de $T$:**

$$
\frac{\partial T}{\partial \dot\theta} = m(l+\theta R)^2\dot\theta
$$

Regla del producto — $(l+\theta R)^2$ depende del tiempo a través de $\theta(t)$:

$$
\frac{d}{dt}\!\left(\frac{\partial T}{\partial \dot\theta}\right)
= m(l+\theta R)^2\ddot\theta + 2mR(l+\theta R)\dot\theta^2
$$

$$
\frac{\partial T}{\partial \theta} = mR(l+\theta R)\dot\theta^2
$$

$$
\therefore\quad \text{lado izq} = m(l+\theta R)^2\ddot\theta + mR(l+\theta R)\dot\theta^2
$$

**Lado derecho — proyección de fuerzas sobre $\theta$:**

$$
\frac{\partial y}{\partial \theta} = -(l+\theta R)\sin\theta
$$

$$
Q_\theta = F_y\frac{\partial y}{\partial \theta} = mg\cdot\left[-(l+\theta R)\sin\theta\right] = -mg(l+\theta R)\sin\theta
$$

_La gravedad actúa en $y$, y como $y$ depende de $\theta$ a través de la geometría del sistema, sí contribuye al lado derecho._

**Igualando y dividiendo por $m(l+\theta R)$:**

$$
m(l+\theta R)^2\ddot\theta + mR(l+\theta R)\dot\theta^2 = -mg(l+\theta R)\sin\theta
$$

$$
\color{orange}{\boxed{(l+\theta R)\ddot\theta + R\dot\theta^2 + g\sin\theta = 0}}
$$
