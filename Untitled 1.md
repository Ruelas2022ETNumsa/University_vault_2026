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


---

| Tipo              | Ejemplo            | Descripción                            |
| ----------------- | ------------------ | -------------------------------------- |
| **Clausura** | Si tomás dos números reales y los sumás o los multiplicás, el resultado será, sin ninguna duda, otro número real.|$a+b \in \mathbb{R}$ $a \cdot b=b \cdot a$|
| Ecuación          | $x^2-4=0$          | Verdadera solo para algunos $x$        |
| Identidad         | $x^2-4=(x-2)(x+2)$ | Verdadera para todo $x \in \mathbb{R}$ |


---


--- start-multi-column: cornell-001
```column-settings
number of columns: 2
column size: [45%, 45%]
border: off
```
%%## 📝 Definición formal%%

1. **Clausura**
Si tomás dos números reales y los sumás o los multiplicás, el resultado será, sin ninguna duda, otro número real.
2. **Conmutatividad**
	- $a+b=b+a$
	- $a \cdot b=b \cdot a$
3. **Asociatividad**
	- $(a+b)+c=a+(b+c)$
	- $(a \cdot b) \cdot c=a \cdot(b \cdot c)$
4. **Existencia de neutros**
	- $\exists\, 0 \in \mathbb{R}$ tal que $a+0=a$ — neutro para $+$
	- $\exists\, 1 \in \mathbb{R}$ tal que $a \cdot 1=a$ — neutro para $\times$
5. **Existencia de inversos aditivos**
	- $\forall a \in \mathbb{R},\ \exists\, {-a} \in \mathbb{R}$ tal que $a+(-a)=0$
	- $-a$ se denomina inverso aditivo de $a$
6. **Existencia de inversos multiplicativos**
	- $\forall a \in \mathbb{R}\setminus\{0\}$, $\exists\, a^{-1} \in \mathbb{R}$ tal que $a \cdot a^{-1}=1$
	- $a^{-1}=\dfrac{1}{a}$ es el inverso multiplicativo de $a$
7. **Distributividad**
	- $a(b+c)=ab+ac$

--- end-column ---

%%##  Fórmulas clave%%

1. 
	- $a+b \in \mathbb{R}$
	- $a \cdot b \in \mathbb{R}$


2. **Conmutatividad**
	- $a+b=b+a$
	- $a \cdot b=b \cdot a$
3. **Asociatividad**
	- $(a+b)+c=a+(b+c)$
	- $(a \cdot b) \cdot c=a \cdot(b \cdot c)$
4. **Existencia de inversos aditivos**
	- $\forall a \in \mathbb{R},\ \exists\, {-a} \in \mathbb{R}$ tal que $a+(-a)=0$
	- $-a$ se denomina inverso aditivo de $a$
5. **Existencia de inversos multiplicativos**
	- $\forall a \in \mathbb{R}\setminus\{0\}$, $\exists\, a^{-1} \in \mathbb{R}$ tal que $a \cdot a^{-1}=1$
	- $a^{-1}=\dfrac{1}{a}$ es el inverso multiplicativo de $a$
6. **Distributividad**
	- $a(b+c)=ab+ac$


--- end-multi-column

> **Resumen:**


Sean $a, b, c \in \mathbb{R}$

1. **Clausura**
	- $a+b \in \mathbb{R}$
	- $a \cdot b \in \mathbb{R}$

2. **Conmutatividad**
	- $a+b=b+a$
	- $a \cdot b=b \cdot a$

3. **Asociatividad**
	- $(a+b)+c=a+(b+c)$
	- $(a \cdot b) \cdot c=a \cdot(b \cdot c)$

4. **Existencia de neutros**
	- $\exists\, 0 \in \mathbb{R}$ tal que $a+0=a$ — neutro para $+$
	- $\exists\, 1 \in \mathbb{R}$ tal que $a \cdot 1=a$ — neutro para $\times$

5. **Existencia de inversos aditivos**
	- $\forall a \in \mathbb{R},\ \exists\, {-a} \in \mathbb{R}$ tal que $a+(-a)=0$
	- $-a$ se denomina inverso aditivo de $a$

6. **Existencia de inversos multiplicativos**
	- $\forall a \in \mathbb{R}\setminus\{0\}$, $\exists\, a^{-1} \in \mathbb{R}$ tal que $a \cdot a^{-1}=1$
	- $a^{-1}=\dfrac{1}{a}$ es el inverso multiplicativo de $a$

7. **Distributividad**
	- $a(b+c)=ab+ac$

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
