# Números reales y desigualdades

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
4. **Existencia de neutros**
	- Neutro aditivo: $\exists\,0\in\mathbb{R}: a+0=a$
	- Neutro multiplicativo: $\exists\,1\in\mathbb{R}: a\cdot1=a$
5. **Existencia de negativos**
	- $\forall\,a\in\mathbb{R},\ \exists\,(-a)\in\mathbb{R}: a+(-a)=0$
6. **Existencia de inversos**
	- $\forall\,a\in\mathbb{R},\ a\neq0,\ \exists\,a^{-1}\in\mathbb{R}: a\cdot a^{-1}=1$
7. **Distributividad**
	- $a(b+c)=ab+ac$

--- end-column ---

🔑 **Claves**

- $\mathbb{R}$ es un **cuerpo** — cerrado bajo suma y producto
- Neutros: $0$ para suma, $1$ para producto
- Todo real tiene opuesto $(-a)$; todo real no nulo tiene inverso $a^{-1}$
- Distributividad conecta suma y producto
- Resta y división **no** son axiomas — se derivan

--- end-multi-column

> **Resumen:** Los 7 axiomas de cuerpo garantizan que $\mathbb{R}$ tiene operaciones de suma y producto bien definidas, con neutros, inversos y distributividad.

---

## Axiomas de igualdad

--- start-multi-column: cornell-002
```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

Sea $a,b,c\in\mathbb{R}$.
1. **Reflexividad**
	- $a=a$
2. **Simetría**
	- $a=b \implies b=a$
3. **Transitividad**
	- $a=b \land b=c \implies a=c$

--- end-column ---

🔑 **Claves**

- Reflexividad: todo elemento es igual a sí mismo
- Simetría: la igualdad no tiene dirección
- Transitividad: base de las cadenas de igualdades en demostraciones
- Estos 3 axiomas definen una **relación de equivalencia**

--- end-multi-column

> **Resumen:** La igualdad en $\mathbb{R}$ es reflexiva, simétrica y transitiva — una relación de equivalencia sobre los reales.

---

## Definiciones

--- start-multi-column: cornell-003
```column-settings
number of columns: 2
column size: [60%, 40%]
border: off
```

📝 **Desarrollo**

1. **Resta**
	- $b-a=b+(-a)$
2. **División**
	- $\dfrac{b}{a}=b\cdot a^{-1}$, con $a\neq0$

--- end-column ---

🔑 **Claves**

- Restar $a$ ≡ sumar $(-a)$
- Dividir por $a$ ≡ multiplicar por $a^{-1}$
- $a\neq0$ es **condición obligatoria** para la división
- Son operaciones **derivadas**, no primitivas

--- end-multi-column

> [!note]
> La resta y la división no son operaciones fundamentales.
> - La resta se define a partir de la suma y del opuesto aditivo.
> - La división se define a partir de la multiplicación y del inverso multiplicativo.

> **Resumen:** Resta y división son abreviaciones de suma con opuesto y producto con inverso, respectivamente.

---

## Observaciones

Es importante distinguir entre una igualdad, una ecuación y una identidad.

| Tipo                  | Ejemplo            | Descripción                                   | Alcance                                                                    |
|:--------------------- |:------------------ |:--------------------------------------------- |:-------------------------------------------------------------------------- |
| **Igualdad numérica** | $2^3=8$            | Afirmación entre valores numéricos concretos. | Puede ser verdadera o falsa.                                               |
| **Ecuación**          | $x^2-4=0$          | Contiene incógnitas.                          | Verdadera únicamente para los valores que pertenecen al conjunto solución. |
| **Identidad**         | $x^2-4=(x-2)(x+2)$ | Equivalencia algebraica.                      | Verdadera para todo valor del dominio.                                     |

### Ejemplos

- **Igualdad numérica :**   $2^3=8$

- **Ecuación**

	$x^2-4=0$

	Conjunto solución:

	$x=\pm2$

- **Identidad**

	$x^2-4=(x-2)(x+2)$

	Se verifica para todo $x\in\mathbb{R}$.

---