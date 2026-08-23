% ETN1015 — DFT y FFT / Capítulo 5 Proakis
% Ejercicio: DFT de Señales a y b con zero-padding y comparación con DTFT
% Fuente: Ingle & Proakis — Cap. 5 / Palani — Cap. 2
clear; clc; close all;

% [bloque 1 — Definición de señales y parámetros]
xa = ones(1, 5);          % Señal a: x(n) = [1 1 1 1 1]
xb = (0.5).^(0:4);        % Señal b: x(n) = [1, 0.5, 0.25, 0.125, 0.0625]

N_vals = [5, 10, 50];     % Valores de N para evaluar la DFT (con zero-padding)
w_dense = linspace(0, 2*pi, 1000); % Frecuencia densa para graficar la DTFT continua

% [bloque 2 — Cálculo de la DTFT continua de referencia]
% Señal a: Expresión analítica (evitando división por cero en múltiplos de 2*pi)
Xa_dtft = exp(-j * 2 * w_dense) .* sin(2.5 * w_dense) ./ sin(0.5 * w_dense);
Xa_dtft(abs(sin(0.5 * w_dense)) < 1e-10) = 5; % L'Hôpital para límites en 0 y 2*pi

% Señal b: Evaluación directa de la sumatoria finita de 5 puntos
Xb_dtft = zeros(size(w_dense));
for n = 0:4
    Xb_dtft = Xb_dtft + xb(n+1) * exp(-j * w_dense * n);
end

% [bloque 3 — Gráficas para la Señal a]
% Figura 1: Magnitud de la Señal a
figure(1);
for i = 1:length(N_vals)
    N = N_vals(i);
    X_dft = fft(xa, N);
    w_dft = (0:N-1) * 2 * pi / N;
    
    subplot(3, 1, i);
    plot(w_dense/pi, abs(Xa_dtft), 'r--', 'LineWidth', 1.2); hold on;
    stem(w_dft/pi, abs(X_dft), 'filled', 'b', 'LineWidth', 1.2);
    xlabel('Frecuencia normalizada (\omega / \pi)');
    ylabel('Magnitud');
    title(['Señal a - Magnitud (N = ', num2str(N), ')']);
    xlim([0, 2]);
    grid on;
    if i == 1
        legend('DTFT referencia', 'DFT muestras');
    end
end

% Figura 2: Fase de la Señal a
figure(2);
for i = 1:length(N_vals)
    N = N_vals(i);
    X_dft = fft(xa, N);
    % Limpieza de ruido numérico en fase para muestras con magnitud nula
    X_dft_clean = X_dft;
    X_dft_clean(abs(X_dft_clean) < 1e-10) = 0;
    w_dft = (0:N-1) * 2 * pi / N;
    
    subplot(3, 1, i);
    plot(w_dense/pi, angle(Xa_dtft), 'r--', 'LineWidth', 1.2); hold on;
    stem(w_dft/pi, angle(X_dft_clean), 'filled', 'b', 'LineWidth', 1.2);
    xlabel('Frecuencia normalizada (\omega / \pi)');
    ylabel('Fase (rad)');
    title(['Señal a - Fase (N = ', num2str(N), ')']);
    xlim([0, 2]);
    ylim([-pi-0.5, pi+0.5]);
    grid on;
end

% [bloque 4 — Gráficas para la Señal b]
% Figura 3: Magnitud de la Señal b
figure(3);
for i = 1:length(N_vals)
    N = N_vals(i);
    X_dft = fft(xb, N);
    w_dft = (0:N-1) * 2 * pi / N;
    
    subplot(3, 1, i);
    plot(w_dense/pi, abs(Xb_dtft), 'r--', 'LineWidth', 1.2); hold on;
    stem(w_dft/pi, abs(X_dft), 'filled', 'b', 'LineWidth', 1.2);
    xlabel('Frecuencia normalizada (\omega / \pi)');
    ylabel('Magnitud');
    title(['Señal b - Magnitud (N = ', num2str(N), ')']);
    xlim([0, 2]);
    grid on;
    if i == 1
        legend('DTFT referencia', 'DFT muestras');
    end
end

% Figura 4: Fase de la Señal b
figure(4);
for i = 1:length(N_vals)
    N = N_vals(i);
    X_dft = fft(xb, N);
    X_dft_clean = X_dft;
    X_dft_clean(abs(X_dft_clean) < 1e-10) = 0;
    w_dft = (0:N-1) * 2 * pi / N;
    
    subplot(3, 1, i);
    plot(w_dense/pi, angle(Xb_dtft), 'r--', 'LineWidth', 1.2); hold on;
    stem(w_dft/pi, angle(X_dft_clean), 'filled', 'b', 'LineWidth', 1.2);
    xlabel('Frecuencia normalizada (\omega / \pi)');
    ylabel('Fase (rad)');
    title(['Señal b - Fase (N = ', num2str(N), ')']);
    xlim([0, 2]);
    ylim([-pi-0.5, pi+0.5]);
    grid on;
end
