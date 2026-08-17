## 2.2 Sistemas de Coordenadas

> [!note] Complemento (Nivel C)
>
> 1. Definición formal
> Uno de los primeros pasos en el tratamiento de cualquier problema es el de seleccionar coordenadas apropiadas. Las ecuaciones de transformación juegan un papel importante al expresar la energía cinética, la aceleración y muchas otras cantidades en términos de las coordenadas elegidas.
>
> 2. Idea clave
> Las ecuaciones de transformación permiten definir la posición, velocidad y aceleración en sistemas curvilíneos locales (polares, cilíndricos, esféricos) a partir de coordenadas cartesianas mediante factores de escala y versores unitarios.
>
> 3. Figura o diagrama
>
> [[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=12]]
> *Fig. 2-3*
> *Cylindrical Coordinates*
> %%IMA-SRC | fuente: Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf | página: 12 | id: Fig. 2-3 | posición: centro de la página | justificación: Esta figura muestra la definición geométrica y las relaciones de transformación del sistema de coordenadas cilíndricas en el espacio tridimensional.%%
>
> [[Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf#page=12]]
> *Fig. 2-4*
> *Spherical Coordinates*
> %%IMA-SRC | fuente: Dare A. Wells-SCHAUM'S Lagrangian Dynamics-McGraw-Hill.pdf | página: 12 | id: Fig. 2-4 | posición: centro-derecha de la página | justificación: Esta figura ilustra la orientación angular y la distancia radial que definen a las coordenadas esféricas.%%
>
> ```tikz
> \usepackage{tikz}
> \begin{document}
> \begin{tikzpicture}[scale=1.3, >=stealth]
>   % Ejes Cartesianos
>   \draw[->, thick, black] $0,0$ -- $4,0$ node[anchor=west] {$x$};
>   \draw[->, thick, black] $0,0$ -- $0,3.5$ node[anchor=south] {$y$};
>   
>   % Vector de posición y Punto P
>   \draw[->, ultra thick, teal] $0,0$ -- $2.6, 1.5$ node[midway, above left] {$\vec{r}$};
>   \filldraw[teal] $2.6, 1.5$ circle (2pt) node[anchor=south west] {$P(r, \theta)$};
>   
>   % Arco de ángulo theta
>   \draw[->, thick, orange] $0.8,0$ arc (0:30:0.8);
>   \node[orange] at $1.0, 0.25$ {$\theta$};
>   
>   % Versores unitarios de coordenadas polares
>   \draw[->, thick, teal] $2.6, 1.5$ -- $3.46, 2.0$ node[anchor=west] {$\mathbf{e}_r$};
>   \draw[->, thick, orange] $2.6, 1.5$ -- $2.1, 2.36$ node[anchor=south] {$\mathbf{e}_\theta$};
>   
>   % Proyecciones a los ejes
>   \draw[dashed, thin, gray] $2.6, 1.5$ -- $2.6, 0$ node[midway, right] {$y = r\text{sen}\,\theta$};
>   \draw[dashed, thin, gray] $2.6, 1.5$ -- $0, 1.5$ node[midway, above] {$x = r\text{cos}\,\theta$};
> \end{tikzpicture}
> \end{document}
> ```
>
> 4. Ejercicios resueltos (solo nivel C)
>
> ##### Ej. 1: Cuenta deslizándose en un alambre circular en rotación uniforme
> Una cuenta de masa $m$ está obligada a moverse sobre un aro de radio $R$ en un plano horizontal que gira con velocidad angular constante $\omega$ alrededor de un eje vertical. Determine la ecuación de movimiento de la cuenta utilizando coordenadas polares.
>
> **Resolución:**
> Empleamos coordenadas polares planas $(r, \theta)$ con el origen en el centro del movimiento. La ligadura del alambre impone que el radio sea constante $r = R$, y que la orientación angular sea $\theta = \omega t$. 
>
> La energía cinética en coordenadas polares es:
> 
$$
T = \dfrac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2)
$$

>
> Si consideramos el caso donde la cuenta se desliza radialmente a lo largo de una varilla recta en rotación constante $\theta = \omega t$:
> 
$$
T = \dfrac{1}{2}m(\dot{r}^2 + r^2\omega^2)
$$

>
> Aplicamos la ecuación de Lagrange para la coordenada libre $r$:
> 
$$
\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{r}}\right) - \dfrac{\partial T}{\partial r} = Q_r
$$

>
> Calculamos las derivadas parciales de la energía cinética:
> 
$$
\begin{array}{rcl}
> \dfrac{\partial T}{\partial \dot{r}} & = & m\dot{r} \\
> \dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{r}}\right) & = & m\ddot{r} \\
> \dfrac{\partial T}{\partial r} & = & mr\omega^2
> \end{array}
$$

>
> Sustituyendo en la ecuación de Lagrange con $Q_r = 0$ (sin fricción radial):
> 
$$
m\ddot{r} - mr\omega^2 = 0 \implies \ddot{r} = r\omega^2
$$

>
> Esta ecuación diferencial describe la aceleración centrípeta que empuja la cuenta hacia el extremo exterior de la varilla giratoria.
>
> ##### Ej. 2: Fuerza de reacción en una hélice cilíndrica
> Una partícula de masa $m$ está restringida a moverse a lo largo de una hélice cilíndrica tallada sobre un cilindro de radio constante $r = R$ con la relación $z = b\phi$. Si no actúan fuerzas externas activas más que la gravedad en la dirección de $z$ ($F_z = -mg$), determine las componentes de la fuerza de reacción reactiva ($f_r, f_\phi, f_z$) en coordenadas cilíndricas.
>
> **Resolución:**
> En coordenadas cilíndricas $(r, \phi, z)$, las ecuaciones del movimiento con fuerzas reactivas de ligadura son:
> 
$$
\begin{array}{rcl}
> m(\ddot{r} - r\dot{\phi}^2) - F_r & = & f_r \\
> m(r^2\ddot{\phi} + 2r\dot{r}\dot{\phi}) - rF_\phi & = & r f_\phi \\
> m\ddot{z} - F_z + mg & = & f_z
> \end{array}
$$

>
> Dado que la partícula está obligada a permanecer en la trayectoria helicoidal con las condiciones de restricción:
> 
$$
r = R \implies \dot{r} = \ddot{r} = 0
$$

> 
$$
z = b\phi \implies \ddot{z} = b\ddot{\phi}
$$

>
> Sustituyendo estas restricciones y las fuerzas activas ($F_r = 0, F_\phi = 0, F_z = -mg$) en las ecuaciones de movimiento, obtenemos de inmediato:
> 
$$
\begin{array}{rcl}
> f_r & = & -m R \dot{\phi}^2 \\
> f_\phi & = & m R \ddot{\phi} \\
> f_z & = & m b \ddot{\phi}
> \end{array}
$$

>
> Las componentes de la fuerza reactiva de ligadura se determinan de forma directa en términos de la evolución angular del sistema.
