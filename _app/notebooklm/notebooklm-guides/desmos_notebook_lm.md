---
title: Desmos — Guía unificada para Obsidian
galaxy_body: beacon
scope: vault
tool: desmos-plugin
audience:
  - usuario
  - notebooklm
  - claude
tags:
  - beacon
  - desmos
  - infraestructura
date_created: 2026-01-01
date_updated: 2026-06-26
status: activo
---

# 📈 GUÍA UNIFICADA DE DESMOS PARA OBSIDIAN

> Plugin: `obsidian-desmos` — renderiza gráficas de [desmos.com](https://www.desmos.com/calculator) directamente en tus notas.
> Este documento está organizado en tres bloques: **Reglas de sintaxis (N1–N10)**, **Checklist (N11)**, y **Biblioteca de ejemplos por tema MAT101 (N12–N19)**.

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM genere bloques Desmos correctos listos para copiar en Obsidian. Cuando el usuario pida una gráfica, responder con un bloque de código — no con imagen ni enlace.

---

## BLOQUE A — SINTAXIS Y REGLAS

---

### N1. REGLA CRÍTICA — EL `---` ES SIEMPRE OBLIGATORIO + ESTRUCTURA

**Sin `---` el plugin no renderiza nada.** No importa si hay configuración o no.

#### Estructura obligatoria del bloque

```
[parámetros de ventana: left right bottom top]
[parámetros de tamaño: width height]
---
[ecuaciones con modificadores]
```

**Orden de parámetros — siempre este orden, sin excepción:**

1. Primero `left`, `right`, `bottom`, `top` — definen la ventana
2. Después `width`, `height` — definen el tamaño del canvas

❌ Incorrecto — sin `---`:

```desmos-graph
width=300; height=200;
y=x^2|#005F73
```

❌ Incorrecto — orden de parámetros invertido:
```
width=350; height=120;
left=-6; right=6; bottom=-1; top=1;
---
y=x^2|#005F73
```

✅ Correcto — con configuración:

```desmos-graph
left=-6; right=6; bottom=-1; top=1;
width=350; height=120;
---
y=x^2|#005F73
```

✅ Correcto — sin configuración, el `---` igual va:

```desmos-graph
---
y=x^2|#005F73
```

> El plugin no da error visible cuando el orden es incorrecto, pero puede causar comportamiento inesperado en el renderizado.

---

### N2. PARÁMETROS DE CONFIGURACIÓN

| Parámetro | Qué hace           | Valor típico |
| --------- | ------------------ | ------------ |
| `left`    | Límite izquierdo x | `-5`         |
| `right`   | Límite derecho x   | `5`          |
| `bottom`  | Límite inferior y  | `-3`         |
| `top`     | Límite superior y  | `3`          |
| `width`   | Ancho en px        | ver tabla    |
| `height`  | Alto en px         | ver tabla    |

**Tamaños estándar confirmados:**

| Tipo           | width | height | Uso                                          |
| -------------- | ----- | ------ | -------------------------------------------- |
| Pequeño        | 300   | 200    | Rectas numéricas, intervalos, un punto       |
| Mediano        | 400   | 350    | Funciones, parábolas, trigonométricas        |
| Grande         | 550   | 450    | Múltiples curvas, etiquetas, regiones        |
| Cornell        | 320   | 250    | Máximo dentro de bloque multi-column         |
| Plano cuadrado | 500   | 500    | Regiones, geometría, área entre curvas       |

Para rectas numéricas usar ratio horizontal (3:1). Para funciones estándar ratio 4:3.

---

### N3. SINTAXIS DE ECUACIONES

| Matemática                      | Código Desmos                                               |
| ------------------------------- | ----------------------------------------------------------- |
| y = xⁿ (entero)                 | `y=x^2`, `y=x^3`                                            |
| y = x^(p/q)                     | `y=x^{3/2}`, `y=x^{2/3}`                                    |
| y = x^(-p/q)                    | `y=x^{-1/2}`, `y=x^{-2/3}`                                  |
| y = 1/x                         | `y=1/x`, `y=\frac{1}{x}`                                                     |
| x² + y² = r²                    | `x^2+y^2=r^2`                                               |
| y = 2^x                         | `y=2^x`                                                     |
| y = eˣ                          | `y=e^x`                                                     |
| y = log(x)                      | `y=\log(x)`                                                 |
| y = ln(x)                       | `y=\ln(x)`                                                  |
| y = sin(x)                      | `y=\sin(x)`                                                 |
| y = cos(x)                      | `y=\cos(x)`                                                 |
| y = tan(x)                      | `y=\tan(x)`                                                 |
| y = arcsin(x)                   | `y=\arcsin(x)\|-1<=x<=1`                                    |
| y = arccos(x)                   | `y=\arccos(x)\|-1<=x<=1`                                    |
| y = arctan(x)                   | `y=\arctan(x)`                                              |
| y = sinh(x)                     | `y=\sinh(x)`                                                |
| y = cosh(x)                     | `y=\cosh(x)`                                                |
| y = \|x\|                       | `y=\abs(x)`                                                 |
| y = \|f(x)\| compuesta          | `y=\abs(x^{2}-4x+3)`                                        |
| y = ⌊x⌋                         | `y=\floor(x)`                                               |
| y = sgn(x)                      | `y=\operatorname{sgn}(x)`                                   |
| distancia al entero más cercano | `y=\min(\operatorname{mod}(x,1),1-\operatorname{mod}(x,1))` |



#### Notación funcional y derivadas

| Matemática                      | Código Desmos                                  |
| ------------------------------- | ---------------------------------------------- |
| f(x) = expresión                | `f(x)=x^2`                                     |
| y = f'(x)                       | `y=f'(x)`                                      |
| f(x) con dominio fijo           | `f(x)=x^2|0<=x<=3`                          |
| f(x) con dominio por variables  | `a=1` / `b=4` / `f(x)=x^3` / `y=f(x)|a<x<b` |
| f(x) oculta, solo f'(x) visible | `f(x)=x^2\|hidden` luego `y=f'(x)`             |

---

### N4. CONSTANTES Y FUNCIONES DEFINIDAS POR EL USUARIO

#### Constantes escalares

Desmos permite declarar constantes con cualquier letra del abecedario **excepto `x` e `y`** (reservadas como variables de graficación). Las letras válidas van de `a` a `z` excluyendo `x` e `y`:

```
a=2
b=-3
c=0.5
```

Luego se usan directamente en ecuaciones y restricciones:

```desmos-graph
---
a=2
y=\abs(x)|hidden
(-a,0)|label:-2|#C1121F
(a,0)|label:2|#C1121F
y=0|-a<x<a|#005F73
```

> **Importante:** las constantes **no pueden usarse en la configuración** (arriba del `---`). `left=a` no funciona — escribir siempre el valor numérico directamente.

**Nota sobre etiquetas:** las constantes no se evalúan dentro de `label:` — se imprimen como texto literal. Si se necesita mostrar el valor en la etiqueta, escribir el número directamente:

`(a,0)|label:2|#C1121F` ✅  →  a=2
`(a,0)|label:a|#C1121F` → imprime la letra "a", no el valor `2` ⚠️

#### El valor de π

Desmos reconoce `\pi` como constante nativa dentro de las gráficas (debajo del `---`). Usarlo directamente en ecuaciones y restricciones:

```
y=\sin(x)|-\pi<=x<=\pi|#005F73     ✅
```

`\pi` **no funciona en la configuración** (arriba del `---`). Usar el valor numérico:

```
left=-3.1416; right=3.1416;    ✅
left=-\pi; right=\pi;          ❌
```

#### Funciones definidas por el usuario

Las funciones se definen con cualquier letra del abecedario seguida de `(x)` o `(y)`, **excepto `x` e `y`**:

```
a(x)=x^2
b(x)=\sin(x)
f(x)=x^3-3x
```

La función puede depender de `x` o de `y`:

```
f(x)=x^2     → función de x (la más común)
f(y)=y^2     → función de y (curva horizontal)
```

> **Distinción clave:** `a=2` es una constante escalar. `a(x)=x^2` es una función. Desmos los distingue por la presencia o ausencia de `(x)`.

---

### N5. MODIFICADORES Y COLORES

```
|#hex          → color (SIEMPRE usar hex)
|SOLID         → línea sólida (default)
|DASHED        → línea segmentada
|DOTTED        → línea punteada
|0<=x<=1       → restricción de dominio
|hidden        → ocultar curva
|open          → punto vacío / discontinuidad abierta
|cross         → punto con cruz
(x,y)|#hex    → punto sólido (default, sin modificador extra)
```

#### ⚠️ Regla de color: SIEMPRE hex, NUNCA nombres en mayúsculas

El plugin acepta nombres (`RED`, `BLUE`, etc.) pero producen colores saturados y duros. Usar siempre hex.

#### Paleta para curvas y líneas (sólidas)

```
#005F73   → azul petróleo   (curva principal)
#0A9396   → verde azulado   (curva secundaria)
#EE9B00   → ámbar           (destaque)
#BB3E03   → naranja quemado (curva de advertencia)
#629900   → verde oliva     (curva auxiliar)
#5A189A   → morado          (punto especial)
#C1121F   → rojo            (curva de error / evento)
#DA627D   → rosa            (curva alternativa)
#FFD60A   → amarillo        (resaltado)
#474448   → gris antracita  (ejes, bordes, auxiliares)
```

#### Paleta para líneas segmentadas (50% color + 50% blanco)
```
#80AFB9   → azul petróleo segmentado
#85C9CB   → verde azulado segmentado
#F7CD80   → ámbar segmentado
#DD9F81   → naranja quemado segmentado
#B1CC80   → verde oliva segmentado
#AD8CCD   → morado segmentado
#E0898F   → rojo segmentado
#EDB1BE   → rosa segmentado
#FFEB85   → amarillo segmentado
#A3A2A4   → gris antracita segmentado
```

#### Paleta para rellenos (áreas sombreadas — 25% color + 75% blanco)
```
#BFD7DC   → azul petróleo claro   (región principal)
#C2E4E5   → verde azulado claro   (región secundaria)
#FBE6BF   → ámbar claro           (región de destaque)
#EECFC0   → naranja quemado claro (región de advertencia)
#D8E6BF   → verde oliva claro     (región auxiliar)
#D6C5E6   → morado claro          (región auxiliar)
#F0C4C7   → rojo claro            (región de evento)
#F6D8DF   → rosa claro            (región alternativa)
#FFF5C2   → amarillo claro        (región de resaltado)
#D1D0D1   → gris claro            (región neutra)
```

> Los hex de curvas son los colores internos de Desmos web. Los de rellenos son sus versiones pastel.

---

### N6. ESTRUCTURA DE UNA LÍNEA DE ECUACIÓN

Cada línea debajo del `---` se divide en segmentos separados por `|`:

```
expresión | modificador_2 | modificador_3 | ... | #color
    1     |      2       |      3        |     |   n
```

- **Segmento 1** — la expresión principal: ecuación, inecuación, punto, o constante
- **Segmentos 2+** — modificadores opcionales en cualquier orden: restricciones de dominio, `hidden`, `open`, `cross`, `DASHED`, `DOTTED`, color hex
- El color hex siempre va al final, pero el plugin lo acepta en cualquier posición

#### ⚠️ Llaves `{}` — solo válidas en el segmento 1

Las llaves `{}` (usadas en potencias fraccionarias como `x^{1/2}`) **solo funcionan en el segmento 1**. En segmentos 2 en adelante producen error de renderizado sin aviso visible.

❌ No funciona — llaves en segmento 2:
```
x<y^{2/3}|y<x^{1/2}|x>0|y>0|#BFD7DC
```

✅ Solución — declarar una constante y usarla en restricciones:
```
n=0.5
x<y^{2/3}|y<x^n|x>0|y>0|#BFD7DC
```

También funciona `n=1/2` — Desmos evalúa ambas formas correctamente.

#### Llaves escapadas `\{` `\}` — alternativa para restricciones en funciones por tramos

- Forma preferida con `|`: `y=f(x)|a<x<b|#hex`
- Alternativa válida: `y=f(x)\{a<x<b\}|#hex` — el backslash es obligatorio
- `{...}` sin backslash NO funciona en el plugin
- Sintaxis web que NO funciona en el plugin: `{a<x<b: k}` o `{a<x<b: f(x)}`

---

### N7. ÁREAS SOMBREADAS Y FUNCIONES POR TRAMOS

Usar inecuaciones con todas las condiciones en **una sola línea** pueden ser de 2 tipos:

```desmos-graph
---
y<3-x|y>x-3|x>=-4|x<=2|#BFD7DC
y<3-x|y>x-3|-4<=x<=2|#BFD7DC
```

#### ⚠️ Rectángulos sombreados — cuatro condiciones obligatorias

Para sombrear una región rectangular incluir SIEMPRE las cuatro restricciones en una sola línea:

```desmos-graph
---
x>=0|x<=1|y>=0|y<=1|#BFD7DC
```

No usar `y<=1|y>=0` sin las restricciones de x — Desmos extenderá el relleno fuera del rectángulo.

#### Región entre dos curvas

```desmos-graph
left=-0.5; right=5.5; bottom=-1; top=24;
---
x<y<=x^2|2<=x<=4
y=x^2
y=x
```

>igual funciona la notación `x<y<=x^2\{2<=x<=4\}`

Dos ejemplos adicionales con regiones más complejas:

##### ejemplo 1

```desmos-graph
---
x>=(y-2)^2-2|y>=(x-3)^2-1|(x-4)/2<=y-1/5|y<=-(x-4)^3+1.5|#BFD7DC
```

##### ejemplo 2

```desmos-graph
width=500; height=500;
---
n=0.5
y=x^2|0<=x<=4|#005F73
y=x^{1/2}|0<=x<=4|#0A9396
x<y^2|y<x^n|x>0|y>0|#BFD7DC
x>y^2|y>x^n|x>0|y>0|#C2E4E5
```

#### Funciones por tramos

**Forma preferida** — separador `|`:

```desmos-graph
---
y=1.5|-1<x<5|#005F73
```

Alternativa válida con llaves escapadas — documentada pero no preferida:

```desmos-graph
---
y=1.5\{-1<x<5\}|#005F73
```

> `\{` y `\}` son llaves escapadas — el backslash es obligatorio. `{...}` sin backslash no funciona en el plugin.

##### Ejemplo completo — función escalonada

```desmos-graph
left=-1; right=7; bottom=-0.5; top=0.6;
width=600; height=180;
---
y=0

a=1
b=4
c=6

(a,0)|label:a
(b,0)|label:b
(c,0)|label:c

y=0.10|a<x<b|#005F73
y=0.20|b<x<c|#005F73
y=0.35|a<x<c|#0A9396
```

- La forma preferida es `y=0.10|a<x<b|#005F73` con separador `|`.
- Alternativa válida con llaves escapadas: `y=0.10\{a<x<b\}|#005F73`, también `\{a<x<b: 0.1\}`.
- Nunca usar sin escapar: `y=0.10 {a<x<b}` ni `{a<x<b: 0.1}`.

##### Patrón general

- Valor constante en intervalo: `y=k|a<x<b|#hex` — **forma preferida**
- Función en intervalo: `y=f(x)|a<x<b|#hex`
- Múltiples tramos: una línea `y=f(x)|a<x<b|#hex` por cada tramo
- Llaves escapadas (alternativa): `y=f(x)\{a<x<b\}|#hex`
- Punto de unión entre tramos: `(b, f(b))|open|#hex`
- Etiquetar un tramo: agregar punto en el centro `(medio, k)|label:texto|#hex`
- Sintaxis web que NO funciona en el plugin: `{a<x<b: k}` o `{a<x<b: f(x)}`

---

### N8. PUNTOS Y ETIQUETAS

Tres tipos de punto — el sólido es default, no lleva modificador:

- Punto sólido: `(x,y)|#hex`
- Punto vacío: `(x,y)|open|#hex`
- Punto con cruz: `(x,y)|cross|#hex`

```desmos-graph
---
(1,1)|label:(1,1)|#005F73
(1,2)|open|label:(1,2)|#005F73
(1,3)|cross|label:(1,3)|#005F73
```

#### Fracciones y LaTeX en etiquetas

`\frac{}{}` y cualquier notación LaTeX en `label:` imprime el texto literal, no renderiza. Usar siempre equivalente ASCII:

✅ `(3,0)|open|label:(d-b)/(a-c)|#C1121F`
❌ `(3,0)|open|label:\frac{d-b}{a-c}|#C1121F`

> Excepción: superíndices simples como x² + y² = r² sí se imprimen bien en labels.

#### Etiquetas en funciones

`label:` solo funciona en puntos, no en líneas. Dos usos:

- Punto visible con etiqueta: `(x,y)|label:texto|#hex`
```desmos-graph
---
(0, 2)|label:f(x)|#005F73
(1, 1)|label:f(x)|cross|#005F73
(2, 0)|label:f(x)|open|#005F73
```

- Solo etiqueta, punto oculto: `(x,y)|label:texto|hidden`
```desmos-graph
---
(0, 2)|label:f(x)|hidden|#005F73
(1, 1)|label:f(x)|cross|hidden|#005F73
(2, 0)|label:f(x)|open|hidden|#005F73
```

---

### N9. VALOR ABSOLUTO

El plugin soporta `\abs()` para valor absoluto simple — es la forma preferida para curvas.

#### Forma con `\abs()` — primera opción para curvas:

```desmos-graph
---
y=\abs(x)|#005F73
y=\abs(2x-3)|#0A9396
y=\abs(x^{2}-4x+3)|#EE9B00
y=\abs(\abs(x^{2}-4)-4)|#005F73
```

#### Forma por tramos — obligatoria para regiones sombreadas:

`\abs()` no funciona en condiciones de relleno. Usar tramos:

```desmos-graph
---
y=\abs(x)|hidden
y>=x|y>=-x|y<=3|#C2E4E5
```

#### Tabla de usos

| Intención              | Correcto (✅)                 | Incorrecto (❌)          |
| ---------------------- | ----------------------------- | ------------------------ |
| Curva y=\|x\|          | `y=\abs(x)`                   | `y=\|x\|`               |
| Curva compuesta        | `y=\abs(x^{2}-4x+3)`         | `y=\|x^2-4x+3\|`        |
| Región bajo y=\|x\|    | tramos con cotas numéricas    | `-\|y\|<=x<=\|y\|`      |

---

### N10. RAÍZ CUADRADA — TRES FORMAS VÁLIDAS

Usar en orden de preferencia:

**Forma 1 — primera opción:**
```desmos-graph
---
y=x^{1/2}|#005F73
```

**Forma 2 — segunda opción:**
```desmos-graph
---
y=\sqrt{x}|#0A9396
```

**Forma 3 — tercera opción (relación implícita):**
```desmos-graph
---
x=y^2|y>=0|#EE9B00
```

#### ⚠️ Formas que NO funcionan — nunca usar:

```
y=sqrt(x)
y=\sqrt(x)
y=sqrt{x}
```

---

## BLOQUE B — CHECKLIST

---

### N11. CHECKLIST ANTES DE RESPONDER

Antes de entregar un bloque Desmos verificar:

- [ ] ¿Dice exactamente ` ```desmos-graph ` en la línea de apertura?
- [ ] ¿Tiene `---`?
- [ ] ¿Todos los parámetros terminan en `;`?
- [ ] ¿Sin espacios alrededor de `|`?
- [ ] ¿Sin llaves `{}` en restricciones inline? (`|0<=x<=3|` no `|{0<=x<=3}|`)
- [ ] ¿Sin comentarios `//`?
- [ ] ¿Rectángulos sombreados con las 4 condiciones `x>=a|x<=b|y>=c|y<=d`?
- [ ] ¿Colores de curvas en hex (`#C1121F`, `#005F73`, etc.) y NO nombres en mayúsculas?
- [ ] ¿Rellenos con hex pastel (`#BFD7DC`, `#F0C4C7`, etc.)?
- [ ] ¿Funciones por tramos usan `y=k|a<x<b|#hex` como forma preferida y NO `{a<x<b: k}` sin escapar?
- [ ] ¿Sin `y=|x|`, `y=abs(x)` ni `|x|` en condiciones de relleno?
- [ ] ¿Raíz cuadrada usa `x^{1/2}` como primera opción — NO `y=sqrt(x)` ni `y=\sqrt(x)`?

---

## BLOQUE C — BIBLIOTECA DE EJEMPLOS POR TEMA (MAT101)

Todos los ejemplos de esta sección han sido confirmados y renderizan correctamente.

**Reglas críticas de sintaxis (recordatorio) — ver N1–N10 para detalle completo:**
- Potencias siempre con `{}`: `x^{3/2}` nunca `x^(3/2)`
- Llaves `{}` solo válidas en segmento 1 de cada línea — ver N6
- Palabras reservadas con `\`: `\cos`, `\sin`, `\ln`, `\frac{}{}`
- Funciones especiales: `\abs()`, `\floor()`, `\operatorname{sgn}()`, `\operatorname{mod}()`
- Colores de la paleta oficial únicamente

---

### N12. T0 — NÚMEROS REALES Y DESIGUALDADES

> Tema introductorio. Rectas numéricas, intervalos, valor absoluto básico, inecuaciones.

#### Intervalo abierto \]a, b\[

```desmos-graph
left=-1; right=5; bottom=-1; top=1;
width=300; height=100;
---
(1,0)|open|label:a|#005F73
(3,0)|open|label:b|#005F73
y=0|1<x<3|#005F73
```

#### Intervalo cerrado \[a, b\]

```desmos-graph
left=-1; right=5; bottom=-1; top=1;
width=300; height=100;
---
(1,0)|label:a|#005F73
(3,0)|label:b|#005F73
y=0|1<=x<=3|#005F73
```

#### Intervalo mixto \[a, b\[

```desmos-graph
left=-1; right=5; bottom=-1; top=1;
width=300; height=100;
---
(1,0)|label:a|#005F73
(3,0)|label:b|open|#005F73
y=0|1<=x<3|#005F73
```

#### Intervalo con infinito \]inf, b\[

```desmos-graph
left=-1; right=5; bottom=-1; top=1;
width=300; height=100;
---
(3,0)|label:b|open|#005F73
y=0|x<=3|#005F73
```

#### Intervalo con infinito \[a, inf\[

```desmos-graph
left=-1; right=5; bottom=-1; top=1;
width=300; height=100;
---
(1,0)|label:a|#005F73
y=0|1<=x|#005F73
```

#### Inecuación — tabla de signos y solución

Este patrón usa **dos gráficas en secuencia** para resolver una inecuación:

**Gráfica 1 — análisis de signos:** muestra los intervalos con etiquetas V/F
y los puntos críticos como abiertos (aún no se sabe si pertenecen a la solución).
Usar `|hidden` para flotar etiquetas de intervalo y veredicto encima/debajo del eje.

**Gráfica 2 — solución final:** misma recta numérica pero con los extremos
corregidos: cerrados `(x,0)|#hex` si el punto pertenece a la solución,
abiertos `(x,0)|open|#hex` si no.

Ejemplo — $x^4 \ge 9x^2$, puntos críticos $x=-3,\ 0,\ 3$:

```desmos-graph
left=-6; right=6; bottom=-1; top=1;
width=350; height=120;
---
(-4,0.5)|label:V|#005F73|hidden
(-2,0.5)|label:F|#005F73|hidden
(0,0.5)|label:V|#005F73|hidden
(2,0.5)|label:F|#005F73|hidden
(4,0.5)|label:V|#005F73|hidden
y=0 |-6<x<=-3|#F0C4C7
y=0 |3<=x<6|#F0C4C7
(-3,0)|label:-3|open|#F0C4C7
(0,0)|label:0|open|#F0C4C7
(3,0)|label:3|open|#F0C4C7
(-4,-0.5)|label:I_1|#005F73|hidden
(-0.5,-0.5)|label:I_2|#005F73|hidden
(0.5,-0.5)|label:I_3|#005F73|hidden
(4,-0.5)|label:I_4|#005F73|hidden
```

```desmos-graph
left=-6; right=6; bottom=-1; top=1;
width=350; height=120;
---
y=0 |-6<x<=-3|#F0C4C7
y=0 |3<=x<6|#F0C4C7
(-3,0)|label:-3|#F0C4C7
(0,0)|label:0|#F0C4C7
(3,0)|label:3|#F0C4C7
```

Solución: $C_s = ]-\infty,-3] \cup \{0\} \cup [3,+\infty[$

#### Valor absoluto — región $\vert x \vert \leq a$

```desmos-graph
left=-5; right=5; bottom=-1; top=5;
width=300; height=200;
---
a=2
y=\abs(x)|dashed|#80AFB9
y>=\abs(x)|0<y<4|-a<x<a|#BFD7DC
(-2,0)|label:-a|#C1121F
(2,0)|label:a|#C1121F
```


---

### N13. T1 — FUNCIONES REALES

> Primer parcial. Dominio, imagen, gráficas de familias de funciones, transformaciones.

#### Función simple

```desmos-graph
left=-4; right=4; bottom=-2; top=6;
width=300; height=200;
---
y=x^2|#005F73
```

#### Polinomios

```desmos-graph
left=-3; right=3; bottom=-2; top=5;
width=300; height=200;
---
y=x^4-4x^2+3|#005F73
```

```desmos-graph
left=-3; right=3; bottom=-4; top=4;
width=300; height=200;
---
y=x^3-3x|#0A9396
```

#### Potenciales generalizadas

```desmos-graph
left=-0.5; right=4; bottom=-0.5; top=4;
width=300; height=200;
---
y=x^{3/2}|#EE9B00
```

```desmos-graph
left=-0.5; right=7; bottom=-0.5; top=5;
width=300; height=200;
---
y=x^{-1/2}|#BB3E03
```

```desmos-graph
left=-10; right=10; bottom=-0.5; top=5;
width=300; height=200;
---
y=x^{2/3}|#629900
```

```desmos-graph
left=-5; right=5; bottom=-0.5; top=5;
width=300; height=200;
---
y=x^{-2/3}|#5A189A
```

#### Exponenciales y logarítmicas

```desmos-graph
left=-5; right=3; bottom=-0.5; top=5;
width=300; height=200;
---
y=2^x|#C1121F
```

```desmos-graph
left=-5; right=3; bottom=-0.5; top=5;
width=300; height=200;
---
y=e^x|#DA627D
```

```desmos-graph
left=-0.5; right=5; bottom=-3; top=2;
width=300; height=200;
---
y=\log(x)|#FFD60A
```

```desmos-graph
left=-0.5; right=5; bottom=-3; top=2;
width=300; height=200;
---
y=\ln(x)|#474448
```

#### Trigonométricas

```desmos-graph
left=-3.1416; right=3.1416; bottom=-2; top=2;
width=300; height=200;
---
y=\sin(x)|#005F73
```

```desmos-graph
left=-3.1416; right=3.1416; bottom=-2; top=2;
width=300; height=200;
---
y=\cos(x)|#0A9396
```

```desmos-graph
width=400; height=350;
---
y=\tan(x)|#EE9B00
```

#### Trigonométricas inversas

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=400; height=350;
---
y=\sin(x)|-3<=x<=3|#80AFB9|DASHED
y=x|-3<=x<=3|#85C9CB|DASHED
y=\arcsin(x)|-1<=x<=1|#BB3E03|SOLID
(1,1.5708)|label:(1,pi/2)|#BB3E03|cross
(-1,-1.5708)|label:(-1,-pi/2)|#BB3E03|cross
```

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=400; height=350;
---
y=\cos(x)|-3<=x<=3|#80AFB9|DASHED
y=x|-3<=x<=3|#85C9CB|DASHED
y=\arccos(x)|-1<=x<=1|#629900|SOLID
(1,0)|label:(1,0)|#629900|cross
(0,1.5708)|label:(0,pi/2)|#629900|cross
(-1,3.1416)|label:(-1,pi)|#629900|cross
```

```desmos-graph
left=-3; right=3; bottom=-3; top=3;
width=400; height=350;
---
y=\tan(x)|-1.55<=x<=1.55|#80AFB9|DASHED
y=x|-7<=x<=7|#85C9CB|DASHED
y=\arctan(x)|-7<=x<=7|#5A189A|SOLID
x=-1.5708|-3<=y<=3|#80AFB9|DASHED
x=1.5708|-3<=y<=3|#80AFB9|DASHED
y=-1.5708|-7<=x<=7|#F7CD80|DASHED
y=1.5708|-7<=x<=7|#F7CD80|DASHED
(0,0)|label:(0,0)|#5A189A|cross
```

#### Hiperbólicas

```desmos-graph
left=-2; right=2; bottom=-2; top=2;
width=300; height=200;
---
y=\sinh(x)|#C1121F
```

```desmos-graph
left=-2; right=2; bottom=-0.5; top=4;
width=300; height=200;
---
y=\cosh(x)|#DA627D
(0,1)|label:(0,1)|#DA627D|cross
```

#### Valor absoluto (`\abs()`)

```desmos-graph
left=-2; right=2; bottom=-0.5; top=2;
width=300; height=200;
---
y=\abs(x)|#FFD60A
```

```desmos-graph
left=-1; right=4; bottom=-0.5; top=4;
width=300; height=200;
---
y=\abs(2x-3)|#474448
```

```desmos-graph
left=-1; right=5; bottom=-0.5; top=3;
width=300; height=200;
---
y=\abs(x^{2}-4x+3)|#005F73
```

```desmos-graph
left=-5; right=5; bottom=-0.5; top=6;
width=300; height=200;
---
y=\abs(\abs(x^{2}-4)-4)|#0A9396
```

#### Parte entera (`\floor()`)

```desmos-graph
left=-4; right=4; bottom=-4; top=4;
width=300; height=200;
---
y=\floor(x)|#EE9B00
```

#### Función signo

```desmos-graph
left=-2; right=2; bottom=-2; top=2;
width=300; height=200;
---
y=\operatorname{sgn}(x)|#BB3E03
(0,-1)|#BB3E03|open
(0,1)|#BB3E03|open
```

#### Función escalón y por tramos

```desmos-graph
left=-2; right=2; bottom=-1; top=2;
width=300; height=200;
---
y=0|-2<=x<0|#629900
y=1|0<=x<=2|#5A189A
(0,0)|#629900|open
(0,1)|label:(0,1)|#5A189A
```

```desmos-graph
left=-3; right=10; bottom=-3; top=15;
width=320; height=250;
---
y=x|-3<=x<0|#005F73
y=3x|0<=x<4|#0A9396
y=-3x+24|4<=x<8|#EE9B00
y=0|8<=x<=10|#BB3E03
(0,0)|label:(0,0)|#005F73
(4,12)|label:(4,12)|#0A9396
(8,0)|label:(8,0)|#EE9B00
(0,0)|#005F73|open
(4,12)|#0A9396|open
(8,0)|#EE9B00|open
```

#### Función distancia al entero más cercano

```desmos-graph
left=-2; right=2; bottom=-0.5; top=1;
width=300; height=200;
---
y=\min(\operatorname{mod}(x,1),1-\operatorname{mod}(x,1))|#C1121F
```

---

### N14. T2 — LÍMITES Y CONTINUIDAD

> Primer parcial. Límites laterales, discontinuidades, comportamiento asintótico.

*(Agregar ejemplos confirmados aquí)*

---

### N15. T3 — DERIVACIÓN

> Segundo parcial. Pendiente de tangente, reglas de derivación, derivadas de funciones elementales.

*(Agregar ejemplos confirmados aquí)*

---

### N16. T4 — APLICACIONES DE LA DERIVACIÓN

> Segundo parcial. Máximos y mínimos, concavidad, optimización, teorema del valor medio.

*(Agregar ejemplos confirmados aquí)*

---

### N17. T5 — INTEGRACIÓN

> Tercer parcial. Integral definida, primitivas, regla de Barrow.

*(Agregar ejemplos confirmados aquí)*

---

### N18. T6 — APLICACIONES DE LA INTEGRACIÓN

> Tercer parcial. Área entre curvas, volúmenes de revolución.

*(Agregar ejemplos confirmados aquí)*

---

### N19. T7 — SERIES REALES (BONUS)

> Fuera de parciales. Series numéricas, criterios de convergencia.

*(Agregar ejemplos confirmados aquí)*

---

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
%%
