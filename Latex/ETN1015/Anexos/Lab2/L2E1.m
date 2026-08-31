% ETN1015 — Discrete and Fast Fourier Transforms (DFT and FFT)
% Ejercicio: Convolución circular — Ej. 2.22 (Palani)
clear; clc; close all;

% Secuencias de entrada
x1 = [2, 1, 2, 1, 0];
x2 = [1, 2, 3, 4, 5];
N = 5;

% Matriz circulante asociada a x2: cada columna n+1 contiene x2
% desplazada cíclicamente n posiciones usando índices mod N
H = zeros(N, N);
for n = 0:N-1
    H(:, n+1) = x2(mod((0:N-1) - n, N) + 1);
end

% Convolución: producto matriz-vector, resultado como vector fila
x3 = (H * x1')';

% Gráfica de x3 como diagrama de tallo
m = 0:N-1;
figure(1);
stem(m, x3, 'filled', 'LineWidth', 1.5, 'Color', [0.8500 0.3250 0.0980]);
xlabel('m'); ylabel('x_3(m)');
title('Convolución circular x_3(m) = x_1(n) \otimes_5 x_2(n)');
xlim([-0.5, N-0.5]); ylim([0, max(x3)+2]);
set(gca, 'XTick', m);
grid on;
% Etiqueta el valor numérico de x3 sobre cada punto del stem
for k = 1:N
    text(m(k), x3(k)+1.2, num2str(x3(k)), ...
        'HorizontalAlignment', 'center', 'FontSize', 10);
end
