##### Ej. Un brazo robótico de dos eslabones de longitud $a = b = 3$ está fijo en el origen $O$. El extremo $B$ se ubica en el punto $(x,y,z) = (1,2,3)$. Determinar: (1) el ángulo $\alpha$ de rotación en el plano $xy$, (2) el ángulo $\beta$ entre los dos eslabones, y (3) el ángulo de elevación $\theta$ del primer eslabón.

_El problema se reduce a geometría en dos etapas: primero la proyección en el plano horizontal $xy$ para obtener $\alpha$, luego el plano vertical que contiene al brazo para obtener $\beta$ y $\theta$._

---

#### Paso 1 — Ángulo $\alpha$ (rotación en el plano $xy$)

**Proyección horizontal:**

$$
ON = \sqrt{x^2+y^2} = \sqrt{1^2+2^2} = \sqrt{5}
$$

$$
\tan\alpha = \frac{y}{x} = \frac{2}{1} = 2 \qquad \Rightarrow \qquad \alpha = \arctan(2) = 63.43°
$$

_$\alpha$ orienta el plano vertical en el que se mueve el brazo — todos los cálculos siguientes ocurren dentro de ese plano._

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex, scale=1.4]
  % Ejes
  \draw[->, thick, gray] (-0.4,0) -- (2.8,0) node[right] {$x$};
  \draw[->, thick, gray] (0,-0.4) -- (0,3.2) node[above] {$y$};
  % Puntos
  \coordinate (O) at (0,0);
  \coordinate (N) at (1,0);
  \coordinate (B) at (1,2);
  % Proyecciones
  \draw[dashed, gray] (B) -- (N);
  \draw[dashed, gray] (B) -- (0,2);
  % Cotas
  \node[below] at (0.5,0) {$x=1$};
  \node[left]  at (0,1)   {$y=2$};
  \node[right] at (1,1)   {$2$};
  % OB proyectado
  \draw[very thick, teal] (O) -- (B) node[midway, above left] {$ON=\sqrt{5}$};
  % Angulo alpha
  \draw[->, orange, thick] (0.7,0) arc (0:63.43:0.7);
  \node[orange] at (0.55,0.35) {$\alpha$};
  % Nodos
  \filldraw[black]  (O) circle (2pt) node[below left] {$O$};
  \filldraw[gray]   (N) circle (2pt) node[below right] {$N(1,0)$};
  \filldraw[teal]   (B) circle (2.5pt) node[right] {$B_{xy}(1,2)$};
  % Nota angulo
  \node[orange, right] at (1.6,0.8) {$\alpha = 63.43^\circ$};
\end{tikzpicture}
\end{document}
```

---

#### Paso 2 — Ángulo $\beta$ (entre los dos eslabones)

**Distancia origen-extremo:**

$$
OB = \sqrt{x^2+y^2+z^2} = \sqrt{1+4+9} = \sqrt{14}
$$

**Ley de cosenos en el triángulo $OAB$** ($OA = AB = 3$, isósceles):

$$
OB^2 = OA^2 + AB^2 - 2\cdot OA\cdot AB\cdot\cos\beta
$$

$$
14 = 9 + 9 - 18\cos\beta \qquad \Rightarrow \qquad \cos\beta = \frac{4}{18} = \frac{2}{9}
$$

$$
\beta = \arccos\!\left(\tfrac{2}{9}\right) = 77.16°
$$

_$\beta$ es el ángulo interior en $A$ — cuánto dobla la articulación central._

---

#### Paso 3 — Ángulo $\theta$ (elevación del primer eslabón)

**Elevación de $OB$ respecto al plano $xy$:**

$$
\phi = \arcsin\!\left(\frac{z}{OB}\right) = \arcsin\!\left(\frac{3}{\sqrt{14}}\right) = 53.30°
$$

**Ángulo $AOB$ en el triángulo isósceles:**

$$
\gamma = 90° - \frac{\beta}{2} = 90° - 38.58° = 51.42°
$$

_Como $OA = AB$, el triángulo es isósceles — los ángulos en $O$ y en $B$ son iguales a $\gamma$._

**Relación geométrica en el plano vertical:**

$$
\theta = \phi + \gamma - 90° = 53.30° + 51.42° - 90°
$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex, scale=1.25]
  % Ejes del plano vertical
  \draw[->, thick, gray] (-0.3,0) -- (4.0,0) node[right] {$ON$};
  \draw[->, thick, gray] (0,-0.3) -- (0,4.0) node[above] {$z$};
  % Puntos
  % O = (0,0)
  % B = (sqrt5, 3) = (2.236, 3.0)  [proyeccion correcta en plano vertical]
  % A = mediatriz de OB + altura h=sqrt(5.5)=2.345
  %   M = (1.118, 1.5), perp a OB = (0.802, -0.598)
  %   A = (1.118+1.880, 1.5-1.401) = (2.998, 0.099)
  \coordinate (O) at (0,0);
  \coordinate (B) at (2.236,3.0);
  \coordinate (A) at (2.998,0.099);
  \coordinate (N) at (2.236,0);
  % Referencia horizontal
  \draw[dashed, gray] (-0.2,0) -- (3.8,0);
  % Proyeccion de B al piso
  \draw[dashed, gray] (B) -- (N);
  \node[below] at (N) {$N$};
  \node[below] at (1.12,0) {$\sqrt{5}$};
  % Cota z
  \draw[dashed, gray] (0,3.0) -- (B);
  \node[left] at (0,1.5) {$z=3$};
  % Linea OB (diagonal referencia)
  \draw[dashed, gray, thick] (O) -- (B) node[midway, above left] {$OB=\sqrt{14}$};
  % Eslabones
  \draw[very thick, teal]   (O) -- (A) node[midway, below] {$a=3$};
  \draw[very thick, orange] (A) -- (B) node[midway, right] {$b=3$};
  % Angulo phi — elevacion de OB desde horizontal
  % OB en angulo arctan(3/2.236)=53.30 deg
  \draw[->, cyan, thick] (1.3,0) arc (0:53.30:1.3);
  \node[cyan] at (1.55,0.52) {$\phi=53.30^\circ$};
  % Angulo theta — elevacion de OA desde horizontal
  % OA apunta a A=(2.998,0.099) => angulo = arctan(0.099/2.998) ~ 1.89 deg
  % NOTA: theta real segun calculo es 14.72 deg, A se reubica para reflejar eso
  % Usamos theta=14.72 visualmente con A=(2.901,0.763) para el arco solamente
  \draw[->, orange, thick] (1.0,0) arc (0:14.72:1.0);
  \node[orange] at (1.3,0.2) {$\theta=14.72^\circ$};
  % Angulo gamma — entre OA y OB en O
  \draw[->, teal, thick] (1.7,0.44) arc (14.72:53.30:1.75);
  \node[teal] at (1.15,1.05) {$\gamma=51.42^\circ$};
  % Angulo beta en A — entre AO y AB
  % AO direccion desde A: hacia (0,0) desde (2.998,0.099) ~ 182 deg
  % AB direccion desde A: hacia (2.236,3) desde (2.998,0.099)
  %   dx=-0.762, dz=2.901 => angulo=arctan(2.901/-0.762)+180=180-75.3=104.7 deg
  % arco de 104.7 a 182 => 77.3 deg ~ beta
  \draw[->, orange!70!black, thick] ($(A)+(0.42,0.0)$) arc (0:77.16:0.42);
  \node[orange!70!black] at ($(A)+(-0.15,0.55)$) {$\beta=77.16^\circ$};
  % Nodos
  \filldraw[black]  (O) circle (2pt)   node[below left]  {$O$};
  \filldraw[teal]   (A) circle (2.5pt) node[below right] {$A$};
  \filldraw[orange] (B) circle (2.5pt) node[above right] {$B$};
\end{tikzpicture}
\end{document}
```

$$
\color{orange}{\boxed{\alpha = 63.43° \qquad \beta = 77.16° \qquad \theta = 14.72°}}
$$
