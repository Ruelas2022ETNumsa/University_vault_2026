# Analogía electromecánica (analogía de voltajes)

Los sistemas mecánicos son equivalentes a los circuitos eléctricos. En esta analogía la **fuerza** corresponde a un **voltaje**, así que cada malla del circuito corresponde a un cuerpo del sistema mecánico. Las ecuaciones de Lagrange sirven para resolver ambos sistemas.

---

## 1. Tabla de equivalencias

| Mecánico | Símbolo | Eléctrico | Símbolo |
|---|---|---|---|
| Fuerza | F | Fuente | V (o E) |
| Masa | M | Inductancia | L |
| Resorte | K | Capacitor | 1/C |
| Amortiguador | C | Resistencia | R |
| **Posición** | x | Carga | q |
| Velocidad | ẋ | **Corriente** | i |

El docente marca con asterisco la **posición** (mecánico) y la **corriente** (eléctrico). La coordenada generalizada del lado eléctrico es la carga q, y la corriente de malla es su derivada, i = q̇.

**Cuidado con las letras:** en el lado mecánico, C es la constante del amortiguador. En el lado eléctrico, C es la capacitancia y el resorte K corresponde a 1/C. El amortiguador mecánico corresponde a la resistencia R.

---

## 2. Leyes de cada elemento

| Tipo de fuerza | Mecánico | Eléctrico |
|---|---|---|
| Inercia (Newton) | F = m ẍ | V = L di/dt |
| Conservativa | F = K x | V = (1/C) ∫ i dt |
| Disipativa | F = C ẋ | V = R i |

---

## 3. Energías y función potencia en variables eléctricas

Con la analogía, las tres funciones de Lagrange quedan en función de la corriente i:

- **Energía cinética (inductancia):** T = (L/2) i²
- **Energía potencial (capacitor y fuente):** V = (1/2C) (∫ i dt)² + E ∫ i dt
- **Función potencia (resistencia):** P = (R/2) i²

---

## 4. Ecuación de Lagrange

**Ecuación original (mecánica):**

d/dt (∂T/∂q̇ᵣ) − ∂T/∂qᵣ = − ∂V/∂qᵣ − ∂P/∂q̇ᵣ

**Ecuación actualizada (circuitos):**

d/dt (∂T/∂iᵣ) = − ∂V/∂(∫ iᵣ dt) − ∂P/∂iᵣ

Como T depende solo de las corrientes y no de las cargas, desaparece el término ∂T/∂q de la ecuación original. Se plantea una ecuación por cada corriente de malla iᵣ.

---

## 5. Reglas para hallar equivalencias

- El **número de mallas** es igual a los **grados de libertad** (N).
- **No pueden existir inductancias ni fuentes compartidas** entre mallas. Inductancia es cuerpo y fuente es fuerza, y un cuerpo o una fuerza no se comparte. Si hay una compartida, se gira el circuito.
- Los capacitores y los resistores sí pueden ser compartidos. Un elemento compartido une los cuerpos de sus dos mallas.
- **Serie se vuelve paralelo y viceversa.** Ejemplo del docente: dos resortes K₂ en paralelo en el sistema mecánico aparecen como dos capacitores 1/K₂ en serie en el circuito.
- Las ecuaciones de continuidad (LKC en cada nodo) dan la corriente de cada elemento compartido en función de las corrientes de malla. Por ejemplo, i₁₂ = i₁ − i₂.

---

## 6. Leyes de Kirchhoff (apoyo)

- **LKC (nodo):** Σ i = 0. Las corrientes que entran son iguales a las que salen.
- **LKV (malla):** Σ V = 0. Los voltajes activos (fuentes) son iguales a los pasivos (caídas de tensión).
