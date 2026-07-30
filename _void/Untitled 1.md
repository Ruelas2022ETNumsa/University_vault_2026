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