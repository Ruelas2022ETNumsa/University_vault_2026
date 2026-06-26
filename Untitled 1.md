## Axiomas de cuerpo de los números reales

--- start-multi-column: cornell-001
```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

Sea $a,b,c \in \mathbb{R}$.

1. **Clausura**
	- $a+b \in \mathbb{R}$
	- $a\cdot b \in \mathbb{R}$
2. **Conmutatividad**
	- Suma: $a+b=b+a$
	- Producto: $a\cdot b=b\cdot a$
3. **Asociatividad**
	- Suma: $(a+b)+c=a+(b+c)$
	- Producto: $(a\cdot b)\cdot c=a\cdot(b\cdot c)$
4. **Existencia de elementos neutros únicos**
	$\exists$ 0 y 1 $\in$ $\mathbb{R}$ donde ($1 \neq 0$)
	- Neutro aditivo: $\exists\,0\in\mathbb{R}: a+0=a$
	- Neutro multiplicativo: $\exists\,1\in\mathbb{R}: a\cdot1=a$
5. **Existencia de opuestos (negativos) únicos**
	Para cada $a$ $\exists$ un único $-a$
	- $\forall\,a\in\mathbb{R},\ \exists\,(-a)\in\mathbb{R}: a+(-a)=0$
6. **Existencia de recíprocos (inversos)**
	Para cada $a$ $\exists$ un único $a^{-1}$
	- $\forall\,a\in\mathbb{R},\ a\neq0,\ \exists\,a^{-1}\in\mathbb{R}: a\cdot a^{-1}=1$
7. **Distributividad**
	   $\forall a, b, c \in \mathbb{R}$ 
	- $a(b+c)=ab+ac$
```desmos-graph
left=-6.5; right=5.5; bottom=-1; top=1;
width=500; height=120;
---
y=0 \{x<-6\}|#26a69a|DOTTED
y=0 \{-6<x<-4\}|#26a69a
(-4,0)|OPEN|label:-4|#26a69a

y=0 \{-1<x<0\}|#26a69a
(-1,0)|OPEN|label:-1|#26a69a
(0,0)|OPEN|label:0|#26a69a

y=0 \{2<x<5\}|#26a69a
y=0 \{x>5\}|#26a69a|DOTTED
(2,0)|OPEN|label:2|#26a69a
```
La gráfica de $y=f(x)$ es simétrica respecto al eje $y$.

--- end-column ---

🔑 **Claves**

- $\mathbb{R}$ es un **cuerpo** — cerrado bajo suma y producto
- Neutros: $0$ para suma, $1$ para producto y $1\neq 0$
- Todo real tiene opuesto $(-a)$; todo real no nulo tiene inverso $a^{-1}$, estos elementos son únicos para cada $a$
- Distributividad conecta suma y producto
%```desmos-graph
%```
- Resta y división **no** son axiomas — se derivan

--- end-multi-column

> **Resumen:** Los 7 axiomas de cuerpo garantizan que $\mathbb{R}$ tiene operaciones de suma y producto bien definidas, con neutros, inversos y distributividad.

>**Los axiomas de cuerpo definen a** R **como una estructura algebraica cerrada con elementos neutros e inversos únicos que fundamentan todas las operaciones aritméticas.**

### Contenido complementario

```
```