##### Ej. Sistema masa-resorte-amortiguador de 1 GDL sometido a una fuerza externa $F$ (edo3.pdf)

**Enunciado:**
Un bloque de masa $M$ se desliza horizontalmente sin fricción sobre una superficie plana. Por su lado izquierdo está conectado en paralelo a un resorte de rigidez $K$ y un amortiguador viscoso de coeficiente $C$, ambos anclados a una pared rígida fija. Sobre el lado derecho del bloque actúa una fuerza externa $F$ dirigida hacia la derecha. Obtenga la ecuación de movimiento del sistema usando las ecuaciones de Lagrange.

**Descripción de la figura:**
El diagrama muestra un bloque de masa $M$ apoyado sobre una superficie horizontal sin fricción, con una pared rígida a su izquierda. Desde esa pared parten dos elementos en paralelo que se conectan al lado izquierdo del bloque: el resorte $K$ en la parte superior y el amortiguador $C$ en la parte inferior. Sobre el lado derecho del bloque actúa la fuerza externa $F$ apuntando hacia la derecha. La coordenada $x$ indica el desplazamiento horizontal del bloque medido desde su posición de equilibrio estático.

```tikz
\usetikzlibrary{patterns,decorations.pathmorphing}
\begin{document}
\begin{tikzpicture}[scale=1.0, >=latex]
    \colorlet{maincolor}{teal}
    \colorlet{accentcolor}{orange}

    % Pared izquierda
    \fill[pattern=north east lines] (-0.3,-0.5) rectangle (0,3.0);
    \draw[thick] (0,-0.5) -- (0,3.0);

    % Piso horizontal
    \fill[pattern=north east lines] (0,-0.3) rectangle (5.5,0);
    \draw[thick] (0,0) -- (5.5,0);

    % Bloque M
    \draw[fill=teal!10, draw=maincolor, thick] (2.5,0.3) rectangle (4.0,2.2);
    \node[maincolor, font=\Large] at (3.25,1.25) {$M$};

    % Resorte K (Pared a Bloque M)
    \draw[decoration={aspect=0.3, segment length=2mm, amplitude=2.5mm, coil}, decorate, maincolor, thick] (0,2.0) -- (2.5,2.0);
    \node[above, maincolor] at (1.25,2.15) {$K$};

    % Amortiguador C (Pared a Bloque M)
    \draw[thick, maincolor] (0,0.8) -- (0.8,0.8);
    \draw[thick, maincolor] (0.8,0.5) -- (0.8,1.1);
    \draw[thick, maincolor] (0.7,1.1) -- (1.6,1.1);
    \draw[thick, maincolor] (0.7,0.5) -- (1.6,0.5);
    \draw[thick, maincolor] (1.3,0.65) -- (1.3,0.95);
    \draw[thick, maincolor] (1.3,0.8) -- (2.5,0.8);
    \node[above, maincolor] at (1.25,1.1) {$C$};

    % Fuerza F
    \draw[->, red, ultra thick] (4.0,1.25) -- (5.2,1.25) node[right] {$F$};

    % Coordenada x
    \draw[->, maincolor, thick] (2.5,2.6) -- (3.5,2.6) node[midway, above] {$x$};
    \draw[dotted] (2.5,2.2) -- (2.5,2.8);
\end{tikzpicture}
\end{document}
```

---

**Paso 0 — Identificación**
Sistema mecánico translacional de 1 grado de libertad (1 GDL) constituido por un bloque de masa $M$, acoplado en paralelo a un resorte de rigidez $K$ y un amortiguador viscoso de coeficiente $C$, sometido a una fuerza impulsora externa $F$.

**Paso 1 — Coordenadas y GDL**
Coordenada independiente de desplazamiento horizontal: $x$ medida desde la posición de equilibrio estático.
Grados de libertad: $\text{GDL} = 1$.

**Paso 2 — Energía cinética**
Energía cinética del sistema:


$$
T = \frac{1}{2}M\dot{x}^2
$$


**Paso 3 — Energía potencial**
Energía potencial elástica acumulada en el resorte:


$$
V = \frac{1}{2}Kx^2
$$


Función de disipación de Rayleigh del amortiguador:


$$
\mathcal{F} = \frac{1}{2}C\dot{x}^2
$$


**Paso 4 — Ecuaciones de Lagrange**
Ecuación diferencial de movimiento planteada mediante la ecuación de Lagrange extendida con disipación viscosa y fuerza generalizada externa:


$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}}\right) - \frac{\partial T}{\partial x} + \frac{\partial \mathcal{F}}{\partial \dot{x}} + \frac{\partial V}{\partial x} = F
$$


Sustituyendo las derivadas parciales:


$$
M\ddot{x} + C\dot{x} + Kx = F
$$


Ensayo de solución exponencial propuesta en el apunte ($x = c e^{\lambda t}$):


$$
\dot{x} = c\lambda e^{\lambda t}, \qquad \ddot{x} = c\lambda^2 e^{\lambda t}
$$


Casos de solución según la naturaleza de las raíces $\lambda$ del polinomio característico:

1. **Solución 1: Sobreamortiguado ($\lambda \in \mathbb{R}$, raíces reales distintas)**
   
$$
x(t) = c_1 e^{-\alpha_1 t} + c_2 e^{-\alpha_2 t}
$$


2. **Solución 2: Amortiguamiento crítico ($\lambda \in \mathbb{R}$, raíces reales iguales $\lambda_1 = \lambda_2 = -\alpha$)**
   
$$
x(t) = c_1 e^{-\alpha t} + c_2 t e^{-\alpha t}
$$


3. **Solución 3: Subamortiguado ($\lambda \in \mathbb{C}$, raíces complejas conjugadas $-\alpha \pm i\beta$)**
   
$$
x(t) = c_1 e^{-\alpha t} \sin(\beta t) + c_2 e^{-\alpha t} \cos(\beta t)
$$


Parámetros de frecuencia y período del apunte:


$$
\omega_n = \sqrt{\frac{K}{M}}
$$


Ejemplo numérico asignado en el apunte (para $K = 2$, $M = 3$):


$$
\omega_n = \sqrt{\frac{2}{3}}
$$



$$
f = \frac{\omega_n}{2\pi}, \qquad T = \frac{1}{f}
$$


**Paso 5 — EDOs finales**

$$
\boxed{M\ddot{x} + C\dot{x} + Kx = F}
$$

