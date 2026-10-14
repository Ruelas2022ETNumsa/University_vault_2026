% Doble péndulo con fricción viscosa (n = 1): Lagrange + función de Rayleigh
syms t m1 m2 l g c1 c2 real
syms th1(t) th2(t)

% Posiciones cartesianas
x1 = l*sin(th1);        y1 = l*cos(th1);
x2 = x1 + l*sin(th2);   y2 = y1 + l*cos(th2);

% Velocidades al cuadrado
v1sq = diff(x1,t)^2 + diff(y1,t)^2;
v2sq = diff(x2,t)^2 + diff(y2,t)^2;

% Energías y función de disipación de Rayleigh
T = simplify(m1/2*v1sq + m2/2*v2sq);
V = -m1*g*y1 - m2*g*y2;
P = simplify(c1/2*v1sq + c2/2*v2sq);

% Símbolos auxiliares (a = θ, w = θpunto) para poder derivar parcialmente
syms a1 a2 w1 w2 real
toS = @(e) subs(subs(e, [diff(th1,t) diff(th2,t)], [w1 w2]), [th1 th2], [a1 a2]);
toF = @(e) subs(e, [a1 a2 w1 w2], [th1 th2 diff(th1,t) diff(th2,t)]);
Ts = toS(T);  Vs = toS(V);  Ps = toS(P);

% d/dt(dT/dw) - dT/da + dV/da + dP/dw = 0
eq1 = diff(toF(diff(Ts,w1)),t) - toF(diff(Ts,a1)) + toF(diff(Vs,a1)) + toF(diff(Ps,w1)) == 0;
eq2 = diff(toF(diff(Ts,w2)),t) - toF(diff(Ts,a2)) + toF(diff(Vs,a2)) + toF(diff(Ps,w2)) == 0;

% Mostrar EDOs simplificadas
disp('EDO para theta1:');  disp(simplify(eq1));
disp('EDO para theta2:');  disp(simplify(eq2));
