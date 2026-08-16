Para calcular el coeficiente de correlación lineal ($\\rho\_{XY}$) entre una variable aleatoria $X$ y su combinación lineal $Y \= aX \+ b$, utilizaremos las propiedades de la esperanza, la varianza y la covarianza descritas en las fuentes.

### 1\. Fórmula del Coeficiente de Correlación

El coeficiente de correlación se define como el cociente de la covarianza de las dos variables entre el producto de sus desviaciones estándar 1-3:$$\\rho\_{XY} \= \\frac{Cov(X, Y)}{\\sigma\_X \\sigma\_Y}$$

### 2\. Cálculo de la Covarianza $Cov(X, Y)$

Sustituyendo $Y \= aX \+ b$ en la fórmula de la covarianza y utilizando sus propiedades lineales 4-6:

* **Propiedad distributiva:** $Cov(X, aX \+ b) \= Cov(X, aX) \+ Cov(X, b)$.  
* **Constante:** La covarianza de una variable con una constante ($b$) es **0** 5\.  
* **Factor multiplicativo:** $Cov(X, aX) \= a \\cdot Cov(X, X)$.  
* **Relación con la varianza:** Como $Cov(X, X) \= Var(X)$, tenemos que 5, 7:$$Cov(X, Y) \= a \\cdot Var(X)$$

### 3\. Cálculo de las Desviaciones Estándar

* Para $X$: La desviación estándar es $\\sigma\_X \= \\sqrt{Var(X)}$ 2, 8\.  
* Para $Y$: Aplicando la propiedad de la varianza para combinaciones lineales, $Var(aX \+ b) \= a^2 Var(X)$ 4, 9, 10\. Por lo tanto:$$\\sigma\_Y \= \\sqrt{a^2 Var(X)} \= |a| \\sigma\_X$$

### 4\. Resultado Final

Sustituimos los valores obtenidos en la fórmula inicial:$$\\rho\_{XY} \= \\frac{a \\cdot Var(X)}{\\sigma\_X \\cdot |a| \\sigma\_X} \= \\frac{a \\cdot Var(X)}{|a| \\cdot Var(X)} \= \\frac{a}{|a|}$$  
Dependiendo del valor de la constante **$a$**, el resultado es 3, 11, 12:

* Si **$a \> 0$**, entonces $\\rho\_{XY} \= \\mathbf{1}$. Existe una relación lineal positiva perfecta.  
* Si **$a \< 0$**, entonces $\\rho\_{XY} \= \\mathbf{-1}$. Existe una relación lineal negativa perfecta.  
* Si **$a \= 0$**, $Y$ se convierte en una constante ($Y \= b$), su varianza es cero y la correlación no está definida o se considera cero en términos de dependencia 11\.

En conclusión, el coeficiente de correlación lineal entre $X$ y una transformación lineal de sí misma siempre será **1 o \-1**, dependiendo únicamente del **signo de la pendiente $a$** 3, 11\.  
