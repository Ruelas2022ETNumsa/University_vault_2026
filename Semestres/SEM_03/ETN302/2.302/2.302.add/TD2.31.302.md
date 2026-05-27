---

Alias: [T2-Graficar la señal]
Tags: [Leaves, Desmos]

---

Teoria
- Ejercicio 1
```desmos-graph
height=250;width=450;
top=4; bottom=-3;
left=-3; right=5;
grid=true;
degreeMode=radians;
---
y=2\cos(2x+\pi/4)|-2.7<x<4.2|dashed|#CA6702
y=2\cos(2x+\pi/4)|-0.39<x<1.18|#BB3E03

y=2|-10<x<10|dashed|#EE9B00
y=-2|-10<x<10|dashed|#EE9B00

(-0.39,2)|label: (-0.39, 2)|#BB3E03
(0,\sqrt{2})|label: (0, 1.41)|#CA6702
(0.39,0)|label: (0.39, 0)|#BB3E03
(1.18,-2)|label: (1.18, -2)|#BB3E03

(-2.5,2)|label: +2|#EE9B00
(-2.5,-2)|label: -2|#EE9B00

(0,3)|label: i(t)|black
(4.5,0)|label: t[ms]|black
```

- Ejercicio 2
```desmos-graph
height=250; width=450;
top=2.5; bottom=-0.5;
left=-2; right=5.5;
---
y=0.01|-2<x<0|dashed|#BB3E03
y=0.01|0<x<3|#BB3E03
(3,0.01)|open|#BB3E03

(3,2)|#BB3E03
y=2|3<x<4|#BB3E03
y=2|4<x<6|dashed|#BB3E03

(0,2)|cross|label:2|#CA6702
(4,2)|label:F(t)|#BB3E03
(5,0)|label: t|black
```

- Ejercicio 3
```desmos-graph
height=250; width=450;
top=10; bottom=-2;
left=-4; right=10;
---
u(x)=1|x\ge 3|dotted|#f1faee
r(x)=x-2|x\ge 2|dashed|#E9D8A6

t(x)=\sin(x)|-10<x<10|dashed|#94D2BD
f_{1}(x)=r(x)+t(x)|dashed|#E9D8A6
f=u(x)+r(x)|dashed|#fbc4ab

t(x)|-\pi\le x\le 2|#005F73
f_{1}(x)|2\le x\le 3|#BB3E03
f_{2}(x)=t(x)+r(x)+u(x)|x<10|#AE2012
```

- Ejercicio 4
```desmos-graph
height=300; width=300;
top=0.0019; bottom=-0.0015;
left=2.6; right=5.5;
---
u(x)=1|x\ge 3|dotted|#f1faee
g(x)=e^{-2x}|dashed|#94D2BD
h(x)=\cos(10x-(7\pi)/(36))|dotted|#f1faee

y=-e^{-2x}|dashed|#94D2BD
x=3|0.1>y>-0.1|dashed|#E9D8A6
f_{1}(x)=u(x)*g(x)*h(x)|x<7|#005F73
(3,0)|label: 3|black
```

- Ejercicio 5
```desmos-graph
height=300; width=300;
top=9; bottom=-1.2;
left=-0.5; right=10;
---
x=2|0<y<e^2|dashed|#9B2226
y=e^2|0<x<2|dashed|#9B2226

f(x)=e^{x}|0<x<2|#f1faee
g(x)=e^2+2-x|2<x<e^2+2|#f1faee

0\le y\le f(x)\left\{(0-x)(2-x)<0\right\}|#EE9B00
0\le y\le g(x)\left\{(2-x)(10-x)<0\right\}|#AE2012

y=-0.5|0<x<e^2+2|dotted|#EE9B00

(1,2.7)|label: e^t|#EE9B00
(0,8.4)|label: V(t)|black
(0,e^2)|label: e^2|#9B2226
(e^2+2,0)|label: e^2+1|#9B2226
(5,-0.5)|label: T=Periodo|#EE9B00
```
