## [3. Procedimiento de Diseño de Filtros Digitales IIR Chebyshev Pasa-Bajo]

title: Complemento (Nivel C)

1. Explicación intuitiva
El diseño de un **filtro digital IIR pasa-bajo de Chebyshev Tipo I** combina la alta selectividad del prototipo analógico equirrizo con una transformación del plano $s$ al plano $z$ [1-3]. A diferencia del filtro Butterworth, el filtro de Chebyshev introduce rizo de amplitud constante en la banda de paso a cambio de lograr una banda de transición significativamente más estrecha para un mismo orden $N$ [2, 4].

El procedimiento estándar no diseña el filtro directamente en el dominio discreto. En su lugar, utiliza el método de **Transformación Bilineal $BLT$** [3, 5, 6]:
1. Las especificaciones de frecuencia del filtro digital ($\omega_p$, $\omega_s$) se trasladan al dominio analógico continuo mediante una deformación no lineal previa denominada **pre-warping** [7, 8]. Esto evita que la distorsión frecuencial de la transformación bilineal desplace las frecuencias de corte deseadas [7, 8].
2. Se determina el orden mínimo $N$, el parámetro de rizo $\epsilon$ y los polos del prototipo analógico de Chebyshev [3, 9, 10].
3. Se construye la función de transferencia analógica $H_a(s)$ [9, 11].
4. Finalmente, mediante la sustitución algebraico-racional de la Transformación Bilineal, se obtiene la función de transferencia digital $H(z)$, la cual resulta intrínsecamente estable y libre de *aliasing* [5, 6, 12].

5. Procedimiento paso a paso y formulación formal

### Paso 1: Conversión de especificaciones y Pre-warping de frecuencias
Dado el filtro digital con especificaciones:
- $\omega_p$: Frecuencia límite de la banda de paso (rad).
- $\omega_s$: Frecuencia de inicio de la banda de rechazo (rad).
- $R_p$ (o $A_p$): Atenuación/rizo máximo en la banda de paso (dB).
- $A_s$: Atenuación mínima en la banda de rechazo (dB).

Para corregir la distorsión de frecuencia introducida por la Transformación Bilineal, las frecuencias analógicas equivalentes $\Omega_p$ y $\Omega_s$ se calculan mediante [3, 13]:

$$
\Omega_p = \frac{2}{T} \tan\left(\frac{\omega_p}{2}\right), \quad \Omega_s = \frac{2}{T} \tan\left(\frac{\omega_s}{2}\right)
$$

*(Por conveniencia algebraica, habitualmente se elige $T = 1\text{ s}$ o $T = 2\text{ s}$ sin pérdida de generalidad, ya que el factor $2/T$ se cancela durante la transformación final [14, 15]).*

### Paso 2: Cálculo del parámetro de rizo $\epsilon$ y relación de transición
El parámetro de rizo $\epsilon$ se obtiene directamente de la especificación en dB de la banda de paso [3, 9]:

$$
\epsilon = \sqrt{10^{0.1 R_p} - 1} = \left( \frac{1}{A_p^2} - 1 \right)^{1/2}
$$

La relación de frecuencias en la banda de transición viene dada por [3, 9]:

$$
\Omega_r = \frac{\Omega_s}{\Omega_p}
$$


### Paso 3: Determinación del orden del filtro $N$
El orden mínimo entero $N$ necesario para satisfacer la atenuación en la banda de rechazo se calcula como [3, 9]:

$$
N \ge \frac{\cosh^{-1}\left( \frac{\sqrt{10^{0.1 A_s} - 1}}{\epsilon} \right)}{\cosh^{-1}(\Omega_r)} = \frac{\ln\left(g + \sqrt{g^2 - 1}\right)}{\ln\left(\Omega_r + \sqrt{\Omega_r^2 - 1}\right)}, \quad g = \frac{\sqrt{10^{0.1 A_s} - 1}}{\epsilon}
$$

Se adopta el valor entero superior $N = \lceil N \rceil$ [9, 16].

### Paso 4: Ubicación de los polos analógicos del prototipo
Los polos del filtro analógico $H_a(s)$ se ubican sobre una elipse en el semiplano izquierdo de Laplace $\text{Re}\{s\} < 0$ [3, 17]. Se calcula el parámetro auxiliar $Y_N$ [11]:

$$
Y_N = \frac{1}{2} \left[ \left( \sqrt{\frac{1}{\epsilon^2} + 1} + \frac{1}{\epsilon} \right)^{1/N} - \left( \sqrt{\frac{1}{\epsilon^2} + 1} + \frac{1}{\epsilon} \right)^{-1/N} \right]
$$

Las coordenadas de los polos $s_k = -\sigma_k + j\Omega_k$ para $k = 1, 2, \dots, N$ están dadas por [11]:

$$
b_k = 2 Y_N \sin\left( \frac{(2k - 1)\pi}{2N} \right)
$$


$$
c_k = Y_N^2 + \cos^2\left( \frac{(2k - 1)\pi}{2N} \right)
$$


### Paso 5: Construcción de la función de transferencia analógica $H_a(s)$
Utilizando secciones cuadráticas y de primer orden [11]:

- **Si $N$ es par:**

$$
H_a(s) = \prod_{k=1}^{N/2} \frac{B_k \Omega_p^2}{s^2 + b_k \Omega_p s + c_k \Omega_p^2}
$$

donde las constantes $B_k$ se ajustan para garantizar que en $s = 0$, la ganancia sea $H_a(0) = \frac{1}{\sqrt{1 + \epsilon^2}}$.

- **Si $N$ es odd:**

$$
H_a(s) = \left( \frac{B_0 \Omega_p}{s + Y_N \Omega_p} \right) \prod_{k=1}^{(N-1)/2} \frac{B_k \Omega_p^2}{s^2 + b_k \Omega_p s + c_k \Omega_p^2}
$$

donde la ganancia en DC se ajusta a $H_a(0) = 1$.

### Paso 6: Transformación Bilineal a $H(z)$
Sustituyendo la transformación analógica a digital [6, 11, 18]:

$$
s \leftarrow \frac{2}{T} \left( \frac{1 - z^{-1}}{1 + z^{-1}} \right)
$$

en $H_a(s)$, se simplifica algebraicamente para obtener la función de transferencia digital racional final [6, 18]:

$$
H(z) = \frac{\sum_{k=0}^{N} b_k z^{-k}}{1 + \sum_{k=1}^{N} a_k z^{-k}}
$$


3. Figura o diagrama
Diagrama de flujo del procedimiento sistemático de diseño de un filtro IIR Chebyshev pasa-bajo mediante Transformación Bilineal:

```tikz
\usepackage{tikz}
\usepackage{amsmath}
\begin{document}
\begin{tikzpicture}[scale=1.1, >=latex,
    node distance=1.3cm,
    block/.style={draw, rectangle, fill=teal!10, text width=5.5cm, align=center, rounded corners=2pt, minimum height=0.8cm},
    line/.style={draw, ->, thick, teal}]

    % Nodos del flujo
    \node [block] (step1) {\textbf{Paso 1: Especificaciones Digitales}\\ $\omega_p, \omega_s, R_p\text{ (dB)}, A_s\text{ (dB)}$};
    \node [block, below=0.8cm of step1] (step2) {\textbf{Paso 2: Pre-warping Frecuencial}\\ $\Omega_p = \frac{2}{T}\tan(\frac{\omega_p}{2}),\ \Omega_s = \frac{2}{T}\tan(\frac{\omega_s}{2})$};
    \node [block, below=0.8cm of step2] (step3) {\textbf{Paso 3: Parámetros de Chebyshev}\\ $\epsilon = \sqrt{10^{0.1 R_p}-1},\ \Omega_r = \frac{\Omega_s}{\Omega_p}$\\ $N = \lceil \frac{\cosh^{-1}(g)}{\cosh^{-1}(\Omega_r)} \rceil$};
    \node [block, below=0.8cm of step3] (step4) {\textbf{Paso 4: Polos Analógicos}\\ Calcular $Y_N$, coeficientes $b_k, c_k$\\ Obtener $H_a(s)$};
    \node [block, below=0.8cm of step4] (step5) {\textbf{Paso 5: Transformación Bilineal}\\ Sustituir $s = \frac{2}{T} \frac{1 - z^{-1}}{1 + z^{-1}}$ en $H_a(s)$};
    \node [block, fill=orange!20, below=0.8cm of step5] (step6) {\textbf{Resultado Final}\\ Función de Transferencia $H(z)$};

    % Conexiones
    \draw [line] (step1) -- (step2);
    \draw [line] (step2) -- (step3);
    \draw [line] (step3) -- (step4);
    \draw [line] (step4) -- (step5);
    \draw [line] (step5) -- (step6);

\end{tikzpicture}
\end{document}
```

4. Preguntas de comprensión
5. ¿Por qué es obligatorio realizar el procedimiento de *pre-warping* sobre las frecuencias digitales $\omega_p$ y $\omega_s$ antes de calcular el orden $N$ del filtro de Chebyshev cuando se utiliza la Transformación Bilineal [7, 8]?
6. ¿Qué ventaja de diseño ofrece el filtro IIR de Chebyshev frente al filtro IIR de Butterworth cuando se requiere una transición extremadamente rápida entre la banda de paso y la de rechazo [2, 4]?
7. ¿Cómo influye el carácter par o impar del orden $N$ en el valor de la ganancia en continua $H(z)|_{z=1}$ de un filtro digital Chebyshev Tipo I [17, 19]?

8. Ejercicios resueltos

##### Ej. 1: Diseño completo de filtro IIR Chebyshev Tipo I pasa-bajo por Transformación Bilineal
Diseñar un filtro digital IIR pasa-bajo que satisfaga las siguientes especificaciones:
- Frecuencia límite de banda de paso: $\omega_p = 0.2\pi\text{ rad}$.
- Frecuencia límite de banda de rechazo: $\omega_s = 0.3\pi\text{ rad}$.
- Rizo máximo en la banda de paso: $R_p = 1\text{ dB}$.
- Atenuación mínima en la banda de rechazo: $A_s = 15\text{ dB}$.

Utilizar la Transformación Bilineal con $T = 2\text{ s}$ (es decir, $2/T = 1$) [14, 15].

**Resolución:**

**Paso 1: Pre-warping de frecuencias analógicas**
Con $T = 2\text{ s}$ ($\frac{2}{T} = 1$) [14, 15]:

$$
\Omega_p = \tan\left(\frac{0.2\pi}{2}\right) = \tan(0.1\pi) \approx 0.32492\text{ rad/s}
$$


$$
\Omega_s = \tan\left(\frac{0.3\pi}{2}\right) = \tan(0.15\pi) \approx 0.50953\text{ rad/s}
$$


**Paso 2: Parámetro de rizo $\epsilon$ y relación de transición $\Omega_r$**

$$
\epsilon = \sqrt{10^{0.1(1)} - 1} = \sqrt{1.258925 - 1} = \sqrt{0.258925} \approx 0.50885
$$


$$
\Omega_r = \frac{\Omega_s}{\Omega_p} = \frac{0.50953}{0.32492} \approx 1.56817
$$


$$
g = \frac{\sqrt{10^{0.1(15)} - 1}}{\epsilon} = \frac{\sqrt{31.62278 - 1}}{0.50885} = \frac{5.53378}{0.50885} \approx 10.8750
$$


**Paso 3: Determinación del orden $N$**

$$
N \ge \frac{\cosh^{-1}(10.8750)}{\cosh^{-1}(1.56817)} = \frac{\ln\left(10.8750 + \sqrt{10.8750^2 - 1}\right)}{\ln\left(1.56817 + \sqrt{1.56817^2 - 1}\right)} = \frac{\ln(21.7040)}{\ln(2.7770)} = \frac{3.0775}{1.0213} \approx 3.013
$$

Redondeando al entero superior inmediato [9, 16]:

$$
N = 4
$$


**Paso 4: Parámetros del prototipo analógico para $N = 4$**

$$
Y_4 = \frac{1}{2} \left[ \left( \sqrt{\frac{1}{0.50885^2} + 1} + \frac{1}{0.50885} \right)^{1/4} - \left( \sqrt{\frac{1}{0.50885^2} + 1} + \frac{1}{0.50885} \right)^{-1/4} \right]
$$


$$
\sqrt{1 + \frac{1}{\epsilon^2}} + \frac{1}{\epsilon} = 2.20507 + 1.96522 = 4.17029
$$


$$
(4.17029)^{0.25} \approx 1.42886, \quad (4.17029)^{-0.25} \approx 0.69986
$$


$$
Y_4 = \frac{1}{2} (1.42886 - 0.69986) = 0.36450
$$


Calculamos los coeficientes de las 2 secciones cuadráticas ($k = 1, 2$) [11]:
- Para $k = 1$ ($\theta_1 = \frac{\pi}{8} = 22.5^\circ$):
  
$$
b_1 = 2 (0.36450) \sin(22.5^\circ) = 0.72900 (0.38268) \approx 0.27897
$$

  
$$
c_1 = (0.36450)^2 + \cos^2(22.5^\circ) = 0.13286 + 0.85355 = 0.98641
$$

- Para $k = 2$ ($\theta_2 = \frac{3\pi}{8} = 67.5^\circ$):
  
$$
b_2 = 2 (0.36450) \sin(67.5^\circ) = 0.72900 (0.92388) \approx 0.67351
$$

  
$$
c_2 = (0.36450)^2 + \cos^2(67.5^\circ) = 0.13286 + 0.14645 = 0.27931
$$


**Paso 5: Función de transferencia analógica $H_a(s)$**
Desnormalizando con $\Omega_p = 0.32492\text{ rad/s}$ [11]:

$$
b_1 \Omega_p = 0.27897 \times 0.32492 = 0.09064, \quad c_1 \Omega_p^2 = 0.98641 \times (0.32492)^2 = 0.10414
$$


$$
b_2 \Omega_p = 0.67351 \times 0.32492 = 0.21884, \quad c_2 \Omega_p^2 = 0.27931 \times (0.32492)^2 = 0.02949
$$


Para $N = 4$ (par), el término del numerador se ajusta con $H_a(0) = \frac{1}{\sqrt{1+\epsilon^2}} = 0.89125$ [17, 19]:

$$
K = 0.89125 \times (0.10414 \times 0.02949) \approx 0.002737
$$


$$
H_a(s) = \frac{0.002737}{(s^2 + 0.09064 s + 0.10414)(s^2 + 0.21884 s + 0.02949)}
$$


**Paso 6: Transformación Bilineal a $H(z)$**
Sustituyendo $s = \frac{1 - z^{-1}}{1 + z^{-1}}$ (al haber fijado $2/T = 1$) en cada sección cuadrática [6, 11]:
1. Primera sección:
   
$$
s^2 + 0.09064 s + 0.10414 = \left(\frac{1 - z^{-1}}{1 + z^{-1}}\right)^2 + 0.09064\left(\frac{1 - z^{-1}}{1 + z^{-1}}\right) + 0.10414
$$

   Multiplicando por $(1 + z^{-1})^2$:
   
$$
(1 - z^{-1})^2 + 0.09064(1 - z^{-2}) + 0.10414(1 + z^{-1})^2
$$

   
$$
= (1 - 2z^{-1} + z^{-2}) + 0.09064(1 - z^{-2}) + 0.10414(1 + 2z^{-1} + z^{-2})
$$

   
$$
= 1.19478 - 1.79172 z^{-1} + 1.01350 z^{-2} = 1.19478 (1 - 1.4996 z^{-1} + 0.8482 z^{-2})
$$


2. Segunda sección:
   
$$
s^2 + 0.21884 s + 0.02949 \implies (1 - z^{-1})^2 + 0.21884(1 - z^{-2}) + 0.02949(1 + z^{-1})^2
$$

   
$$
= (1 - 2z^{-1} + z^{-2}) + 0.21884(1 - z^{-2}) + 0.02949(1 + 2z^{-1} + z^{-2})
$$

   
$$
= 1.24833 - 1.94102 z^{-1} + 0.81065 z^{-2} = 1.24833 (1 - 1.5549 z^{-1} + 0.6494 z^{-2})
$$


Numerador global con $(1 + z^{-1})^4$:

$$
0.002737 \times (1 + z^{-1})^4
$$

Factor constante global de ganancia:

$$
C = \frac{0.002737}{1.19478 \times 1.24833} \approx 0.001836
$$


Sustituyendo en la expresión final factorizada en cascada [20]:

$$
H(z) = 0.001836 \frac{(1 + z^{-1})^4}{(1 - 1.4996 z^{-1} + 0.8482 z^{-2})(1 - 1.5549 z^{-1} + 0.6494 z^{-2})}
$$


---

##### Ej. 2 (Mayor dificultad): Cálculo analítico directo de polos en el plano $z$
Dado un filtro IIR Chebyshev Tipo I pasa-bajo de primer orden ($N = 1$) con $\omega_p = 0.5\pi\text{ rad}$, $R_p = 3\text{ dB}$ y $T = 2\text{ s}$ ($2/T = 1$), calcular analíticamente la ubicación del polo en el plano $s$ y su polo mapeado en el plano $z$ mediante la Transformación Bilineal.

**Resolución:**

1. **Pre-warping de la frecuencia de corte:**
   
$$
\Omega_p = \tan\left(\frac{0.5\pi}{2}\right) = \tan\left(\frac{\pi}{4}\right) = 1.0\text{ rad/s}
$$


2. **Parámetro de rizo $\epsilon$:**
   Para $R_p = 3\text{ dB}$:
   
$$
\epsilon = \sqrt{10^{0.3} - 1} = \sqrt{1.99526 - 1} \approx 0.99763 \approx 1.0
$$


3. **Cálculo de la posición del polo analógico $s_1$:**
   Para $N = 1$, $Y_1$ es:
   
$$
Y_1 = \frac{1}{2} \left[ \left( \sqrt{1 + 1} + 1 \right)^1 - \left( \sqrt{1 + 1} + 1 \right)^{-1} \right] = \frac{1}{2} \left[ (\sqrt{2} + 1) - (\sqrt{2} - 1) \right] = 1.0
$$

   El único polo estables sobre el semiplano izquierdo de Laplace es [11]:
   
$$
s_1 = -Y_1 \Omega_p = -(1.0)(1.0) = -1.0\text{ rad/s}
$$


4. **Mapeo del polo al plano $z$ mediante la Transformación Bilineal:**
   La relación conforme inversa de la Transformación Bilineal expresa a $z$ en función de $s$ [6, 18]:
   
$$
z = \frac{1 + s T/2}{1 - s T/2}
$$

   Puesto que fijamos $T = 2\text{ s}$ (es decir, $T/2 = 1$):
   
$$
z_1 = \frac{1 + s_1}{1 - s_1} = \frac{1 + (-1.0)}{1 - (-1.0)} = \frac{0}{2} = 0
$$

   
   El polo analógico ubicado en $s_1 = -1.0$ queda mapeado exactamente en el **origen del plano $z$** ($z_1 = 0$), garantizando un filtro digital de fase mínima e incondicionalmente estable [12, 21, 22].
