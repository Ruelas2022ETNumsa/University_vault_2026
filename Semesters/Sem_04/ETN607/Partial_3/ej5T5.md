## Enunciado 5 (ej5T5) — Cuña y bloque con tres fricciones

Dentro de un recinto de ancho d hay dos cuerpos:

- El **cuerpo 1** (masa m₁) se mueve **solo en vertical**, guiado por la pared izquierda. Su punta toca la cuña a una distancia horizontal fija B de la pared izquierda, y su altura sobre el piso es y₁ (positiva hacia arriba).
- El **cuerpo 2** (masa m₂) es una cuña de ángulo α y base horizontal b que se mueve **solo en horizontal** sobre el piso. Su esquina inferior izquierda está a la distancia x₂ del origen (esquina inferior izquierda del recinto). La cuña está unida a la pared derecha por un resorte de constante k, con longitud d − x₂ − b y longitud natural nula.

El cuerpo 1 apoya sobre la cara inclinada de la cuña. Hay tres fricciones viscosas lineales (n = 1):
- c₁: entre el cuerpo 1 y la pared izquierda.
- c₂: entre la cuña y el piso.
- c₃: entre el cuerpo 1 y la cuña, en la cara inclinada.

**Se pide:**
1. N y coordenada generalizada (se sugiere y₁).
2. La ecuación de restricción que relaciona x₂ con y₁.
3. T, V y P en función de y₁ y ẏ₁. Justificar qué velocidad relativa interviene en la fricción c₃.
4. La EDO de movimiento mediante Lagrange.

---

### Solución

**1. N y coordenada**

Coordenadas $(y_1, x_2)$ con 1 restricción de contacto.

$$
N = 2 - 1 = 1, \qquad q = y_1
$$

**2. Restricción**

$$
\tan\alpha = \frac{y_1}{B - x_2} \;\Rightarrow\; x_2 = B - \frac{y_1}{\tan\alpha} = B - y_1\cot\alpha, \qquad \dot{x}_2 = -\dot{y}_1\cot\alpha
$$

**3. T, V, P**

$$
T = \frac{m_1}{2}\dot{y}_1^2 + \frac{m_2}{2}\dot{x}_2^2 = \frac{1}{2}\left(m_1 + m_2\cot^2\alpha\right)\dot{y}_1^2
$$

$$
V = m_1 g y_1 + \frac{k}{2}(d - x_2 - b)^2 = m_1 g y_1 + \frac{k}{2}\left[(d - B - b) + y_1\cot\alpha\right]^2
$$

La fricción $c_3$ depende de la velocidad **relativa** entre los cuerpos en la cara inclinada (su módulo, no la suma de componentes):

$$
\vec{v}_{rel} = \vec{v}_1 - \vec{v}_2 = (\dot{y}_1\cot\alpha,\; \dot{y}_1) \;\Rightarrow\; v_{rel}^2 = \dot{y}_1^2\left(1 + \cot^2\alpha\right) = \frac{\dot{y}_1^2}{\sin^2\alpha}
$$

$$
P_{n=1} = \frac{c_1}{2}\dot{y}_1^2 + \frac{c_2}{2}\dot{x}_2^2 + \frac{c_3}{2}v_{rel}^2 = \frac{1}{2}\left(c_1 + c_2\cot^2\alpha + \frac{c_3}{\sin^2\alpha}\right)\dot{y}_1^2
$$

**4. Lagrange**

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{y}_1}\right) - \frac{\partial T}{\partial y_1} = -\frac{\partial V}{\partial y_1} - \frac{\partial P}{\partial \dot{y}_1}
$$

$$
\frac{\partial T}{\partial y_1} = 0, \qquad \frac{\partial V}{\partial y_1} = m_1 g + k\cot\alpha\left[(d - B - b) + y_1\cot\alpha\right]
$$

$$
\frac{\partial P}{\partial \dot{y}_1} = \left(c_1 + c_2\cot^2\alpha + \frac{c_3}{\sin^2\alpha}\right)\dot{y}_1
$$

**5. Verificación**

Con $c_i = 0$ queda un oscilador conservativo de 1 GDL. Válido solo con contacto: $0 \le y_1 \le b\tan\alpha$.

---

### Resultado final

$$
\boxed{\;\left(m_1 + m_2\cot^2\alpha\right)\ddot{y}_1 + \left(c_1 + c_2\cot^2\alpha + \frac{c_3}{\sin^2\alpha}\right)\dot{y}_1 + k\cot^2\alpha\; y_1 + m_1 g + k(d - B - b)\cot\alpha = 0\;}
$$
