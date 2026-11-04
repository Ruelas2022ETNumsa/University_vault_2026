# E1P4 — Circuito con R₁: sistema mecánico equivalente

## Enunciado

Hallar el sistema mecánico equivalente del circuito, que tiene una resistencia R₁ en serie con la fuente principal.

**Figura:** (dibujar a mano)

---

## Solución por pasos

### Paso 1. Análisis de inductancias y fuentes compartidas (circuito original)

**Mallas** (N = 3 grados de libertad):
- **Malla 1:** P-A-B-D-Q. Contiene E₁, R₁, L₁, L₁₂ y L₁₃ con E₁₃.
- **Malla 2:** A-B-C. Contiene L₁₂, C₂₃ y R₂₃, y C₂.
- **Malla 3:** B-C-D. Contiene C₂₃ y R₂₃, R₃, y L₁₃ con E₁₃.

| Elemento | Rama | Mallas | ¿Compartido? |
|---|---|---|---|
| E₁ | P–Q | 1 | No |
| L₁ | P–A | 1 | No |
| L₁₂ | A–B (izquierda arriba) | 1 y 2 | **Sí** |
| L₁₃ | B–D (izquierda abajo) | 1 y 3 | **Sí** |
| E₁₃ | B–D (izquierda abajo) | 1 y 3 | **Sí** |

**Conclusión:** L₁₂, L₁₃ y E₁₃ están compartidas, así que **se debe girar el circuito**. R₁ no influye en esta decisión.

### Paso 2. Giro del circuito

Se refleja el rombo de izquierda a derecha, con A arriba y D abajo. El vértice C pasa a la izquierda (el lado que toca la malla 1) y el vértice B a la derecha. El circuito exterior no cambia.

**Mallas luego del giro:**
- **Malla 1:** P-A-C-D-Q (es la única que cambia).
- **Malla 2:** A-B-C.
- **Malla 3:** B-C-D.

| Elemento | Rama | Mallas | ¿Compartido? |
|---|---|---|---|
| E₁ | P–Q | 1 | No |
| L₁ | P–A | 1 | No |
| L₁₂ | A–B | 2 | No |
| L₁₃ | B–D | 3 | No |
| E₁₃ | B–D | 3 | No |

Ya no hay inductancias ni fuentes compartidas. **El circuito se puede convertir.**

### Paso 3. Corrientes

Se definen tres corrientes en ramas independientes:
- **i₁:** de P hacia A, por L₁, R₁ y E₁.
- **i₂:** de A hacia C, por C₂.
- **i₃:** de C hacia D, por R₃.

El resto se obtiene con la LKC:
- **Nodo A:** entra i₁ y sale i₂ hacia C. Por A–B sale **i₁ − i₂**.
- **Nodo C:** entra i₂ y sale i₃ hacia D. Por la rama central C–B sale **i₂ − i₃**.
- **Nodo B:** entran (i₁ − i₂) y (i₂ − i₃). Por B–D sale **i₁ − i₃**.
- **Nodo D (verificación):** entran i₃ y (i₁ − i₃), suman i₁, que es la corriente que vuelve por Q–D.

**Corriente por elemento:**

| Elemento | Corriente |
|---|---|
| E₁, R₁, L₁ | i₁ |
| C₂ (A→C) | i₂ |
| R₃ (C→D) | i₃ |
| L₁₂ (A→B) | i₁ − i₂ |
| R₂₃ y C₂₃ (C→B, en serie) | i₂ − i₃ |
| L₁₃ y E₁₃ (B→D, en serie) | i₁ − i₃ |

### Paso 4. Sistema mecánico equivalente

**Cuerpos** (la corriente por la inductancia es la velocidad):
- **Cuerpo L₁** (masa L₁): velocidad v₁ = i₁.
- **Cuerpo L₂** (masa L₁₂): velocidad v₂ = i₁ − i₂.
- **Cuerpo L₃** (masa L₁₃): velocidad v₃ = i₁ − i₃.

**Fuerzas:**
- **F₁** (fuente E₁) sobre **L₁**.
- **F₁₃** (fuente E₁₃) sobre **L₃**.

**Elementos y la corriente que llevan:**

| Elemento | Se conecta entre | Corriente |
|---|---|---|
| Amortiguador **R₁** | L₁ y pared fija | i₁ = v₁ |
| Resorte **1/C₂** | L₁ y L₂ | i₂ = v₁ − v₂ |
| Amortiguador **R₃** | L₁ y L₃ | i₃ = v₁ − v₃ |
| Amortiguador **R₂₃** y resorte **1/C₂₃**, en paralelo | L₂ y L₃ | i₂ − i₃ = v₃ − v₂ |

**Conexiones por cuerpo** (de izquierda a derecha: pared, L₁, L₂, L₃):

- **Cuerpo L₁**
  - Izquierda: amortiguador **R₁** a la pared.
  - Derecha: amortiguador **R₃** al cuerpo L₃, resorte **1/C₂** al cuerpo L₂ y la fuerza **F₁** (fuente E₁).
- **Cuerpo L₂**
  - Izquierda: resorte **1/C₂** al cuerpo L₁.
  - Derecha: amortiguador **R₂₃** y resorte **1/C₂₃** (en paralelo) al cuerpo L₃.
- **Cuerpo L₃**
  - Izquierda: amortiguador **R₃** al cuerpo L₁, y **R₂₃** y **1/C₂₃** (en paralelo) al cuerpo L₂.
  - Derecha: la fuerza **F₁₃** de la fuente E₁₃.

L₂ y L₃ no tienen unión a la pared.

**Correspondencias:**

| Circuito | Sistema mecánico |
|---|---|
| Mallas 1, 2, 3 | Cuerpos L₁, L₂, L₃ |
| E₁ | Fuerza F₁ sobre L₁ |
| E₁₃ | Fuerza F₁₃ sobre L₃ |
| R₁ | Amortiguador entre L₁ y la pared |
| C₂ | Resorte 1/C₂ entre L₁ y L₂ |
| R₃ | Amortiguador R₃ entre L₁ y L₃ |
| R₂₃ y C₂₃ (serie) | Amortiguador R₂₃ y resorte 1/C₂₃ (paralelo) entre L₂ y L₃ |
