% ETN1015 — Discrete-Time Fourier Analysis
% Ejercicio: Análisis de la DTFT para una secuencia finita (Señal a) y una secuencia bilateral infinita (Señal b)
% Fuente: S. Palani — Cap. 2 / Ingle & Proakis — Cap. 3
clear; clc; close all;

% =========================================================================
% PARTE 1: Señal a (Suma de 5 impulsos desplazados)
% x(n) = sum_{k=0}^{4} delta(n-k), n = 0, 1, 2, 3, 4
% =========================================================================

% [bloque 1 — Definición de parámetros y cómputo de la DTFT para la Señal a]
n_a = 0:4;                   % Soporte temporal de la señal a
x_a = ones(1, 5);            % Valores de x(n) = 1 para n = 0,1,2,3,4

N_points = 1000;             % Número de puntos de frecuencia densos
w = linspace(-pi, pi, N_points); % Vector de frecuencias en el rango [-pi, pi]

% Evaluación numérica de la DTFT de la Señal a directamente desde la definición
% X_a(e^{j\omega}) = \sum_{n=0}^{4} x_a[n] * e^{-j * \omega * n}
X_a = x_a * exp(-j * (n_a' * w));

% Cálculo de magnitud y fase
mag_a = abs(X_a);
phase_a = angle(X_a);

% [bloque 2 — Graficación de la DTFT de la Señal a]
figure(1);
subplot(2,1,1);
plot(w/pi, mag_a, 'b', 'LineWidth', 1.5);
xlabel('Frecuencia normalizada (\omega / \pi)');
ylabel('Magnitud |X(e^{j\omega})|');
title('DTFT de la Señal a - Magnitud');
grid on;

subplot(2,1,2);
plot(w/pi, phase_a/pi, 'r', 'LineWidth', 1.5);
xlabel('Frecuencia normalizada (\omega / \pi)');
ylabel('Fase (radianes / \pi)');
title('DTFT de la Señal a - Fase');
grid on;

% =========================================================================
% PARTE 2: Señal b (Secuencia bilateral infinita)
% x(n) = (0.5)^|n|
% =========================================================================

% [bloque 3 — Justificación y cómputo por truncamiento de la Señal b]
% Como la señal es de longitud infinita, se trunca a n_b \in [-Nt, Nt].
% Elegimos Nt = 15 para que la muestra en el extremo sea (0.5)^15 \approx 3e-5,
% lo que garantiza que la energía residual descartada sea insignificante (< 4e-10).
Nt = 15;
n_b = -Nt:Nt;
x_b = (0.5).^abs(n_b);       % Secuencia truncada

% Evaluación numérica de la DTFT para la Señal b desde la definición
X_b = x_b * exp(-j * (n_b' * w));

% Cálculo de magnitud y fase
mag_b = abs(X_b);
phase_b = angle(X_b);

% [bloque 4 — Graficación de la DTFT de la Señal b]
figure(2);
subplot(2,1,1);
plot(w/pi, mag_b, 'b', 'LineWidth', 1.5);
xlabel('Frecuencia normalizada (\omega / \pi)');
ylabel('Magnitud |X(e^{j\omega})|');
title('DTFT de la Señal b - Magnitud');
grid on;

subplot(2,1,2);
plot(w/pi, phase_b/pi, 'r', 'LineWidth', 1.5);
xlabel('Frecuencia normalizada (\omega / \pi)');
ylabel('Fase (radianes / \pi)');
title('DTFT de la Señal b - Fase');
ylim([-1.1 1.1]); % Ajuste de límites para visualizar la fase nula
grid on;
