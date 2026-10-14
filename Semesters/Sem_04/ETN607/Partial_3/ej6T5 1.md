## Enunciado 6 (ej6T5) — Tres masas con resortes y amortiguadores (forma matricial)

Tres bloques se mueven en línea recta, con coordenadas x₁, x₂ y x₃ medidas desde sus posiciones de referencia. Las masas son m₁ = 2, m₂ = 3 y m₃ = 2. Las conexiones son:

- Pared – bloque 1: un resorte de constante 2 y un amortiguador de coeficiente 3.
- Bloque 1 – bloque 2: un resorte de constante 3 y un amortiguador de coeficiente 4.
- Bloque 1 – bloque 3: dos resortes en serie, de constantes 2 y 3.
- Bloque 2 – bloque 3: dos amortiguadores en serie, de coeficientes 2 y 2.
- Pared – bloque 2: dos resortes en paralelo, de constantes 1 y 2.

Sobre el bloque 2 actúa una fuerza externa F.

**Se pide:**
1. Resortes y amortiguadores equivalentes (serie y paralelo).
2. Las matrices M, C y K, y el sistema M·ẍ + C·ẋ + K·x = F.
3. Explicar el tratamiento del término constante k·l₀ en F_R = k(x − l₀) y por qué no aparece en las matrices.

---

### 1. Datos y esquema
- **Masas de los bloques:** $m_1 = 2$, $m_2 = 3$, $m_3 = 2$.
- **Sistema de coordenadas:** Desplazamientos rectilíneos horizontales $\mathbf{x} = [x_1, x_2, x_3]^T$ medidos a partir de las **posiciones de referencia** de cada bloque (se toman como equilibrio estático).
- **Conexiones del sistema:**
  - **Pared – bloque 1:** Resorte $k_{10} = 2$ y amortiguador $c_{10} = 3$ en paralelo.
  - **Bloque 1 – bloque 2:** Resorte $k_{12} = 3$ y amortiguador $c_{12} = 4$ en paralelo.
  - **Bloque 1 – bloque 3:** Dos resortes en serie de constantes $k_a = 2$ y $k_b = 3$.
  - **Bloque 2 – bloque 3:** Dos amortiguadores en serie de coeficientes $c_a = 2$ y $c_b = 2$.
  - **Pared – bloque 2:** Dos resortes en paralelo de constantes $k_{p1} = 1$ y $k_{p2} = 2$.
- **Fuerza externa:** $F(t)$ aplicada sobre el bloque 2 en dirección de $x_2$.

---

### 2. Grados de libertad $N$ y coordenadas generalizadas
- **Número de coordenadas rectilíneas:** 3 ($x_1, x_2, x_3$).
- **Restricciones holónomas:** 0.
- **Grados de libertad:**
  
$$
N = 3 - 0 = 3
$$

- **Coordenadas generalizadas:** $q_1 = x_1, q_2 = x_2, q_3 = x_3$ [Wells, Cap. 2; Goldstein, Cap. 6].

---

### 3. Resortes y amortiguadores equivalentes

1. **Resortes en serie entre bloque 1 y bloque 3 ($k_{13}$):** [Wells, Cap. 5]
   
$$
\frac{1}{k_{13}} = \frac{1}{k_a} + \frac{1}{k_b} = \frac{1}{2} + \frac{1}{3} = \frac{5}{6} \implies k_{13} = \frac{6}{5} = 1.2
$$


2. **Amortiguadores en serie entre bloque 2 y bloque 3 ($c_{23}$):** [Wells, Cap. 6]
   
$$
\frac{1}{c_{23}} = \frac{1}{c_a} + \frac{1}{c_b} = \frac{1}{2} + \frac{1}{2} = 1 \implies c_{23} = 1
$$


3. **Resortes en paralelo entre pared y bloque 2 ($k_{20}$):** [Wells, Cap. 5]
   
$$
k_{20} = k_{p1} + k_{p2} = 1 + 2 = 3
$$


---

### 4. $T$, $V$ y $P$ por separado

- **Energía cinética ($T$):** [Goldstein, Cap. 6; Taylor, Cap. 11]
  
$$
T = \frac{1}{2} m_1 \dot{x}_1^2 + \frac{1}{2} m_2 \dot{x}_2^2 + \frac{1}{2} m_3 \dot{x}_3^2 = \frac{1}{2} (2) \dot{x}_1^2 + \frac{1}{2} (3) \dot{x}_2^2 + \frac{1}{2} (2) \dot{x}_3^2 = \dot{x}_1^2 + \frac{3}{2} \dot{x}_2^2 + \dot{x}_3^2
$$


- **Energía potencial ($V$):** [Goldstein, Cap. 6; Wells, Cap. 5]
  Medida respecto a la posición de equilibrio estático ($\mathbf{x} = \mathbf{0}$):
  
$$
V = \frac{1}{2} k_{10} x_1^2 + \frac{1}{2} k_{20} x_2^2 + \frac{1}{2} k_{12} (x_2 - x_1)^2 + \frac{1}{2} k_{13} (x_3 - x_1)^2
$$

  Sustituyendo los valores de rigidez equivalente:
  
$$
V = \frac{1}{2} (2) x_1^2 + \frac{1}{2} (3) x_2^2 + \frac{1}{2} (3) (x_2 - x_1)^2 + \frac{1}{2} (1.2) (x_3 - x_1)^2
$$


- **Función de disipación de Rayleigh ($P$):** [Goldstein, Cap. 1, Ec. 1.67; Wells, Cap. 6, Ec. 6.16]
  Para fricción viscosa lineal ($n=1$):
  
$$
P = \frac{1}{2} c_{10} \dot{x}_1^2 + \frac{1}{2} c_{12} (\dot{x}_2 - \dot{x}_1)^2 + \frac{1}{2} c_{23} (\dot{x}_3 - \dot{x}_2)^2
$$

  Sustituyendo los coeficientes equivalentes:
  
$$
P = \frac{1}{2} (3) \dot{x}_1^2 + \frac{1}{2} (4) (\dot{x}_2 - \dot{x}_1)^2 + \frac{1}{2} (1) (\dot{x}_3 - \dot{x}_2)^2
$$


---

### 5. Derivadas de Lagrange
Aplicando la ecuación extendida de Lagrange para sistemas disipativos [Goldstein, Cap. 1, Ec. 1.70]:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}_i}\right) - \frac{\partial T}{\partial x_i} + \frac{\partial V}{\partial x_i} + \frac{\partial P}{\partial \dot{x}_i} = Q_i, \qquad (i=1, 2, 3)
$$


#### **Para la coordenada $x_1$:**
- $\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}_1}\right) = 2 \ddot{x}_1$, $\quad \frac{\partial T}{\partial x_1} = 0$
- $\frac{\partial V}{\partial x_1} = 2 x_1 - 3 (x_2 - x_1) - 1.2 (x_3 - x_1) = 6.2 x_1 - 3 x_2 - 1.2 x_3$
- $\frac{\partial P}{\partial \dot{x}_1} = 3 \dot{x}_1 - 4 (\dot{x}_2 - \dot{x}_1) = 7 \dot{x}_1 - 4 \dot{x}_2$
- $Q_1 = 0$

#### **Para la coordenada $x_2$:**
- $\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}_2}\right) = 3 \ddot{x}_2$, $\quad \frac{\partial T}{\partial x_2} = 0$
- $\frac{\partial V}{\partial x_2} = 3 x_2 + 3 (x_2 - x_1) = -3 x_1 + 6 x_2$
- $\frac{\partial P}{\partial \dot{x}_2} = 4 (\dot{x}_2 - \dot{x}_1) - 1 (\dot{x}_3 - \dot{x}_2) = -4 \dot{x}_1 + 5 \dot{x}_2 - \dot{x}_3$
- $Q_2 = F(t)$

#### **Para la coordenada $x_3$:**
- $\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{x}_3}\right) = 2 \ddot{x}_3$, $\quad \frac{\partial T}{\partial x_3} = 0$
- $\frac{\partial V}{\partial x_3} = 1.2 (x_3 - x_1) = -1.2 x_1 + 1.2 x_3$
- $\frac{\partial P}{\partial \dot{x}_3} = 1 (\dot{x}_3 - \dot{x}_2) = -\dot{x}_2 + \dot{x}_3$
- $Q_3 = 0$

---

### 6. EDO final (modelo matemático matricial)
Ensamblando en la forma matricial $\mathbf{M} \ddot{\mathbf{x}} + \mathbf{C} \dot{\mathbf{x}} + \mathbf{K} \mathbf{x} = \mathbf{F}$ [Goldstein, Cap. 6; Taylor, Cap. 11]:


$$
\begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{bmatrix} \begin{bmatrix} \ddot{x}_1 \\ \ddot{x}_2 \\ \ddot{x}_3 \end{bmatrix} + \begin{bmatrix} 7 & -4 & 0 \\ -4 & 5 & -1 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \\ \dot{x}_3 \end{bmatrix} + \begin{bmatrix} 6.2 & -3 & -1.2 \\ -3 & 6 & 0 \\ -1.2 & 0 & 1.2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ F(t) \\ 0 \end{bmatrix}
$$


O con la matriz $\mathbf{K}$ en fracciones exactas:

$$
\mathbf{K} = \begin{bmatrix} \dfrac{31}{5} & -3 & -\dfrac{6}{5} \\[6pt] -3 & 6 & 0 \\[6pt] -\dfrac{6}{5} & 0 & \dfrac{6}{5} \end{bmatrix}
$$


---

### 7. Tratamiento del término constante $k \cdot l_0$ en $F_R = k(x - l_0)$
1. **Fuerza y potencial absolutos:** Para un resorte de constante $k$ y longitud libre sin deformar $l_0$, la fuerza elástica es $F_R = -k(x_{abs} - l_0)$, la cual proviene de un potencial de la forma $V_{abs} = \frac{1}{2}k(x_{abs} - l_0)^2$ [Wells, Cap. 3].
2. **Equilibrio estático:** Al definir las coordenadas $x_i$ como **desplazamientos dinámicos incrementales** respecto a la posición de equilibrio estático $\mathbf{x}_{eq}$ (es decir, $x_{abs,i} = x_{eq,i} + x_i$), las fuerzas de pretensión constantes $\sum \pm k_j l_{0,j}$ se equilibran exactamente con las reacciones estáticas del sistema [Taylor, Cap. 11].
3. **Cancelación en las ecuaciones de movimiento:** En el punto de equilibrio estático $\mathbf{x} = \mathbf{0}$, la condición de mínimo o estado de reposo impone que $\left.\frac{\partial V_{abs}}{\partial x_i}\right|_{\mathbf{0}} = 0$. Al desarrollar la energía potencial incremental alrededor del equilibrio, los términos lineales que contienen $k \cdot l_0$ se anulan idénticamente con las fuerzas estáticas de pretensión.
4. **Conclusión:** La energía potencial relevante para la dinámica reduce a una **forma cuadrática pura** $V = \frac{1}{2} \mathbf{x}^T \mathbf{K} \mathbf{x}$. Por esta razón, el término constante $k \cdot l_0$ no afecta las derivadas restauradoras dinámicas y **no aparece en las matrices $\mathbf{M}, \mathbf{C}, \mathbf{K}$**.

---

### 8. Verificación

#### **Análisis dimensional:**
- Matriz de masa: $[M_{ij}] = \text{kg}$.
- Matriz de amortiguamiento: $[C_{ij}] = \text{kg/s}$.
- Matriz de rigidez: $[K_{ij}] = \text{N/m} = \text{kg/s}^2$.
- Términos de la EDO: $[\mathbf{M}\ddot{\mathbf{x}}] = [\mathbf{C}\dot{\mathbf{x}}] = [\mathbf{K}\mathbf{x}] = \text{kg}\cdot\text{m/s}^2 = \text{N}$ (todos homogéneos en unidades de fuerza).

#### **Propiedades de las matrices:**
- $\mathbf{M}$ es diagonal, simétrica y definida positiva ($\det \mathbf{M} = 12 > 0$).
- $\mathbf{C}$ es simétrica y definida positiva ($\det \mathbf{C} = 12 > 0$).
- $\mathbf{K}$ es simétrica y definida positiva ($\det \mathbf{K} = 25.2 > 0$).

---

### Resultado final

$$
\begin{aligned}
1.\quad & k_{13} = \frac{6}{5} = 1.2, \qquad c_{23} = 1, \qquad k_{20} = 3 \\
2.\quad & \mathbf{M} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{bmatrix}, \qquad \mathbf{C} = \begin{bmatrix} 7 & -4 & 0 \\ -4 & 5 & -1 \\ 0 & -1 & 1 \end{bmatrix}, \qquad \mathbf{K} = \begin{bmatrix} 6.2 & -3 & -1.2 \\ -3 & 6 & 0 \\ -1.2 & 0 & 1.2 \end{bmatrix} \\
& \mathbf{M}\ddot{\mathbf{x}} + \mathbf{C}\dot{\mathbf{x}} + \mathbf{K}\mathbf{x} = \begin{bmatrix} 0 \\ F(t) \\ 0 \end{bmatrix} \\
3.\quad & \text{El término } k\cdot l_0 \text{ se cancela con las reacciones estáticas de pretensión en la posición de equilibrio,} \\
& \text{por lo que no altera la matriz de rigidez } \mathbf{K} \text{ ni aparece en el modelo dinámico alrededor del equilibrio.}
\end{aligned}
$$


---

**Dudas o supuestos:** Se supone que todas las oscilaciones son de pequeña amplitud alrededor de la posición de equilibrio estático y que los elementos disipativos son puramente viscosos lineales ($n=1$).

💡 ¿Te gustaría calcular los modos normales y frecuencias naturales del sistema o determinar la función de transferencia del bloque 2 ante la fuerza $F(t)$?
