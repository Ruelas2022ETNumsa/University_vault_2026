---
title: MATLAB — Guía de código para NotebookLM (ETN1015)
galaxy_body: beacon
scope: vault
tool: notebooklm
audience:
  - notebooklm
tags:
  - beacon
  - matlab
  - infraestructura
  - ETN1015
date_created: 2026-08-20
date_updated: 2026-08-20
status: activo
---

# Guía de código MATLAB para NotebookLM — ETN1015

Esta guía define cómo NotebookLM debe estructurar y entregar código MATLAB para ETN1015.
Todo código debe ser ejecutable, comentado y verificable. Seguir estos bloques exactamente.

---

## 1. Estructura de bloque de código

Siempre usar bloque fenced con identificador `matlab`:

~~~
```matlab
% código aquí
```
~~~

Nunca entregar código inline. Nunca mezclar código con LaTeX dentro del mismo bloque.

---

## 2. Encabezado de script

Todo script de ejercicio lleva encabezado mínimo:

```matlab
% ETN1015 — [Tema / Capítulo Palani]
% Ejercicio: [enunciado breve]
% Fuente: [libro — cap. X, ej. X.X]
clear; clc; close all;
```

---

## 3. Comentarios

- Una línea de comentario por bloque lógico.
- Comentarios en español.
- No comentar lo obvio (`a = 1; % a vale 1`).
- Sí comentar el propósito del bloque (`% Diseño del filtro IIR por bilineal`).

---

## 4. Señales discretas

### Definición de secuencias

```matlab
n = -10:10;                         % rango de índices
x = (0.5).^n .* (n >= 0);          % señal causal: x[n] = 0.5^n * u[n]
delta = (n == 0);                   % impulso unitario δ[n]
u = (n >= 0);                       % escalón unitario u[n]
```

### Convolución

```matlab
y = conv(x, h);                     % convolución lineal
n_y = (n(1) + n_h(1)) : (n(end) + n_h(end));  % rango de salida
```

### Stem para señales discretas

```matlab
stem(n, x, 'filled');
xlabel('n'); ylabel('x[n]');
title('Señal discreta x[n]');
grid on;
```

---

## 5. Transformada Z y función de transferencia

### Definición de H(z) con coeficientes

```matlab
b = [1, -0.5];                      % numerador: coeficientes de z^{-k}
a = [1, -0.8, 0.15];               % denominador: coeficientes de z^{-k}
```

Convención: primer elemento = coeficiente de z^0 (orden descendente en potencias de z^{-1}).

### Polos y ceros

```matlab
[z, p, k] = tf2zp(b, a);           % ceros, polos, ganancia
zplane(b, a);                       % diagrama de polos y ceros
title('Diagrama de polos y ceros');
```

### Respuesta en frecuencia

```matlab
[H, w] = freqz(b, a, 512);         % 512 puntos en [0, π]
figure;
subplot(2,1,1);
plot(w/pi, abs(H));
xlabel('\omega / \pi'); ylabel('|H(e^{j\omega})|');
title('Respuesta en magnitud');
grid on;

subplot(2,1,2);
plot(w/pi, angle(H));
xlabel('\omega / \pi'); ylabel('\angle H(e^{j\omega}) [rad]');
title('Respuesta en fase');
grid on;
```

---

## 6. DFT y FFT

### DFT directa

```matlab
N = length(x);
X = fft(x, N);                      % DFT de N puntos
k = 0:N-1;
f = k/N;                            % frecuencia normalizada [0, 1)
```

### Visualización espectro

```matlab
figure;
subplot(2,1,1);
stem(k, abs(X), 'filled');
xlabel('k'); ylabel('|X[k]|');
title('Espectro de magnitud');
grid on;

subplot(2,1,2);
stem(k, angle(X), 'filled');
xlabel('k'); ylabel('\angle X[k] [rad]');
title('Espectro de fase');
grid on;
```

### FFT centrada en cero

```matlab
X_shift = fftshift(X);
k_shift = -N/2 : N/2-1;
```

---

## 7. Diseño de filtros IIR

### Butterworth paso bajo

```matlab
Wp = 0.3 * pi;                      % frecuencia de paso (rad/muestra)
Ws = 0.5 * pi;                      % frecuencia de stop
Rp = 3;                             % riple en paso [dB]
Rs = 40;                            % atenuación en stop [dB]

[n_ord, Wn] = buttord(Wp/pi, Ws/pi, Rp, Rs);
[b, a] = butter(n_ord, Wn);
```

### Chebyshev tipo I

```matlab
[n_ord, Wn] = cheb1ord(Wp/pi, Ws/pi, Rp, Rs);
[b, a] = cheby1(n_ord, Rp, Wn);
```

### Transformación bilineal manual

```matlab
% Diseño analógico → digital por bilineal
T = 1;                              % período de muestreo
[b_d, a_d] = bilinear(b_a, a_a, 1/T);
```

---

## 8. Diseño de filtros FIR

### Ventana rectangular

```matlab
M = 20;                             % orden del filtro
wc = 0.4 * pi;                      % frecuencia de corte normalizada
h = fir1(M, wc/pi);                % paso bajo con ventana de Hamming (default)
```

### Otras ventanas

```matlab
h_rect  = fir1(M, wc/pi, rectwin(M+1));
h_hann  = fir1(M, wc/pi, hann(M+1));
h_black = fir1(M, wc/pi, blackman(M+1));
```

### Respuesta al impulso FIR

```matlab
stem(0:M, h, 'filled');
xlabel('n'); ylabel('h[n]');
title('Respuesta al impulso FIR');
grid on;
```

---

## 9. Efectos de palabra finita

### Cuantización

```matlab
B = 8;                              % bits totales
Q = 2^(-(B-1));                     % paso de cuantización (fraccionario)
x_q = round(x / Q) * Q;            % cuantización por redondeo
e = x - x_q;                       % error de cuantización
```

### Coeficientes cuantizados

```matlab
b_q = round(b / Q) * Q;
a_q = round(a / Q) * Q;
```

---

## 10. Multi-rate DSP

### Decimación

```matlab
M = 4;                              % factor de decimación
y_dec = x(1:M:end);                % submuestreo directo (sin filtro anti-aliasing)

% Con filtro previo:
x_filt = filter(b_lpf, a_lpf, x);
y_dec = x_filt(1:M:end);
```

### Interpolación

```matlab
L = 4;                              % factor de interpolación
y_up = upsample(x, L);             % inserción de ceros
y_int = filter(b_lpf, 1, y_up);   % filtro de interpolación
```

---

## 11. Visualización — convenciones

| Señal | Función | Nota |
|---|---|---|
| Discreta (stem) | `stem(n, x, 'filled')` | Siempre `'filled'` |
| Continua (plot) | `plot(t, x)` | |
| Espectro | `stem` o `plot` según discreta/continua | |
| Polos y ceros | `zplane(b, a)` | |
| Respuesta H | `freqz(b, a, N)` | |

Siempre incluir:
```matlab
xlabel('...'); ylabel('...'); title('...'); grid on;
```

Subplots cuando se muestran magnitud y fase juntas — siempre `subplot(2,1,1)` / `subplot(2,1,2)`.

---

## 12. Funciones clave por capítulo Palani

| Capítulo | Funciones principales |
|---|---|
| Cap. 1 — Discrete Signals | `stem`, `conv`, `filter`, `fliplr` |
| Cap. 2 — DFT y FFT | `fft`, `ifft`, `fftshift`, `abs`, `angle` |
| Cap. 3 — Filtros IIR | `butter`, `cheby1`, `cheby2`, `ellip`, `bilinear`, `freqz`, `zplane` |
| Cap. 4 — Filtros FIR | `fir1`, `fir2`, `firls`, `freqz`, `stem` |
| Cap. 5 — Word Length | `round`, `floor`, `fix`, `quantize` |
| Cap. 6 — Multi-rate | `upsample`, `downsample`, `resample`, `decimate`, `interp` |

---

%%
# galaxy-links
[[ETN1015_latex.md]]
[[ETN1015_octave.md]]
%%
