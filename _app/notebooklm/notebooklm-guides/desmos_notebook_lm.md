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
> Este documento está organizado en tres bloques: **Reglas de sintaxis (N1–N9)**, **Checklist y ejemplos técnicos (N10–N12)**, y **Biblioteca de ejemplos por tema MAT101 (N13–N20)**.

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM genere bloques Desmos correctos listos para copiar en Obsidian. Cuando el usuario pida una gráfica, responder con un bloque de código — no con imagen ni enlace.

---

## BLOQUE A — SINTAXIS Y REGLAS

---

### N1. REGLA CRÍTICA — EL `---` ES SIEMPRE OBLIGATORIO

**Sin `---` el plugin no renderiza nada.** No importa si hay configuración o no.

❌ Incorrecto:

```desmos-graph
width=500; height=500;
y=x^2|BLUE
```

✅ Correcto:

```desmos-graph
width=500; height=500;
---
y=x^2|#2d70b3
```

✅ Sin configuración, el `---` igual va:

```desmos-graph
---
y=x^2|#2d70b3
```

---

### N2. ESTRUCTURA OBLIGATORIA

```
[parámetros terminados en ;]
---
[ecuaciones con modificadores]
```

Regla de orden: **parámetros arriba → `---` → ecuaciones abajo**. Sin excepción.

---

### N3. PARÁMETROS DE CONFIGURACIÓN

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

### N4. SINTAXIS DE ECUACIONES

| Matemática                      | Código Desmos                                               |
| ------------------------------- | ----------------------------------------------------------- |
| y = xⁿ (entero)                 | `y=x^2`, `y=x^3`                                            |
| y = x^(p/q)                     | `y=x^{3/2}`, `y=x^{2/3}`                                    |
| y = x^(-p/q)                    | `y=x^{-1/2}`, `y=x^{-2/3}`                                  |
| y = 1/x                         | `y=1/x`                                                     |
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

#### Paleta para curvas y líneas

```
#c74440   → rojo medio      (curva principal / frontera)
#2d70b3   → azul medio      (curva secundaria)
#388c46   → verde medio     (curva terciaria)
#fa7e19   → naranja         (destaque)
#6042a6   → morado          (punto especial)
#000000   → negro           (ejes, bordes, auxiliares)
```

#### Paleta para rellenos (áreas sombreadas)

```
#a5d8ff   → azul claro      (región / área principal)
#b2f2bb   → verde claro     (región secundaria)
#ffd8a8   → naranja claro   (región de advertencia)
#ff7b7b   → rojo claro      (región de evento)
#d0bfff   → morado claro    (región auxiliar)
```

> Los hex de curvas son los colores internos de Desmos web. Los de rellenos son sus versiones pastel.

---

### N6. ÁREAS SOMBREADAS

Usar inecuaciones con todas las condiciones en **una sola línea**:

```desmos-graph
y<3-x|y>x-3|x>=-4|x<=2|#a5d8ff
```

#### ⚠️ Rectángulos sombreados — cuatro condiciones obligatorias

Para sombrear una región rectangular incluir SIEMPRE las cuatro restricciones en una sola línea:

```desmos-graph
x>=0|x<=1|y>=0|y<=1|#a5d8ff
```

No usar `y<=1|y>=0` sin las restricciones de x — Desmos extenderá el relleno fuera del rectángulo.

#### Región entre dos curvas

```desmos-graph
left=-0.5; right=5.5; bottom=-1; top=24;
---
x<y<=x^2 \{2<=x<=4\}
y=x^2
y=x
```

igual funciona la notación `x<y<=x^2|2<=x<=4`

otro ejemplos mas complejo

```desmos-graph
left=-0.5; right=5.5; bottom=-1; top=24;
---
x<y^2|y<x^2|2<x^2-1|x<4y|
```
x<y<=x^2|2<=x<=4|
y<3-x|y>x-3|x>=-4|x<=2|#a5d8ff


---

### N7. PUNTOS Y ETIQUETAS

```desmos-graph
(1,2)|label:(1,2)|#000000
(1,2)|open|label:(1,2)|#000000
(1,2)|cross|label:(1,2)|#000000
```

#### ⚠️ Fracciones en etiquetas — solo slash

`\frac{}{}` no renderiza en `label:` — aparece el texto literal. Usar siempre slash:

✅ `(3,0)|open|label:(d-b)/(a-c)|#c74440`
❌ `(3,0)|open|label:\frac{d-b}{a-c}|#c74440`

### ⚠️ Valor absoluto en texto y tablas Markdown

El símbolo `|` rompe las tablas Markdown. Para valor absoluto en texto o dentro de tablas:

| Contexto | Correcto (✅)          | Incorrecto (❌) |
| -------- | --------------------- | -------------- |
| Texto    | `$\vert x \vert$`     | `$|x|$`        |
| Tablas   | `$\vert f(x) \vert$`  | `$|f(x)|$`     |

---

### N8. VALOR ABSOLUTO

El plugin soporta `\abs()` para valor absoluto simple — es la forma preferida para curvas.

#### Forma con `\abs()` — primera opción para curvas:

```
y=\abs(x)
y=\abs(2x-3)
y=\abs(x^{2}-4x+3)
y=\abs(\abs(x^{2}-4)-4)
```

#### Forma por tramos — obligatoria para regiones sombreadas:

`\abs()` no funciona en condiciones de relleno. Usar tramos:

```desmos-graph
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
y=2|#000000|DASHED
-2<=x<=2|y<=2|y>=0|#a5d8ff
```

#### Tabla de usos

| Intención              | Correcto (✅)                 | Incorrecto (❌)          |
| ---------------------- | ----------------------------- | ------------------------ |
| Curva y=\|x\|          | `y=\abs(x)`                   | `y=\|x\|`               |
| Curva compuesta        | `y=\abs(x^{2}-4x+3)`         | `y=\|x^2-4x+3\|`        |
| Región bajo y=\|x\|    | tramos con cotas numéricas    | `-\|y\|<=x<=\|y\|`      |

---

### N9. RAÍZ CUADRADA — TRES FORMAS VÁLIDAS

Usar en orden de preferencia:

**Forma 1 — primera opción:**
```desmos-graph
y=x^{1/2}|x>=0|#2d70b3
```

**Forma 2 — segunda opción:**
```desmos-graph
y=\sqrt{x}|x>=0|#2d70b3
```

**Forma 3 — tercera opción (relación implícita):**
```desmos-graph
x=y^2
y>=0
```

#### ⚠️ Formas que NO funcionan — nunca usar:

```
y=sqrt(x)
y=\sqrt(x)
y=sqrt{x}
```








---

## BLOQUE B — CHECKLIST Y EJEMPLOS TÉCNICOS

---

## N10. EJEMPLOS TÉCNICOS DE REFERENCIA

Estos ejemplos ilustran técnicas de sintaxis, no temas específicos.

### Función simple

```desmos-graph
left=-4; right=4; bottom=-2; top=6;
width=500; height=400;
---
y=x^2|#2d70b3
```

### Región triangular

```desmos-graph
left=-0.2; right=1.5; bottom=-0.2; top=2.5;
width=500; height=500;
---
y=x|0<=x<=1|#c74440|SOLID
y=2-x|0<=x<=1|#2d70b3|SOLID
x=0|0<=y<=2|#000000|DASHED
y<2-x|y>x|x>=0|x<=1|#a5d8ff
(0,0)|label:(0,0)|#000000
(1,1)|label:(1,1)|#c74440
(0,2)|label:(0,2)|#2d70b3
```

### Rectángulo sombreado

```desmos-graph
left=-0.2; right=1.3; bottom=-0.2; top=1.3;
width=500; height=500;
---
x>=0|x<=1|y>=0|y<=1|#a5d8ff
x=1|0<=y<=1|#2d70b3|DASHED
y=1|0<=x<=1|#2d70b3|DASHED
(0,0)|label:(0,0)|#000000
(1,1)|label:(1,1)|#000000
```

### Región entre curva y recta

```desmos-graph
left=-0.1; right=1.3; bottom=-0.1; top=1.3;
width=500; height=500;
---
y=x|0<=x<=1|#c74440|SOLID
y=x^{1/2}|0<=x<=1|#388c46|SOLID
y<x^{1/2}|y>x|0<=x<=1|#b2f2bb
(0,0)|label:(0,0)|#000000
(1,1)|label:(1,1)|#000000
```

### Valor absoluto con región sombreada

```desmos-graph
left=-5; right=5; bottom=-1; top=5;
width=500; height=300;
---
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
y=2|#000000|DASHED
-2<=x<=2|y<=2|y>=0|#a5d8ff
(-2,2)|label:(-a,a)|#c74440
(2,2)|label:(a,a)|#c74440
```

---

## N11. CHECKLIST ANTES DE RESPONDER

Antes de entregar un bloque Desmos verificar:

- [ ] ¿Dice exactamente ` ```desmos-graph ` en la línea de apertura?
- [ ] ¿Tiene `---`?
- [ ] ¿Todos los parámetros terminan en `;`?
- [ ] ¿Sin espacios alrededor de `|`?
- [ ] ¿Sin llaves `{}` en restricciones inline? (`|0<=x<=3|` no `|{0<=x<=3}|`)
- [ ] ¿Sin comentarios `//`?
- [ ] ¿Rectángulos sombreados con las 4 condiciones `x>=a|x<=b|y>=c|y<=d`?
- [ ] ¿Colores de curvas en hex (`#c74440`, `#2d70b3`, etc.) y NO nombres en mayúsculas?
- [ ] ¿Rellenos con hex pastel (`#a5d8ff`, `#ff7b7b`, etc.)?
- [ ] ¿Funciones por tramos usan `y=k \{a<x<b\}` y NO `{a<x<b: k}`?
- [ ] ¿Sin `y=|x|`, `y=abs(x)` ni `|x|` en condiciones de relleno?
- [ ] ¿Raíz cuadrada usa `x^{1/2}` como primera opción — NO `y=sqrt(x)` ni `y=\sqrt(x)`?
- [ ] ¿Valor absoluto en texto/tablas usa `\vert` en lugar de `|`?

---

## N12. FUNCIONES POR TRAMOS — SINTAXIS DEL PLUGIN

### ⚠️ Sintaxis web `{intervalo: valor}` NO funciona en el plugin

**Sintaxis correcta para el plugin:** usar `y=valor \{condición\}` con las llaves escapadas:

```desmos-graph
y=0.10 \{a<x<b\}|#2d70b3
```

### Ejemplo completo — función escalonada

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

y=0.10 \{a<x<b\}|#2d70b3
y=0.20 \{b<x<c\}|#2d70b3
y=0.35 \{a<x<c\}|#c74440
```

### Patrón general

| Intención                | Sintaxis plugin (✅)              | Sintaxis web (❌)    |
| ------------------------ | -------------------------------- | ------------------- |
| Valor fijo en intervalo  | `y=k \{a<x<b\}\|#hex`            | `{a<x<b: k}`        |
| Función en intervalo     | `y=f(x) \{a<x<b\}\|#hex`         | `{a<x<b: f(x)}`     |

### Nota sobre etiquetas en funciones por tramos

`label:` solo funciona en puntos. Para etiquetar un tramo, agregar un punto en el centro:

```desmos-graph
y=0.10 \{a<x<b\}|#2d70b3
(2.5, 0.10)|label:f(x)|#2d70b3
```

---

## BLOQUE C — BIBLIOTECA DE EJEMPLOS POR TEMA (MAT101)

Todos los ejemplos de esta sección han sido confirmados y renderizan correctamente.

**Reglas críticas de sintaxis (recordatorio):**
- Potencias siempre con `{}`: `x^{3/2}` nunca `x^(3/2)`
- Palabras reservadas con `\`: `\cos`, `\sin`, `\ln`
- Funciones especiales: `\abs()`, `\floor()`, `\operatorname{sgn}()`, `\operatorname{mod}()`
- Colores de la paleta oficial únicamente

---

## N13. T0 — NÚMEROS REALES Y DESIGUALDADES

> Tema introductorio. Rectas numéricas, intervalos, valor absoluto básico, inecuaciones.

### Intervalo abierto (a, b)

```desmos-graph
width=300; height=100;
left=-1; right=5; bottom=-1; top=1;
---
y=0|-1<=x<=5|#000000
(1,0)|open|label:a|#c74440
(3,0)|open|label:b|#c74440
y=0|1<x<3|#c74440
```

### Intervalo cerrado [a, b]

```desmos-graph
width=300; height=100;
left=-1; right=5; bottom=-1; top=1;
---
y=0|-1<=x<=5|#000000
(1,0)|label:a|#2d70b3
(3,0)|label:b|#2d70b3
y=0|1<=x<=3|#2d70b3
```

### Valor absoluto — curva básica

```desmos-graph
width=300; height=200;
left=-4; right=4; bottom=-0.5; top=4;
---
y=\abs(x)|#2d70b3
```

### Valor absoluto — región $\vert x \vert \leq a$

```desmos-graph
left=-5; right=5; bottom=-1; top=5;
width=400; height=200;
---
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
y=2|#000000|DASHED
-2<=x<=2|y<=2|y>=0|#a5d8ff
(-2,0)|open|label:-a|#c74440
(2,0)|open|label:a|#c74440
```

---

## N14. T1 — FUNCIONES REALES

> Primer parcial. Dominio, imagen, gráficas de familias de funciones, transformaciones.

### Polinomios

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-2; top=5;
---
y=x^4-4x^2+3|#2d70b3
```

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-4; top=4;
---
y=x^3-3x|#2d70b3
```

### Potenciales generalizadas

```desmos-graph
width=300; height=200;
---
y=x^{3/2}|#2d70b3
```

```desmos-graph
width=300; height=200;
left=-0.5; right=7; bottom=-0.5; top=5;
---
y=x^{-1/2}|#2d70b3
```

```desmos-graph
width=300; height=200;
left=-10; right=10; bottom=-0.5; top=5;
---
y=x^{2/3}|#2d70b3
```

```desmos-graph
width=300; height=200;
left=-5; right=5; bottom=-0.5; top=5;
---
y=x^{-2/3}|#2d70b3
```

### Exponenciales y logarítmicas

```desmos-graph
width=300; height=200;
left=-5; right=3; bottom=-0.5; top=5;
---
y=2^x|#2d70b3
```

```desmos-graph
width=300; height=200;
left=-5; right=3; bottom=-0.5; top=5;
---
y=e^x|#c74440
```

```desmos-graph
width=300; height=200;
left=-0.5; right=5; bottom=-3; top=2;
---
y=\log(x)|#388c46
```

```desmos-graph
width=300; height=200;
left=-0.5; right=5; bottom=-3; top=2;
---
y=\ln(x)|#fa7e19
```

### Trigonométricas

```desmos-graph
width=300; height=200;
left=-3.14; right=3.14; bottom=-2; top=2;
---
y=\sin(x)|#2d70b3
```

```desmos-graph
width=300; height=200;
left=-3.14; right=3.14; bottom=-2; top=2;
---
y=\cos(x)|#c74440
```

```desmos-graph
width=400; height=350;
---
y=\tan(x)|#388c46
```

### Trigonométricas inversas

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=400; height=350;
---
y=\sin(x)|-3<=x<=3|#2d70b3|DASHED
y=x|-3<=x<=3|#000000|DASHED
y=\arcsin(x)|-1<=x<=1|#fa7e19|SOLID
(1,1.5708)|label:(1,pi/2)|#fa7e19|cross
(-1,-1.5708)|label:(-1,-pi/2)|#fa7e19|cross
```

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=400; height=350;
---
y=\cos(x)|-3<=x<=3|#2d70b3|DASHED
y=x|-3<=x<=3|#000000|DASHED
y=\arccos(x)|-1<=x<=1|#fa7e19|SOLID
(1,0)|label:(1,0)|#fa7e19|cross
(0,1.5708)|label:(0,pi/2)|#fa7e19|cross
(-1,3.1416)|label:(-1,pi)|#fa7e19|cross
```

```desmos-graph
left=-7; right=7; bottom=-3; top=3;
width=400; height=350;
---
y=\tan(x)|-1.55<=x<=1.55|#2d70b3|DASHED
y=x|-7<=x<=7|#000000|DASHED
y=\arctan(x)|-7<=x<=7|#fa7e19|SOLID
x=-1.5708|-3<=y<=3|#2d70b3|DASHED
x=1.5708|-3<=y<=3|#2d70b3|DASHED
y=-1.5708|-7<=x<=7|#c74440|DASHED
y=1.5708|-7<=x<=7|#c74440|DASHED
(0,0)|label:(0,0)|#fa7e19|cross
```

### Hiperbólicas

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-2; top=2;
---
y=\sinh(x)|#2d70b3
```

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=4;
---
y=\cosh(x)|#fa7e19
(0,1)|label:(0,1)|#fa7e19|cross
```

### Valor absoluto (`\abs()`)

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=2;
---
y=\abs(x)|#2d70b3
```

```desmos-graph
width=300; height=200;
left=-1; right=4; bottom=-0.5; top=4;
---
y=\abs(2x-3)|#c74440
```

```desmos-graph
width=300; height=200;
left=-1; right=5; bottom=-0.5; top=3;
---
y=\abs(x^{2}-4x+3)|#388c46
```

```desmos-graph
width=300; height=200;
left=-5; right=5; bottom=-0.5; top=6;
---
y=\abs(\abs(x^{2}-4)-4)|#6042a6
```

### Parte entera (`\floor()`)

```desmos-graph
width=300; height=200;
left=-4; right=4; bottom=-4; top=4;
---
y=\floor(x)|#fa7e19
```

### Función signo

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-2; top=2;
---
y=\operatorname{sgn}(x)|#fa7e19
(0,-1)|#fa7e19|open
(0,1)|#fa7e19|open
```

### Función escalón y por tramos

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-1; top=2;
---
y=0|-2<=x<0|#2d70b3
y=1|0<=x<=2|#2d70b3
(0,0)|#2d70b3|open
(0,1)|label:(0,1)|#2d70b3
```

```desmos-graph
width=320; height=250;
left=-3; right=10; bottom=-2; top=15;
---
y=x|-3<=x<0|#2d70b3
y=3x|0<=x<4|#2d70b3
y=-3x+24|4<=x<8|#2d70b3
y=0|8<=x<=10|#2d70b3
(0,0)|label:(0,0)|#2d70b3
(4,12)|label:(4,12)|#2d70b3
(8,0)|label:(8,0)|#2d70b3
(0,0)|#2d70b3|open
(4,12)|#2d70b3|open
(8,0)|#2d70b3|open
```

### Función distancia al entero más cercano

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=1;
---
y=\min(\operatorname{mod}(x,1),1-\operatorname{mod}(x,1))|#6042a6
```

---

## N15. T2 — LÍMITES Y CONTINUIDAD

> Primer parcial. Límites laterales, discontinuidades, comportamiento asintótico.

*(Agregar ejemplos confirmados aquí)*

---

## N16. T3 — DERIVACIÓN

> Segundo parcial. Pendiente de tangente, reglas de derivación, derivadas de funciones elementales.

*(Agregar ejemplos confirmados aquí)*

---

## N17. T4 — APLICACIONES DE LA DERIVACIÓN

> Segundo parcial. Máximos y mínimos, concavidad, optimización, teorema del valor medio.

*(Agregar ejemplos confirmados aquí)*

---

## N18. T5 — INTEGRACIÓN

> Tercer parcial. Integral definida, primitivas, regla de Barrow.

*(Agregar ejemplos confirmados aquí)*

---

## N19. T6 — APLICACIONES DE LA INTEGRACIÓN

> Tercer parcial. Área entre curvas, volúmenes de revolución.

*(Agregar ejemplos confirmados aquí)*

---

## N20. T7 — SERIES REALES (BONUS)

> Fuera de parciales. Series numéricas, criterios de convergencia.

*(Agregar ejemplos confirmados aquí)*

---

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
%%
