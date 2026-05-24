# INSTRUCCIONES PARA NOTEBOOKLM: Generación de Código Desmos para Obsidian

## PROPÓSITO DE ESTE DOCUMENTO

Este documento le enseña a NotebookLM cómo generar bloques de código Desmos compatibles con el plugin `obsidian-desmos`. Cuando el usuario pida graficar una ecuación o ejercicio, NotebookLM debe responder con un bloque de código listo para copiar y pegar en Obsidian, NO con una imagen ni un enlace externo.

---

## REGLA PRINCIPAL

Cuando el usuario pida una gráfica, siempre responde con un bloque de código en este formato exacto:

```
```desmos-graph
[configuración]
---
[ecuaciones]
```
```

El bloque SIEMPRE comienza con ` ```desmos-graph ` y termina con ` ``` `.

---

## ESTRUCTURA DEL BLOQUE

Un bloque Desmos tiene dos secciones separadas por `---`:

**Sección 1 (antes del `---`): Configuración del plano**
**Sección 2 (después del `---`): Ecuaciones, curvas, puntos**

Si no se necesita configuración, se puede omitir el `---` y poner solo ecuaciones.

### Parámetros de configuración disponibles

| Parámetro | Qué hace | Valor típico |
|-----------|----------|--------------|
| `left` | Límite izquierdo del eje x | `-5` |
| `right` | Límite derecho del eje x | `5` |
| `bottom` | Límite inferior del eje y | `-3` |
| `top` | Límite superior del eje y | `3` |
| `width` | Ancho en píxeles | `500` |
| `height` | Alto en píxeles | `400` |
| `grid` | Mostrar cuadrícula | `true` o `false` |
| `degreeMode` | Modo ángulos | `degrees` o `radians` |

Los parámetros se separan con `;` o saltos de línea.

---

## SINTAXIS DE ECUACIONES

Las ecuaciones usan formato LaTeX matemático estándar.

### Ecuaciones básicas

| Matemática | Código a escribir |
|------------|-------------------|
| y = x² | `y=x^2` |
| y = √x | `y=\sqrt{x}` |
| y = 1/x | `y=\frac{1}{x}` |
| y = eˣ | `y=e^x` |
| y = sin(x) | `y=\sin(x)` |
| y = cos(x) | `y=\cos(x)` |
| y = ln(x) | `y=\ln(x)` |
| x² + y² = r² | `x^2+y^2=r^2` (circunferencia) |
| x = a | `x=a` (línea vertical) |
| y = b | `y=b` (línea horizontal) |

### Funciones definidas por el usuario

Se puede definir una función y luego usarla:

```
f(x)=2x+1
g(x)=x^2-3
```

Para graficar la derivada de una función definida:
```
f(x)=x^2|hidden
f'(x)|BLUE
```

El modificador `|hidden` oculta la curva base pero la mantiene disponible para usar.

---

## MODIFICADORES — COLOR, ESTILO Y RESTRICCIONES

Después de cada ecuación se agregan modificadores separados por `|`. El orden no importa.

### Colores disponibles

```
|RED       → Rojo
|BLUE      → Azul
|GREEN     → Verde
|ORANGE    → Naranja
|PURPLE    → Morado
|YELLOW    → Amarillo
|MAGENTA   → Magenta
|CYAN      → Cian
|BLACK     → Negro
|WHITE     → Blanco
|#42ddf5   → Cualquier color hexadecimal
```

Colores claros recomendados para rellenos de área:
- `#a5d8ff` → Azul claro
- `#b2f2bb` → Verde claro
- `#ffd8a8` → Naranja claro
- `#d0bfff` → Morado claro

### Estilos de línea

```
|SOLID     → Línea continua (por defecto)
|DASHED    → Línea discontinua
|DOTTED    → Línea punteada
```

### Restricción de dominio

Para graficar solo en un rango de x o y:

```
y=x^2|0<=x<=3            → Parábola solo entre x=0 y x=3
y=\sqrt{x}|x>=0          → Raíz solo donde está definida
x=2|0<=y<=5              → Línea vertical entre y=0 y y=5
y=\sin(x)|-3<=x<=0       → Seno en parte negativa
```

### Combinación de modificadores

Se pueden combinar en cualquier orden:
```
y=x^2|RED|DASHED|0<=x<=3
```

---

## ÁREAS SOMBREADAS (INECUACIONES)

Para sombrear una región, usar una inecuación en lugar de ecuación. Para sombrear la **intersección** de varias condiciones, ponerlas todas en una sola línea separadas por `|`:

```
y<x^2                         → Debajo de la parábola
y>x                           → Encima de y=x
x^2+y^2<4                     → Interior del círculo radio 2
y<2-x|y>x|x>=0|x<=1|#a5d8ff  → Intersección con color
```

**Nota importante:** Para rellenos usar siempre colores hexadecimales claros (`#a5d8ff`, `#b2f2bb`, `#ffd8a8`, `#d0bfff`) porque los colores con nombre salen demasiado saturados en áreas.

---

## PUNTOS Y ETIQUETAS

```
(1,2)                      → Punto sólido en (1,2)
(1,2)|OPEN                 → Punto hueco (límite excluido)
(1,2)|CROSS                → Punto en cruz
(1,2)|label:texto          → Punto con etiqueta
(1,2)|OPEN|label:(1,2)     → Combinación estilo + etiqueta
```

---

## EJEMPLOS COMPLETOS LISTOS PARA COPIAR

### Ejemplo 1: Función cuadrática simple

```desmos-graph
left=-4; right=4; bottom=-2; top=6;
width=500; height=400;
---
y=x^2|BLUE
```

### Ejemplo 2: Varias funciones con colores

```desmos-graph
left=-5; right=5; bottom=-3; top=3;
width=500; height=400;
---
y=\sin(x)|BLUE|SOLID
y=\cos(x)|RED|DASHED
y=\frac{1}{2}x|GREEN|DOTTED
```

### Ejemplo 3: Región sombreada entre dos curvas

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

### Ejemplo 4: Región triangular (útil para probabilidad conjunta)

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

### Ejemplo 5: Función con derivada

```desmos-graph
left=-3; right=3; bottom=-5; top=5;
width=500; height=400;
---
f(x)=x^3-3x|hidden
f(x)|BLUE|SOLID
f'(x)|RED|DASHED
```

### Ejemplo 6: Densidad de probabilidad con media marcada

```desmos-graph
left=-0.2; right=1.2; bottom=-0.1; top=1.8;
width=600; height=400;
---
f(x)=6x(1-x)|0<=x<=1|BLUE|SOLID
x=0.5|0<=y<=1.5|GREEN|DASHED
(0.5,0)|label:mu=0.5|GREEN
```

---

## CÓMO RESPONDER CUANDO EL USUARIO PIDE UNA GRÁFICA

Cuando el usuario presente un ejercicio y pida graficarlo, NotebookLM debe:

1. **Identificar** qué curvas, regiones o puntos hay que representar.
2. **Calcular** los límites adecuados del plano (que todas las curvas queden visibles con un poco de margen).
3. **Asignar** colores distintos a cada curva para que se diferencien claramente.
4. **Generar** el bloque `desmos-graph` completo.
5. **Explicar brevemente** qué representa cada línea del bloque (opcional pero útil).

### Reglas de buenas prácticas al generar código

- Usar `width=500; height=400` para funciones regulares y `width=500; height=500` para regiones en plano cuadrado (x e y con misma escala).
- Usar restricciones de dominio siempre que la función tenga un dominio natural limitado.
- Usar colores hexadecimales claros para rellenos de área, nunca colores con nombre para inecuaciones.
- Etiquetar los puntos clave (intersecciones, vértices, extremos) con `|label:`.
- Si hay más de una curva, usar colores distintos y mencionar qué color corresponde a qué función.

---

## PLANTILLA UNIVERSAL

Cuando no se sabe qué tamaño usar, esta plantilla sirve como punto de partida:

```
```desmos-graph
left=-5; right=5; bottom=-5; top=5;
width=500; height=500;
---
[ecuaciones aquí]
```
```

---

## RESUMEN DE TODA LA SINTAXIS EN UNA LÍNEA

```
y=ecuacion|COLOR|ESTILO|restriccion    → curva con todo
y<ecuacion|y>otra|0<=x<=1|#hexcolor    → área sombreada con restricción
(x,y)|OPEN|label:texto|COLOR           → punto con estilo y etiqueta
f(x)=ecuacion|hidden                   → función oculta reutilizable
```
