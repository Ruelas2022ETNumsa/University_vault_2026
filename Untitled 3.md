# Enunciados ETN607 — Sistemas disipativos (fricción)

> Cada enunciado es independiente: se puede pegar uno solo en NotebookLM.
> Método esperado: ecuaciones de Lagrange con función de disipación P (ver instrucciones del cuaderno).
> Fricción: f = c·vⁿ, opuesta al movimiento. Gravedad g. Ejes: x horizontal, y vertical, salvo que se indique otra cosa.

---

## Enunciado 1 (ej1T5) — Tiro balístico con fricción cuadrática

Una partícula de masa m se lanza en el plano vertical (x, y) y se mueve bajo la gravedad (y positiva hacia arriba). Sobre ella actúa una fricción del aire cuadrática, f = c·v², con v² = ẋ² + ẏ², siempre opuesta a la velocidad (n = 2).

**Se pide:**
1. Grados de libertad N y coordenadas generalizadas.
2. T, V y P.
3. Las ecuaciones de movimiento de x(t) e y(t) mediante Lagrange.
4. Verificar que con c = 0 se recupera el tiro parabólico sin fricción.

---

## Enunciado 2 (ej2T5) — Partícula sobre una barra parabólica

Una partícula de masa m se mueve obligada sobre una barra con forma de parábola y = 4x², en un plano vertical (y positiva hacia arriba, gravedad g). Entre la partícula y la barra hay fricción viscosa lineal, f = c·v (n = 1).

**Se pide:**
1. Grados de libertad N y la coordenada generalizada elegida (la restricción reduce N de 2 a 1).
2. ẏ en función de x y ẋ.
3. T, V y P en función de x y ẋ.
4. La EDO de movimiento (modelo matemático) mediante Lagrange.

---

## Enunciado 3 (ej3T5) — Péndulo simple con fricción viscosa

Una masa puntual m cuelga de una varilla rígida sin masa de longitud l, articulada en un punto fijo. El péndulo oscila en un plano vertical, con ángulo θ medido desde la vertical (y positiva hacia abajo). Hay fricción viscosa lineal, f = c·v (n = 1), sobre la masa.

**Se pide:**
1. N y coordenada generalizada (en polares, r = l y ṙ = 0).
2. T, V y P.
3. La EDO de movimiento (no lineal) mediante Lagrange.
4. Linealizar para ángulos pequeños.
5. Pasar a espacio de estados con u₁ = θ y u₂ = θ̇, y escribir la forma matricial u̇ = A·u + F.
6. Verificación dimensional del coeficiente de fricción en la ecuación final.

---

## Enunciado 4 (ej4T5) — Poleas, resorte y cables (sistema no inercial)

Entre el techo y el piso hay una distancia H. Del techo cuelga un **resorte** (constante k, longitud natural l₀) que sostiene la **polea 1**. Se miden hacia abajo desde el techo las posiciones y₁ (polea 1), y₂ (polea 2) e y₃ (masa 3).

- Un **cable 1** (longitud l₁) parte de un punto fijo del piso, sube, rodea la polea 1 (radio R₁, media vuelta) y baja hasta sostener el centro de la **polea 2**.
- Un **cable 2** (longitud l₂) parte de otro punto fijo del piso, sube, rodea la polea 2 (radio R₂, media vuelta) y baja una distancia a hasta sostener la **masa 3**, de modo que a = y₃ − y₂.

Las masas de la polea 1, la polea 2 y el bloque 3 son m₁, m₂ y m₃. Las poleas tienen momento de inercia nulo (I₁ = I₂ = 0). Los cables son inextensibles y sin masa. Cada masa sufre fricción viscosa lineal (n = 1) con coeficientes c₁, c₂ y c₃ respectivamente.

**Se pide:**
1. N = (cantidad de masas) − (cantidad de cables); elegir la coordenada generalizada (se sugiere a).
2. Las ecuaciones de restricción de cada cable.
3. y₁, y₂, y₃ y sus velocidades en función de a y ȧ.
4. T, V y P.
5. La EDO de movimiento en a mediante Lagrange.

---

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

## Enunciado 7 (ej7T5) — Doble péndulo con fricción

Dos masas puntuales m₁ y m₂ forman un doble péndulo plano. La masa 1 cuelga de un punto fijo mediante una varilla rígida sin masa de longitud l; la masa 2 cuelga de la masa 1 mediante otra varilla de longitud l. Los ángulos θ₁ y θ₂ se miden desde la vertical (y positiva hacia abajo), cada uno respecto de su propia vertical local. Hay fricción en cada masa, proporcional a la velocidad de esa masa, con coeficientes c₁ (masa 1) y c₂ (masa 2).

**Se pide:**
1. N y coordenadas generalizadas.
2. Posición y velocidad de cada masa.
3. T, V y P (n = 1).
4. Las dos EDO acopladas mediante Lagrange.
5. Verificar el caso límite c₁ = c₂ = 0.
6. Opcional: obtener las ecuaciones con MATLAB simbólico (+15 pts).

---

## Enunciado 8 (ej8T5) — Péndulo que se desenrolla de un cilindro fijo

Un cilindro fijo de radio R tiene un hilo inextensible y sin masa enrollado en su superficie. Del extremo libre del hilo cuelga una masa m. El origen está en el centro del cilindro, con x horizontal y y vertical hacia abajo. En θ = 0 el hilo sale tangente al cilindro en el punto (R, 0) y cuelga vertical con una longitud libre l. Al girar un ángulo θ, la parte libre del hilo (tangente al cilindro) mide d = l + R·θ. Hay fricción en la masa, f = c·vⁿ.

**Se pide:**
1. N y coordenada generalizada.
2. Posición (x, y) y velocidad de la masa en función de θ y θ̇.
3. T y V.
4. P para n = 1 y para n = 2.
5. La EDO de movimiento para n = 2 mediante Lagrange; indicar cómo cambia para n = 1.
