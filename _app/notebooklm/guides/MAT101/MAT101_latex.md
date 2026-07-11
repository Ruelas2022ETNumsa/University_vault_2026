---
title: LaTeX — Guía de notación para NotebookLM (MAT101)
galaxy_body: beacon
scope: vault
tool: notebooklm
audience:
  - notebooklm
  - claude
tags:
  - beacon
  - latex
  - infraestructura
  - MAT101
date_created: 2026-07-02
date_updated: 2026-07-02
status: activo
---

ultima prueba

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
El valor se cancela pero la expresión de origen aún tiene un excedente.

```latex
$x + \cancel{2} = \cancelto{\color{YellowOrange}2}{4}$
```
Aquí el 2 desaparece, pero el 4 no desaparece — se transforma en 2.

### `\cancelto` — transformación con nuevo valor
Muestra que una expresión se reemplaza por otro valor.
El nuevo valor aparece en YellowOrange para distinguirlo.

```latex
$\dfrac{2}{\cancelto{\color{YellowOrange}2}{4}}$

$\dfrac{\bcancel{3} \cdot 5}{\cancelto{\color{YellowOrange}5}{15}}$
```

Regla: `\cancelto{\color{YellowOrange}nuevo_valor}{expresión_original}`

---

## 5. Sistema de colores

Notación estándar: `{\color{Color} contenido}` — llaves envolviendo todo el bloque.

| Color | Uso |
|---|---|
| NavyBlue | Valores intermedios que se usarán más adelante |
| TealBlue | Resultado final del desarrollo |
| YellowOrange | Valor nuevo tras una cancelación o corrección |
| BrickRed | Error o término incorrecto señalado |
| RedOrange | Advertencia o caso especial |
| BlueGreen | Definición o condición aplicada |
| Violet | Hipótesis o dato del enunciado destacado |
| OliveGreen | Sustitución — reemplazo de variable por su valor |
| Mahogany | Condición de no existencia — restricción de dominio, denominador = 0 |

Violet y OliveGreen se usan únicamente como color de texto inline, no en cajas.

Ejemplos:

```latex
{\color{NavyBlue} m = 3}
{\color{TealBlue} x = 2}
{\color{BrickRed} \text{Error: no se puede dividir por cero}}
{\color{Violet} \text{Dato: } f(0) = 1}
{\color{OliveGreen} x = 2 \text{ sustituido en } f(x)}
{\color{Mahogany} x \neq 0}
```

---

## 6. Cajas de resultado

Borde y texto del mismo color, fondo siempre `white`.

| Tipo | Color | Uso |
|---|---|---|
| TA | RedOrange | Resultado final de un inciso |
| TD | TealBlue | Resultado final del ejercicio (sin incisos) |
| B | NavyBlue | Valor intermedio con peso |
| C | Gray | Valor auxiliar menor |
| E | Mahogany | Condición de restricción o no existencia |
| `\boxed` | — | Resultado intermedio simple, sin color |

Jerarquía visual: TD > TA > B > E > C > `\boxed`

Sintaxis:

```latex
\bbox[2px,border:2px solid #FF4500;background:white]{\color{#FF4500} x = 1}

\bbox[2px,border:2px solid #008080;background:white]{\color{#008080} x = 2}

\bbox[2px,border:2px solid #000080;background:white]{\color{#000080} m = 3}

\bbox[2px,border:2px solid #808080;background:white]{\color{#808080} y = 4}

\bbox[2px,border:2px solid #C04000;background:white]{\color{#C04000} x \neq 0}

\boxed{m = 3}
```

---

## 7. Tachado de expresiones incorrectas

Para marcar una expresión como error (no cancelación algebraica):

```latex
$${\color{BrickRed}\bcancel{{\color{black}\text{Expresión incorrecta}}}}$$
```

El tachado en rojo señala error. Diferente al `\bcancel` algebraico que usa negro.

---

## 8. Valor absoluto y norma en tablas

Dentro de tablas Markdown `|` es separador de columnas — genera conflicto si se usa en expresiones matemáticas.

- Valor absoluto: `$\vert x \vert$` — nunca `|x|` dentro de tablas
- Norma: `$\Vert v \Vert$` — nunca `||v||` dentro de tablas
- Fuera de tablas en texto plano: `\|x\|` es válido

---

## 9. Ejemplos completos

### Desarrollo algebraico con cancelaciones

```latex
$$\begin{array}{rcl}
\dfrac{x \cdot \bcancel{2}}{\bcancel{2}} & = & \dfrac{6}{2} \\
x & = & 3
\end{array}$$
```

### Paso con transformación

```latex
$$x + \cancel{2} = \cancelto{\color{YellowOrange}2}{4} \Rightarrow {\color{TealBlue} x = 2}$$
```

### Inciso con resultado intermedio y final

```latex
Hallamos la pendiente: $\bbox[2px,border:2px solid #000080;background:white]{\color{#000080} m = \dfrac{3}{2}}$

$$\bbox[2px,border:2px solid #FF4500;background:white]{\color{#FF4500} y = \dfrac{3}{2}x + 1}$$

```

### Sistema de ecuaciones con valor auxiliar

```latex
$$\begin{array}{rcl}
2x + y & = & 7 \\
x - y & = & 2
\end{array}$$

$\bbox[2px,border:2px solid #808080;background:white]{\color{#808080} x = 3}$

$$\bbox[2px,border:2px solid #008080;background:white]{\color{#008080} y = 1}$$
```
