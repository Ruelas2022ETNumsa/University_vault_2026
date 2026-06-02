---
title: "Desmos — Guía unificada para Obsidian"
galaxy_body: beacon
scope: vault
tool: desmos-plugin
audience: [usuario, notebooklm, claude]
tags: [beacon, desmos, infraestructura]
date_created: 2026-01-01
date_updated: 2026-06-01
status: activo
---

# 📈 GUÍA UNIFICADA DE DESMOS PARA OBSIDIAN

> Plugin: `obsidian-desmos` — renderiza gráficas de [desmos.com](https://www.desmos.com/calculator) directamente en tus notas.
> Este documento tiene tres secciones según quién lo usa: **Usuario**, **NotebookLM** y **Claude**.

---

# 👤 SECCIÓN USUARIO

Referencia rápida para escribir bloques Desmos a mano en Obsidian.

---

## U1. ESTRUCTURA BÁSICA

Todo bloque Desmos se escribe así:

```desmos-graph
[configuración opcional]
---
[ecuaciones]
```

- La sección antes del `---` es **configuración** (límites, tamaño).
- La sección después del `---` son las **ecuaciones y curvas**.
- El `---` es **siempre obligatorio**.

---

## U2. CONFIGURACIÓN — LÍMITES Y TAMAÑO

| Parámetro    | Descripción                | Ejemplo              |
| ------------ | -------------------------- | -------------------- |
| `left`       | Límite izquierdo del eje x | `left=-5`            |
| `right`      | Límite derecho del eje x   | `right=5`            |
| `bottom`     | Límite inferior del eje y  | `bottom=-3`          |
| `top`        | Límite superior del eje y  | `top=3`              |
| `width`      | Ancho en píxeles           | `width=500`          |
| `height`     | Alto en píxeles            | `height=400`         |
| `grid`       | Mostrar/ocultar cuadrícula | `grid=false`         |
| `degreeMode` | Modo de ángulos            | `degreeMode=degrees` |

> 💡 Para gráficas de estudio usa `width=500; height=400`. Para plano xy cuadrado usa `width=500; height=500`.

---

## U3. ECUACIONES — SINTAXIS LaTeX

| Lo que quieres       | Código          |
| -------------------- | --------------- |
| $y = x^2$            | `y=x^2`         |
| $y = \sqrt{x}$       | `y=\sqrt{x}`    |
| $y = \frac{1}{x}$    | `y=\frac{1}{x}` |
| $y = e^x$            | `y=e^x`         |
| $y = \sin(x)$        | `y=\sin(x)`     |
| $y = \ln(x)$         | `y=\ln(x)`      |
| $x^2 + y^2 = 1$      | `x^2+y^2=1`     |
| $x = 2$ (vertical)   | `x=2`           |
| $y = 3$ (horizontal) | `y=3`           |

---

## U4. COLORES

Agregar `|COLOR` después de la ecuación.

El plugin acepta dos formatos:
- **Nombres en mayúsculas** (7 colores fijos): `RED` `BLUE` `GREEN` `ORANGE` `PURPLE` `BLACK` `WHITE`
- **Hex** `#rrggbb`: cualquier color válido — preferido para mejor resultado visual

> 💡 Los nombres en mayúsculas usan los colores saturados por defecto de Desmos. Usar hex da resultados más agradables.

### Paleta recomendada — curvas y líneas

| Hex       | Visual      | Uso recomendado                       |
| --------- | ----------- | ------------------------------------- |
| `#c74440` | Rojo medio  | Curva principal / frontera importante |
| `#2d70b3` | Azul medio  | Curva secundaria                      |
| `#388c46` | Verde medio | Curva terciaria                       |
| `#fa7e19` | Naranja     | Curva de destaque                     |
| `#6042a6` | Morado      | Curva de evento / probabilidad        |
| `#000000` | Negro       | Ejes, bordes, líneas auxiliares       |

> Estos son los hex exactos que usa Desmos web internamente — reconocibles pero no saturados.

### Paleta recomendada — rellenos (áreas)

| Hex       | Visual        | Uso recomendado                 |
| --------- | ------------- | ------------------------------- |
| `#a5d8ff` | Azul claro    | Soporte / región principal      |
| `#b2f2bb` | Verde claro   | Región secundaria               |
| `#ffd8a8` | Naranja claro | Región de advertencia           |
| `#ff7b7b` | Rojo claro    | Región de evento / probabilidad |
| `#d0bfff` | Morado claro  | Región auxiliar                 |

### Estilos de línea

`DASHED` — discontinua | `DOTTED` — punteada | `SOLID` — continua (defecto)

---

## U5. RESTRICCIONES DE DOMINIO

```desmos-graph
y=x^2|0<=x<=3
y=\sqrt{x}|x>=0
x=2|0<=y<=5
```

---

## U6. ÁREAS SOMBREADAS

Usar inecuaciones. Para intersección de condiciones, todo en **una sola línea** separado por `|`:

```desmos-graph
y<2-x|y>x|x>=0|x<=1|#a5d8ff
```

### ⚠️ Rectángulos sombreados

Para sombrear un rectángulo **no usar** `y<=cte|y>=cte` solo — hay que incluir también las restricciones en x. Sintaxis correcta:

```desmos-graph
x>=0|x<=1|y>=0|y<=1|#a5d8ff
```

Esto es equivalente a decir: "la región donde x está entre 0 y 1, e y está entre 0 y 1". Si se omite alguna condición, Desmos extiende el relleno infinitamente en esa dirección.

---

## U7. PUNTOS Y ETIQUETAS

```desmos-graph
(1,2)                   → Punto sólido
(1,2)|OPEN              → Punto hueco
(1,2)|label:texto|BLACK → Punto con etiqueta
```

---

## U8. FUNCIONES OCULTAS

```desmos-graph
f(x)=x^2|hidden
f'(x)|BLUE
```

---

## U9. CHEATSHEET RÁPIDO

```desmos-graph
left=; right=; bottom=; top=;   ← ventana del plano
width=; height=;                 ← tamaño en px
---
y=ec                             ← curva básica
y=ec|COLOR|DASHED                ← con color y estilo
y=ec|0<=x<=1|COLOR               ← con restricción de dominio
y<ec|y>otra|#hexcolor            ← área sombreada entre curvas
x>=a|x<=b|y>=c|y<=d|#hexcolor   ← rectángulo sombreado
(x,y)|label:texto|COLOR          ← punto etiquetado
f(x)=ec|hidden                   ← función oculta
y=x \{x>=0\}|#hex               ← valor absoluto tramo positivo
y=-x \{x<=0\}|#hex              ← valor absoluto tramo negativo
```

---

## U10. VALOR ABSOLUTO

El plugin **no soporta** `y=|x|` ni `y=abs(x)`. La única forma correcta es separar en dos tramos con `\{...\}`:

```desmos-graph
left=-5; right=5; bottom=-1; top=5;
width=500; height=300;
---
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
```

Para sombrear la región bajo $y=|x|$ hasta una altura $a$, usar inecuaciones concretas en x e y — **no** usar `|x|` ni `abs(x)` dentro de las condiciones de relleno:

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

| Lo que querés graficar   | Sintaxis plugin (✅)                          | No funciona (❌)                        |
| ------------------------ | -------------------------------------------- | --------------------------------------- |
| Curva $y = \|x\|$        | dos tramos `y=x \{x>=0\}` y `y=-x \{x<=0\}` | `y=\|x\|` · `y=abs(x)`                 |
| Región bajo $y = \|x\|$  | inecuaciones concretas `a<=x<=b\|y<=cte`     | `-\|y\|<=x<=\|y\|` · `y<=abs(x)`       |

---

## U11. RECURSOS

| Recurso           | URL                                        |
| ----------------- | ------------------------------------------ |
| Desmos Calculator | https://www.desmos.com/calculator          |
| Plugin GitHub     | https://github.com/nigecat/obsidian-desmos |
| Learn Desmos      | https://learn.desmos.com                   |

**Caché del plugin:** los SVGs generados se almacenan en `.cache/desmos/` dentro del vault (ruta configurada manualmente). Esta carpeta es ignorada por File Hider y no es contenido académico — no crear notas ahí.

---

---

# 🤖 SECCIÓN NOTEBOOKLM

Instrucciones para que NotebookLM genere bloques Desmos correctos listos para copiar en Obsidian. Cuando el usuario pida una gráfica, responder con un bloque de código — no con imagen ni enlace.

---

## N1. REGLA CRÍTICA — EL `---` ES SIEMPRE OBLIGATORIO

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
y=x^2|BLUE
```

✅ Sin configuración, el `---` igual va:

```desmos-graph
---
y=x^2|BLUE
```

---

## N2. ESTRUCTURA OBLIGATORIA

```desmos-graph
[parámetros terminados en ;]
---
[ecuaciones con modificadores]
```

---

## N3. PARÁMETROS DE CONFIGURACIÓN

| Parámetro | Qué hace           | Valor típico |
| --------- | ------------------ | ------------ |
| `left`    | Límite izquierdo x | `-5`         |
| `right`   | Límite derecho x   | `5`          |
| `bottom`  | Límite inferior y  | `-3`         |
| `top`     | Límite superior y  | `3`          |
| `width`   | Ancho en px        | `500`        |
| `height`  | Alto en px         | `400`        |

Usar `width=500; height=500` para plano cuadrado (probabilidad, geometría).

---

## N4. SINTAXIS DE ECUACIONES

| Matemática   | Código          |
| ------------ | --------------- |
| y = x²       | `y=x^2`         |
| y = √x       | `y=\sqrt{x}`    |
| y = 1/x      | `y=\frac{1}{x}` |
| y = eˣ       | `y=e^x`         |
| y = sin(x)   | `y=\sin(x)`     |
| x² + y² = r² | `x^2+y^2=r^2`   |

---

## N5. MODIFICADORES Y COLORES

```desmos-graph
|#hex                                            → color (SIEMPRE usar hex)
|SOLID, |DASHED, |DOTTED                         → estilo de línea
|0<=x<=1                                         → restricción de dominio
|hidden                                          → ocultar curva
```

### ⚠️ Regla de color: SIEMPRE hex, NUNCA nombres en mayúsculas

El plugin acepta nombres (`RED`, `BLUE`, etc.) pero producen colores saturados y duros. Usar siempre hex.

### Paleta para curvas y líneas

```desmos-graph
#c74440   → rojo medio      (curva principal / frontera)
#2d70b3   → azul medio      (curva secundaria)
#388c46   → verde medio     (curva terciaria)
#fa7e19   → naranja         (destaque)
#6042a6   → morado          (evento / probabilidad)
#000000   → negro           (ejes, bordes, auxiliares)
```

### Paleta para rellenos (áreas sombreadas)

```desmos-graph
#a5d8ff   → azul claro      (región / soporte principal)
#b2f2bb   → verde claro     (región secundaria)
#ffd8a8   → naranja claro   (región de advertencia)
#ff7b7b   → rojo claro      (región de evento)
#d0bfff   → morado claro    (región auxiliar)
```

> Los hex de curvas son los colores internos de Desmos web. Los de rellenos son sus versiones pastel.

---

## N6. ÁREAS SOMBREADAS

Usar inecuaciones con todas las condiciones en **una sola línea**:

```desmos-graph
y<2-x|y>x|x>=0|x<=1|#a5d8ff
```

### ⚠️ Rectángulos sombreados

Para sombrear una región rectangular incluir SIEMPRE las cuatro restricciones en una sola línea:

```desmos-graph
x>=0|x<=1|y>=0|y<=1|#a5d8ff
```

No usar `y<=1|y>=0` sin las restricciones de x — Desmos extenderá el relleno fuera del rectángulo.

---

## N7. PUNTOS

```desmos-graph
(1,2)|label:(1,2)|BLACK
(1,2)|OPEN|label:(1,2)|BLACK
```

---

## N8. VALOR ABSOLUTO — REGLA CRÍTICA

El plugin **no soporta** `y=|x|` ni `y=abs(x)`. Tampoco funcionan `|x|` ni `abs(x)` dentro de condiciones de relleno.

### ⚠️ Nunca generar estas formas:

```desmos-graph
y=|x|
y=abs(x)
-|y|<=x<=|y|
y<=abs(x)
```

### Forma correcta — curva por tramos:

```desmos-graph
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
```

### Forma correcta — región bajo y=|x| hasta altura a:

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

La región sombreada usa límites concretos en x e y — no referencias a `|x|`.

| Intención                       | Correcto (✅)                                  | Incorrecto (❌)              |
| ------------------------------- | --------------------------------------------- | --------------------------- |
| Graficar y = abs(x)             | `y=x \{x>=0\}` + `y=-x \{x<=0\}`             | `y=abs(x)` · `y=\|x\|`     |
| Sombrear región bajo y = abs(x) | inecuaciones con valores numéricos en x e y   | `-\|y\|<=x<=\|y\|`         |

---

## N9. EJEMPLOS COMPLETOS

### Función simple

```desmos-graph
left=-4; right=4; bottom=-2; top=6;
width=500; height=400;
---
y=x^2|#2d70b3
```

### Región triangular (probabilidad)

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

### Rectángulo sombreado (soporte cuadrado)

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
y=\sqrt{x}|0<=x<=1|#388c46|SOLID
y<\sqrt{x}|y>x|0<=x<=1|#b2f2bb
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

## N10. CHECKLIST ANTES DE RESPONDER

Antes de entregar un bloque Desmos verificar:
- [ ] ¿Tiene `---`?
- [ ] ¿Todos los parámetros terminan en `;`?
- [ ] ¿Sin espacios alrededor de `|`?
- [ ] ¿Sin llaves `{}` en restricciones?
- [ ] ¿Sin comentarios `//`?
- [ ] ¿Rectángulos sombreados con las 4 condiciones `x>=|x<=|y>=|y<=`?
- [ ] ¿Colores de curvas en hex (`#c74440`, `#2d70b3`, etc.) y NO nombres en mayúsculas?
- [ ] ¿Rellenos con hex pastel (`#a5d8ff`, `#ff7b7b`, etc.)?
- [ ] ¿Funciones por tramos usan `y=k \{a<x<b\}` y NO `{a<x<b: k}`?
- [ ] ¿Sin `y=|x|`, `y=abs(x)` ni `|x|` en condiciones de relleno?

---

## N11. FUNCIONES POR TRAMOS Y VALORES EN INTERVALOS

### ⚠️ Sintaxis web `{intervalo: valor}` NO funciona en el plugin

Desmos web acepta `{a<x<b: 0.2}` para definir una función que vale 0.2 en ese intervalo. **El plugin de Obsidian no soporta esta sintaxis** — el bloque se renderiza vacío o no renderiza.

**Sintaxis correcta para el plugin:** usar `y=valor \{condición\}` con las llaves escapadas:

```desmos-graph
y=0.10 \{a<x<b\}|#2d70b3
```

Las llaves `\{...\}` actúan como restricción de dominio sobre la línea `y=valor`.

### Ejemplo completo — función escalonada con variables

Este bloque renderiza correctamente:

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

Este bloque **no renderiza** (sintaxis web):

```desmos-graph
left=-2; right=8; bottom=-1; top=1;
width=500; height=100;
---
y=0|#000000
a=1
b=4
c=6
(a,0)|label:a|#2d70b3
(b,0)|label:b|#2d70b3
(c,0)|label:c|#2d70b3
{a<x<b: 0.1}|#2d70b3
{b<x<c: 0.1}|#2d70b3
{a<x<c: 0.3}|label:Transitividad|#c74440
```

### Patrón general

| Intención                             | Sintaxis plugin (✅)                         | Sintaxis web (❌)    |
| ------------------------------------- | ------------------------------------------- | ------------------- |
| Valor fijo en intervalo               | `y=k \{a<x<b\}\|#hex`                       | `{a<x<b: k}`        |
| Función en intervalo                  | `y=f(x) \{a<x<b\}\|#hex`                    | `{a<x<b: f(x)}`     |
| Variable definida, valor en intervalo | `y=k \{a<x<b\}\|#hex` con `a=1` etc. arriba | igual — no funciona |

### Nota sobre etiquetas en funciones por tramos

`label:` **no se puede poner en una línea de función** — solo funciona en puntos. Para etiquetar un tramo, agregar un punto con label en el centro del intervalo:

```desmos-graph
y=0.10 \{a<x<b\}|#2d70b3
(2.5, 0.10)|label:P(A)|#2d70b3
```

---

---

# 🧠 SECCIÓN CLAUDE

Reglas y patrones que Claude debe aplicar al generar o corregir bloques Desmos en archivos `.md` del vault. Esta sección es la referencia de trabajo activa para Claude.

---

## C1. REGLAS ABSOLUTAS DE SINTAXIS

Estas reglas no tienen excepciones. Cualquier bloque que las viole debe corregirse:

| Regla                                        | Correcto                              | Incorrecto                                                |
| -------------------------------------------- | ------------------------------------- | --------------------------------------------------------- |
| Separador `---` siempre presente             | `width=500;\n---\ny=x`               | `width=500;\ny=x`                                         |
| Sin espacios alrededor de `\|`               | `y=x\|#c74440`                       | `y = x \| RED`                                            |
| Sin llaves `{}` en restricciones             | `y=x\|0<=x<=1`                       | `y=x\|{0<=x<=1}`                                          |
| Sin comentarios `//`                         | —                                    | `y=x^2 // parábola`                                       |
| Raíces con `\sqrt{x}`                        | `y=\sqrt{x}`                         | `y=sqrt(x)`                                               |
| Fracciones con `\frac{a}{b}`                 | `y=\frac{3}{8}x`                     | `y=(3/8)x`                                                |
| Pi con `\pi`                                 | `y=\frac{1}{\pi}`                    | `y=1/pi`                                                  |
| Restricciones de líneas con dominio          | `y=x\|0<=x<=2\|#2d70b3`             | `y=x\|#2d70b3` (se desborda)                              |
| Colores siempre en hex                       | `\|#c74440`                          | `\|RED` (saturado)                                        |
| Funciones por tramos / valores en intervalos | `y=0.10 \{a<x<b\}\|#hex`            | `{a<x<b: 0.10}` (sintaxis web — no funciona en el plugin) |
| Valor absoluto siempre por tramos            | `y=x \{x>=0\}` + `y=-x \{x<=0\}`   | `y=\|x\|` · `y=abs(x)`                                   |
| Sin `\|x\|` ni `abs(x)` en rellenos         | inecuaciones con valores numéricos   | `-\|y\|<=x<=\|y\|` · `y<=abs(x)`                         |

---

## C2. RECTÁNGULOS SOMBREADOS

Para sombrear una región rectangular usar las **cuatro condiciones en una sola línea**:

```desmos-graph
x>=a|x<=b|y>=c|y<=d|#a5d8ff
```

**Ejemplo — soporte cuadrado [0,1]×[0,1]:**

```desmos-graph
x>=0|x<=1|y>=0|y<=1|#a5d8ff
```

**Nunca** usar solo `y<=1|y>=0|#a5d8ff` — Desmos extiende el relleno fuera del rectángulo porque no conoce los límites en x.

Para agregar los bordes del rectángulo como líneas encima del relleno:

```desmos-graph
x>=0|x<=1|y>=0|y<=1|#a5d8ff
x=1|0<=y<=1|#2d70b3|DASHED
y=1|0<=x<=1|#2d70b3|DASHED
```

---

## C3. VALOR ABSOLUTO

El plugin no renderiza `y=|x|` ni `y=abs(x)`. Tampoco acepta `|x|` ni `abs(x)` en condiciones de relleno.

**Patrón correcto — curva:**

```desmos-graph
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
```

**Patrón correcto — región sombreada bajo y=|x|:**

```desmos-graph
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
y=2|#000000|DASHED
-2<=x<=2|y<=2|y>=0|#a5d8ff
(-2,2)|label:(-a,a)|#c74440
(2,2)|label:(a,a)|#c74440
```

La clave: el relleno usa cotas numéricas concretas (`-2<=x<=2|y<=2|y>=0`), nunca expresiones con `|x|`.

Si el problema usa una variable `a` en lugar de valor numérico, definirla primero y usar el número en la ventana:

```desmos-graph
a=2
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
y=a|#000000|DASHED
-2<=x<=2|y<=2|y>=0|#a5d8ff
(-a,a)|label:(-a,a)|#c74440
(a,a)|label:(a,a)|#c74440
```

---

## C4. CUÁNDO INCLUIR GRÁFICA

Incluir gráfica solo si aporta claridad visual que el texto no puede dar:

✅ Incluir cuando:
- El soporte tiene geometría no obvia (triángulo, semicírculo, valor absoluto, curva).
- Se pide probabilidad sobre una región con fronteras curvas o partidas.
- La densidad marginal tiene forma visual relevante para entender el problema.
- El enunciado pide explícitamente dibujar la región.

❌ No incluir cuando:
- El resultado es un número (varianza, covarianza, probabilidad simple).
- La conclusión es algebraica (independencia, normalización).
- El soporte es un cuadrado simple y la conclusión no depende de verlo.
- Ya hay una gráfica suficiente en ese inciso.

---

## C5. UNA GRÁFICA POR INCISO

Cada inciso tiene su propio bloque `desmos-graph` independiente. Nunca mezclar ecuaciones de distintos incisos en un solo bloque.

Si el archivo tiene todas las gráficas juntas al final:
1. Identificar a qué inciso pertenece cada ecuación.
2. Crear un bloque por inciso y ubicarlo después del desarrollo de ese inciso.
3. Eliminar el bloque acumulado al final.

---

## C6. FLUJO DE CORRECCIÓN DE UN BLOQUE EXISTENTE

Cuando Claude encuentra un bloque Desmos con errores:

1. Identificar todos los errores (ver C1).
2. Corregir directamente en el archivo con Filesystem — no mostrar el bloque corregido en el chat.
3. Si el bloque usa ` ``` ` genérico en lugar de ` ```desmos-graph `, corregir el tipo también.
4. Si la gráfica no aporta al inciso, eliminarla (ver C4).

---

## C7. PLANTILLA BASE PARA REGIONES DE PROBABILIDAD

```desmos-graph
left=-0.2; right=X; bottom=-0.2; top=Y;
width=500; height=500;
---
[fronteras del dominio con restricciones de dominio y colores hex]
[región sombreada como inecuación con todas las condiciones en una línea]
[puntos clave con label]
```

Ajustar `right` y `top` según el tamaño del soporte más un margen de ~20%.

---

## C8. PALETA DE COLORES RECOMENDADA POR ROL

**Regla:** usar siempre hex. Los nombres en mayúsculas (`RED`, `BLUE`…) son saturados — nunca usarlos.

| Rol visual                      | Hex                                     | Visual            |
| ------------------------------- | --------------------------------------- | ----------------- |
| Soporte / región principal      | `#a5d8ff`                               | azul claro        |
| Región de evento / probabilidad | `#ff7b7b`                               | rojo claro        |
| Región secundaria               | `#b2f2bb`                               | verde claro       |
| Frontera superior del dominio   | `#2d70b3`                               | azul medio        |
| Frontera inferior / diagonal    | `#c74440`                               | rojo medio        |
| Curva de evento                 | `#6042a6`                               | morado            |
| Líneas auxiliares               | `#000000\|DASHED`                       | negro discontinuo |
| Puntos clave                    | `#000000` o el hex de la curva asociada |                   |

%%
galaxy-links
[[_galaxy-system]]
[[_note-system]]
%%
