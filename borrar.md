


1. Formar una comparación con cero:

$$
\frac{P(x)}{Q(x)} > 0
$$

(o la desigualdad correspondiente).

2. Factorizar totalmente \(P\) y \(Q\):

$$
\frac{
(x-a_1)(x-a_2)\cdots(x-a_k)
}{
(x-b_1)(x-b_2)\cdots(x-b_j)
}
>0
$$

3. Representar en la recta real los valores

$$
a_1,\;a_2,\;\ldots,\;a_k,\;b_1,\;b_2,\;\ldots,\;b_j
$$

quedando definidos \(n\) intervalos:

```desmos-graph
left=-1; right=11; bottom=-1; top=1;
width=500; height=120;
---
y=0 \{0<x<2\}|#ff7b7b
y=0 \{2<x<5\}|#ff7b7b
y=0 \{5<x<8\}|#ff7b7b
y=0 \{8<x<10\}|#ff7b7b

(2,0)|OPEN|label:a_1|#ff7b7b
(5,0)|OPEN|label:a_2|#ff7b7b
(8,0)|OPEN|label:b_1|#ff7b7b
(10,0)|OPEN|label:b_2|#ff7b7b
````

Intervalos:

$$  
I_1,;I_2,;I_3,;\ldots,;I_k  
$$

4. **Prueba de signos**
    

De (I_1) se toma un valor cualquiera (no extremo) y se prueban los signos sustituyendo en cada factor.

Ejemplo:

 $$  
\frac{(+)(-)(+)}{(-)(+)(+)}

(+)  
$$

o

$$  
\frac{(+)(-)(+)}{(-)(+)(+)}

(-)  
$$

5. Resultan dos posibilidades:
    

- Si la desigualdad es verdadera en el intervalo analizado, entonces:
    

$$  
I_i \subset C_s  
$$

- Si la desigualdad es falsa en el intervalo analizado, entonces:
    

$$  
I_i \not\subset C_s  
$$

6. Repetir el procedimiento para los demás intervalos:
    

$$  
I_2,;I_3,;\ldots  
$$

7. El conjunto solución buscado se obtiene mediante la unión de todos los intervalos que verifican la inecuación:
    

$$  
C_s=\bigcup I_i  
$$

donde la unión se realiza únicamente sobre los intervalos válidos.








```

Hay una parte de los signos de ejemplo que en la fotografía no se distingue con total nitidez. La estructura y los pasos sí son legibles, pero si quieres una transcripción 100% fiel puedo continuar con los ejemplos de la página siguiente, donde el método se aplica completamente.
```