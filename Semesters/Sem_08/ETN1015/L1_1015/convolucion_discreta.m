% ETN1015 — Discrete Signals and Systems
% Ejercicio: Convolución lineal de secuencias finitas x(n) y h(n)
% Fuente: S. Palani — Cap. 1 (Señales y Sistemas Discretos)
clear; clc; close all;

% [bloque 1 — Definición de las secuencias y sus soportes de tiempo]
x = [1, 1, 1, 1];     % Secuencia de entrada
nx = 0:3;             % Soporte de la entrada x[n]

h = [1, 2, 3];        % Respuesta al impulso del sistema LTI
nh = 0:2;             % Soporte de la respuesta al impulso h[n]

% [bloque 2 — Cálculo de la convolución lineal y determinación del soporte]
% La longitud de y es (length(x) + length(h) - 1)
y = conv(x, h);       % Convolución lineal integrada de MATLAB

% El soporte de y comienza en la suma de los inicios y termina en la suma de los fines
ny_inicio = nx(1) + nh(1);
ny_fin = nx(end) + nh(end);
ny = ny_inicio:ny_fin; % Soporte temporal de la salida y[n]

% [bloque 3 — Visualización de la señal resultante]
figure(1);
stem(ny, y, 'filled', 'LineWidth', 1.5, 'Color', [0 0.4470 0.7410]);
xlabel('Índice de tiempo n');
ylabel('Amplitud y[n]');
title('Convolución lineal resultante y[n] = x[n] * h[n]');
xlim([ny_inicio-1, ny_fin+1]);
ylim([0, max(y)+1]);
grid on;
