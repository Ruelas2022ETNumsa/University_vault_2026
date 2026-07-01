# Guía de notación LaTeX para NotebookLM

Esta guía define la notación LaTeX usada en las notas de Cálculo I.
Al generar ecuaciones, seguir estos ejemplos exactamente.

---

## 1. Saltos de línea en desarrollos multilínea

Usar siempre `\\` (doble barra) para saltar de línea dentro de `\begin{array}`.
Nunca `\` simple — en Obsidian/KaTeX no produce salto de línea.

```latex
$$\begin{array}{rcl}
a \cdot 1 & = & a \cdot (1 + 0) \\
a & = & a \cdot 1 + a \cdot 0 \\
a + 0 & = & a + a \cdot 0 \\
0 & = & a \cdot 0
\end{array}$$
```

Alineación estándar: `{rcl}` — lado izquierdo · signo · lado derecho.

---

## 2. Fracciones

Usar siempre `\dfrac` en lugar de `\frac`.
`\frac` en display inline `$...$` se vuelve pequeño y difícil de leer.

```latex
$\dfrac{2}{4}$          ← correcto
$\frac{2}{4}$           ← evitar
```

---

## 3. Flechas de transición

Dos flechas con roles distintos:

```latex
ecuación_1 \longrightarrow ecuación_2
```
Indica que se realizó una operación y se pasa a la siguiente expresión.

```latex
\Rightarrow x = 2
```
Indica que se llegó a un resultado — parcial o final del ejercicio.

---

## 4. Cancelaciones

Tres comandos con significado distinto:

### `\bcancel` — eliminación completa
El valor se consume por completo. No queda resto.
Usado en restas donde dos términos iguales se anulan, o en divisiones donde el valor desaparece.

```latex
$x + \bcancel{2} - \bcancel{2} = 0$

$\dfrac{\bcancel{2}}{\bcancel{2}} = 1$
```

### `\cancel` — se consume pero deja resto
El valor se cancela pero la expresión origen aún tiene un excedente.

```latex
$x + \cancel{2} = \cancelto{\color{YellowOrange}2}{4}$
```
Aquí el 2 desaparece, pero el 4 no desaparece — se transforma en 2.

### `\cancelto` — transformación con nuevo valor
Muestra que una expresión se reemplaza por otro valor.
El nuevo valor aparece en color YellowOrange para distinguirlo.

```latex
$\dfrac{2}{\cancelto{\color{YellowOrange}2}{4}}$

$\dfrac{\bcancel{3} \cdot 5}{\cancelto{\color{YellowOrange}5}{15}}$
```

Regla: `\cancelto{\color{YellowOrange}nuevo\_valor}{expresión\_original}`

---

## 5. Sistema de colores

Usar siempre dentro de `\color{}` o `{\color{} contenido}`.

| Color | Comando | Uso |
|---|---|---|
| NavyBlue | `\color{NavyBlue}` | Valores intermedios que se usarán más adelante |
| TealBlue | `\color{TealBlue}` | Resultado final del desarrollo |
| YellowOrange | `\color{YellowOrange}` | Valor nuevo tras una cancelación o corrección |
| BrickRed | `\color{BrickRed}` | Error o término incorrecto señalado |
| RedOrange | `\color{RedOrange}` | Advertencia o caso especial |
| BlueGreen | `\color{BlueGreen}` | Definición o condición aplicada |
| Violet | `\color{Violet}` | Hipótesis o dato del enunciado destacado |
| OliveGreen | `\color{OliveGreen}` | Sustitución — reemplazo de variable por su valor |
| Mahogany | `\color{Mahogany}` | Condición de no existencia — restricción de dominio, denominador = 0 |

Notación estándar: `{\color{Color} contenido}` — llaves envolviendo todo el bloque.
Evitar `\color{Color}{contenido}` — menos robusto dentro de comandos anidados.

Ejemplos:

```latex
{\color{NavyBlue} m = 3}

{\color{TealBlue} x = 2}

{\color{BrickRed} \text{Error: no se puede dividir por cero}}

{\color{Violet} \text{Dato: } f(0) = 1}

{\color{OliveGreen} x = 2 \text{ sustituido en } f(x)}

{\color{Mahogany} x \neq 0}
```

Violeta y OliveGreen se usan únicamente como color de texto inline, no en cajas.

---

## 6. Cajas de resultado

Sistema de cajas con borde y texto del mismo color, fondo siempre blanco (`white`)
para que el color interno resalte de forma uniforme.

### Tipo A (TA) — Resultado final de un inciso
Usado cuando el ejercicio tiene varios incisos y se cierra cada uno.

```latex
\fcolorbox{RedOrange}{white}{\color{RedOrange} x = 1}
```

### Tipo D (TD) — Resultado final del ejercicio (sin incisos)
Usado cuando el ejercicio es una sola pregunta con un solo resultado.

```latex
\fcolorbox{TealBlue}{white}{\color{TealBlue} x = 2}
```

### Tipo B — Valor intermedio con peso
Valor hallado en el desarrollo que tiene importancia para pasos posteriores,
pero no es el resultado final.

```latex
\fcolorbox{NavyBlue}{white}{\color{NavyBlue} m = 3}
```

### Tipo C — Valor auxiliar menor
Valor hallado de menor peso, por ejemplo una variable de sistema de ecuaciones
que se usará para sustituir.

```latex
\fcolorbox{Gray}{white}{\color{Gray} y = 4}
```

### Tipo E — Condición de restricción / no existencia
Usado para resaltar restricciones de dominio o condiciones de no existencia.

```latex
\fcolorbox{Mahogany}{white}{\color{Mahogany} x \neq 0}
```

### Sin caja — Resultado intermedio simple
Para un paso intermedio sin necesidad de resaltado por color, usar `\boxed`
sin color.

```latex
\boxed{m = 3}
```

Jerarquía visual: TD > TA > Tipo B > Tipo E > Tipo C > `\boxed` simple

---

## 7. Tachado de expresiones incorrectas

Para mostrar que una expresión es incorrecta (no cancelación algebraica sino error):

```latex
$${\color{BrickRed}\bcancel{{\color{black}\text{Expresión incorrecta}}}}$$
```

El tachado en rojo señala error. Diferente a `\bcancel` algebraico que usa color negro.

---

## 8. Ejemplos completos

### Desarrollo algebraico con cancelaciones

```latex
$$\begin{array}{rcl}
\dfrac{x \cdot \bcancel{2}}{\bcancel{2}} & = & \dfrac{6}{2} \\
x & = & 3
\end{array}$$
```

### Paso con transformación

```latex
$$x + \cancel{2} = \cancelto{\color{YellowOrange}2}{4} \Rightarrow {\color{TealBlue}x = 2}$$
```

### Inciso con resultado intermedio y final

```latex
Hallamos la pendiente: $\fcolorbox{NavyBlue}{white}{\color{NavyBlue} m = \dfrac{3}{2}}$

$
\fcolorbox{RedOrange}{white}{
    $\color{RedOrange}y=\dfrac{3}{2}x+1$
}
$
```
### Sistema de ecuaciones con valor auxiliar

```latex
$$\begin{array}{rcl}
2x + y & = & 7 \\
x - y & = & 2
\end{array}$$

$\fcolorbox{Gray}{white}{\color{Gray} x = 3}$

$\fcolorbox{TealBlue}{white}{\color{TealBlue} y = 1}$
```

---

## 9. Valor absoluto y norma en tablas

Dentro de tablas Markdown, el carácter `|` es el separador de columnas y genera
conflicto si se usa directo en una expresión matemática. Reglas:

- Fuera de tablas o en texto plano: `\|x\|` (escapado) es válido.
- Dentro de bloques LaTeX/KaTeX: usar siempre `$\vert x \vert# Guía de notación LaTeX para NotebookLM

Esta guía define la notación LaTeX usada en las notas de Cálculo I.
Al generar ecuaciones, seguir estos ejemplos exactamente.

---

## 1. Saltos de línea en desarrollos multilínea

Usar siempre `\\` (doble barra) para saltar de línea dentro de `\begin{array}`.
Nunca `\` simple — en Obsidian/KaTeX no produce salto de línea.

```latex
$$\begin{array}{rcl}
a \cdot 1 & = & a \cdot (1 + 0) \\
a & = & a \cdot 1 + a \cdot 0 \\
a + 0 & = & a + a \cdot 0 \\
0 & = & a \cdot 0
\end{array}$$
```

Alineación estándar: `{rcl}` — lado izquierdo · signo · lado derecho.

---

## 2. Fracciones

Usar siempre `\dfrac` en lugar de `\frac`.
`\frac` en display inline `$...$` se vuelve pequeño y difícil de leer.

```latex
$\dfrac{2}{4}$          ← correcto
$\frac{2}{4}$           ← evitar
```

---

## 3. Flechas de transición

Dos flechas con roles distintos:

```latex
ecuación_1 \longrightarrow ecuación_2
```
Indica que se realizó una operación y se pasa a la siguiente expresión.

```latex
\Rightarrow x = 2
```
Indica que se llegó a un resultado — parcial o final del ejercicio.

---

## 4. Cancelaciones

Tres comandos con significado distinto:

### `\bcancel` — eliminación completa
El valor se consume por completo. No queda resto.
Usado en restas donde dos términos iguales se anulan, o en divisiones donde el valor desaparece.

```latex
$x + \bcancel{2} - \bcancel{2} = 0$

$\dfrac{\bcancel{2}}{\bcancel{2}} = 1$
```

### `\cancel` — se consume pero deja resto
El valor se cancela pero la expresión origen aún tiene un excedente.

```latex
$x + \cancel{2} = \cancelto{\color{YellowOrange}2}{4}$
```
Aquí el 2 desaparece, pero el 4 no desaparece — se transforma en 2.

### `\cancelto` — transformación con nuevo valor
Muestra que una expresión se reemplaza por otro valor.
El nuevo valor aparece en color YellowOrange para distinguirlo.

```latex
$\dfrac{2}{\cancelto{\color{YellowOrange}2}{4}}$

$\dfrac{\bcancel{3} \cdot 5}{\cancelto{\color{YellowOrange}5}{15}}$
```

Regla: `\cancelto{\color{YellowOrange}nuevo\_valor}{expresión\_original}`

---

## 5. Sistema de colores

Usar siempre dentro de `\color{}` o `{\color{} contenido}`.

| Color | Comando | Uso |
|---|---|---|
| NavyBlue | `\color{NavyBlue}` | Valores intermedios que se usarán más adelante |
| TealBlue | `\color{TealBlue}` | Resultado final del desarrollo |
| YellowOrange | `\color{YellowOrange}` | Valor nuevo tras una cancelación o corrección |
| BrickRed | `\color{BrickRed}` | Error o término incorrecto señalado |
| RedOrange | `\color{RedOrange}` | Advertencia o caso especial |
| BlueGreen | `\color{BlueGreen}` | Definición o condición aplicada |
| Violet | `\color{Violet}` | Hipótesis o dato del enunciado destacado |
| OliveGreen | `\color{OliveGreen}` | Sustitución — reemplazo de variable por su valor |
| Mahogany | `\color{Mahogany}` | Condición de no existencia — restricción de dominio, denominador = 0 |

Notación estándar: `{\color{Color} contenido}` — llaves envolviendo todo el bloque.
Evitar `\color{Color}{contenido}` — menos robusto dentro de comandos anidados.

Ejemplos:

```latex
{\color{NavyBlue} m = 3}

{\color{TealBlue} x = 2}

{\color{BrickRed} \text{Error: no se puede dividir por cero}}

{\color{Violet} \text{Dato: } f(0) = 1}

{\color{OliveGreen} x = 2 \text{ sustituido en } f(x)}

{\color{Mahogany} x \neq 0}
```

Violeta y OliveGreen se usan únicamente como color de texto inline, no en cajas.

---

## 6. Cajas de resultado

Sistema de cajas con borde y texto del mismo color, fondo siempre blanco (`white`)
para que el color interno resalte de forma uniforme.

### Tipo A (TA) — Resultado final de un inciso
Usado cuando el ejercicio tiene varios incisos y se cierra cada uno.

```latex
\fcolorbox{RedOrange}{white}{\color{RedOrange} x = 1}
```

### Tipo D (TD) — Resultado final del ejercicio (sin incisos)
Usado cuando el ejercicio es una sola pregunta con un solo resultado.

```latex
\fcolorbox{TealBlue}{white}{\color{TealBlue} x = 2}
```

### Tipo B — Valor intermedio con peso
Valor hallado en el desarrollo que tiene importancia para pasos posteriores,
pero no es el resultado final.

```latex
\fcolorbox{NavyBlue}{white}{\color{NavyBlue} m = 3}
```

### Tipo C — Valor auxiliar menor
Valor hallado de menor peso, por ejemplo una variable de sistema de ecuaciones
que se usará para sustituir.

```latex
\fcolorbox{Gray}{white}{\color{Gray} y = 4}
```

### Tipo E — Condición de restricción / no existencia
Usado para resaltar restricciones de dominio o condiciones de no existencia.

```latex
\fcolorbox{Mahogany}{white}{\color{Mahogany} x \neq 0}
```

### Sin caja — Resultado intermedio simple
Para un paso intermedio sin necesidad de resaltado por color, usar `\boxed`
sin color.

```latex
\boxed{m = 3}
```

Jerarquía visual: TD > TA > Tipo B > Tipo E > Tipo C > `\boxed` simple

---

## 7. Tachado de expresiones incorrectas

Para mostrar que una expresión es incorrecta (no cancelación algebraica sino error):

```latex
$${\color{BrickRed}\bcancel{{\color{black}\text{Expresión incorrecta}}}}$$
```

El tachado en rojo señala error. Diferente a `\bcancel` algebraico que usa color negro.

---

## 8. Ejemplos completos

### Desarrollo algebraico con cancelaciones

```latex
$$\begin{array}{rcl}
\dfrac{x \cdot \bcancel{2}}{\bcancel{2}} & = & \dfrac{6}{2} \\
x & = & 3
\end{array}$$
```

### Paso con transformación

```latex
$$x + \cancel{2} = \cancelto{\color{YellowOrange}2}{4} \Rightarrow {\color{TealBlue}x = 2}$$
```

### Inciso con resultado intermedio y final

```latex
Hallamos la pendiente: $\fcolorbox{NavyBlue}{white}{\color{NavyBlue} m = \dfrac{3}{2}}$

$
\fcolorbox{RedOrange}{white}{
    $\color{RedOrange}y=\dfrac{3}{2}x+1$
}
$
```
### Sistema de ecuaciones con valor auxiliar

```latex
$$\begin{array}{rcl}
2x + y & = & 7 \\
x - y & = & 2
\end{array}$$

$\fcolorbox{Gray}{white}{\color{Gray} x = 3}$

$\fcolorbox{TealBlue}{white}{\color{TealBlue} y = 1}$
```

---

## 9. Valor absoluto y norma en tablas

Dentro de tablas Markdown, el carácter `|` es el separador de columnas y genera
conflicto si se usa directo en una expresión matemática. Reglas:

 para valor absoluto
  y `$\Vert v \Vert# Guía de notación LaTeX para NotebookLM

Esta guía define la notación LaTeX usada en las notas de Cálculo I.
Al generar ecuaciones, seguir estos ejemplos exactamente.

---

## 1. Saltos de línea en desarrollos multilínea

Usar siempre `\\` (doble barra) para saltar de línea dentro de `\begin{array}`.
Nunca `\` simple — en Obsidian/KaTeX no produce salto de línea.

```latex
$$\begin{array}{rcl}
a \cdot 1 & = & a \cdot (1 + 0) \\
a & = & a \cdot 1 + a \cdot 0 \\
a + 0 & = & a + a \cdot 0 \\
0 & = & a \cdot 0
\end{array}$$
```

Alineación estándar: `{rcl}` — lado izquierdo · signo · lado derecho.

---

## 2. Fracciones

Usar siempre `\dfrac` en lugar de `\frac`.
`\frac` en display inline `$...$` se vuelve pequeño y difícil de leer.

```latex
$\dfrac{2}{4}$          ← correcto
$\frac{2}{4}$           ← evitar
```

---

## 3. Flechas de transición

Dos flechas con roles distintos:

```latex
ecuación_1 \longrightarrow ecuación_2
```
Indica que se realizó una operación y se pasa a la siguiente expresión.

```latex
\Rightarrow x = 2
```
Indica que se llegó a un resultado — parcial o final del ejercicio.

---

## 4. Cancelaciones

Tres comandos con significado distinto:

### `\bcancel` — eliminación completa
El valor se consume por completo. No queda resto.
Usado en restas donde dos términos iguales se anulan, o en divisiones donde el valor desaparece.

```latex
$x + \bcancel{2} - \bcancel{2} = 0$

$\dfrac{\bcancel{2}}{\bcancel{2}} = 1$
```

### `\cancel` — se consume pero deja resto
El valor se cancela pero la expresión origen aún tiene un excedente.

```latex
$x + \cancel{2} = \cancelto{\color{YellowOrange}2}{4}$
```
Aquí el 2 desaparece, pero el 4 no desaparece — se transforma en 2.

### `\cancelto` — transformación con nuevo valor
Muestra que una expresión se reemplaza por otro valor.
El nuevo valor aparece en color YellowOrange para distinguirlo.

```latex
$\dfrac{2}{\cancelto{\color{YellowOrange}2}{4}}$

$\dfrac{\bcancel{3} \cdot 5}{\cancelto{\color{YellowOrange}5}{15}}$
```

Regla: `\cancelto{\color{YellowOrange}nuevo\_valor}{expresión\_original}`

---

## 5. Sistema de colores

Usar siempre dentro de `\color{}` o `{\color{} contenido}`.

| Color | Comando | Uso |
|---|---|---|
| NavyBlue | `\color{NavyBlue}` | Valores intermedios que se usarán más adelante |
| TealBlue | `\color{TealBlue}` | Resultado final del desarrollo |
| YellowOrange | `\color{YellowOrange}` | Valor nuevo tras una cancelación o corrección |
| BrickRed | `\color{BrickRed}` | Error o término incorrecto señalado |
| RedOrange | `\color{RedOrange}` | Advertencia o caso especial |
| BlueGreen | `\color{BlueGreen}` | Definición o condición aplicada |
| Violet | `\color{Violet}` | Hipótesis o dato del enunciado destacado |
| OliveGreen | `\color{OliveGreen}` | Sustitución — reemplazo de variable por su valor |
| Mahogany | `\color{Mahogany}` | Condición de no existencia — restricción de dominio, denominador = 0 |

Notación estándar: `{\color{Color} contenido}` — llaves envolviendo todo el bloque.
Evitar `\color{Color}{contenido}` — menos robusto dentro de comandos anidados.

Ejemplos:

```latex
{\color{NavyBlue} m = 3}

{\color{TealBlue} x = 2}

{\color{BrickRed} \text{Error: no se puede dividir por cero}}

{\color{Violet} \text{Dato: } f(0) = 1}

{\color{OliveGreen} x = 2 \text{ sustituido en } f(x)}

{\color{Mahogany} x \neq 0}
```

Violeta y OliveGreen se usan únicamente como color de texto inline, no en cajas.

---

## 6. Cajas de resultado

Sistema de cajas con borde y texto del mismo color, fondo siempre blanco (`white`)
para que el color interno resalte de forma uniforme.

### Tipo A (TA) — Resultado final de un inciso
Usado cuando el ejercicio tiene varios incisos y se cierra cada uno.

```latex
\fcolorbox{RedOrange}{white}{\color{RedOrange} x = 1}
```

### Tipo D (TD) — Resultado final del ejercicio (sin incisos)
Usado cuando el ejercicio es una sola pregunta con un solo resultado.

```latex
\fcolorbox{TealBlue}{white}{\color{TealBlue} x = 2}
```

### Tipo B — Valor intermedio con peso
Valor hallado en el desarrollo que tiene importancia para pasos posteriores,
pero no es el resultado final.

```latex
\fcolorbox{NavyBlue}{white}{\color{NavyBlue} m = 3}
```

### Tipo C — Valor auxiliar menor
Valor hallado de menor peso, por ejemplo una variable de sistema de ecuaciones
que se usará para sustituir.

```latex
\fcolorbox{Gray}{white}{\color{Gray} y = 4}
```

### Tipo E — Condición de restricción / no existencia
Usado para resaltar restricciones de dominio o condiciones de no existencia.

```latex
\fcolorbox{Mahogany}{white}{\color{Mahogany} x \neq 0}
```

### Sin caja — Resultado intermedio simple
Para un paso intermedio sin necesidad de resaltado por color, usar `\boxed`
sin color.

```latex
\boxed{m = 3}
```

Jerarquía visual: TD > TA > Tipo B > Tipo E > Tipo C > `\boxed` simple

---

## 7. Tachado de expresiones incorrectas

Para mostrar que una expresión es incorrecta (no cancelación algebraica sino error):

```latex
$${\color{BrickRed}\bcancel{{\color{black}\text{Expresión incorrecta}}}}$$
```

El tachado en rojo señala error. Diferente a `\bcancel` algebraico que usa color negro.

---

## 8. Ejemplos completos

### Desarrollo algebraico con cancelaciones

```latex
$$\begin{array}{rcl}
\dfrac{x \cdot \bcancel{2}}{\bcancel{2}} & = & \dfrac{6}{2} \\
x & = & 3
\end{array}$$
```

### Paso con transformación

```latex
$$x + \cancel{2} = \cancelto{\color{YellowOrange}2}{4} \Rightarrow {\color{TealBlue}x = 2}$$
```

### Inciso con resultado intermedio y final

```latex
Hallamos la pendiente: $\fcolorbox{NavyBlue}{white}{\color{NavyBlue} m = \dfrac{3}{2}}$

$
\fcolorbox{RedOrange}{white}{
    $\color{RedOrange}y=\dfrac{3}{2}x+1$
}
$
```
### Sistema de ecuaciones con valor auxiliar

```latex
$$\begin{array}{rcl}
2x + y & = & 7 \\
x - y & = & 2
\end{array}$$

$\fcolorbox{Gray}{white}{\color{Gray} x = 3}$

$\fcolorbox{TealBlue}{white}{\color{TealBlue} y = 1}$
```

---

## 9. Valor absoluto y norma en tablas

Dentro de tablas Markdown, el carácter `|` es el separador de columnas y genera
conflicto si se usa directo en una expresión matemática. Reglas:

 para norma.
- Nunca usar `|x|` sin escapar dentro de una tabla — rompe la nomenclatura de Obsidian.

```latex
| Expresión | En tabla |
|---|---|
| \|x\| | $\vert x \vert$ |
```