## 3.4 Especificaciones de desempeño (Performance Specifications)

title: Complemento (Nivel C)

### 1. Explicación intuitiva
Antes de construir cualquier filtro, es necesario definir exactamente qué "partes" de la señal queremos conservar y cuáles queremos eliminar. Las especificaciones de desempeño son el conjunto de requisitos técnicos que describen el comportamiento ideal que esperamos del filtro. Como es físicamente imposible crear un filtro "perfecto" (que corte una frecuencia de forma instantánea sin distorsión), definimos márgenes de tolerancia. Estos márgenes permiten que el filtro tenga pequeñas variaciones en las frecuencias que deja pasar (rizo de banda de paso) y que no elimine por completo, sino que atenúe lo suficiente, las frecuencias no deseadas (atenuación de banda de supresión). El espacio entre estas dos zonas se llama banda de transición, y define qué tan "afilado" es nuestro filtro.

### 2. Definición formal
El diseño de un filtro digital comienza con la definición de su respuesta en magnitud $|H(e^{j\omega})|$ a través de los siguientes parámetros fundamentales:

*   **Banda de paso $[0, \omega_p]$:** Rango de frecuencias que el filtro permite pasar. Se define una tolerancia $\delta_1$ $o $\delta_p$$ tal que $1 - \delta_1 \leq |H(e^{j\omega})| \leq 1 + \delta_1$.
*   **Banda de supresión $[\omega_s, \pi]$:** Rango de frecuencias que deben ser eliminadas. Se define una tolerancia $\delta_2$ $o $\delta_s$$ tal que $|H(e^{j\omega})| \leq \delta_2$.
*   **Frecuencias de borde:** $\omega_p$ es la frecuencia de borde de banda de paso y $\omega_s$ es la frecuencia de borde de banda de supresión.
*   **Banda de transición:** El intervalo $(\omega_p, \omega_s)$ donde la respuesta cae de la banda de paso a la de supresión.

En la práctica, estas especificaciones suelen expresarse en escala logarítmica (decibeles):
*   **Rizo en banda de paso $$R_p$$:** $R_p = -20 \log_{10} \left( \frac{1-\delta_1}{1+\delta_1} \right) \text{ dB}$.
*   **Atenuación en banda de supresión $$A_s$$:** $A_s = -20 \log_{10} \left( \frac{\delta_2}{1+\delta_1} \right) \text{ dB}$.

### 3. Figura o diagrama

```desmos-graph
left=-0.1; right=3.2; bottom=-0.2; top=1.3;
width=400; height=350;
---
\omega_p = 0.8
\omega_s = 1.4
\delta_1 = 0.1
\delta_2 = 0.15
# Zonas de tolerancia
# Banda de paso
y = 1+\delta_1 | 0 \le x \le \omega_p | #629900
y = 1-\delta_1 | 0 \le x \le \omega_p | #629900
# Banda de supresión
y = \delta_2 | \omega_s \le x \le 3.14 | #C1121F
# Curva de respuesta ejemplo
y = $1-0.1\cos(10x)$ / $1 + (x/1.1)^{8}$
f(x) | #005F73
```
%%IMA-SRC | fuente: Ingle & Proakis — Digital Signal Processing Using MATLAB — 3rd ed.pdf | página: 305 | id: Fig. 7.1 | posición: superior
justificación: La figura ilustra los límites de tolerancia (rizo y atenuación) y las bandas críticas (paso, transición y supresión) en una respuesta de magnitud típica.%%

### 4. Preguntas de comprensión
1. ¿Qué sucede con el orden del filtro (complejidad) si se requiere una banda de transición muy estrecha?
2. ¿Por qué es necesario permitir un rizo $$\delta_1$$ en la banda de paso en lugar de exigir una ganancia unitaria exacta?
3. En términos de decibeles, ¿qué significa que un filtro tenga una atenuación de 60 dB en la banda de supresión en comparación con uno de 20 dB?

### 5. Ejercicios resueltos

##### Ej. Conversión de especificaciones relativas a absolutas (Ingle Ej. 7.1)
Un filtro digital tiene las siguientes especificaciones: rizo en banda de paso $R_p = 0.25$ dB y atenuación en banda de supresión $A_s = 50$ dB. Determine los valores de las tolerancias absolutas $\delta_1$ y $\delta_2$.

**Resolución:**
1. Para el rizo en banda de paso, utilizamos la relación:
   
$$
R_p = -20 \log_{10} \frac{1-\delta_1}{1+\delta_1}
$$

   Despejando el cociente:
   
$$
\frac{1-\delta_1}{1+\delta_1} = 10^{-0.25/20} \approx 0.9716
$$

   
$$
1 - \delta_1 = 0.9716(1 + \delta_1) \implies 1 - 0.9716 = \delta_1(1 + 0.9716)
$$

   
$$
\delta_1 = \frac{0.0284}{1.9716} \approx 0.01441
$$


2. Para la atenuación en la banda de supresión:
   
$$
A_s = -20 \log_{10} \frac{\delta_2}{1+\delta_1}
$$

   Despejando $\delta_2$:
   
$$
\frac{\delta_2}{1+\delta_1} = 10^{-50/20} = 10^{-2.5} = 0.00316
$$

   
$$
\delta_2 = 0.00316 \times (1 + 0.01441) \approx 0.00321
$$


##### Ej. Determinación de banda de transición (Palani Ej. 3.25 modificado)
Si un filtro pasa-bajo tiene una frecuencia de borde de banda de paso $\omega_p = 0.2\pi$ y una frecuencia de borde de banda de supresión $\omega_s = 0.3\pi$, calcule el ancho de la banda de transición y la frecuencia central de corte aproximada.

**Resolución:**
1. El ancho de la banda de transición $$\Delta\omega$$ es la diferencia entre los bordes:
   
$$
\Delta\omega = \omega_s - \omega_p = 0.3\pi - 0.2\pi = 0.1\pi \text{ rad/muestra}
$$

2. La frecuencia de corte $$\omega_c$$ suele ubicarse idealmente en el punto medio de la banda de transición para diseños simplificados:
   
$$
\omega_c = \frac{\omega_p + \omega_s}{2} = \frac{0.2\pi + 0.3\pi}{2} = 0.25\pi \text{ rad/muestra}
$$




