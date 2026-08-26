##### Ej. Una masa \\(m\\) cuelga de un hilo inextensible de longitud \\(\ell\\) fija al techo. Un resorte de constante \\(k\\) y longitud natural \\(\ell_0\\) conecta la masa con un punto del piso ubicado directamente debajo del punto de suspensión, a una distancia vertical \\(H\\) del techo. El sistema opera en el plano \\(z=0\\). La única coordenada generalizada es \\(\theta\\) (ángulo de la cuerda con la vertical). Las coordenadas de la masa son \\(x = \ell\sin\theta\\), \\(y = \ell\cos\theta\\). La longitud del resorte en función de \\(\theta\\) es \\(r = \sqrt{H^2 + \ell^2 - 2H\ell\cos\theta}\\). Fuerzas: gravedad \\(mg\\) hacia abajo, resorte \\(k(r-\ell_0)\\) a lo largo de \\(r\\). Obtener la GDE para \\(q_r = \theta\\).

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex, scale=1.2]
  % Ceiling
  \draw[thick] (-1.5,0) -- (1.5,0);
  \foreach \x in {-1.5,-1.2,-0.9,-0.6,-0.3,0,0.3,0.6,0.9,1.2,1.5}
    \draw (\x,0) -- (\x+0.1,0.2);
  
  % Floor (at y = -3)
  \draw[thick] (-1.5,-3) -- (1.5,-3);
  \foreach \x in {-1.5,-1.2,-0.9,-0.6,-0.3,0,0.3,0.6,0.9,1.2,1.5}
    \draw (\x,-3) -- (\x-0.1,-3.2);

  % Vertical reference line
  \draw[dashed, gray] (0,0) -- (0,-3);
  
  % Coordinates of points
  \coordinate (O) at (0,0);
  \coordinate (P) at (0,-3);
  \coordinate (M) at (1,-1.73);
  
  % Pendulum cord
  \draw[teal, ultra thick] (O) -- (M) node[midway, above right] {$\ell$};
  
  % Angle \theta
  \draw[->, orange, thick] (0,-0.6) arc (-90:-60:0.6) node[midway, below] {$\theta$};
  
  % Spring from M to P
  \draw[orange, thick, dashed] (M) -- (P) node[midway, right] {$k, \ell_0$};
  \node[left] at (0.5,-2.36) {$r$};

  % Mass
  \filldraw[orange] (M) circle (2.5pt) node[above right, black] {$m$};
  
  % Gravity arrow
  \draw[->, red, thick] (M) -- ++(0,-0.8) node[below] {$mg$};
\end{tikzpicture}
\end{document}
```

**Resolución**
Construir la función lagrangiana \\(L = T - V\\) considerando la energía cinética de la masa y el potencial combinado gravitatorio y elástico.

\\[
\begin{array}{rcl}
x & = & \ell\sin\theta \quad \Rightarrow \quad \dot{x} = \ell\dot{\theta}\cos\theta \\[6pt]
y & = & \ell\cos\theta \quad \Rightarrow \quad \dot{y} = -\ell\dot{\theta}\sin\theta \\[6pt]
T & = & \dfrac{1}{2}m\left(\dot{x}^2 + \dot{y}^2\right) = \dfrac{1}{2}m\ell^2\dot{\theta}^2 \\[10pt]
V & = & -mgy + \dfrac{1}{2}k\left(r-\ell_0\right)^2 = -mg\ell\cos\theta + \dfrac{1}{2}k\left(r-\ell_0\right)^2 \\[10pt]
L & = & T - V = \dfrac{1}{2}m\ell^2\dot{\theta}^2 + mg\ell\cos\theta - \dfrac{1}{2}k\left(r-\ell_0\right)^2 \\[10pt]
\dfrac{\partial L}{\partial \dot{\theta}} & = & m\ell^2\dot{\theta} \quad \Rightarrow \quad \dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{\theta}}\right) = m\ell^2\ddot{\theta} \\[10pt]
\dfrac{\partial L}{\partial \theta} & = & -mg\ell\sin\theta - k\left(r-\ell_0\right)\dfrac{\partial r}{\partial \theta} \\[10pt]
r^2 & = & H^2 + \ell^2 - 2H\ell\cos\theta \quad \Rightarrow \quad 2r\dfrac{\partial r}{\partial \theta} = 2H\ell\sin\theta \\[10pt]
\dfrac{\partial r}{\partial \theta} & = & \dfrac{H\ell\sin\theta}{r} \\[10pt]
\dfrac{\partial L}{\partial \theta} & = & -mg\ell\sin\theta - k\left(1 - \dfrac{\ell_0}{r}\right)H\ell\sin\theta \\[10pt]
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{\theta}}\right) - \dfrac{\partial L}{\partial \theta} & = & 0 \\[10pt]
m\ell^2\ddot{\theta} + \left[ mg + kH\left(1 - \dfrac{\ell_0}{r}\right) \right] \ell\sin\theta & = & 0 \\[10pt]
\therefore\quad \color{orange}{m\ell^2\ddot{\theta} + \left[ mg + kH\left(1 - \frac{\ell_0}{r}\right) \right] \ell\sin\theta = 0}
\end{array}
\\]