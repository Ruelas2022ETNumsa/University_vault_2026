---
title: "ETN806 — Formulario 2do Parcial — Variables Aleatorias Continuas Múltiples"
aliases: [Formulario806, formulario-2p]
tags: [ETN806, formulario, referencia, variables-aleatorias-multiples, 2do-parcial]
materia: Procesos Estocásticos (ETN806)
parcial: 2do Parcial
tipo: formulario
fecha: 2026-05-25
estado: activo
temas: [normalizacion, marginal, independencia, esperanza, varianza, covarianza, correlacion, densidad-condicional]
---

# 📋 FORMULARIO — PROCESOS ESTOCÁSTICOS

## Variables Aleatorias Continuas Múltiples

---

## 1. FUNCIÓN DE DENSIDAD DE PROBABILIDAD (1 variable)

### Propiedades

$$f(x) \geq 0$$

$$\int_{-\infty}^{\infty} f(x),dx = 1$$

### Probabilidad en un intervalo

$$P(a \leq X \leq b) = \int_{a}^{b} f(x),dx$$

> **Nota:** En variables continuas $P(X = a) = 0$

---

## 2. ESPERANZA MATEMÁTICA (1 variable)

$$E[X] = \mu_X = \int_{-\infty}^{\infty} x, f(x),dx$$

---

## 3. VARIANZA (1 variable)

$$VAR[X] = \int_{-\infty}^{\infty}(x - \mu_X)^2, f(x),dx$$

### Fórmula alternativa (más práctica)

$$VAR[X] = E[X^2] - \mu_X^2$$

donde: $$E[X^2] = \int_{-\infty}^{\infty} x^2, f(x),dx$$

---

## 4. DESVIACIÓN ESTÁNDAR (1 variable)

$$\sigma = \sqrt{VAR[X]}$$

---

## 5. FUNCIÓN DE DENSIDAD CONJUNTA (2 variables)

### Propiedades

$$f_{X,Y}(x,y) \geq 0$$

$$\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f_{X,Y}(x,y),dx,dy = 1$$

### Probabilidad en una región $R$

$$P\big((X,Y) \in R\big) = \iint_{R} f_{X,Y}(x,y),dx,dy$$

### Relación con la distribución acumulativa conjunta

$$f_{X,Y}(x,y) = \frac{\partial^2 F_{X,Y}(x,y)}{\partial x,\partial y}$$

---

## 6. FUNCIÓN DE DISTRIBUCIÓN ACUMULATIVA CONJUNTA

$$F_{X,Y}(x,y) = P{X \leq x,; Y \leq y} = \int_{-\infty}^{x}\int_{-\infty}^{y} f_{X,Y}(u,v),dv,du$$

### Propiedades

|Propiedad|Expresión|
|---|---|
|Rango|$0 \leq F_{X,Y}(x,y) \leq 1$|
|Marginal de X|$F_X(x) = F_{X,Y}(x,\infty)$|
|Marginal de Y|$F_Y(y) = F_{X,Y}(\infty,y)$|
|Límites inferiores|$F_{X,Y}(-\infty,y) = F_{X,Y}(x,-\infty) = 0$|
|Límite superior|$F_{X,Y}(\infty,\infty) = 1$|

---

## 7. DENSIDAD DE DISTRIBUCIÓN MARGINAL

$$\boxed{f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y),dy}$$

$$\boxed{f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y),dx}$$

---

## 8. INDEPENDENCIA ESTADÍSTICA

$X$ e $Y$ son **estadísticamente independientes** si y solo si:

$$\boxed{f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)}$$

> **Procedimiento:** Calcular $f_X(x)$ y $f_Y(y)$ por separado, multiplicarlas y verificar si el resultado es igual a $f_{X,Y}(x,y)$.

---

## 9. VALOR ESPERADO (2 variables)

Para $W = g(X,Y)$:

$$E[W] = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} g(X,Y), f_{X,Y}(x,y),dy,dx$$

### Linealidad de la esperanza

$$E[X + Y] = E[X] + E[Y]$$

---

## 10. VARIANZA Y COVARIANZA EN SUMA

### Varianza de la suma

$$VAR[X+Y] = VAR[X] + VAR[Y] + 2,E!\left[(X-\mu_X)(Y-\mu_Y)\right]$$

> Si $X$ e $Y$ son **independientes**: $;VAR[X+Y] = VAR[X] + VAR[Y]$

### Covarianza

$$COV[X,Y] = E!\left[(X - \mu_X)(Y - \mu_Y)\right]$$

### Fórmula alternativa (más práctica)

$$\boxed{COV[X,Y] = E[XY] - \mu_X,\mu_Y}$$

donde: $$E[XY] = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} x,y; f_{X,Y}(x,y),dy,dx$$

---

## 11. COEFICIENTE DE CORRELACIÓN

$$\boxed{\rho_{X,Y} = \frac{COV[X,Y]}{\sqrt{VAR[X]\cdot VAR[Y]}}}$$

$$-1 \leq \rho_{X,Y} \leq 1$$

|Valor de $\rho$|Interpretación|
|---|---|
|$\rho = 1$|Correlación positiva perfecta|
|$\rho = -1$|Correlación negativa perfecta|
|$\rho = 0$|No correlacionadas (si independientes)|

---

## 12. DENSIDAD DE DISTRIBUCIÓN CONDICIONAL

### Dado un evento $B$ con $P[B] > 0$

$$\boxed{f_{X,Y/B}(x,y) = \frac{f_{X,Y}(x,y)}{P[B]}, \quad (x,y) \in B}$$

$$f_{X,Y/B}(x,y) = 0, \quad \text{en otro caso}$$

### Dado la observación de otra variable

$$f_{X/Y}!\left(\frac{x}{y}\right) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$$

$$f_{Y/X}!\left(\frac{y}{x}\right) = \frac{f_{X,Y}(x,y)}{f_X(x)}$$

### Regla de la cadena (de ambas expresiones)

$$f_{X,Y}(x,y) = f_{X/Y}!\left(\frac{x}{y}\right) f_Y(y) = f_{Y/X}!\left(\frac{y}{x}\right) f_X(x)$$

---

## 13. RESUMEN — PASOS PARA RESOLVER EJERCICIOS

### Para hallar $k$

1. Plantear $\displaystyle\int!!\int f_{X,Y}(x,y),dx,dy = 1$
2. Integrar con los límites dados y despejar $k$

### Para hallar densidades marginales

1. $f_X(x)$: integrar $f_{X,Y}$ respecto a $y$ en su rango
2. $f_Y(y)$: integrar $f_{X,Y}$ respecto a $x$ en su rango

### Para verificar independencia

1. Calcular $f_X(x)$ y $f_Y(y)$
2. Verificar si $f_{X,Y}(x,y) \stackrel{?}{=} f_X(x)\cdot f_Y(y)$

### Para calcular $VAR[X+Y]$

1. Hallar $\mu_X = E[X]$ y $\mu_Y = E[Y]$
2. Hallar $E[X^2]$ y $E[Y^2]$
3. Calcular $VAR[X] = E[X^2] - \mu_X^2$ y $VAR[Y] = E[Y^2] - \mu_Y^2$
4. Calcular $COV[X,Y] = E[XY] - \mu_X\mu_Y$
5. Aplicar $VAR[X+Y] = VAR[X] + VAR[Y] + 2,COV[X,Y]$

### Para densidad condicional dado evento $B$

1. Calcular $P[B] = \displaystyle\iint_B f_{X,Y}(x,y),dx,dy$
2. Aplicar $f_{X,Y/B}(x,y) = \dfrac{f_{X,Y}(x,y)}{P[B]}$ para $(x,y)\in B$