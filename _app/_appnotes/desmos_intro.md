# 📈 Guía de Desmos en Obsidian
> Plugin: `obsidian-desmos` — renderiza gráficas de [desmos.com](https://www.desmos.com/calculator) directamente en tus notas.

---

## 1. ESTRUCTURA BÁSICA

Todo bloque Desmos se escribe así en Obsidian:

````
```desmos-graph
[configuración opcional]
---
[ecuaciones]
```
````

- La sección antes del `---` es **configuración** (límites, tamaño, etc.)
- La sección después del `---` son las **ecuaciones y curvas**
- Si no necesitas configurar nada, puedes omitir el `---` y poner solo las ecuaciones

**Ejemplo mínimo:**
````
```desmos-graph
y=x^2
```
````

```desmos-graph
y=x^2
```

---

## 2. CONFIGURACIÓN — LÍMITES Y TAMAÑO

Estos parámetros van **antes** del `---`, separados por `;` o saltos de línea:

| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| `left` | Límite izquierdo del eje x | `left=-5` |
| `right` | Límite derecho del eje x | `right=5` |
| `bottom` | Límite inferior del eje y | `bottom=-3` |
| `top` | Límite superior del eje y | `top=3` |
| `width` | Ancho de la imagen en píxeles | `width=600` |
| `height` | Alto de la imagen en píxeles | `height=400` |
| `grid` | Mostrar/ocultar la cuadrícula | `grid=false` |
| `degreeMode` | Modo de ángulos | `degreeMode=degrees` |

**Ejemplo con configuración:**
````
```desmos-graph
left=-2; right=4; bottom=-1; top=5;
width=500; height=400;
---
y=x^2
```
````

```desmos-graph
left=-2; right=4; bottom=-1; top=5;
width=500; height=400;
---
y=x^2
```

> 💡 **Consejo de tamaño:** Para notas de estudio usa `width=500; height=400`. Para gráficas cuadradas (plano xy) usa `width=500; height=500`.

---

## 3. ECUACIONES — SINTAXIS LaTeX

Las ecuaciones usan **formato LaTeX matemático**. Ejemplos de lo más común:

| Lo que quieres | Código a escribir |
|----------------|-------------------|
| $y = x^2$ | `y=x^2` |
| $y = \sqrt{x}$ | `y=\sqrt{x}` |
| $y = \frac{1}{x}$ | `y=\frac{1}{x}` |
| $y = e^x$ | `y=e^x` |
| $y = \sin(x)$ | `y=\sin(x)` |
| $y = \ln(x)$ | `y=\ln(x)$ |
| $x^2 + y^2 = 1$ | `x^2+y^2=1` (circunferencia) |
| $x = 2$ | `x=2` (línea vertical) |
| $y = 3$ | `y=3` (línea horizontal) |

**Ejemplo con múltiples ecuaciones:**
````
```desmos-graph
left=-5; right=5; bottom=-3; top=3;
---
y=\sin(x)
y=\cos(x)
y=\frac{1}{2}x
```
````

```desmos-graph
left=-5; right=5; bottom=-3; top=3;
---
y=\sin(x)
y=\cos(x)
y=\frac{1}{2}x
```

---

## 4. COLORES DISPONIBLES

Después de la ecuación, agrega `|COLOR` para cambiar el color de la curva.

| Nombre | Color |
|--------|-------|
| `RED` | Rojo |
| `BLUE` | Azul |
| `GREEN` | Verde |
| `ORANGE` | Naranja |
| `PURPLE` | Morado |
| `YELLOW` | Amarillo |
| `MAGENTA` | Magenta |
| `CYAN` | Cian |
| `BLACK` | Negro |
| `WHITE` | Blanco |
| `#42ddf5` | Cualquier color hexadecimal |
| `#a5d8ff` | Azul claro (útil para rellenos) |
| `#b2f2bb` | Verde claro |
| `#ffd8a8` | Naranja claro |
| `#d0bfff` | Morado claro |

**Ejemplo con colores:**
````
```desmos-graph
left=-4; right=4; bottom=-2; top=5;
---
y=x^2|RED
y=x+1|BLUE
y=\sqrt{x}|GREEN
y=-x^2+4|PURPLE
```
````

```desmos-graph
left=-4; right=4; bottom=-2; top=5;
---
y=x^2|RED
y=x+1|BLUE
y=\sqrt{x}|GREEN
y=-x^2+4|PURPLE
```

---

## 5. ESTILOS DE LÍNEA

Puedes combinar color y estilo en cualquier orden, separados por `|`:

| Estilo | Descripción |
|--------|-------------|
| `SOLID` | Línea continua (por defecto) |
| `DASHED` | Línea discontinua |
| `DOTTED` | Línea punteada |

**Ejemplo:**
````
```desmos-graph
left=-3; right=3; bottom=-1; top=4;
---
y=x^2|BLUE|SOLID
y=x^2+1|RED|DASHED
y=x^2+2|GREEN|DOTTED
```
````

```desmos-graph
left=-3; right=3; bottom=-1; top=4;
---
y=x^2|BLUE|SOLID
y=x^2+1|RED|DASHED
y=x^2+2|GREEN|DOTTED
```

---

## 6. RESTRICCIONES — LIMITAR EL DOMINIO

Para graficar solo en un rango, agrega la restricción como condición en el `|`:

**Sintaxis:** `ecuación|condición`

| Ejemplo | Resultado |
|---------|-----------|
| `y=x^2\|0<=x<=3` | Parabola solo entre x=0 y x=3 |
| `y=\sqrt{x}\|x>=0` | Raíz solo donde está definida |
| `x=2\|0<=y<=5` | Línea vertical solo entre y=0 y y=5 |
| `y=\sin(x)\|-3<=x<=0` | Seno solo en parte negativa |

**Ejemplo práctico:**
````
```desmos-graph
left=-1; right=4; bottom=-1; top=4;
---
y=x|0<=x<=1|RED
y=2-x|0<=x<=1|BLUE
x=0|0<=y<=2|BLACK|DASHED
```
````

```desmos-graph
left=-1; right=4; bottom=-1; top=4;
---
y=x|0<=x<=1|RED
y=2-x|0<=x<=1|BLUE
x=0|0<=y<=2|BLACK|DASHED
```

---

## 7. COLOREAR ÁREAS — REGIONES SOMBREADAS

Para sombrear una región, usa una **inecuación** en lugar de una ecuación.

| Inecuación | Región sombreada |
|------------|-----------------|
| `y<x^2` | Debajo de la parábola |
| `y>x` | Encima de la recta y=x |
| `x^2+y^2<4` | Interior del círculo radio 2 |
| `y>x \| y<2` | Intersección de dos regiones |

Para sombrear la intersección de varias condiciones, ponlas todas en **una sola línea** separadas por `\|`:

````
```desmos-graph
left=-0.5; right=1.5; bottom=-0.5; top=2.5;
width=500; height=500;
---
y=x|0<=x<=1|RED
y=2-x|0<=x<=1|BLUE
y<2-x|y>x|x>=0|x<=1|#a5d8ff
```
````

```desmos-graph
left=-0.5; right=1.5; bottom=-0.5; top=2.5;
width=500; height=500;
---
y=x|0<=x<=1|RED
y=2-x|0<=x<=1|BLUE
y<2-x|y>x|x>=0|x<=1|#a5d8ff
```

> ⚠️ **Importante:** Las áreas de color por defecto son semitransparentes en Desmos. Para colores suaves de relleno usa colores hexadecimales claros como `#a5d8ff`, `#b2f2bb`, `#ffd8a8`, `#d0bfff`.

---

## 8. PUNTOS Y ETIQUETAS

Puedes graficar puntos individuales y ponerles etiqueta:

| Sintaxis | Descripción |
|----------|-------------|
| `(1,2)` | Punto sólido en (1,2) |
| `(1,2)\|OPEN` | Punto hueco (círculo abierto) |
| `(1,2)\|CROSS` | Punto en forma de cruz |
| `(1,2)\|label:texto` | Punto con etiqueta |
| `(1,2)\|OPEN\|label:(1,2)` | Combinación de estilo y etiqueta |

**Ejemplo:**
````
```desmos-graph
left=-1; right=3; bottom=-1; top=3;
---
y=x^2|BLUE
(0,0)|label:(0,0)|BLACK
(1,1)|label:(1,1)|RED
(2,4)|OPEN|label:(2,4)|GREEN
```
````

```desmos-graph
left=-1; right=3; bottom=-1; top=3;
---
y=x^2|BLUE
(0,0)|label:(0,0)|BLACK
(1,1)|label:(1,1)|RED
(2,4)|OPEN|label:(2,4)|GREEN
```

---

## 9. ECUACIONES OCULTAS (helper variables)

A veces defines una función para usarla en otra, sin querer graficarla directamente:

````
```desmos-graph
left=-3; right=3; bottom=-2; top=5;
---
f(x)=x^2|hidden
f'(x)|BLUE
```
````

```desmos-graph
left=-3; right=3; bottom=-2; top=5;
---
f(x)=x^2|hidden
f'(x)|BLUE
```

Aquí `f(x)=x^2` se define pero no se dibuja; solo se grafica su derivada $f'(x) = 2x$.

---

## 10. EJEMPLOS COMPLETOS PARA PROBABILIDAD

### Región triangular (dominio de una PDF conjunta)
````
```desmos-graph
left=-0.2; right=1.5; bottom=-0.2; top=2.5;
width=500; height=500;
---
y=x|0<=x<=1|RED|SOLID
y=2-x|0<=x<=1|BLUE|SOLID
x=0|0<=y<=2|BLACK|DASHED
y<2-x|y>x|x>=0|x<=1|#a5d8ff
(0,0)|label:(0,0)|BLACK
(1,1)|label:(1,1)|RED
(0,2)|label:(0,2)|BLUE
```
````

```desmos-graph
left=-0.2; right=1.5; bottom=-0.2; top=2.5;
width=500; height=500;
---
y=x|0<=x<=1|RED|SOLID
y=2-x|0<=x<=1|BLUE|SOLID
x=0|0<=y<=2|BLACK|DASHED
y<2-x|y>x|x>=0|x<=1|#a5d8ff
(0,0)|label:(0,0)|BLACK
(1,1)|label:(1,1)|RED
(0,2)|label:(0,2)|BLUE
```

### Región entre curva y recta (para cálculo de probabilidades)
````
```desmos-graph
left=-0.1; right=1.3; bottom=-0.1; top=1.3;
width=500; height=500;
---
y=x|0<=x<=1|RED|SOLID
y=\sqrt{x}|0<=x<=1|GREEN|SOLID
y<\sqrt{x}|y>x|0<=x<=1|#b2f2bb
(0,0)|label:(0,0)|BLACK
(1,1)|label:(1,1)|BLACK
```
````

```desmos-graph
left=-0.1; right=1.3; bottom=-0.1; top=1.3;
width=500; height=500;
---
y=x|0<=x<=1|RED|SOLID
y=\sqrt{x}|0<=x<=1|GREEN|SOLID
y<\sqrt{x}|y>x|0<=x<=1|#b2f2bb
(0,0)|label:(0,0)|BLACK
(1,1)|label:(1,1)|BLACK
```

### Densidad marginal con media marcada
````
```desmos-graph
left=-0.2; right=1.2; bottom=-0.1; top=1.8;
width=600; height=400;
---
f(x)=6x(1-x)|0<=x<=1|BLUE|SOLID
x=0.5|0<=y<=1.5|GREEN|DASHED
(0.5,0)|label:mu=0.5|GREEN
```
````

```desmos-graph
left=-0.2; right=1.2; bottom=-0.1; top=1.8;
width=600; height=400;
---
f(x)=6x(1-x)|0<=x<=1|BLUE|SOLID
x=0.5|0<=y<=1.5|GREEN|DASHED
(0.5,0)|label:mu=0.5|GREEN
```

---

## 11. RESUMEN RÁPIDO — CHEATSHEET

```
```desmos-graph
left=; right=; bottom=; top=;     ← límites del plano
width=; height=;                   ← tamaño imagen en px
grid=false;                        ← ocultar cuadrícula
degreeMode=degrees;                ← cambiar a grados
---
y=ecuacion                         ← curva básica
y=ecuacion|COLOR                   ← con color
y=ecuacion|COLOR|DASHED            ← con estilo
y=ecuacion|0<=x<=1|COLOR           ← con restricción
y<ecuacion|y>otra|COLOR_HEX        ← área sombreada
(x0,y0)|label:texto|COLOR          ← punto etiquetado
f(x)=ecuacion|hidden               ← función oculta
```
```
```

---

## 12. RECURSOS PARA SEGUIR PRACTICANDO





| Recurso | URL | Para qué sirve |
|---------|-----|----------------|
| 🔧 **Desmos Calculator** | https://www.desmos.com/calculator | Probar gráficas en vivo antes de poner en Obsidian |
| 📚 **Learn Desmos** | https://learn.desmos.com | Tutoriales oficiales paso a paso |
| 🧪 **Activity Builder** | https://teacher.desmos.com/activitybuilder/public | Ejemplos de la comunidad |
| 📖 **API Docs** | https://www.desmos.com/api/v1.9/docs/index.html | Documentación técnica completa |
| 💬 **Reddit r/desmos** | https://www.reddit.com/r/desmos | Comunidad con gráficas avanzadas |
| 🔌 **Plugin GitHub** | https://github.com/nigecat/obsidian-desmos | Código fuente y sintaxis del plugin |

> 💡 **Flujo recomendado:** Construye y prueba la gráfica en **desmos.com/calculator** → cuando te quede bien, copia las ecuaciones al bloque `desmos-graph` en Obsidian.
