% ETN1015 — Discrete and Fast Fourier Transforms (DFT and FFT)
% Ejercicio: Convolución circular de x1(n) y x2(n) modificada (N = 5) usando matriz circulante
% Fuente: S. Palani — Cap. 2, Ej. 2.22 / Ingle & Proakis — Cap. 5
clear; clc; close all;

% [bloque 1 — Definición de las secuencias de entrada con relleno de ceros y parámetros]
x1 = [2, 1, 2, 1, 0];   % Secuencia x1(n) de 4 muestras rellenada con un cero para N = 5
x2 = [1, 2, 3, 4, 5];   % Secuencia x2(n) modificada de longitud N = 5
N = 5;                 % Longitud de la convolución circular

% [bloque 2 — Construcción de la matriz circulante y cálculo de la convolución]
% Construimos la matriz circulante H (de tamaño N x N) asociada a x2
H = zeros(N, N);
for n = 0:N-1
    H(:, n+1) = x2(mod((0:N-1) - n, N) + 1);
end

% Multiplicación de la matriz circulante H por el vector columna x1 para obtener x3
x3 = (H * x1')';       % Transponemos para mantener x3 como vector fila

% [bloque 3 — Visualización de la señal resultante mediante stem]
m = 0:N-1;             % Soporte temporal de la salida
figure(1);
stem(m, x3, 'filled', 'LineWidth', 1.5, 'Color', [0.8500 0.3250 0.0980]);
xlabel('Índice de tiempo m');
ylabel('Amplitud x3(m)');
title('Convolución circular x3(m) = x1(n) \otimes_5 x2(n)');
xlim([-0.5, N-0.5]);
ylim([0, max(x3)+2]);
set(gca, 'XTick', m);  % Asegura que las etiquetas del eje x sean enteras
grid on;
