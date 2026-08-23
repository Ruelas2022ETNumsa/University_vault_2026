% ETN1015 — Ejercicio 5: DFT con zero-padding vs DTFT
% Ref: Palani Cap. 2 · Oppenheim Cap. 8 · Ingle & Proakis Cap. 5
clear; clc; close all;

xa = ones(1,5);
xb = (0.5).^(0:4);
N_vals = [5, 10, 50];
w = linspace(0, 2*pi, 1000);

% DTFT de referencia
Xa_ref = exp(-1j*2*w) .* sin(2.5*w) ./ sin(0.5*w);
Xa_ref(abs(sin(0.5*w)) < 1e-10) = 5;
Xb_ref = ones(1,5) * exp(-1j * ((0:4)' * w));  % evaluación directa 5 muestras

for sig = 1:2
    if sig == 1; x = xa; Xref = Xa_ref; label = 'a';
    else;        x = xb; Xref = Xb_ref; label = 'b'; end

    figure(2*sig-1); % Magnitud
    for i = 1:3
        N = N_vals(i);
        Xdft = fft(x, N);
        wk = (0:N-1)*2*pi/N;
        subplot(3,1,i);
        plot(w/pi, abs(Xref), 'r--', 'LineWidth', 1.2); hold on;
        stem(wk/pi, abs(Xdft), 'filled', 'b', 'LineWidth', 1.2);
        xlabel('\omega/\pi'); ylabel('|X[k]|');
        title(['Señal ' label ' — Magnitud (N=' num2str(N) ')']);
        xlim([0 2]); grid on;
        if i==1; legend('DTFT','DFT'); end
    end

    figure(2*sig); % Fase
    for i = 1:3
        N = N_vals(i);
        Xdft = fft(x, N);
        Xdft(abs(Xdft) < 1e-10) = 0;
        wk = (0:N-1)*2*pi/N;
        subplot(3,1,i);
        plot(w/pi, angle(Xref), 'r--', 'LineWidth', 1.2); hold on;
        stem(wk/pi, angle(Xdft), 'filled', 'b', 'LineWidth', 1.2);
        xlabel('\omega/\pi'); ylabel('\angle X[k] (rad)');
        title(['Señal ' label ' — Fase (N=' num2str(N) ')']);
        xlim([0 2]); ylim([-pi-0.5 pi+0.5]); grid on;
    end
end
