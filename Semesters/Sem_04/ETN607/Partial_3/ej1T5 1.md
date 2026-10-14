## Enunciado 1 (ej1T5) — Tiro balístico con fricción cuadrática

Una partícula de masa m se lanza en el plano vertical (x, y) y se mueve bajo la gravedad (y positiva hacia arriba). Sobre ella actúa una fricción del aire cuadrática, f = c·v², con v² = ẋ² + ẏ², siempre opuesta a la velocidad (n = 2).

**Se pide:**
1. Grados de libertad N y coordenadas generalizadas.
2. T, V y P.
3. Las ecuaciones de movimiento de x(t) e y(t) mediante Lagrange.
4. Verificar que con c = 0 se recupera el tiro parabólico sin fricción.

---

### 1. Datos y esquema
- **Masa de la partícula:** $m$
- **Aceleración de la gravedad:** $\vec{g} = -g \hat{j}$ (eje $y$ positivo hacia arriba).
- **Fuerza de fricción cuadrática del aire ($n=2$):**
  
$$
\vec{f} = -c v \vec{v} = -c \sqrt{\dot{x}^2 + \dot{y}^2} (\dot{x}\hat{i} + \dot{y}\hat{j})
$$

  cuya magnitud es $f = c v^2$, actuando siempre en dirección opuesta a la velocidad instantánea $\vec{v} = \dot{x}\hat{i} + \dot{y}\hat{j}$ [Taylor, Cap. 2].
- **Sistema de referencia:** Ejes cartesianos inerciales $(x, y)$ en el plano vertical.

---

### 2. Grados de libertad $N$ y coordenadas generalizadas
- **Número de coordenadas cartesianas:** 2 ($x, y$).
- **Número de restricciones holónomas ($k$):** 0.
- **Grados de libertad:**
  
$$
N = 2 - 0 = 2
$$

- **Coordenadas generalizadas:** $q_1 = x$, $q_2 = y$ [Wells, Cap. 2].

---

### 3. Restricciones y posiciones/velocidades
- **Vector de posición:** $\vec{r} = x \hat{i} + y \hat{j}$
- **Vector de velocidad:** $\vec{v} = \dot{x} \hat{i} + \dot{y} \hat{j}$
- **Rapidez instantánea:** $v = |\vec{v}| = \sqrt{\dot{x}^2 + \dot{y}^2}$
- **Restricciones:** No existen restricciones holónomas ni no holónomas ($k = 0$).

---

### 4. $T$, $V$ y $P$ por separado
- **Energía cinética ($T$):** [Wells, Cap. 2; Taylor, Cap. 1]
  
$$
T = \frac{1}{2} m v^2 = \frac{1}{2} m \left(\dot{x}^2 + \dot{y}^2\right)
$$


- **Energía potencial ($V$):** [Wells, Cap. 5; Goldstein, Cap. 1]
  Tomando el nivel de referencia $V(x, 0) = 0$:
  
$$
V = m g y
$$


- **Función de disipación de Rayleigh ($P$):** [Goldstein, Cap. 1; Wells, Cap. 6, Ec. 6.17]
  Para una fuerza disipativa de magnitud $f = c v^n$ con exponente $n = 2$, la función de disipación de Rayleigh se expresa como:
  
$$
P = \frac{c}{n+1} v^{n+1} = \frac{c}{3} v^3 = \frac{c}{3} \left(\dot{x}^2 + \dot{y}^2\right)^{3/2}
$$


---

### 5. Derivadas de Lagrange
Se aplica la ecuación de Lagrange extendida para sistemas disipativos [Goldstein, Cap. 1, Ec. 1.70; Wells, Cap. 6]:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{q}_i}\right) - \frac{\partial T}{\partial q_i} + \frac{\partial V}{\partial q_i} + \frac{\partial P}{\partial \dot{q}_i} = 0, \qquad (i=1, 2)
$$


#### Para la coordenada $q_1 = x$:
- $\dfrac{\partial T}{\partial \dot{x}} = m \dot{x} \implies \dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{x}}\right) = m \ddot{x}$
- $\dfrac{\partial T}{\partial x} = 0$
- $\dfrac{\partial V}{\partial x} = 0$
- $\dfrac{\partial P}{\partial \dot{x}} = \dfrac{c}{3} \cdot \frac{3}{2} \left(\dot{x}^2 + \dot{y}^2\right)^{1/2} (2\dot{x}) = c \sqrt{\dot{x}^2 + \dot{y}^2} \dot{x}$

#### Para la coordenada $q_2 = y$:
- $\dfrac{\partial T}{\partial \dot{y}} = m \dot{y} \implies \dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{y}}\right) = m \ddot{y}$
- $\dfrac{\partial T}{\partial y} = 0$
- $\dfrac{\partial V}{\partial y} = m g$
- $\dfrac{\partial P}{\partial \dot{y}} = \dfrac{c}{3} \cdot \frac{3}{2} \left(\dot{x}^2 + \dot{y}^2\right)^{1/2} (2\dot{y}) = c \sqrt{\dot{x}^2 + \dot{y}^2} \dot{y}$

---

### 6. EDO final (modelo matemático)
Sustituyendo los términos en la ecuación de Lagrange para cada coordenada:

- **Ecuación de movimiento para $x(t)$:**
  
$$
m \ddot{x} + c \sqrt{\dot{x}^2 + \dot{y}^2} \dot{x} = 0 \implies \ddot{x} = -\frac{c}{m} \sqrt{\dot{x}^2 + \dot{y}^2} \dot{x}
$$


- **Ecuación de movimiento para $y(t)$:**
  
$$
m \ddot{y} + m g + c \sqrt{\dot{x}^2 + \dot{y}^2} \dot{y} = 0 \implies \ddot{y} = -g - \frac{c}{m} \sqrt{\dot{x}^2 + \dot{y}^2} \dot{y}
$$


---

### 7. Verificación

#### Análisis dimensional:
- Coeficiente de fricción: $[c] = \frac{[f]}{[v^2]} = \frac{\text{N}}{(\text{m/s})^2} = \frac{\text{kg}\cdot\text{m/s}^2}{\text{m}^2/\text{s}^2} = \text{kg/m}$.
- Término de aceleración por arrastre: $\left[\frac{c}{m} v \dot{x}\right] = \frac{\text{kg/m}}{\text{kg}} \cdot (\text{m/s}) \cdot (\text{m/s}) = \text{m/s}^2$ (unidades de aceleración, correcto).
- Función de disipación $P$: $[P] = \left[\frac{c}{3} v^3\right] = (\text{kg/m}) \cdot (\text{m}^3/\text{s}^3) = \text{kg}\cdot\text{m}^2/\text{s}^3 = \text{W}$ (unidades de potencia disipada, correcto).

#### Caso límite $c = 0$ (sistema conservativo sin resistencia):
Sustituyendo $c = 0$ en el modelo matemático:

$$
\ddot{x} = 0 \implies \dot{x}(t) = v_{0x} \implies x(t) = x_0 + v_{0x} t
$$


$$
\ddot{y} = -g \implies \dot{y}(t) = v_{0y} - g t \implies y(t) = y_0 + v_{0y} t - \frac{1}{2} g t^2
$$

Se recupera exactamente el modelo parabólico del tiro de proyectiles sin fricción [Alonso & Finn, Cap. 5; Taylor, Cap. 2].

---

### Resultado final

$$
\begin{aligned}
1.\quad N &= 2 \quad \text{con coordenadas generalizadas } (x, y) \\
2.\quad T &= \frac{1}{2}m\left(\dot{x}^2 + \dot{y}^2\right) \\
V &= mgy \\
P &= \frac{c}{3}\left(\dot{x}^2 + \dot{y}^2\right)^{3/2} \\
3.\quad \ddot{x} &= -\frac{c}{m}\sqrt{\dot{x}^2 + \dot{y}^2}\,\dot{x} \\
\ddot{y} &= -g - \frac{c}{m}\sqrt{\dot{x}^2 + \dot{y}^2}\,\dot{y} \\
4.\quad \text{Si } c &= 0 \implies \ddot{x} = 0, \quad \ddot{y} = -g \quad \text{(tiro parabólico conservativo)}.
\end{aligned}
$$


---

**Dudas o supuestos:** Se asume densidad del aire y aceleración de la gravedad $g$ constantes a lo largo de toda la trayectoria, sin efectos de sustentación ni viento lateral.

💡 ¿Deseas que analicemos la velocidad límite o el espacio de estados matricial del sistema?
