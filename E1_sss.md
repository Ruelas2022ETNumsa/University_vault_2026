La resolución está bien encaminada, pero está demasiado “compactada”.  
Para una entrega académica conviene separar más los pasos algebraicos y justificar cada integral.  
Además hay una pequeña parte que puede explicarse mucho mejor para que no parezca magia algebraica.

Esta sería una versión verdaderamente paso a paso:

---

# Resolución paso a paso

Dada la función:

[  
f_{X,Y}(x,y)=  
\begin{cases}  
\dfrac{k(1+x+y)}{(1+x)^4(1+y)^4}, & x\ge0,; y\ge0 \  
0, & \text{en otro caso}  
\end{cases}  
]

Se pide:

1. Encontrar (k)
    
2. Hallar la marginal (f_X(x))
    

---

# 1. Determinación de (k)

Para que una función sea densidad conjunta válida debe cumplirse:

[  
\int_0^\infty \int_0^\infty f_{X,Y}(x,y),dy,dx =1  
]

Sustituyendo la función:

[  
\int_0^\infty \int_0^\infty  
\dfrac{k(1+x+y)}{(1+x)^4(1+y)^4}  
,dy,dx  
=1  
]

Sacamos (k) fuera de la integral:

[  
k  
\int_0^\infty  
\int_0^\infty  
\dfrac{1+x+y}{(1+x)^4(1+y)^4}  
,dy,dx  
=1  
]

---

## Paso 1 — Separar el numerador

Observamos que:

[  
1+x+y=(1+x)+y  
]

Entonces:

# [  
\dfrac{1+x+y}{(1+x)^4(1+y)^4}

\dfrac{1+x}{(1+x)^4(1+y)^4}  
+  
\dfrac{y}{(1+x)^4(1+y)^4}  
]

Simplificando el primer término:

# [

\dfrac{1}{(1+x)^3(1+y)^4}  
+  
\dfrac{y}{(1+x)^4(1+y)^4}  
]

Entonces la integral queda:

[  
k\int_0^\infty  
\left[  
\int_0^\infty  
\dfrac{1}{(1+x)^3(1+y)^4},dy  
+  
\int_0^\infty  
\dfrac{y}{(1+x)^4(1+y)^4},dy  
\right]dx  
]

Factorizamos respecto a (x):

[  
k\int_0^\infty  
\left[  
\dfrac{1}{(1+x)^3}  
\int_0^\infty (1+y)^{-4}dy  
+  
\dfrac{1}{(1+x)^4}  
\int_0^\infty y(1+y)^{-4}dy  
\right]dx  
]

---

# Paso 2 — Resolver las integrales respecto a (y)

## Primera integral

[  
\int_0^\infty (1+y)^{-4}dy  
]

Integramos:

# [

\left[  
\dfrac{(1+y)^{-3}}{-3}  
\right]_0^\infty  
]

Evaluando:

# [

0-\left(-\dfrac13\right)  
=\dfrac13  
]

---

## Segunda integral

[  
\int_0^\infty y(1+y)^{-4}dy  
]

Usamos el cambio:

[  
u=1+y  
]

Entonces:

[  
du=dy  
]

y:

[  
y=u-1  
]

Cuando:

- (y=0 \Rightarrow u=1)
    
- (y\to\infty \Rightarrow u\to\infty)
    

La integral queda:

[  
\int_1^\infty (u-1)u^{-4}du  
]

Distribuyendo:

# [

\int_1^\infty  
(u^{-3}-u^{-4})du  
]

Integramos término a término:

# [

\left[  
-\dfrac1{2u^2}  
+\dfrac1{3u^3}  
\right]_1^\infty  
]

Evaluando:

# [

0-  
\left(  
-\dfrac12+\dfrac13  
\right)  
]

# [

\dfrac12-\dfrac13  
=\dfrac16  
]

---

# Paso 3 — Sustituir resultados

Reemplazamos:

[  
k\int_0^\infty  
\left[  
\dfrac1{(1+x)^3}\left(\dfrac13\right)  
+  
\dfrac1{(1+x)^4}\left(\dfrac16\right)  
\right]dx  
=1  
]

Sacamos factor común (\frac16):

[  
k\int_0^\infty  
\dfrac{2(1+x)+1}{6(1+x)^4}  
dx  
=1  
]

Simplificando:

# [

\dfrac{k}{6}  
\int_0^\infty  
\dfrac{2x+3}{(1+x)^4}  
dx  
]

---

# Paso 4 — Resolver la integral respecto a (x)

Escribimos:

[  
2x+3=2(1+x)+1  
]

Entonces:

[  
\dfrac{k}{6}  
\int_0^\infty  
\left[  
2(1+x)^{-3}  
+(1+x)^{-4}  
\right]dx  
]

Separando:

# [

\dfrac{k}{6}  
\left[  
2\int_0^\infty (1+x)^{-3}dx  
+  
\int_0^\infty (1+x)^{-4}dx  
\right]  
]

---

## Resolver cada integral

### Primera:

# [  
\int_0^\infty (1+x)^{-3}dx

# \left[  
\dfrac{(1+x)^{-2}}{-2}  
\right]_0^\infty

\dfrac12  
]

### Segunda:

# [  
\int_0^\infty (1+x)^{-4}dx

# \left[  
\dfrac{(1+x)^{-3}}{-3}  
\right]_0^\infty

\dfrac13  
]

---

# Paso 5 — Hallar (k)

Sustituyendo:

[  
\dfrac{k}{6}  
\left[  
2\left(\dfrac12\right)  
+\dfrac13  
\right]  
=1  
]

[  
\dfrac{k}{6}  
\left[  
1+\dfrac13  
\right]  
=1  
]

[  
\dfrac{k}{6}\left(\dfrac43\right)=1  
]

[  
\dfrac{2k}{9}=1  
]

Finalmente:

[  
\boxed{k=\dfrac92}  
]

---

# 2. Función marginal de (X)

La marginal se obtiene integrando respecto a (y):

[  
f_X(x)=  
\int_0^\infty  
f_{X,Y}(x,y),dy  
]

Sustituyendo (k=\frac92):

[  
f_X(x)=  
\int_0^\infty  
\dfrac{\frac92(1+x+y)}  
{(1+x)^4(1+y)^4}  
dy  
]

Usando el resultado ya calculado:

# [  
\int_0^\infty  
\dfrac{1+x+y}{(1+y)^4}  
dy

\dfrac{2x+3}{6}  
]

Entonces:

[  
f_X(x)=  
\dfrac{\frac92}{(1+x)^4}  
\cdot  
\dfrac{2x+3}{6}  
]

Simplificando:

[  
f_X(x)=  
\dfrac{3(2x+3)}  
{4(1+x)^4}  
]

para:

[  
x\ge0  
]

Respuesta final:

[  
\boxed{  
f_X(x)=  
\dfrac{3(2x+3)}  
{4(1+x)^4}  
}  
]