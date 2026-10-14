## Enunciado 7 (ej7T5) — Doble péndulo con fricción

Dos masas puntuales m₁ y m₂ forman un doble péndulo plano. La masa 1 cuelga de un punto fijo mediante una varilla rígida sin masa de longitud l; la masa 2 cuelga de la masa 1 mediante otra varilla de longitud l. Los ángulos θ₁ y θ₂ se miden desde la vertical (y positiva hacia abajo), cada uno respecto de su propia vertical local. Hay fricción en cada masa, proporcional a la velocidad de esa masa, con coeficientes c₁ (masa 1) y c₂ (masa 2).

**Se pide:**
1. N y coordenadas generalizadas.
2. Posición y velocidad de cada masa.
3. T, V y P $n = 1$.
4. Las dos EDO acopladas mediante Lagrange.
5. Verificar el caso límite c₁ = c₂ = 0.
6. Opcional: obtener las ecuaciones con MATLAB simbólico (+15 pts).

---

### 1. Datos y esquema
- **Masas puntuales:** $m_1$ y $m_2$.
- **Varillas rígidas sin masa:** Longitudes $l_1 = l_2 = l$.
- **Coordenadas angulares:** $\theta_1(t)$ y $\theta_2(t)$, medidas desde la vertical descendente (eje $y$ positivo hacia abajo, eje $x$ hacia la derecha).
- **Fricción viscosa lineal ($n=1$):** Actúa sobre cada masa de forma proporcional a su velocidad instantánea respecto al marco inercial, con coeficientes $c_1$ (para $m_1$) y $c_2$ (para $m_2$).

---

### 2. Grados de libertad $N$ y coordenadas generalizadas
- **Número de coordenadas cartesianas:** 4 ($x_1, y_1, x_2, y_2$).
- **Restricciones holónomas ($k = 2$):** Longitudes fijas de las dos varillas ($l_1 = l, l_2 = l$).
- **Grados de libertad ($N$):**
  
$$
N = 4 - 2 = 2
$$

- **Coordenadas generalizadas:** $q_1 = \theta_1$, $q_2 = \theta_2$.

---

### 3. Posición y velocidad de cada masa

#### **Masa 1 ($m_1$):**
- Posición:
  
$$
x_1 = l \sin\theta_1, \qquad y_1 = l \cos\theta_1
$$

- Velocidad:
  
$$
\dot{x}_1 = l \cos\theta_1 \, \dot{\theta}_1, \qquad \dot{y}_1 = -l \sin\theta_1 \, \dot{\theta}_1
$$

- Módulo al cuadrado de la velocidad:
  
$$
v_1^2 = \dot{x}_1^2 + \dot{y}_1^2 = l^2 \dot{\theta}_1^2
$$


#### **Masa 2 ($m_2$):**
- Posición:
  
$$
x_2 = l \sin\theta_1 + l \sin\theta_2, \qquad y_2 = l \cos\theta_1 + l \cos\theta_2
$$

- Velocidad:
  
$$
\dot{x}_2 = l \cos\theta_1 \, \dot{\theta}_1 + l \cos\theta_2 \, \dot{\theta}_2, \qquad \dot{y}_2 = -l \sin\theta_1 \, \dot{\theta}_1 - l \sin\theta_2 \, \dot{\theta}_2
$$

- Módulo al cuadrado de la velocidad:
  
$$
v_2^2 = \dot{x}_2^2 + \dot{y}_2^2 = l^2 \dot{\theta}_1^2 + l^2 \dot{\theta}_2^2 + 2 l^2 \dot{\theta}_1 \dot{\theta}_2 \cos(\theta_1 - \theta_2)
$$


---

### 4. $T$, $V$ y $P$ por separado

- **Energía cinética ($T$):**
  
$$
T = \frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2 = \frac{1}{2} (m_1 + m_2) l^2 \dot{\theta}_1^2 + \frac{1}{2} m_2 l^2 \dot{\theta}_2^2 + m_2 l^2 \dot{\theta}_1 \dot{\theta}_2 \cos(\theta_1 - \theta_2)
$$


- **Energía potencial ($V$):**
  Tomando nivel de referencia $V = 0$ en el pivote fijo ($y = 0$):
  
$$
V = -m_1 g y_1 - m_2 g y_2 = -(m_1 + m_2) g l \cos\theta_1 - m_2 g l \cos\theta_2
$$


- **Función de disipación de Rayleigh ($P$):**
  Para fricción viscosa lineal ($n = 1$), $P = \frac{1}{2} \sum c_k v_k^2$:
  
$$
P = \frac{1}{2} c_1 v_1^2 + \frac{1}{2} c_2 v_2^2 = \frac{1}{2} (c_1 + c_2) l^2 \dot{\theta}_1^2 + \frac{1}{2} c_2 l^2 \dot{\theta}_2^2 + c_2 l^2 \dot{\theta}_1 \dot{\theta}_2 \cos(\theta_1 - \theta_2)
$$


---

### 5. Derivadas de Lagrange
Se aplica la ecuación de Lagrange extendida para sistemas disipativos:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}_i}\right) - \frac{\partial T}{\partial \theta_i} + \frac{\partial V}{\partial \theta_i} + \frac{\partial P}{\partial \dot{\theta}_i} = 0, \qquad (i = 1, 2)
$$


#### **Para la coordenada $\theta_1$:**
1. $\dfrac{\partial T}{\partial \dot{\theta}_1} = (m_1 + m_2) l^2 \dot{\theta}_1 + m_2 l^2 \dot{\theta}_2 \cos(\theta_1 - \theta_2)$
2. $\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{\theta}_1}\right) = (m_1 + m_2) l^2 \ddot{\theta}_1 + m_2 l^2 \ddot{\theta}_2 \cos(\theta_1 - \theta_2) - m_2 l^2 \dot{\theta}_2 (\dot{\theta}_1 - \dot{\theta}_2) \sin(\theta_1 - \theta_2)$
3. $\dfrac{\partial T}{\partial \theta_1} = -m_2 l^2 \dot{\theta}_1 \dot{\theta}_2 \sin(\theta_1 - \theta_2)$
4. Término inercial neto:
   
$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}_1}\right) - \frac{\partial T}{\partial \theta_1} = (m_1 + m_2) l^2 \ddot{\theta}_1 + m_2 l^2 \ddot{\theta}_2 \cos(\theta_1 - \theta_2) + m_2 l^2 \dot{\theta}_2^2 \sin(\theta_1 - \theta_2)
$$

5. $\dfrac{\partial V}{\partial \theta_1} = (m_1 + m_2) g l \sin\theta_1$
6. $\dfrac{\partial P}{\partial \dot{\theta}_1} = (c_1 + c_2) l^2 \dot{\theta}_1 + c_2 l^2 \dot{\theta}_2 \cos(\theta_1 - \theta_2)$

#### **Para la coordenada $\theta_2$:**
1. $\dfrac{\partial T}{\partial \dot{\theta}_2} = m_2 l^2 \dot{\theta}_2 + m_2 l^2 \dot{\theta}_1 \cos(\theta_1 - \theta_2)$
2. $\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{\theta}_2}\right) = m_2 l^2 \ddot{\theta}_2 + m_2 l^2 \ddot{\theta}_1 \cos(\theta_1 - \theta_2) - m_2 l^2 \dot{\theta}_1 (\dot{\theta}_1 - \dot{\theta}_2) \sin(\theta_1 - \theta_2)$
3. $\dfrac{\partial T}{\partial \theta_2} = m_2 l^2 \dot{\theta}_1 \dot{\theta}_2 \sin(\theta_1 - \theta_2)$
4. Término inercial neto:
   
$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}_2}\right) - \frac{\partial T}{\partial \theta_2} = m_2 l^2 \ddot{\theta}_2 + m_2 l^2 \ddot{\theta}_1 \cos(\theta_1 - \theta_2) - m_2 l^2 \dot{\theta}_1^2 \sin(\theta_1 - \theta_2)
$$

5. $\dfrac{\partial V}{\partial \theta_2} = m_2 g l \sin\theta_2$
6. $\dfrac{\partial P}{\partial \dot{\theta}_2} = c_2 l^2 \dot{\theta}_2 + c_2 l^2 \dot{\theta}_1 \cos(\theta_1 - \theta_2)$

---

### 6. EDO final (modelo matemático acoplado)

Sustituyendo los términos en las ecuaciones de Lagrange correspondientes:

- **Ecuación para $\theta_1(t)$:**
  
$$
(m_1 + m_2) l^2 \ddot{\theta}_1 + m_2 l^2 \ddot{\theta}_2 \cos(\theta_1 - \theta_2) + m_2 l^2 \dot{\theta}_2^2 \sin(\theta_1 - \theta_2) + (m_1 + m_2) g l \sin\theta_1 + (c_1 + c_2) l^2 \dot{\theta}_1 + c_2 l^2 \dot{\theta}_2 \cos(\theta_1 - \theta_2) = 0
$$


- **Ecuación para $\theta_2(t)$:**
  
$$
m_2 l^2 \ddot{\theta}_2 + m_2 l^2 \ddot{\theta}_1 \cos(\theta_1 - \theta_2) - m_2 l^2 \dot{\theta}_1^2 \sin(\theta_1 - \theta_2) + m_2 g l \sin\theta_2 + c_2 l^2 \dot{\theta}_2 + c_2 l^2 \dot{\theta}_1 \cos(\theta_1 - \theta_2) = 0
$$


---

### 7. Verificación del caso límite $c_1 = c_2 = 0$
Haciendo $c_1 = c_2 = 0$, la función de disipación es nula ($P = 0$) y las EDOs se reducen a:

$$
(m_1 + m_2) l^2 \ddot{\theta}_1 + m_2 l^2 \ddot{\theta}_2 \cos(\theta_1 - \theta_2) + m_2 l^2 \dot{\theta}_2^2 \sin(\theta_1 - \theta_2) + (m_1 + m_2) g l \sin\theta_1 = 0
$$


$$
m_2 l^2 \ddot{\theta}_2 + m_2 l^2 \ddot{\theta}_1 \cos(\theta_1 - \theta_2) - m_2 l^2 \dot{\theta}_1^2 \sin(\theta_1 - \theta_2) + m_2 g l \sin\theta_2 = 0
$$

Coincide exactamente con el modelo no lineal conservativo del doble péndulo plano de longitudes iguales.

---

### 8. Opcional: Obtención con MATLAB Simbólico (+15 pts)

```matlab
% Doble péndulo con fricción viscosa (n = 1): Lagrange + función de Rayleigh
syms t m1 m2 l g c1 c2 real
syms th1(t) th2(t)

% Posiciones cartesianas
x1 = l*sin(th1);        y1 = l*cos(th1);
x2 = x1 + l*sin(th2);   y2 = y1 + l*cos(th2);

% Velocidades al cuadrado
v1sq = diff(x1,t)^2 + diff(y1,t)^2;
v2sq = diff(x2,t)^2 + diff(y2,t)^2;

% Energías y función de disipación de Rayleigh
T = simplify(m1/2*v1sq + m2/2*v2sq);
V = -m1*g*y1 - m2*g*y2;
P = simplify(c1/2*v1sq + c2/2*v2sq);

% Símbolos auxiliares (a = θ, w = θpunto) para poder derivar parcialmente
syms a1 a2 w1 w2 real
toS = @(e) subs(subs(e, [diff(th1,t) diff(th2,t)], [w1 w2]), [th1 th2], [a1 a2]);
toF = @(e) subs(e, [a1 a2 w1 w2], [th1 th2 diff(th1,t) diff(th2,t)]);
Ts = toS(T);  Vs = toS(V);  Ps = toS(P);

% d/dt(dT/dw) - dT/da + dV/da + dP/dw = 0
eq1 = diff(toF(diff(Ts,w1)),t) - toF(diff(Ts,a1)) + toF(diff(Vs,a1)) + toF(diff(Ps,w1)) == 0;
eq2 = diff(toF(diff(Ts,w2)),t) - toF(diff(Ts,a2)) + toF(diff(Vs,a2)) + toF(diff(Ps,w2)) == 0;

% Mostrar EDOs simplificadas
disp('EDO para theta1:');  disp(simplify(eq1));
disp('EDO para theta2:');  disp(simplify(eq2));
```

---

### Resultado final

$$
\begin{aligned}
1.\quad N &= 2, \qquad q = (\theta_1, \theta_2) \\
2.\quad \vec{r}_1 &= (l\sin\theta_1, \, l\cos\theta_1), \qquad v_1^2 = l^2\dot{\theta}_1^2 \\
\vec{r}_2 &= (l\sin\theta_1 + l\sin\theta_2, \, l\cos\theta_1 + l\cos\theta_2), \qquad v_2^2 = l^2\dot{\theta}_1^2 + l^2\dot{\theta}_2^2 + 2l^2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1-\theta_2) \\
3.\quad T &= \frac{1}{2}(m_1+m_2)l^2\dot{\theta}_1^2 + \frac{1}{2}m_2 l^2\dot{\theta}_2^2 + m_2 l^2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1-\theta_2) \\
V &= -(m_1+m_2)gl\cos\theta_1 - m_2 gl\cos\theta_2 \\
P &= \frac{1}{2}(c_1+c_2)l^2\dot{\theta}_1^2 + \frac{1}{2}c_2 l^2\dot{\theta}_2^2 + c_2 l^2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1-\theta_2) \\
4.\quad &(m_1+m_2)l^2\ddot{\theta}_1 + m_2 l^2\ddot{\theta}_2\cos(\theta_1-\theta_2) + m_2 l^2\dot{\theta}_2^2\sin(\theta_1-\theta_2) + (m_1+m_2)gl\sin\theta_1 + (c_1+c_2)l^2\dot{\theta}_1 + c_2 l^2\dot{\theta}_2\cos(\theta_1-\theta_2) = 0 \\
&m_2 l^2\ddot{\theta}_2 + m_2 l^2\ddot{\theta}_1\cos(\theta_1-\theta_2) - m_2 l^2\dot{\theta}_1^2\sin(\theta_1-\theta_2) + m_2 gl\sin\theta_2 + c_2 l^2\dot{\theta}_2 + c_2 l^2\dot{\theta}_1\cos(\theta_1-\theta_2) = 0 \\
5.\quad &\text{Si } c_1 = c_2 = 0 \implies \text{se recupera el modelo conservativo clásico del doble péndulo plano.}
\end{aligned}
$$


---

**Dudas o supuestos:** Se asume que las varillas son indeformables, el movimiento permanece confinado al plano vertical y los coeficientes $c_1, c_2$ representan disipación viscosa proporcional a la velocidad absoluta de cada masa respecto al sistema inercial.

💡 ¿Te gustaría linealizar las ecuaciones para pequeñas oscilaciones ($\theta_1, \theta_2 \ll 1$) y expresar el sistema en forma matricial $M\mathbf{\ddot{\theta}} + C\mathbf{\dot{\theta}} + K\mathbf{\theta} = \mathbf{0}$?
