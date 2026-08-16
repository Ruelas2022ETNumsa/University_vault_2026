Para demostrar la igualdad **$EE(Y|X) \= EY$** (conocida como la **Ley de Esperanza Total** o **Esperanza Iterada**) para variables aleatorias discretas, utilizaremos las definiciones y propiedades encontradas en las fuentes 1-4.

### Demostración paso a paso:

**1\. Definición de la esperanza condicional:**La esperanza condicional de $Y$ dado que $X$ toma un valor específico $x$ se define como el promedio ponderado de los valores de $Y$ bajo la probabilidad condicional 1, 5, 6:$$EY | X \= x \= \\sum\_{y} y \\cdot P(Y \= y | X \= x)$$  
**2\. $EY|X$ como una variable aleatoria:**Debemos entender que $EY|X$ es en sí misma una **variable aleatoria** que es función de $X$. Toma el valor $EY | X \= x$ con una probabilidad igual a $P(X \= x)$ 1, 3, 7\.  
**3\. Aplicación de la esperanza a la función $EY|X$:**Por la definición de esperanza para una función de una variable aleatoria discreta, sumamos sus valores posibles multiplicados por sus respectivas probabilidades 2, 4, 8:$$E\[EY|X\] \= \\sum\_{x} EY|X \= x \\cdot P(X \= x)$$  
**4\. Sustitución y desarrollo:**Sustituimos la definición del paso 1 en la ecuación del paso 3 2, 4:$$E\[EY|X\] \= \\sum\_{x} \\left( \\sum\_{y} y \\cdot P(Y \= y | X \= x) \\right) P(X \= x)$$$$E\[EY|X\] \= \\sum\_{x} \\sum\_{y} y \\cdot P(Y \= y | X \= x) \\cdot P(X \= x)$$  
**5\. Uso de la probabilidad conjunta:**Recordamos la propiedad fundamental de la probabilidad condicional: $P(Y=y | X=x) \\cdot P(X=x) \= P(X=x, Y=y)$, que representa la probabilidad conjunta de que ambos eventos ocurran simultáneamente 9-11:$$E\[EY|X\] \= \\sum\_{x} \\sum\_{y} y \\cdot P(X \= x, Y \= y)$$  
**6\. Reordenamiento de las sumas:**Cambiamos el orden de la sumatoria para agrupar los términos de $Y$ 2, 4:$$E\[EY|X\] \= \\sum\_{y} y \\cdot \\left( \\sum\_{x} P(X \= x, Y \= y) \\right)$$  
**7\. Identificación de la distribución marginal:**La suma de la probabilidad conjunta sobre todos los valores posibles de $X$ resulta en la **distribución marginal** de $Y$, es decir, $P(Y \= y)$ 11-13:$$E\[EY|X\] \= \\sum\_{y} y \\cdot P(Y \= y)$$  
**8\. Conclusión:**La expresión final es, por definición, la esperanza matemática de $Y$ 2, 4:$$E\[EY|X\] \= EY$$  
**Resumen conceptual:** Esta igualdad indica que para hallar el promedio global de $Y$, puedes primero calcular el promedio de $Y$ dentro de cada grupo definido por $X$ y luego sacar el promedio de esos resultados grupales 4, 14\.  
