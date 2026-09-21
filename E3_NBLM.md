##### Ej. Sistema de dos poleas y tres masas acopladas por cables y resortes $K$ y $K'$

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    % Colores
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Techo superior
    \fill[pattern=north east lines] (-0.5,4.5) rectangle (3.5,4.8);
    \draw[thick] (-0.5,4.5) -- (3.5,4.5);
    \node[right] at (3.5,4.5) {$H$};

    % Piso inferior
    \fill[pattern=north east lines] (-0.5,-0.3) rectangle (3.5,0);
    \draw[thick] (-0.5,0) -- (3.5,0);

    % Resorte K (desde techo a Polea 1)
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (0.8,4.5) -- (0.8,3.2);
    \node[left, maincolor] at (0.6,3.85) {$K$};

    % Polea 1
    \draw[thick, fill=teal!10, draw=maincolor] (0.8,2.9) circle (0.3);
    \fill[maincolor] (0.8,2.9) circle (0.04);
    \node[left, maincolor] at (0.5,2.9) {$1$};

    % Resorte K' en ramal izquierdo
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2mm, coil}, decorate, maincolor, thick] (0.5,0) -- (0.5,1.5);
    \node[left, maincolor] at (0.5,0.75) {$K'$};
    \draw[thick, maincolor] (0.5,1.5) -- (0.5,2.9);

    % Cable que conecta Polea 1 a Polea 2 (ramal derecho)
    \draw[thick, accentcolor] (1.1,2.9) -- (1.1,1.8);

    % Polea 2
    \draw[thick, fill=orange!10, draw=accentcolor] (1.1,1.5) circle (0.3);
    \fill[accentcolor] (1.1,1.5) circle (0.04);
    \node[right, accentcolor] at (1.4,1.5) {$2$};

    % Cable 2 (pasa por Polea 2)
    \draw[thick] (0.8,4.5) -- (0.8,1.5);
    \draw[thick] (1.4,1.5) -- (1.4,-0.5);

    % Bloque m3
    \draw[fill=orange!20, draw=accentcolor, thick] (1.15,-1.1) rectangle (1.65,-0.5);
    \node[accentcolor] at (1.4,-0.8) {$m_3$};

    % Cotas y coordenadas
    \draw[->, maincolor, thick] (2.2,4.5) -- (2.2,2.9) node[midway, right] {$y_1$};
    \draw[dotted] (0.8,2.9) -- (2.3,2.9);

    \draw[->, accentcolor, thick] (2.7,4.5) -- (2.7,1.5) node[midway, right] {$y_2$};
    \draw[dotted] (1.1,1.5) -- (2.8,1.5);

    \draw[->, accentcolor, thick] (3.2,4.5) -- (3.2,-0.8) node[midway, right] {$y_3$};
    \draw[dotted] (1.65,-0.8) -- (3.3,-0.8);

    \draw[<->, teal, thick] (1.8,2.9) -- (1.8,1.5) node[midway, right] {$a$};

\end{tikzpicture}
\end{document}
```

**Paso 0 — Identificación**
Sistema mecánico compuesto por dos poleas $$m_1$ e $I_1 = 0$, $m_2$ e $I_2 = 0$$, una masa suspendida $m_3$ y dos resortes ($K$ y $K'$). La polea 1 está suspendida del techo por el resorte $K$; del ramal izquierdo de la polea 1 cuelga un resorte $K'$ unido al piso, mientras que del ramal derecho cuelga la polea 2 a una distancia $a$. Un cable inextensible de longitud $\ell$ pasa por la polea 2 sujetando la masa $m_3$. Tema: Ecuaciones de Lagrange.

**Paso 1 — Coordenadas y GDL**
Coordenadas absolutas de posición desde el techo:


$$
N = (y_1, y_2, y_3)
$$


Ecuación de ligadura del cable que pasa por la polea 2:


$$
H - y_2 + \pi R_2 + y_3 - y_2 = \ell \implies y_2 = \frac{1}{2}\left(H + \pi R_2 + y_3 - \ell\right)
$$


Derivando con respecto al tiempo:


$$
\dot{y}_2 = \frac{\dot{y}_3}{2}
$$


Grados de libertad:


$$
\text{GDL} = 3 - 1 = 2
$$


Relación entre la distancia $a$ entre poleas y las coordenadas verticales:


$$
y_2 = y_1 + a \implies y_1 = y_2 - a = \frac{1}{2}\left(H + \pi R_2 + y_3 - \ell\right) - a
$$



$$
\dot{y}_1 = \frac{\dot{y}_3}{2} - \dot{a}
$$


Coordenadas independientes seleccionadas: $(y_3, a)$.

**Paso 2 — Energía cinética**
Energía cinética total expresada en función de las coordenadas independientes $(y_3, a)$:


$$
T = \frac{m_1}{2}\dot{y}_1^2 + \frac{m_2}{2}\dot{y}_2^2 + \frac{m_3}{2}\dot{y}_3^2
$$


Sustituyendo $\dot{y}_1$ y $\dot{y}_2$:


$$
T = \frac{m_1}{2}\left(\frac{\dot{y}_3}{2} - \dot{a}\right)^2 + \frac{m_2}{2}\left(\frac{\dot{y}_3}{2}\right)^2 + \frac{m_3}{2}\dot{y}_3^2
$$


**Paso 3 — Energía potencial**
Energía potencial elástica y gravitatoria del sistema:


$$
V = \frac{K}{2}(y_1 - l_0)^2 - m_1 g y_1 - m_2 g y_2 - m_3 g y_3 + \frac{K'}{2}\left(H - y_1 + \pi R_1 + a - l_0'\right)^2
$$


Sustituyendo $y_1$ y $y_2$ en función de $y_3$ y $a$:


$$
V = \frac{K}{2}\left[\frac{1}{2}(H + \pi R_2 + y_3 - \ell) - a - l_0\right]^2 - m_1 g \left[\frac{1}{2}(H + \pi R_2 + y_3 - \ell) - a\right] - m_2 g \left[\frac{1}{2}(H + \pi R_2 + y_3 - \ell)\right] - m_3 g y_3 + \frac{K'}{2}\left[H - \frac{1}{2}(H + \pi R_2 + y_3 - \ell) + 2a + \pi R_1 - l_0'\right]^2
$$


**Paso 4 — Ecuaciones de Lagrange**
Aplicando la ecuación de Lagrange para cada coordenada generalizada $q_r \in \{y_3, a\}$:

1. **Para la coordenada $y_3$:**


$$
\frac{\partial T}{\partial \dot{y}_3} = \frac{m_1}{2}\left(\frac{\dot{y}_3}{2} - \dot{a}\right) + \frac{m_2}{4}\dot{y}_3 + m_3\dot{y}_3 = \left(\frac{m_1 + m_2 + 4m_3}{4}\right)\dot{y}_3 - \frac{m_1}{2}\dot{a}
$$



$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_3}\right) = \left(\frac{m_1 + m_2 + 4m_3}{4}\right)\ddot{y}_3 - \frac{m_1}{2}\ddot{a}
$$



$$
-\frac{\partial V}{\partial y_3} = -\frac{K}{2}(y_1 - l_0) + \frac{m_1 g}{2} + \frac{m_2 g}{2} + m_3 g + \frac{K'}{2}\left(H - y_1 + \pi R_1 + a - l_0'\right)
$$


2. **Para la coordenada $a$:**


$$
\frac{\partial T}{\partial \dot{a}} = -m_1\left(\frac{\dot{y}_3}{2} - \dot{a}\right) = m_1\dot{a} - \frac{m_1}{2}\dot{y}_3
$$



$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{a}}\right) = m_1\ddot{a} - \frac{m_1}{2}\ddot{y}_3
$$



$$
-\frac{\partial V}{\partial a} = K(y_1 - l_0) - m_1 g - 2K'\left(H - y_1 + \pi R_1 + a - l_0'\right)
$$


**Paso 5 — EDOs finales**


$$
\boxed{\left(\frac{m_1 + m_2 + 4m_3}{4}\right)\ddot{y}_3 - \frac{m_1}{2}\ddot{a} = -\frac{K}{2}(y_1 - l_0) + \left(\frac{m_1 + m_2 + 2m_3}{2}\right)g + \frac{K'}{2}\left(H - y_1 + \pi R_1 + a - l_0'\right)}
$$



$$
\boxed{m_1\ddot{a} - \frac{m_1}{2}\ddot{y}_3 = K(y_1 - l_0) - m_1 g - 2K'\left(H - y_1 + \pi R_1 + a - l_0'\right)}
$$


