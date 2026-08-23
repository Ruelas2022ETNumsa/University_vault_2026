% ETN1015 - Ejercicio 1
clear; clc; close all;

T1 = 1/15;
T0 = 0.2;
dt = 0.0005;

x1 = @(t) 5*cos(2*pi*15*t + 0.25*pi);
x2 = @(t) 5*cos(2*pi*15*t + 0.25*pi) + 5*cos(2*pi*10*t + 0.3*pi);

% Comparacion general
t_comp = 0:dt:3*T0;
figure(1);
plot(t_comp, x1(t_comp), 'b', 'LineWidth', 1.5); hold on;
plot(t_comp, x2(t_comp), 'r', 'LineWidth', 1.5);
xlabel('t (s)'); ylabel('x(t)');
title('Senal 1 y Senal 2 - 3 periodos de x_2(t)');
legend('x_1(t)', 'x_2(t)'); grid on; hold off;

% Senal 1 - 3 periodos
t_x1 = 0:dt:3*T1;
figure(2);
plot(t_x1, x1(t_x1), 'b', 'LineWidth', 1.5);
xlabel('t (s)'); ylabel('x_1(t)');
title('Senal 1 - 3 periodos (T_1 = 1/15 s)'); grid on;

% Senal 2 - 3 periodos
t_x2 = 0:dt:3*T0;
figure(3);
plot(t_x2, x2(t_x2), 'r', 'LineWidth', 1.5);
xlabel('t (s)'); ylabel('x_2(t)');
title('Senal 2 - 3 periodos (T_0 = 0.2 s)'); grid on;