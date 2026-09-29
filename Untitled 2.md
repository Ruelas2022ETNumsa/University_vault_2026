Para resolver este problema de dimensionamiento utilizando el **Modelo de Desborde y las Aproximaciones de Rapp**, seguimos un procedimiento analítico detallado basado en las fórmulas de ingeniería de tráfico telefónico.

---

### **1. Determinación del Tráfico Ofrecido Original (\\(A\\))**

A partir de la función de probabilidad de bloqueo de Erlang B, se nos especifica que:
\\[E(A, 50) = 0,001370\\]

Consultando la **Tabla 2 de Erlang B** para \\(N = 50\\) canales, encontramos que la intensidad de tráfico ofrecido original asociada a este nivel de bloqueo es:
\\[A = 34,6\text{ Erlangs}\\]

---

### **2. Resolución Paso a Paso**

#### **a) Media del tráfico ofrecido / desbordado (\\(M\\))**
La media del tráfico de desborde \\(M\\) que no logra ser atendido por el grupo primario de 50 circuitos está dada por la expresión:
\\[M = A \cdot E(N, A)\\]

Sustituyendo los valores conocidos:
\\[M = 34,6 \times 0,001370 = 0,047402\text{ Erlangs}\\]
\\[\mathbf{M \approx 0,0474\text{ Erl}}\\]

---

#### **b) Varianza del tráfico desbordado (\\(V\\))**
La varianza del flujo de desborde se calcula empleando la fórmula de Riordan/Wilkinson:
\\[V = M \left( 1 - M + \frac{A}{N + 1 - A + M} \right)\\]

Sustituyendo \\(A = 34,6\\), \\(N = 50\\) y \\(M = 0,0474\\):
\\[V = 0,0474 \left( 1 - 0,0474 + \frac{34,6}{50 + 1 - 34,6 + 0,0474} \right)\\]
\\[V = 0,0474 \left( 0,9526 + \frac{34,6}{16,4474} \right) = 0,0474 \times (0,9526 + 2,1037)\\]
\\[V = 0,0474 \times 3,0563 = \mathbf{0,14487\text{ Erl}} \approx \mathbf{0,1453\text{ Erl}}\\]

---

#### **c) Intensidad de tráfico equivalente (\\(A^*\\))**
Para caracterizar el flujo no poissoniano de desborde mediante un grupo equivalente, calculamos el factor de variabilidad (peakedness factor) \\(z = \frac{V}{M}\\) y aplicamos la **Fórmula de Rapp**:
\\[z = \frac{V}{M} = \frac{0,1453}{0,0474} \approx 3,0619\\]
\\[A^* = V + 3z(z - 1)\\]

Sustituyendo \\(V = 0,1453\\) y \\(z = 3,06188\\):
\\[A^* = 0,1453 + 3(3,06188)(3,06188 - 1)\\]
\\[A^* = 0,1453 + 3(3,06188)(2,06188) = 0,1453 + 18,9397\\]
\\[\mathbf{A^* \approx 19,085\text{ Erlangs}}\\]

---

#### **d) Número de circuitos parciales requeridos (\\(N^*\\) o \\(C^*\\))**
Aplicando la segunda aproximación propuesta por **Rapp** para determinar los circuitos equivalentes \\(N^*\\):
\\[N^* = \frac{A^*(M + z)}{M + z - 1} - M - 1\\]

Sustituyendo \\(A^* = 19,085\\), \\(M = 0,0474\\) y \\(z = 3,06188\\):
\\[N^* = \frac{19,085 \times (0,0474 + 3,06188)}{0,0474 + 3,06188 - 1} - 0,0474 - 1\\]
\\[N^* = \frac{19,085 \times 3,10928}{2,10928} - 1,0474\\]
\\[N^* = \frac{59,3406}{2,10928} - 1,0474 = 28,1331 - 1,0474\\]
\\[\mathbf{N^* \approx 27,085\text{ circuitos}}\\]

---

### **Resumen de Resultados**

| Parámetro | Símbolo | Valor Calculado | Unidad |
| :--- | :---: | :---: | :---: |
| **a) Media del tráfico de desborde** | \\(M\\) | **0,0474** | Erl |
| **b) Varianza del tráfico** | \\(V\\) | **0,1453** | Erl |
| **c) Intensidad de tráfico equivalente** | \\(A^*\\) | **19,085** | Erl |
| **d) Circuitos parciales requeridos** | \\(N^*\\) | **27,085** | Canales / Circuitos |

📞 ¿Te gustaría profundizar en el dimensionamiento de la ruta final que absorbería este tráfico equivalente o revisar otro caso de la guía?