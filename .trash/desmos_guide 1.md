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
date_updated: 2026-06-05
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

> 💡 Tamaños estándar confirmados:
> - **Pequeño** (rectas numéricas, intervalos, un punto): `width=300; height=200`
> - **Mediano** (funciones, parábolas, trigonométricas): `width=400; height=350`
> - **Grande** (múltiples curvas, etiquetas, regiones): `width=550; height=450`
> - **Cornell** (dentro de bloque multi-column): `width=320; height=250` máximo
> - **Plano cuadrado** (probabilidad, geometría): `width=500; height=500`
> 
> Para rectas numéricas usar ratio horizontal (3:1 o 4:2). Para funciones estándar ratio 4:3.

---

## U3. ECUACIONES — SINTAXIS LaTeX

| Lo que quieres       | Código                |
| -------------------- | ------------------- |
| $y = x^2$            | `y=x^2`             |
| $y = \sqrt{x}$       | `x=y^2` + `y>=0`    |
| $y = \frac{1}{x}$    | `y=1/x`             |
| $y = e^x$            | `y=e^x`             |
| $y = \sin(x)$        | `y=\sin(x)`         |
| $y = \ln(x)$         | `y=\ln(x)`          |
| $x^2 + y^2 = 1$      | `x^2+y^2=1`         |
| $x = 2$ (vertical)   | `x=2`               |
| $y = 3$ (horizontal) | `y=3`               |

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
y<3-x|y>x-3|x>=-4|x<=2|#a5d8ff
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

### Fracciones en etiquetas

`\frac{}{}` y potencias fraccionales **no renderizan** dentro de `label:` — el texto literal aparece sin procesar.
La única forma que funciona es slash:

```desmos-graph
(3,0)|OPEN|label:(d-b)/(a-c)|#ff7b7b
```

| Intención         | Correcto (✅)        | Incorrecto (❌)          |
| ----------------- | ------------------- | ------------------------ |
| Fracción en label | `label:(a-b)/(c-d)` | `label:\frac{a-b}{c-d}` |
| Potencia en label | `label:a^(1/2)`     | `label:x^{1/2}`          |

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
x=y^2                            ← raíz cuadrada — forma recomendada (rama positiva)
y>=0                             ← restricción para rama positiva
y=\sqrt{x}|x>=0|#hex            ← raíz cuadrada alternativa (puede fallar en contextos complejos)
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

Para sombrear la región bajo $y=\vert x\vert$ hasta una altura $a$, usar inecuaciones concretas en x e y — **no** usar `|x|` ni `abs(x)` dentro de las condiciones de relleno:

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

| Lo que querés graficar              | Sintaxis plugin (✅)                          | No funciona (❌)                  |
| ----------------------------------- | -------------------------------------------- | --------------------------------- |
| Curva $y = \vert x\vert$            | dos tramos `y=x \{x>=0\}` y `y=-x \{x<=0\}` | `y=\|x\|` · `y=abs(x)`           |
| Región bajo $y = \vert x\vert$      | inecuaciones concretas `a<=x<=b\|y<=cte`     | `-\|y\|<=x<=\|y\|` · `y<=abs(x)` |

---

## U11. RAÍZ CUADRADA

El plugin soporta tres formas para graficar $y = \sqrt{x}$, cada una con un comportamiento distinto:

| Forma | Código | Resultado |
| ----- | ------ | --------- |
| C — Relación implícita | `x=y^2` + `y>=0` | **Recomendada** — más robusta ✅ |
| A — LaTeX con llaves | `y=\sqrt{x}` | Solo rama positiva, puede fallar en contextos complejos ⚠️ |
| B — Potencia fraccional | `y=x^{1/2}` | Solo rama positiva, puede fallar en contextos complejos ⚠️ |

> ⚠️ `y=sqrt(x)` sin llaves y `y=\sqrt(x)` con paréntesis **no funcionan**.

### Forma C — recomendada (relación implícita)

```desmos-graph
left=-0.5; right=5; bottom=-0.5; top=4;
width=500; height=300;
---
x=y^2
y>=0
```

> 💡 La forma C (`x=y^2` + `y>=0`) es la más robusta — preferir siempre. Las formas A y B pueden fallar en algunos contextos.

### Forma A — alternativa (LaTeX con llaves)

```desmos-graph
left=-0.5; right=5; bottom=-0.5; top=4;
width=500; height=300;
---
y=\sqrt{x}|x>=0|#2d70b3
```

> ⚠️ Puede fallar en algunos contextos. Si no renderiza correctamente, usar la forma C.

### Forma B — alternativa (potencia fraccional)

```desmos-graph
left=-0.5; right=5; bottom=-0.5; top=4;
width=500; height=300;
---
y=x^{1/2}|x>=0|#2d70b3
```

> ⚠️ Equivalente a la forma A — mismas limitaciones.

### Ejemplo completo — desigualdad de medias con raíz

Región entre $\sqrt{x}$ y $(x+1)/2$, mostrando que la media aritmética siempre supera o iguala a la geométrica (con $b=1$):

```desmos-graph
left=-2; right=5; bottom=-1; top=4;
width=500; height=300;
---
x=y^2|x>=0|#2d70b3
y=(x+1)/2|#c74440
y<=(x+1)/2|y^2>=x|x>=0|#b2f2bb
(1,1)|label:Igualdad si a=b|#000000
```



Las curvas se tocan en $(0,0)$ y $(1,1)$ — los únicos puntos donde $\sqrt{x} = \frac{x+1}{2}$.

---

## U12. RECURSOS

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

| Matemática   | Código                |
| ------------ | ------------------- |
| y = x²       | `y=x^2`             |
| y = √x       | `x=y^2` + `y>=0`    |
| y = 1/x      | `y=1/x`             |
| y = eˣ       | `y=e^x`             |
| y = sin(x)   | `y=\sin(x)`         |
| x² + y² = r² | `x^2+y^2=r^2`       |

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
y<3-x|y>x-3|x>=-4|x<=2|#a5d8ff
```


```desmos-graph
left=-0.5; right=5.5;
bottom=-1; top=24;
---
x<y<=x^2 \{2<=x<=4\}

y=x^2
y=x
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

### ⚠️ Fracciones en etiquetas — solo slash

`\frac{}{}` no renderiza en `label:` — aparece el texto literal. Usar siempre slash:

✅ `(3,0)|OPEN|label:(d-b)/(a-c)|#ff7b7b`
❌ `(3,0)|OPEN|label:\frac{d-b}{a-c}|#ff7b7b`

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

### Forma correcta — región bajo y=\vert x\vert hasta altura a:

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

| Intención                              | Correcto (✅)                                 | Incorrecto (❌)          |
| -------------------------------------- | --------------------------------------------- | ------------------------ |
| Graficar y = \vert x\vert              | `y=x \{x>=0\}` + `y=-x \{x<=0\}`             | `y=abs(x)` · `y=\|x\|`  |
| Sombrear región bajo y = \vert x\vert  | inecuaciones con valores numéricos en x e y   | `-\|y\|<=x<=\|y\|`      |

---

## N9. RAÍZ CUADRADA — TRES FORMAS VÁLIDAS

El plugin soporta tres formas para $y = \sqrt{x}$. Usar en orden de preferencia:

**Forma C — primera opción (relación implícita, más robusta):**
```desmos-graph
y=\sqrt{x}|x>=0|#2d70b3
```

**Forma A — segunda opción (puede fallar en contextos complejos):**
```desmos-graph
y=x^{1/2}|x>=0|#2d70b3
```

**Forma B — tercera opción (equivalente a la forma A):**
```desmos-graph
x=y^2
y>=0
```

### ⚠️ Formas que NO funcionan — nunca usar:

```desmos-graph
y=sqrt(x)
y=\sqrt(x)
y=sqrt{x}
```

### Matices importantes

- La forma C (`x=y^2` + `y>=0`) es la más robusta — preferir siempre.
- Sin la línea `y>=0` la forma C grafica ambas ramas (la parábola completa `x=y^2`) — siempre incluirla.
- Las formas A y B pueden fallar en contextos complejos (inecuaciones, regiones sombreadas).
- En contexto matemático (Cálculo, desigualdades, probabilidad) usar siempre la rama positiva.

### Ejemplo — desigualdad de medias

```desmos-graph
left=-2; right=5; bottom=-1; top=4;
width=500; height=300;
---
y^2=x|x>=0|#2d70b3
y=(x+1)/2|#c74440
y<=(x+1)/2|y^2>=x|x>=0|#b2f2bb
(1,1)|label:Igualdad si a=b|#000000
```

---

## N10. EJEMPLOS COMPLETOS

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

## N11. CHECKLIST ANTES DE RESPONDER

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
- [ ] ¿Raíz cuadrada usa `x=y^2` + `y>=0` como primera opción — NO `y=sqrt(x)` ni `y=\sqrt(x)`?

---

## N12. FUNCIONES POR TRAMOS Y VALORES EN INTERVALOS

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

# 🧠 SECCIÓN IA — Claude y ChatGPT

Reglas y patrones que Claude debe aplicar al generar o corregir bloques Desmos en archivos `.md` del vault. Esta sección es la referencia de trabajo activa para Claude.

---

## C1. REGLAS ABSOLUTAS DE SINTAXIS

Estas reglas no tienen excepciones. Cualquier bloque que las viole debe corregirse:

| Regla                                        | Correcto                                      | Incorrecto                                                |
| -------------------------------------------- | --------------------------------------------- | --------------------------------------------------------- |
| Separador `---` siempre presente             | `width=500;\n---\ny=x`                        | `width=500;\ny=x`                                         |
| Sin espacios alrededor de `\|`               | `y=x\|#c74440`                                | `y = x \| RED`                                            |
| Sin llaves `{}` en restricciones             | `y=x\|0<=x<=1`                                | `y=x\|{0<=x<=1}`                                          |
| Sin comentarios `//`                         | —                                             | `y=x^2 // parábola`                                       |
| Raíz cuadrada — preferir relación implícita    | `x=y^2` + `y>=0`                              | `y=sqrt(x)` · `y=\sqrt(x)` · `y=\sqrt{x}` (puede fallar) |
| Fracciones en ecuaciones — usar slash          | `y=(3)/(8)`                                   | `y=\frac{3}{8}` (puede fallar)                              |
| Fracciones en `label:` siempre con slash      | `label:(a-b)/(c-d)`                           | `label:\frac{a-b}{c-d}` · `label:x^{1/2}` (no renderiza) |
| Pi con `\pi`                                 | `y=\frac{1}{\pi}`                             | `y=1/pi`                                                  |
| Restricciones de líneas con dominio          | `y=x\|0<=x<=2\|#2d70b3`                       | `y=x\|#2d70b3` (se desborda)                              |
| Colores siempre en hex                       | `\|#c74440`                                   | `\|RED` (saturado)                                        |
| Funciones por tramos / valores en intervalos | `y=0.10 \{a<x<b\}\|#hex`                      | `{a<x<b: 0.10}` (sintaxis web — no funciona en el plugin) |
| Valor absoluto siempre por tramos            | `y=x \{x>=0\}` + `y=-x \{x<=0\}`             | `y=\|x\|` · `y=abs(x)`                                   |
| Sin `\|x\|` ni `abs(x)` en rellenos         | inecuaciones con valores numéricos            | `-\|y\|<=x<=\|y\|` · `y<=abs(x)`                         |

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

**Patrón correcto — región sombreada bajo y=\vert x\vert:**

```desmos-graph
y=x \{x>=0\}|#2d70b3
y=-x \{x<=0\}|#2d70b3
y=2|#000000|DASHED
-2<=x<=2|y<=2|y>=0|#a5d8ff
(-2,2)|label:(-a,a)|#c74440
(2,2)|label:(a,a)|#c74440
```

La clave: el relleno usa cotas numéricas concretas (`-2<=x<=2|y<=2|y>=0`), nunca expresiones con `|x|`.

---

## C4. RAÍZ CUADRADA

Tres formas válidas, en orden de preferencia:

**Primera opción — relación implícita (más robusta):**
```desmos-graph
y=\sqrt{x}|x>=0|#2d70b3
```

**Segunda opción — LaTeX con llaves (puede fallar en contextos complejos):**
```desmos-graph
y=x^{1/2}|x>=0|#2d70b3
```

**Tercera opción — potencia fraccional (equivalente a la segunda):**
```desmos-graph
x=y^2
y>=0
```

Nunca usar `y=sqrt(x)`, `y=\sqrt(x)` ni `y=sqrt{x}` — no renderizan.

La forma implícita (`x=y^2` + `y>=0`) es la más robusta — usar siempre como primera opción. Sin la línea `y>=0` grafica ambas ramas de la parábola — siempre incluirla.

**Ejemplo real — desigualdad de medias:**

```desmos-graph
left=-2; right=5; bottom=-1; top=4;
width=500; height=300;
---
y^2=x|x>=0|#2d70b3
y=(x+1)/2|#c74440
y<=(x+1)/2|y^2>=x|x>=0|#b2f2bb
(1,1)|label:Igualdad si a=b|#000000
```

---

## C5. CUÁNDO INCLUIR GRÁFICA

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

## C6. UNA GRÁFICA POR INCISO

Cada inciso tiene su propio bloque `desmos-graph` independiente. Nunca mezclar ecuaciones de distintos incisos en un solo bloque.

Si el archivo tiene todas las gráficas juntas al final:
1. Identificar a qué inciso pertenece cada ecuación.
2. Crear un bloque por inciso y ubicarlo después del desarrollo de ese inciso.
3. Eliminar el bloque acumulado al final.

---

## C7. FLUJO DE CORRECCIÓN DE UN BLOQUE EXISTENTE

Cuando Claude encuentra un bloque Desmos con errores:

1. Identificar todos los errores (ver C1).
2. Corregir directamente en el archivo con Filesystem — no mostrar el bloque corregido en el chat.
3. Si el bloque usa ` ``` ` genérico en lugar de ` ```desmos-graph `, corregir el tipo también.
4. Si la gráfica no aporta al inciso, eliminarla (ver C5).

---

## C8. PLANTILLA BASE PARA REGIONES DE PROBABILIDAD

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

## C9. PALETA DE COLORES RECOMENDADA POR ROL

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

# ejemplos a reordenarse

# tamaño desmos

**Pequeño — gráficas simples (rectas numéricas, intervalos, un punto):**  
`width=300; height=200;`

**Mediano — uso general (funciones, parábolas, trigonométricas, regiones):**  
`width=400; height=350;`

**Grande — gráficas con muchos detalles (múltiples curvas, etiquetas, regiones sombreadas):**  
`width=550; height=450;`

El punto crítico es la relación ancho/alto — para funciones estándar un ratio cercano a 1:1 o 4:3 se ve bien. Para rectas numéricas el ratio horizontal es mejor (3:1 o 4:2).


## Función par

$y = x^{4} - 4x^{2} + 3$

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-2; top=5;
---
y = x^4 - 4x^2 + 3
```

---

## Función impar

$f(x)=2x^{5}+6x^{3}-8x$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-5; top=5;
---
f(x)=2x^{5}+6x^{3}-8x
```

---

## Función tangente

$f(x)=\tan(x)$

```desmos-graph
width=400; height=350;
---
y=\tan(x)
```

$f(x)=\dfrac{1}{\tan(x)}$

```desmos-graph
width=300; height=200;
left=-4; right=4; bottom=-4; top=4;
---
y=\frac{1}{x}
```




---

## Función de primer grado

$f(x)=2x+1$

**Desmos**

```desmos-graph
width=300; height=200;
---
y=2x+1
```

---

## Función de segundo grado

$f(x)=x^2-4x+3$

**Desmos**

```desmos-graph
width=300; height=200;

left=-3; right=7; bottom=-2; top=7;


---
y=x^2-4x+3
```

## Función potencial generalizada

$$y=x^{\frac{3}{2}}$$

```desmos-graph
width=300; height=200;
---
y=x^{3/2}
```

ojo que en desmos y=x^(3/2) no da, parace que si esta adecuado a la notacion de latex con unas excepciones.

## Función potencial generalizada

$$y=x^{-\frac{1}{2}}$$

```desmos-graph
width=300; height=200;
left=-0.5; right=7; bottom=-0.5; top=5;
---
y=x^{-1/2}
```


## Función potencial generalizada

$$y=x^{\frac{2}{3}}$$

```desmos-graph

width=300; height=200;
left=-10; right=10; bottom=-0.5; top=5;
---
y=x^{2/3}
```

## Función potencial generalizada

$$y=x^{-\frac{2}{3}}$$

```desmos-graph
width=300; height=200;
left=-5; right=5; bottom=-0.5; top=5;
---

y=x^{-2/3}
```

---

## Función de tercer grado

$f(x)=x^3-3x$

**Desmos**

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-4; top=4;
---
y=x^3-3x
```

---

## Función exponencial base 2

$f(x)=2^x$

**Desmos**

```desmos-graph
width=300; height=200;
left=-5; right=3; bottom=-0.5; top=5;
---
y=2^x
```

---

## Función exponencial natural

$f(x)=e^x$

**Desmos**

```desmos-graph
width=300; height=200;
left=-5; right=3; bottom=-0.5; top=5;
---
y=e^x
```

---

## Función logarítmica base 10

$f(x)=\log_{10}(x)$

**Desmos**

```desmos-graph
width=300; height=200;
left=-0.5; right=3; bottom=-2; top=0.5;
---
y=\log(x)
```

---

## Función logarítmica natural (base e)

$f(x)=\ln(x)$

**Desmos**

```desmos-graph
width=300; height=200;
left=-0.5; right=3; bottom=-3; top=2;
---
y=\ln(x)
```

---

## Función seno

$f(x)=\sin(x)$

```desmos-graph
width=300; height=200;
left=-3.14; right=3.14; bottom=-2; top=2;
---
y=\sin(x)
```

## Función coseno

$f(x)=\cos(x)$

```desmos-graph
width=300; height=200;
left=-3.14; right=3.14; bottom=-2; top=2;
---
y=\cos(x)
```

## Función tangente

$f(x)=\tan(x)$

```desmos-graph
width=400; height=350;
---
y=\tan(x)
```

---

## Función arco seno

$$y=\arcsin(x)$$

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=400; height=350;
---
y=\sin(x)   |-3<=x<=3|#5E81AC|DASHED
y=x         |-3<=x<=3|#777777|DASHED
y=-\arcsin(x)-3.1416|-1<=x<=1|#A65C59|dashed
y=-\arcsin(x)+3.1416|-1<=x<=1|#A65C59|dashed
y=\arcsin(x)|-1<=x<=1|#D97706|solid

(1,3.1416/2)|label:(1,pi/2)|#D97706|cross
(-1,-3.1416/2)|label:-(1,pi/2)|#D97706|cross
```

## Función arco coseno

$$y=\arccos(x)$$

```desmos-graph
left=-3; right=3; bottom=-3.5; top=3.5;
width=400; height=350;
---
y=\cos(x)|-3<=x<=3|#5E81AC|DASHED
y=x|-3<=x<=3|#777777|DASHED
y=\arccos(x)|-1<=x<=1|#D97706|SOLID
y=-\arccos(x)|-1<=x<=1|#A65C59|DASHED

(1,0)|label:(1,0)|#D97706|cross
(0,1.5708)|label:(0,pi/2)|#D97706|cross
(-1,3.1416)|label:(-1,pi)|#D97706|cross
```

## Función arco tangente

$f(x)=\arctan(x)$

```desmos-graph
left=-3; right=3; bottom=-3; top=3;
width=400; height=350;
---
y=\tan(x)   |-1.55<=x<=1.55|#5E81AC|DASHED
y=x|-7<=x<=7|#777777|DASHED
y=\arctan(x)|-7<=x<=7|#D97706|SOLID

x=-1.5708|-7<=y<=7|#5E81AC|DASHED
x=1.5708 |-7<=y<=7|#5E81AC|DASHED

y=-1.5708|-7<=x<=7|#A65C59|DASHED
y=1.5708 |-7<=x<=7|#A65C59|DASHED

(0,0)       |label:(0,0)|#D97706|cross
```



---

## Función seno hiperbólico

$f(x)=\sinh(x)$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-2; top=2;
---
y=\sinh(x)
```

## Función coseno hiperbólico

$f(x)=\cosh(x)$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=4;
---
y=\cosh(x)|#D97706
(0,1)|label:(0,1)|#D97706|cross
```

---

## Función valor absoluto

$f(x)=|x|$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=2;
---
y=\abs(x)
```

## Función recta

$f(x)=|2x-3|$

```desmos-graph
width=300; height=200;
left=-1; right=4; bottom=-0.5; top=4;
---
y=\abs(2x-3)
```

## Función valor absoluto de una ecuación de segundo grado

$f(x)=|x^{2}-4x+3|$

```desmos-graph
width=300; height=200;
left=-1; right=5; bottom=-0.5; top=3;
---
y=\abs(x^{2}-4x+3)
```

$y=|x||x-4|$

```desmos-graph
width=300; height=200;
left=-2; right=6; bottom=-0.5; top=5;
---
y=\abs(x)\abs(x-4)
```

$$y=\left||x^2-4|-4\right|$$

```desmos-graph
width=300; height=200;
left=-5; right=5; bottom=-0.5; top=6;
---
y=\abs(\abs(x^{2}-4)-4)
```

---

## Función parte entera

$f(x)=\lfloor x\rfloor$

```desmos-graph
width=300; height=200;
left=-4; right=4; bottom=-4; top=4;
---
y=\floor(x)
```

$f_{x}=x^{2}$

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-0.5; top=6;
---
y=\floor(x^2)
```

---

## Función distancia

$$
\{x\}=
\begin{cases}
0, & \text{si } x\in\mathbb{Z},\\[4pt]
|x-a|, & \text{si } x\notin\mathbb{Z},\ a\in\mathbb{Z}\text{ es el entero más cercano.}
\end{cases}
$$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-0.5; top=1;
---
y=\min(\operatorname{mod}(x,1),1-\operatorname{mod}(x,1))
```

$$y=\{x^2\}$$

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-0.5; top=1;
---
y=\min(\operatorname{mod}(x^{2},1),1-\operatorname{mod}(x^{2},1))
```

---

## Función signo

$$
\operatorname{sgn}(x)=
\begin{cases}
-1, & \text{si } x<0,\\[4pt]
0, & \text{si } x=0,\\[4pt]
1, & \text{si } x>0.
\end{cases}
$$

```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-2; top=2;
---
y=\operatorname{sgn}(x)|#D97706

(0,0)|label:(-1,-1)|#D97706

(0,-1)|#D97706|open
(0,1)|#D97706|open
```

Sea

$$
u=x^4-5x^2+4.
$$

La función signo está definida por

$$
\operatorname{sgn}(u)=
\begin{cases}
-1,&u<0,\\[4pt]
0,&u=0,\\[4pt]
1,&u>0.
\end{cases}
$$

Primero se factoriza el polinomio:

$$
u=x^4-5x^2+4=(x^2-1)(x^2-4)
=(x-2)(x-1)(x+1)(x+2).
$$

Las raíces son

$$
x=-2,\,-1,\,1,\,2.
$$

| Intervalo o punto | Valor de prueba | Signo de $u=x^4-5x^2+4$ | Valor de $\operatorname{sgn}(u)$ |    Representación gráfica     |
|:-----------------:|:---------------:|:-----------------------:|:--------------------------------:|:-----------------------------:|
|  $(-\infty,-2)$   |      $-3$       |           $+$           |               $1$                | Segmento horizontal en $y=1$  |
|      $x=-2$       |      $-2$       |           $0$           |               $0$                |    Punto cerrado $(-2,0)$     |
|     $(-2,-1)$     |     $-1.5$      |           $-$           |               $-1$               | Segmento horizontal en $y=-1$ |
|      $x=-1$       |      $-1$       |           $0$           |               $0$                |    Punto cerrado $(-1,0)$     |
|     $(-1,1)$      |       $0$       |           $+$           |               $1$                | Segmento horizontal en $y=1$  |
|       $x=1$       |       $1$       |           $0$           |               $0$                |     Punto cerrado $(1,0)$     |
|      $(1,2)$      |      $1.5$      |           $-$           |               $-1$               | Segmento horizontal en $y=-1$ |
|       $x=2$       |       $2$       |           $0$           |               $0$                |     Punto cerrado $(2,0)$     |
|   $(2,\infty)$    |       $3$       |           $+$           |               $1$                | Segmento horizontal en $y=1$  |



```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-2; top=2;
---
y=\operatorname{sgn}(x^4-5x^2+4)|#D97706

(-2,0)|label:(-2,0)|#D97706
(-1,0)|label:(-1,0)|#D97706
(1,0)|label:(1,0)|#D97706
(2,0)|label:(2,0)|#D97706

(-2,1)|#D97706|open
(-2,-1)|#D97706|open

(-1,1)|#D97706|open
(-1,-1)|#D97706|open

(1,1)|#D97706|open
(1,-1)|#D97706|open

(2,1)|#D97706|open
(2,-1)|#D97706|open
```

> **Observación:** El caso $u=0$ únicamente determina los **puntos cerrados** de la gráfica, correspondientes a las raíces del polinomio. Matemáticamente, la función **no contiene segmentos verticales** en esos valores de $x$; solo existen los puntos abiertos provenientes de los intervalos adyacentes y el punto cerrado donde $u=0$. Algunos graficadores, como Desmos, dibujan pequeños segmentos verticales para resaltar la discontinuidad o debido a su algoritmo de renderizado, pero dichos segmentos **no forman parte de la gráfica de la función** desde el punto de vista matemático.

**ALTERNATIVA (GRAFICAMENTE CORRECTA )A LA FUNCION SIGNO**

```desmos-graph
width=300; height=200;
left=-3; right=3; bottom=-2; top=2;
---
y=1|-3<=x<-2|#D97706
y=-1|-2<x<-1|#D97706
y=1|-1<x<1|#D97706
y=-1|1<x<2|#D97706
y=1|2<x<=3|#D97706

(-2,0)|label:(-2,0)|#D97706
(-1,0)|label:(-1,0)|#D97706
(1,0)|label:(1,0)|#D97706
(2,0)|label:(2,0)|#D97706

(-2,1)|#D97706|open
(-2,-1)|#D97706|open

(-1,1)|#D97706|open
(-1,-1)|#D97706|open

(1,1)|#D97706|open
(1,-1)|#D97706|open

(2,1)|#D97706|open
(2,-1)|#D97706|open
```







## Función escalón unitario

$$
u(x)=
\begin{cases}
0, & x<0,\\[4pt]
1, & x\ge 0.
\end{cases}
$$


```desmos-graph
width=300; height=200;
left=-2; right=2; bottom=-1; top=2;
---
y=0|-2<=x<0|#D97706
y=1|0<=x<=2|#D97706

(0,0)|#D97706|open
(0,1)|label:(0,1)|#D97706
```

ejemplos

sea la funcion, expresar en terminos de u(x-a)
$$
y=
\begin{cases}
0, & x<0,\\[4pt]
2x, & 0\le x\le3,\\[4pt]
6, & x\ge3.
\end{cases}
$$

### Análisis

```desmos-graph
width=300; height=200;
left=-2; right=5; bottom=-1; top=8;
---
y=0|-2<=x<0|#D97706
y=2x|0<=x<=3|#D97706
y=6|3<=x<=5|#D97706

(0,0)|label:(0,0)|#D97706
(3,6)|label:(3,6)|#D97706
```





---


Dada la función

$$
y=
\begin{cases}
0, & x<0,\\[4pt]
2x, & 0\le x\le3,\\[4pt]
6, & x\ge3.
\end{cases}
$$

Se descompone en dos funciones.

La primera corresponde al tramo lineal que comienza en $x=0$:

$$
y=
\begin{cases}
2x, & x\ge0,\\[4pt]
0, & x<0.
\end{cases}
$$

Esta función se representa mediante

$$
2x\,u(x).
$$

La segunda corresponde a la corrección que transforma la recta $2x$ en la constante $6$ a partir de $x=3$:

$$
y=
\begin{cases}
6-2x, & x\ge3,\\[4pt]
0, & x<3.
\end{cases}
$$

Esta función se representa mediante

$$
(6-2x)\,u(x-3).
$$

Finalmente, sumando ambas contribuciones se obtiene

$$
\boxed{
y=2x\,u(x)+(6-2x)\,u(x-3)
}
$$

---

ejemplo sea
$$
f(x)=
\begin{cases}
x, & x<0,\\[4pt]
3x, & 0\le x<4,\\[4pt]
-3x+24, & 4\le x<8,\\[4pt]
0, & x\ge8.
\end{cases}
$$

### Representación mediante la función escalón

Se descompone la función en las siguientes contribuciones.

La primera corrige el tramo inicial:

$$
\begin{cases}
x, & x<0,\\
0, & x\ge0,
\end{cases}
=-x\,u(x).
$$

La segunda activa la recta $3x$ a partir de $x=0$:

$$
\begin{cases}
3x, & x\ge0,\\
0, & x<0,
\end{cases}
=3x\,u(x).
$$

La tercera reemplaza $3x$ por $-3x+24$ a partir de $x=4$:

$$
(-6x+24)\,u(x-4).
$$

La cuarta anula la función desde $x=8$:

$$
(3x-24)\,u(x-8).
$$

Por tanto,

$$
\boxed{
f(x)=
-x\,u(x)
+3x\,u(x)
+(-6x+24)\,u(x-4)
+(3x-24)\,u(x-8)
}
$$

```desmos-graph
width=320; height=250;
left=-3; right=10; bottom=-2; top=15;
---
y=x|-3<=x<0|#D97706
y=3x|0<=x<4|#D97706
y=-3x+24|4<=x<8|#D97706
y=0|8<=x<=10|#D97706

(0,0)|label:(0,0)|#D97706
(4,12)|label:(4,12)|#D97706
(8,0)|label:(8,0)|#D97706

(0,0)|#D97706|open
(4,12)|#D97706|open
(8,0)|#D97706|open
```




















---


# cosas que le tuve que aclarar a chat gpt

en las graficas desmos:
- en las potencias usar {} por ejemplo x^{potencia} nunca x^(potencia)
- un hallazgo importante en desmos para algunas palabras reservadas se debe usar \ como
- \cos
- \frac{1}{3}







# aca le pregunte a notebooklm que prompt usar para que no se le olvide el desmos-graph, esto contesto pero en su snippet no lo agrego

Tienes toda la razón. Para que el plugin `obsidian-desmos` renderice la gráfica, es imperativo usar el identificador de bloque exacto.

Para asegurarte de que siempre siga estas reglas, puedes usar un **prompt** como este:

> **"Genera la gráfica siguiendo el formato estricto de la `[[desmos_guide]]`, usando el bloque `desmos-graph`, colores en hex y el separador obligatorio."**

Aquí tienes el snippet corregido y ajustado a los estándares de tus guías (usando `width=320` como se sugiere para tus apuntes):

```
left=-5; right=5;
bottom=-1; top=10;
width=320; height=400;
---
y=x^2|#c74440
```

### Por qué es importante (según tus fuentes):

1. **Identificador:** El bloque debe empezar con ` ```desmos-graph ` para que el plugin lo reconozca.
2. **Separador `---`:** Es obligatorio para dividir la configuración de las ecuaciones.
3. **Colores Hex:** Debo usar siempre códigos hexadecimales (como `#c74440`) en lugar de nombres como "RED", ya que los nombres producen colores demasiado saturados.
4. **Configuración:** Cada parámetro (como `width`) debe terminar en punto y coma `;`.

Si incluyes esta gráfica dentro de un **Bloque Cornell**, recuerda que en la columna de **Claves** es obligatorio colocar el bloque comentado `%```desmos-graph` para que se procese correctamente.

---

%%
# galaxy-links
[[_galaxy-system]]
[[_note-system]]
%%
