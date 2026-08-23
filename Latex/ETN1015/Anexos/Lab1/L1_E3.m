% ETN1015 — Discrete Signals and Systems
% Ejercicio: Análisis de sistema recursivo de primer orden
% Fuente: S. Palani — Cap. 1, Ej. 1.11 / Ingle & Proakis — Cap. 2
clear; clc; close all;

% [bloque 1 — Definición de parámetros y preasignación de vectores]
N = 6;                % Número de muestras a evaluar (n = 0 a 5)
y = zeros(1, N);      % Vector de salida y[n]
x = zeros(1, N);      % Vector de entrada x[n] (impulso unitario)
x(1) = 1;             % x[0] = delta[0] = 1

% Condición inicial dada: y[-1] = 0
y_prev = 0;           % Representa y[-1]

% [bloque 2 — Simulación paso a paso con bucle for respetando condiciones iniciales]
for n = 1:N
    if n == 1
        y(n) = 2 * y_prev + x(n);  % Para n = 0 (primer índice), depende de y[-1]
    else
        y(n) = 2 * y(n-1) + x(n);  % Para n > 0, depende del valor anterior en el vector
    end
end

% [bloque 3 — Visualización de la respuesta del sistema]
n_vec = 0:5;          % Soporte temporal para la gráfica (0 <= n <= 5)
figure(1);
stem(n_vec, y, 'filled', 'LineWidth', 1.5, 'Color', [0.8500 0.3250 0.0980]);
xlabel('Índice de tiempo n');
ylabel('Amplitud y[n]');
title('Respuesta al impulso y[n] = 2y[n-1] + x[n]');
xlim([-1, 6]);
ylim([0, max(y)+5]);
grid on;
