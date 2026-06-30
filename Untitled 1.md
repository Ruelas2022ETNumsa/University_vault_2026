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

Ejemplos:

```latex
{\color{NavyBlue} m = 3}

{\color{TealBlue} x = 2}

{\color{BrickRed} \text{Error: no se puede dividir por cero}}
```

---

## 6. Cajas de resultado

Tres tipos con jerarquía visual clara:

### Tipo 1 — Resultado intermedio
Valor o ecuación necesaria para continuar el desarrollo. Sin color.

```latex
\boxed{m = 3}
```

### Tipo 2 — Resultado final del inciso
Resultado definitivo de un inciso o subpregunta. Borde RedOrange, fondo YellowOrange, texto NavyBlue.

```latex
\fcolorbox{RedOrange}{YellowOrange}{\color{NavyBlue} x = 1}
```
### Tipo 3 — Valor auxiliar importante
Valor hallado que no es resultado final pero tiene peso — por ejemplo en sistemas de ecuaciones donde se halla una variable para sustituir. Borde gris, fondo gris claro.

```latex
\fcolorbox{Gray}{lightgray}{\color{black} y = 4}
```

Jerarquía visual: Tipo 2 > Tipo 1 > Tipo 3

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
Hallamos la pendiente: $\boxed{m = \dfrac{3}{2}}$

$$
\fcolorbox{RedOrange}{YellowOrange}{
    $\color{NavyBlue}y=\dfrac{3}{2}x+1$
}
$$
```
### Sistema de ecuaciones con valor auxiliar

```latex
$$\begin{array}{rcl}
2x + y & = & 7 \\
x - y & = & 2
\end{array}$$

$\fcolorbox{Gray}{lightgray}{\color{black} x = 3}$

$$\fcolorbox{RedOrange}{YellowOrange}{\color{NavyBlue} y = 1}$$
```