En la obra de **James Stewart, 9na Edición (Calculus: Early Transcendentals)**, la cobertura de los temas solicitados en el **Capítulo 3** es la siguiente:

### 1. Teorema de Leibniz para la derivada $n$-ésima de un producto

El **Capítulo 3** no incluye el "Teorema de Leibniz" como un cuerpo teórico formal para la $n$-ésima derivada de un producto de dos funciones generales $u$ y $v$.

- **En la teoría:** La Sección 3.2 introduce la **Regla del Producto** únicamente para la primera derivada ($f \cdot g$).
- **Aplicación específica:** En la Sección 3.2, **Ejemplo 1(b)**, se pide hallar la $n$-ésima derivada de una función específica, $f(x) = xe^x$, mediante la observación de un patrón recurrente, obteniendo $f^{(n)}(x) = (x + n)e^x$, pero sin generalizar la fórmula de Leibniz para cualquier producto.
- **En ejercicios (Stewart 7ma Ed):** Se aborda de forma inductiva en el **Ejercicio 60 de la Sección 3.2**, donde se pide demostrar la fórmula para $F''$ y hallar las de $F'''$ y $F^{(4)}$ para un producto $f(x)g(x)$.
- **Ubicación en otros textos:** Si buscas la formulación general $(uv)^{(n)} = \sum \binom{n}{k} u^{(n-k)} v^{(k)}$, esta aparece explícitamente en **Piskunov Cap. 3.22** y en **Maron Cap. 2.3**.

### 2. Derivación en notación paramétrica

La derivación de funciones definidas paramétricamente **no se cubre en el Capítulo 3**. Este tema se desarrolla extensamente más adelante:

- **Ubicación:** **Capítulo 10, Sección 10.2** ("Calculus with Parametric Curves" / "Cálculo con curvas paramétricas").
- **Contenido:** En esta sección se deriva la fórmula fundamental para la pendiente de la recta tangente: $$\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} \quad \text{si } \frac{dx}{dt} \neq 0$$.
- **Derivadas superiores:** El cálculo de la segunda derivada paramétrica ($\frac{d^2y}{dx^2}$) también se explica en esta sección mediante la aplicación de la regla de la cadena.

**Resumen de ubicación en Stewart 9na Ed:**

|Tema|¿Está en Cap. 3?|Sección / Capítulo correcto|
|:--|:--|:--|
|**Teorema de Leibniz ($n$-ésima)**|No (solo inducción en patrones)|Ejercicios de Sec. 3.2 o ver Piskunov Sec. 3.22.|
|**Derivación paramétrica**|No|**Sección 10.2**|

> [!note] Para la **derivación implícita**, que a veces se confunde con la paramétrica, Stewart sí la cubre en la **Sección 3.5** del mismo Capítulo 3.

En resumen, mientras que la base de la regla de Leibniz está en la **Sección 3.2** (como ejercicio de descubrimiento), la derivación paramétrica debe buscarse en la **Sección 10.2**.