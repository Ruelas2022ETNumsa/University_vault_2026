##### Ej. Un brazo robótico de dos eslabones de igual longitud $l_1 = l_2 = 2$ está articulado en el origen $P_1 = (0,0,0)$. El extremo debe alcanzar el punto $P_2 = (1,1,1)$. Determinar: $1$ el ángulo $\alpha$ de rotación en el plano $xy$, $2$ el ángulo $\phi$ entre los dos eslabones, y $3$ el ángulo de elevación $\theta$ del primer eslabón.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.5, >=stealth]
  % Ejes
  \draw[->, thick, gray] (-0.5,0) -- (3,0) node[right, black] {Proyección $xy$ ($ON$)};
  \draw[->, thick, gray] (0,-0.5) -- (0,2.5) node[above, black] {$z$};
  
  % Puntos
  \coordinate (O) at (0,0);
  \coordinate (P2) at (1.414, 1.0);
  \coordinate (Aup) at (-0.334, 1.97);
  
  % Eslabones
  \draw[line width=1.5pt, teal] (O) -- (Aup) node[midway, above left] {$l_1=2$};
  \draw[line width=1.5pt, orange] (Aup) -- (P2) node[midway, above right] {$l_2=2$};
  
  % Línea OP2
  \draw[dashed, black!60] (O) -- (P2);
  
  % Nodos
  \filldraw[black] (O) circle (1.5pt) node[below left] {$O(0,0)$};
  \filldraw[black] (P2) circle (1.5pt) node[right] {$P_2(\sqrt{2}, 1)$};
  \filldraw[black] (Aup) circle (1.5pt) node[above] {$A$};
  
  % Ángulos
  \draw[->, thin] (0.5,0) arc (0:35.26:0.5);
  \node at (0.7,0.25) {$\psi$};
  
  \draw[->, thin] (0.4, 0.28) arc (35.26:99.6:0.5);
  \node at (0.2, 0.6) {$\gamma$};
  
  \draw[->, thin] (0.3,0) arc (0:99.6:0.3);
  \node at (0.1,0.4) [above right] {$\theta$};
\end{tikzpicture}
\end{document}
```

**Resolución**
Determinamos los ángulos de rotación, de articulación intermedia y de elevación del brazo robótico mediante cinemática inversa y relaciones trigonométricas en el plano vertical.

**Análisis Geométrico y Detalle del Paso 3:**
En el plano vertical rotado un ángulo $\alpha$ respecto a los ejes de coordenadas espaciales, el origen $O$, la articulación del codo $A$ y el extremo $P_2$ forman el triángulo $\triangle OAP_2$. Dado que los eslabones tienen la misma longitud ($OA = AP_2 = 2$), el triángulo es **isósceles**, lo que implica que los ángulos basales opuestos a estos lados son idénticos: $\gamma = \angle AOP_2 = \angle OP_2A$. 

La suma de los ángulos internos del triángulo exige que $2\gamma + \phi = 180^\circ$. Por lo tanto, el ángulo relativo $\gamma$ que separa el primer eslabón de la línea de mira directa $OP_2$ es $\gamma = (180^\circ - \phi)/2$. El ángulo de elevación final $\theta$ del primer eslabón respecto al plano horizontal de la base se compone de la elevación sobre la horizontal de la línea $OP_2$ (ángulo $\psi$) y la apertura interna $\gamma$. Dependiendo de la configuración cinemática seleccionada se tienen dos alternativas físicas:
* **Configuración codo-arriba (*elbow-up*):** El eslabón se eleva por encima del vector de posición final, resultando en **$\theta = \psi + \gamma$**.
* **Configuración codo-abajo (*elbow-down*):** El eslabón se inclina por debajo del vector de posición final, resultando en **$\theta = \psi - \gamma$**.
* **Referencia complementaria:** Si la inclinación se calcula respecto al eje vertical normal, se obtiene la expresión complementaria corregida **$\theta_{\text{vert}} = 90^\circ - (\psi + \gamma)$**.


$$
\begin{array}{rcl}
\text{1. Ángulo de rotación de la base } \alpha: && \\
\tan\alpha & = & \displaystyle\frac{y}{x} = \frac{1}{1} = 1 \\
\alpha & = & \arctan(1) \\
\alpha & = & \color{orange}{45.00^\circ} \\
\text{2. Ángulo entre eslabones } \phi \text{ (Ley de Cosenos):} && \\
OP_2 & = & \sqrt{x^2+y^2+z^2} = \sqrt{1^2+1^2+1^2} = \sqrt{3} \\
OP_2^2 & = & l_1^2 + l_2^2 - 2\,l_1\,l_2\cos\phi \\
(\sqrt{3})^2 & = & 2^2 + 2^2 - 2(2)(2)\cos\phi \\
3 & = & 4 + 4 - 8\cos\phi \\
8\cos\phi & = & 5 \\
\cos\phi & = & 0.625 \\
\phi & = & \arccos(0.625) \\
\phi & = & \color{orange}{51.32^\circ} \\
\text{3. Elevación del primer eslabón } \theta \text{ (codo-arriba):} && \\
\psi & = & \arcsin\left(\displaystyle\frac{z}{OP_2}\right) = \arcsin\left(\displaystyle\frac{1}{\sqrt{3}}\right) \approx 35.26^\circ \\
\gamma & = & \displaystyle\frac{180^\circ - \phi}{2} = \frac{180^\circ - 51.32^\circ}{2} = 64.34^\circ \\
\theta & = & \psi + \gamma \\
\theta & = & 35.26^\circ + 64.34^\circ \\
\therefore\quad \theta & = & \color{orange}{99.60^\circ \quad \text{[o bien, elbow-down: } -29.08^\circ\text{]}}
\end{array}
$$

