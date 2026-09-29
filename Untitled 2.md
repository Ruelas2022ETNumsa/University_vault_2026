Para resolver este ejercicio de ingeniería de tráfico telefónico, aplicaremos las fórmulas de análisis y dimensionamiento presentes en las guías de la asignatura.

En los temas abordados, cuando la tasa total de llegada de llamadas $\lambda$ se especifica como un valor constante e independiente del número de fuentes activas (en este caso 3000 llamadas/hora), el sistema se modela habitualmente con la **Distribución de Erlang B** (llegadas Poisson). No obstante, también desarrollaremos el **Modelo de Engset** (fuentes finitas $F = 100$) como enfoque comparativo.

---

### **Datos del Problema**
- **Número de canales de comunicación ($N$):** $4\text{ canales}$
- **Número de fuentes de tráfico ($F$):** $100\text{ fuentes}$
- **Tasa de llegada de llamadas ($\lambda$):** $3000\text{ llamadas/hora}$
- **Tiempo medio de ocupación ($\bar{t}$):** $5\text{ segundos}$

---

### **MODELO PRINCIPAL: Fórmula de Erlang B**
*(Tasa total de llegada constante $\lambda$)*

#### **e) Tráfico ofrecido al sistema (en Erlangs)**
*(Se determina primero para construir la función de probabilidad $P(j)$)*:

$$
A = \lambda \cdot \bar{t} = 3000 \frac{\text{llamadas}}{\text{hora}} \times \frac{1\text{ hora}}{3600\text{ s}} \times 5\text{ s} = \mathbf{4,1667\text{ Erlangs}} \quad \left(\frac{25}{6}\text{ Erl}\right)
$$


#### **a) Expresión general de la probabilidad de estado $P(j)$**
La fórmula general de la probabilidad de estado $P(j)$ para Erlang B es:

$$
P(j) = \frac{\frac{A^j}{j!}}{\sum_{k=0}^{N} \frac{A^k}{k!}}
$$


Sustituyendo $A = 4,1667$ y $N = 4$, calculamos la suma del denominador ($D$):

$$
D = \frac{4,1667^0}{0!} + \frac{4,1667^1}{1!} + \frac{4,1667^2}{2!} + \frac{4,1667^3}{3!} + \frac{4,1667^4}{4!}
$$


$$
D = 1 + 4,1667 + 8,6806 + 12,0563 + 12,5587 = \mathbf{38,4622}
$$


Por lo tanto, la **expresión general** es:

$$
P(j) = \frac{\frac{(4,1667)^j}{j!}}{38,4622}
$$


#### **b) Probabilidades de estado del sistema $P(0), P(1), P(2), P(3), P(4)$**
- **$P(0)$:** \(\frac{1}{38,4622} = \mathbf{0,02600} \quad (\mathbf{2,600\%})\]
- **$P(1)$:** \(\frac{4,1667}{38,4622} = \mathbf{0,10833} \quad (\mathbf{10,833\%})\]
- **$P(2)$:** \(\frac{8,6806}{38,4622} = \mathbf{0,22569} \quad (\mathbf{22,569\%})\]
- **$P(3)$:** \(\frac{12,0563}{38,4622} = \mathbf{0,31346} \quad (\mathbf{31,346\%})\]
- **$P(4)$:** \(\frac{12,5587}{38,4622} = \mathbf{0,32652} \quad (\mathbf{32,652\%})\]

#### **c) Congestión en el tiempo ($E$)**
Es la probabilidad de que todos los canales ($N = 4$) estén ocupados:

$$
E = P(N) = P(4) = \mathbf{0,32652} \quad (\mathbf{32,652\%})
$$


#### **d) Congestión en las llamadas ($B$)**
En el modelo Erlang B (proceso Poisson), la congestión en las llamadas coincide con la congestión en el tiempo:

$$
B = E = \mathbf{0,32652} \quad (\mathbf{32,652\%})
$$


#### **e) Tráfico ofrecido ($A$)**

$$
A = \mathbf{4,1667\text{ Erlangs}}
$$


#### **f) Tráfico cursado por el sistema ($A^l$)**

$$
A^l = A(1 - B) = 4,1667 \times (1 - 0,32652) = \mathbf{2,8062\text{ Erlangs}}
$$


#### **g) Tráfico rechazado ($M$)**

$$
M = A - A^l = A \cdot B = 4,1667 \times 0,32652 = \mathbf{1,3605\text{ Erlangs}}
$$


#### **h) Número de llamadas rechazadas durante una hora ($NLLP$)**

$$
NLLP = \frac{M \times 3600}{\bar{t}} = \frac{1,3605 \times 3600}{5} = \mathbf{979,56\text{ llamadas/hora}} \quad (\approx \mathbf{980\text{ llamadas}})
$$


---

### **MODELO ALTERNATIVO: Modelo de Engset**
*(Considerando la restricción de fuentes finitas $F = 100$)*

Si calculamos la tasa de llegada por fuente libre $a = \frac{\lambda}{F} = \frac{3000}{100} = 30\text{ llam/h/fuente} = \frac{1}{120}\text{ llam/s}$, el tráfico por fuente libre es $b = a \cdot \bar{t} = \frac{1}{120} \times 5 = \mathbf{0,041667\text{ Erlangs}}$.

1. **Expresión general $P(j)$:** $P(j) = \frac{\binom{100}{j} (0,041667)^j}{\sum_{i=0}^4 \binom{100}{i} (0,041667)^i}$
2. **Probabilidades de estado:**
   - **$P(0)$:** **$0,02683$** $2,683%$
   - **$P(1)$:** **$0,11178$** $11,178%$
   - **$P(2)$:** **$0,23054$** $23,054%$
   - **$P(3)$:** **$0,31379$** $31,379%$
   - **$P(4)$:** **$0,31706$** $31,706%$
3. **Congestión en el tiempo ($E$):** $E = P(4) = \mathbf{0,31706}\quad (\mathbf{31,706\%})$
4. **Congestión en las llamadas ($B$):**
   
$$
B = \frac{\binom{99}{4} (0,041667)^4}{\sum_{j=0}^4 \binom{99}{j} (0,041667)^j} = \mathbf{0,31309}\quad (\mathbf{31,309\%})
$$

5. **Tráfico cursado ($A^l$):** $A^l = \frac{F \cdot b (1 - B)}{1 + b(1 - B)} = \mathbf{2,7825\text{ Erlangs}}$
6. **Tráfico ofrecido ($A$):** $A = \frac{A^l}{1 - B} = \mathbf{4,0507\text{ Erlangs}}$
7. **Tráfico rechazado ($M$):** $M = A - A^l = \mathbf{1,2682\text{ Erlangs}}$
8. **Llamadas rechazadas/hora ($NLLP$):** $NLLP = \frac{M \times 3600}{\bar{t}} = \mathbf{913,14\text{ llamadas/hora}}$

---

📊 ¿Te gustaría calcular la carga individual por canal $a(j)$ o el factor de mejoría de este sistema?
