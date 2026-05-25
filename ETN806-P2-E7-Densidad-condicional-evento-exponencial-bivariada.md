---
title: "ETN806 — Práctica 2 — E7: Densidad condicional dado evento A — exponencial bivariada"
aliases: [E7a, P2-E7]
tags: [ETN806, practica2, variables-aleatorias-multiples, densidad-condicional, exponencial-bivariada, evento]
materia: Procesos Estocásticos (ETN806)
parcial: 2do Parcial
tipo: ejercicio-practica
fuente: Práctica 2
fecha: 2026-05-25
estado: revisado
temas: [densidad-condicional, probabilidad-evento, region-triangular, exponencial-bivariada]
---

*   **E7.** Las variables aleatorias $X, Y$ tienen la función de densidad 
    de distribución de probabilidad conjunta que se indica:
    $$f_{X,Y}(x,y) = \begin{cases} 6e^{-(2x+3y)} & \text{si } x \ge 0, y \ge 0 \\ 0 & \text{en otro caso} \end{cases}$$
    Determine la función de densidad de distribución condicional $f_{X,Y|A}(x,y)$, sabiendo que $A$ es el evento dado por la expresión $x+y \le 1$ y que la densidad condicional es igual a la densidad conjunta dividida entre la probabilidad del evento $A$ para el rango $(x,y) \in A$.

Para resolver el **Ejercicio E7** de la **Práctica 2**, seguiremos el procedimiento para determinar una función de densidad condicional dado un evento específico $A$, utilizando las propiedades de las funciones de densidad conjunta y el cálculo de probabilidades en regiones del plano.

### 1. Definición de la región y la función

La función de densidad conjunta está dada por $f_{X,Y}(x,y) = 6e^{-(2x+3y)}$ para el primer cuadrante ($x, y \ge 0$). El evento $A$ corresponde a la región triangular delimitada por las desigualdades $x \ge 0, y \ge 0$ y $x+y \le 1$.

Para hallar la densidad condicional, la fórmula establecida es: $$f_{X,Y|A}(x,y) = \frac{f_{X,Y}(x,y)}{P[A]}, \quad \text{si } (x,y) \in A$$ Y es igual a $0$ en cualquier otro caso.

### 2. Cálculo de la probabilidad del evento $A$ ($P[A]$)

La probabilidad del evento $A$ se obtiene integrando la función de densidad conjunta sobre la región triangular descrita:

$$P[A] = \int_{0}^{1} \int_{0}^{1-x} 6e^{-(2x+3y)} , dy , dx$$

- **Integración interna (respecto a $y$):** Separamos los términos exponenciales: $6e^{-2x} \int_{0}^{1-x} e^{-3y} , dy$. La integral de $e^{-3y}$ es $\left[ \frac{e^{-3y}}{-3} \right]_0^{1-x} = -\frac{1}{3}(e^{-3(1-x)} - e^{0}) = \frac{1}{3}(1 - e^{3x-3})$. Multiplicando por la constante: $6e^{-2x} \cdot \frac{1}{3}(1 - e^{3x-3}) = 2e^{-2x} - 2e^{x-3}$.
    
- **Integración externa (respecto a $x$):** $\int_{0}^{1} (2e^{-2x} - 2e^{x-3}) , dx = \left[ -e^{-2x} - 2e^{x-3} \right]_0^1$. Evaluando en los límites: En $x=1$: $-e^{-2} - 2e^{-2} = -3e^{-2}$. En $x=0$: $-e^{0} - 2e^{-3} = -1 - 2e^{-3}$. Restando los valores: $(-3e^{-2}) - (-1 - 2e^{-3}) = \mathbf{1 - 3e^{-2} + 2e^{-3}}$.

> [!correction] Corrección — evaluación en $x=1$
> **Error identificado:** El archivo escribía $-e^{-2} - 2e^{0}$ en $x=1$, confundiendo $e^{x-3}\big|_{x=1} = e^{-2}$ con $e^{0}$.
>
> **Corrección:** $e^{x-3}\big|_{x=1} = e^{1-3} = e^{-2}$, por lo que el valor correcto es $-e^{-2} - 2e^{-2} = -3e^{-2}$. El resultado final $P[A]=1-3e^{-2}+2e^{-3}$ era correcto aunque el paso intermedio estaba mal.
    

### 3. Función de densidad condicional final

Sustituimos el valor de $P[A]$ en la definición de la densidad condicional para obtener el resultado:

$$\mathbf{f_{X,Y|A}(x,y) = \begin{cases} \frac{6e^{-(2x+3y)}}{1 - 3e^{-2} + 2e^{-3}} & \text{si } x \ge 0, y \ge 0, x+y \le 1 \ 0 & \text{en otro caso} \end{cases}}$$

_Nota: El valor numérico de la constante de normalización es aproximadamente $1/0.6936 \approx 1.442$._

> [!check] Correcto
> Fórmula del formulario aplicada correctamente: $f_{X,Y|A}=f_{X,Y}/P[A]$ para $(x,y)\in A$, cero fuera. $P[A]=1-3e^{-2}+2e^{-3}\approx 0.6936$ ✓.

---

### Gráfica en Desmos

La gráfica representa la región de soporte $A$ (el triángulo) donde la densidad condicional es distinta de cero.

```desmos-graph
left=-0.2; right=1.3; bottom=-0.2; top=1.3;
width=500; height=500;
---
x+y<=1|x>=0|y>=0|#a5d8ff
y=1-x|BLUE|0<=x<=1
(0,0)|label:(0,0)|BLACK
(1,0)|label:(1,0)|BLACK
(0,1)|label:(0,1)|BLACK
```

> [!correction] Corrección — Gráfica
> **Error identificado:** Faltaban parámetros de ventana. Las líneas `x=0` e `y=0` usan variables distintas de $x$ e $y$ en Desmos y pueden causar error.
>
> **Corrección:** Se agregaron `left=-0.2; right=1.3; bottom=-0.2; top=1.3;` y se eliminaron `x=0|BLUE` e `y=0|BLUE` (los ejes de Desmos ya los muestran por defecto).

**Explicación de la gráfica:**

- **Área sombreada (#a5d8ff):** Representa el dominio del evento $A$ ($x+y \le 1$) donde la variable aleatoria condicionada tiene probabilidad definida.
- **Líneas Azules:** Son las fronteras que delimitan el triángulo de soporte en el primer cuadrante.
- **Puntos etiquetados:** Indican los vértices de la región de integración utilizada para calcular $P[A]$.