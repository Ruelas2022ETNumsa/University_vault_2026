 **E2.** Determinar si las variables aleatorias $U$ y $V$ son 
    estadísticamente independientes sabiendo que su función de densidad 
	de distribución conjunta está dada por:
    $$f_{U,V}(u,v) = \begin{cases} 24uv & \text{si } u \ge 0; v \ge 0; u+v \le 1 \\ 0 & \text{en otro caso} \end{cases}$$
Para resolver el ejercicio **E2** de la **Práctica 2**, seguiremos el procedimiento establecido en los manuales para verificar la independencia estadística de dos variables aleatorias continuas.

### Paso 1: Definir la función y su región de soporte

La función de densidad conjunta es: $$f_{U,V}(u,v) = \begin{cases} 24uv & \text{si } u \ge 0; v \ge 0; u+v \le 1 \ 0 & \text{en otro caso} \end{cases}$$ La región donde la probabilidad es distinta de cero es un **triángulo** en el primer cuadrante delimitado por la recta $v = 1 - u$.

### Paso 2: Calcular la función de densidad marginal de $U$ ($f_U(u)$)

Para hallar la marginal de $U$, integramos la función conjunta respecto a $v$ sobre su rango de definición ($0 \le v \le 1-u$): $$f_U(u) = \int_{0}^{1-u} 24uv , dv$$ $f_U(u) = 24u \left[ \frac{v^2}{2} \right]_0^{1-u} = 12u(1-u)^2, \quad \text{para } 0 \le u \le 1.$

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario.

### Paso 3: Calcular la función de densidad marginal de $V$ ($f_V(v)$)

Dada la simetría de la función conjunta y de la región de soporte, el cálculo para $V$ es análogo integrando respecto a $u$ ($0 \le u \le 1-v$): $f_V(v) = \int_{0}^{1-v} 24uv \, du = 12v(1-v)^2, \quad \text{para } 0 \le v \le 1.$

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario.

### Paso 4: Verificar la condición de independencia

Dos variables son independientes si y solo si $f_{U,V}(u,v) = f_U(u) \cdot f_V(v)$ para todos los valores de su rango.

- Producto de las marginales: $[12u(1-u)^2] \cdot [12v(1-v)^2] = 144uv(1-u)^2(1-v)^2$.
- Función conjunta: $24uv$.

Claramente, **el producto de las marginales no es igual a la función conjunta** ($24uv \neq 144uv(1-u)^2(1-v)^2$).

**Conclusión:** Las variables aleatorias $U$ y $V$ **no son independientes**. Además, el hecho de que la región de soporte sea un triángulo (donde los límites de una variable dependen de la otra) es una prueba suficiente de que existe dependencia.

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario. La comparación $24uv \neq 144uv(1-u)^2(1-v)^2$ es correcta. La alerta sobre el dominio triangular como condición suficiente de dependencia también es correcta.

---

### Gráfica en Desmos

La gráfica representa la región triangular de soporte y las curvas de las densidades marginales calculadas.

```desmos-graph
left=-0.2; right=1.3; bottom=-0.2; top=1.3;
width=500; height=500;
---
x+y<=1|x>=0|y>=0|#a5d8ff
y=1-x|BLUE|0<=x<=1
f(x)=12x(1-x)^2|RED|0<=x<=1
(0,0)|label:(0,0)|BLACK
(1,0)|label:(1,0)|BLACK
(0,1)|label:(0,1)|BLACK
```

> [!correction] Corrección — Gráfica
> **Error identificado:** Faltaban los parámetros de ventana (`left`, `right`, `bottom`, `top`) antes del `---`.
>
> **Corrección:** Se agregaron `left=-0.2; right=1.3; bottom=-0.2; top=1.3;` para encuadrar correctamente el triángulo de soporte.

**Explicación de la gráfica:**

- **Área sombreada (#a5d8ff):** Representa el dominio del triángulo donde la densidad conjunta es $24uv$ ($u+v \le 1$).
- **Línea Roja ($f(x)$):** Representa la forma de las densidades marginales $12u(1-u)^2$ o $12v(1-v)^2$, mostrando que la probabilidad máxima no está en los extremos.
- **Puntos etiquetados:** Marcan los vértices de la región de soporte definida en el enunciado.