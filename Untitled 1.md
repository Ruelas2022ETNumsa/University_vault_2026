---
title: "MAT101-numeros-reales-desigualdades"
galaxy_body: planet
subject: MAT-101
semester: 1
partial: 1
topic: T01_numeros-reales
star: ""
moons: []
comets: []
tags: [MAT-101, galaxy-planet, P1]
date_created: 2026-05-30
status: activo
---

# Números reales y desigualdades

## Axiomas de cuerpo de los números reales
Los axiomas de cuerpo son el conjunto de reglas fundamentales que definen cómo operan la adición y la multiplicación en el sistema de los números reales.
Sean $a, b, c \in \mathbb{R}$

|  N  | Axioma                     | Descripción                                                   | Notación                                                   | Concepto                                                                                           |
| :-: | -------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
|  1  | **Clausura**               | Operar dos reales siempre<br>produce un real                  | $a+b \in \mathbb{R}$<br>$a \cdot b \in \mathbb{R}$         | $\forall\, a,b \in \mathbb{R}:$<br>$a+b \in \mathbb{R}\ \wedge\ a \cdot b \in \mathbb{R}$          |
|  2  | **Conmutatividad**         | El orden de los operandos<br>no altera el resultado           | $a+b=b+a$<br>$a \cdot b=b \cdot a$                         | $\forall\, a,b \in \mathbb{R}:$<br>$a+b=b+a\ \wedge\ a \cdot b=b \cdot a$                          |
|  3  | **Asociatividad**          | El agrupamiento no altera<br>el resultado                     | $(a+b)+c=a+(b+c)$<br>$(ab)\,c=a\,(bc)$                     | $\forall\, a,b,c \in \mathbb{R}:$<br>$(a+b)+c=a+(b+c)$<br>$\wedge\ (ab)c=a(bc)$                    |
|  4  | **Distributividad**        | La multiplicación se <br>distribuye sobre la suma             | $a(b+c)=ab+ac$                                             | $\forall\, a,b,c \in \mathbb{R}:$<br>$a(b+c)=ab+ac$                                                |
|  5  | **Elemento neutro**        | El 0 es neutro aditivo;<br>el 1 es neutro multiplicativo      | $a+0=a$<br>$a\cdot 1=a$                                    | $\exists!\, 0 \in \mathbb{R}: a+0=a$<br>$\wedge\ \exists!\, 1 \in \mathbb{R}: a\cdot 1=a$          |
|  6  | **Inverso aditivo**        | Todo real tiene un opuesto<br>que anula la suma               | $a+(-a)=0$                                                 | $\forall\, a \in \mathbb{R},\ \exists\,{-a} \in \mathbb{R}:$<br>$a+(-a)=0$                         |
|  7  | **Inverso multiplicativo** | Todo real no nulo tiene un<br>recíproco que anula el producto | $a \cdot a^{-1}=1,\quad a \neq 0$<br>$a^{-1}=\dfrac{1}{a}$ | $\forall\, a \in \mathbb{R}\setminus\{0\},\ \exists\, a^{-1} \in \mathbb{R}:$<br>$a\cdot a^{-1}=1$ |



---

## Axiomas de igualdad

Sean $a, b, c \in \mathbb{R}$

1. **Reflexividad** 
	$a=a$
2. **Simetría** 
	$a=b \Rightarrow b=a$
3. **Transitividad**
	$(a=b \wedge b=c) \Rightarrow a=c$

---

## Definiciones

- **Resta** 
	$a-b=a+(-b)$
- **División**
	$\dfrac{a}{b}=a \cdot \dfrac{1}{b}=a \cdot b^{-1},\quad b \neq 0$

---

## Observaciones sobre tipos de igualdad

| Tipo              | Ejemplo            | Descripción                            |
| ----------------- | ------------------ | -------------------------------------- |
| Igualdad numérica | $2^3=8$            | Siempre verdadera                      |
| Ecuación          | $x^2-4=0$          | Verdadera solo para algunos $x$        |
| Identidad         | $x^2-4=(x-2)(x+2)$ | Verdadera para todo $x \in \mathbb{R}$ |

---

## Teoremas básicos

Sean $a, b, c, x \in \mathbb{R}$

1. $a+b=a+c \Rightarrow b=c$
2. $(a \cdot b=a \cdot c) \wedge a \neq 0 \Rightarrow b=c$
3. $a+x=b \Rightarrow x=b-a$
4. $(a \cdot x=b) \wedge a \neq 0 \Rightarrow x=\dfrac{b}{a}$
5. $a \cdot 0=0$
6. $a \cdot b=0 \Rightarrow (a=0 \vee b=0)$
7. $a=b \Rightarrow -a=-b$
8. $a(-b)=-(ab)$
9. $(-a)(-b)=ab$
10. $\dfrac{a}{b}+\dfrac{c}{b}=\dfrac{a+c}{b},\quad b \neq 0$

%%
galaxy-links

%%



```desmos-graph
left=-1; right=8; bottom=-1; top=1;
width=600; height=180;
---
y=0|-1<=x<=7|BLACK
(2,0)|label:a|BLUE
(3,0)|label:b|GREEN
(5,0)|label:a+b|RED
```