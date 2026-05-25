---
title: "ETN806 — Práctica 2 — Enunciados Variables Aleatorias Continuas Múltiples"
aliases: [Practica2, practica-ii]
tags: [ETN806, practica2, enunciados, variables-aleatorias-multiples, 2do-parcial]
materia: Procesos Estocásticos (ETN806)
parcial: 2do Parcial
tipo: enunciados
fecha: 2026-05-25
estado: activo
temas: [normalizacion, independencia, varianza, marginal, densidad-condicional, pdf-multivariable]
---

Aquí tienes los enunciados completos de los ejercicios que conforman la 
**PRACTICA Nº2** de **PROCESOS ESTOCASTICOS**, la cual se enfoca en 
variables aleatorias continuas múltiples:

*   **E1.** Encontrar el valor de $k$ en la siguiente función 
    $f_{X,Y}(x,y)$ y también la función de distribución marginal de $X$:
    $$f_{X,Y}(x,y) = \begin{cases} \frac{k}{(1+x+y)^4} & \text{si } 0 \le x \le \infty; 0 \le y \le \infty \\ 0 & \text{en otro caso} \end{cases}$$

*   **E2.** Determinar si las variables aleatorias $U$ y $V$ son 
    estadísticamente independientes sabiendo que su función de densidad 
	de distribución conjunta está dada por:
    $$f_{U,V}(u,v) = \begin{cases} 24uv & \text{si } u \ge 0; v \ge 0; u+v \le 1 \\ 0 & \text{en otro caso} \end{cases}$$

*   **E3.** Determinar si las variables aleatorias $X, Y$ cuya densidad 
    de distribución conjunta:
    $$f_{X,Y}(x,y) = \begin{cases} 4xy & \text{si } 0 \le x \le 1; 0 \le y \le 1 \\ 0 & \text{en otro caso} \end{cases}$$
    **a)** Son estadísticamente independientes.
    **b)** Calcular la varianza de $X+Y$.

*   **E4.** Las funciones aleatorias $X, Y$ tiene la función de densidad de
    distribución conjunta que se indica calcular la varianza de $W = X+Y$:
    $$f_{X,Y}(x,y) = \begin{cases} 2 & \text{si } x \ge 0, y \ge 0, x+y \le 1 \\ 0 & \text{en otro caso} \end{cases}$$

*   **E5.** Dada la función de densidad de distribución de probabilidad 
    conjunta como se indica a continuación:
    $$f_{W,X,Y,Z}(w,x,y,z) = \begin{cases} 16wxyz & \text{si } 0 \le w \le 1, 0 \le x \le 1, 0 \le y \le 1, 0 \le z \le 1 \\ 0 & \text{en otro caso} \end{cases}$$
    **a)** Hallar la probabilidad de $W \le 3$ y que $Y \le \frac{1}{2}$.
    **b)** Encontrar la función de densidad marginal de $W$.

*   **E6.** Las variables aleatorias $X, Y$ tiene la función de densidad de 
    distribución de probabilidad que se indica:
    $$f_{X,Y}(x,y) = \begin{cases} \frac{1}{2} & \text{si } -1 \le x \le 1, 0 \le y \le 1, |x| \ge y \\ 0 & \text{en otro caso} \end{cases}$$
    **a)** Dibujar la región de probabilidad distinta de cero.
    **b)** Determinar la función de densidad marginal de $X$.
    **c)** Determine $P(X > 0)$.
    **d)** Determinar el valor esperado de $X$.

*   **E7.** Las variables aleatorias $X, Y$ tienen la función de densidad 
    de distribución de probabilidad conjunta que se indica:
    $$f_{X,Y}(x,y) = \begin{cases} 6e^{-(2x+3y)} & \text{si } x \ge 0, y \ge 0 \\ 0 & \text{en otro caso} \end{cases}$$
    Determine la función de densidad de distribución condicional $f_{X,Y|A}(x,y)$, sabiendo que $A$ es el evento dado por la expresión $x+y \le 1$ y que la densidad condicional es igual a la densidad conjunta dividida entre la probabilidad del evento $A$ para el rango $(x,y) \in A$.