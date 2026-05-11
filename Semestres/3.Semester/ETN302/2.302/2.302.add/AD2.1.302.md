# Auxiliatura

## Señales
%%
- Ejercicio 1
```desmos-graph
height=200; width=400;
top=1.5; bottom=-1.5;
left=-0.1; right=0.5;

---
a=\pi/4

f(x)=\cos(70x-a)|-0.2<x<0.5|#f1faee
g(x)=e^{-3x}|-0.2<x<0.5|dashed|#E9D8A6
-g(x)|dashed|#E9D8A6

h(x)=f(x)*g(x)|x>a/70|#CA6702
h(x)=f(x)*g(x)|dashed|x<a/70|#E9D8A6

(0.0106,0.96)|cross|label: (0.01 , 0.96)|#AE2012
(0.0106+\pi/35,0)|cross|label: T|#AE2012
(0.0106+2*\pi/35,0)|cross|label: 2T|#AE2012
(0.0106+3*\pi/35,0)|cross|label: 3T|#AE2012
```

- Ejercicio 2
```desmos-graph
height=200; width=400;
top=2; bottom=-2;
left=-0.5; right=15;
---
a=\pi/2
u(x)=1|x>a|dashed|#E9D8A6
y=-1|x>a|dashed|#E9D8A6
f(x)=\sin(x)|0<x<10*a|#f1faee

f(x)|x<a|dashed|#94D2BD
f(x)|a<x<9a|#005F73
f(x)|x>9a|dashed|#94D2BD

x=a|-1<y<1|dashed|#E9D8A6
(\pi/2,1)|cross|label: (pi/2 , 1)|#AE2012
(\pi/2,0)|cross|label: pi/2|#AE2012
(5*\pi/2,0)|cross|label: T|#AE2012
(9*\pi/2,0)|cross|label: 2T|#AE2012
```

- Ejercicio 3
```desmos-graph
height=150; width=400;
top=15; bottom=-15;
left=-0.5; right=15;
---
r(x)=x-\pi/2|x>\pi/2|dashed|#E9D8A6
y=-(x-\pi/2)|x>\pi/2|dashed|#E9D8A6
f(x)=\sin(x)|-0.5<x<15|dashed|#f1faee
f(x)*r(x)|x>\pi/2|#EE9B00

(\pi/2,0)|cross|label: pi/2|#AE2012
```

## Parametros basicos
- E2
```desmos-graph
height=150; width=400;
top=5; bottom=-0.5;
left=-0.5; right=7;
---
y=2|-2<x<10|dashed|#E9D8A6
x=1|0<y<4|dashed|#E9D8A6
x=2|0<y<4|dashed|#E9D8A6
x=3|0<y<4|dashed|#E9D8A6
x=4|0<y<4|dashed|#E9D8A6
x=5|0<y<4|dashed|#E9D8A6
x=6|0<y<4|dashed|#E9D8A6

f(x)=4|0<x<7|#f1faee
f(x)|0<x<1|#9B2226
f(x)|2<x<3|#9B2226
f(x)|4<x<5|#9B2226
f(x)|6<x<7|dotted|#9B2226

g(x)=0|1<x<6|#f1faee
g(x)|1<x<2|#9B2226
g(x)|3<x<4|#9B2226
g(x)|5<x<6|dotted|#9B2226

(0,2)|cross|label: 2|#AE2012
(0,4)|label: 4|#AE2012
(1,0)|label: 1|#AE2012
(2,0)|label: 2|#AE2012
```


- E3

```desmos-graph
height=150; width=400;
top=1.5; bottom=-1;
left=-0.5; right=6.5;
---
y=1|0<x<8|dashed|#E9D8A6
y=-0.5|0<x<8|dashed|#E9D8A6

f(x)=\sin(\pi*x)|0<x<8|#f1faee
0<=y<=f(x)|#005F73

g(x)=(-x)/2|0<x<1|#f1faee
g(x-1)<=y<=0|#005F73
g(x-3)<=y<=0|#005F73
g(x-5)<=y<=0|#005F73
g(x-7)<=y<=0|#005F73

x=2|-0.5<y<0|#005F73
x=4|-0.5<y<0|#005F73
x=6|-0.5<y<0|#005F73

y=0|0<y<8|black
(1,0)|cross|label: 1|#AE2012
(2,0)|cross|label: 2|#AE2012
(0,1)|cross|label: 1|#AE2012
(0,-0.5)|cross|label: -0.5|#AE2012
```

- E4
```desmos-graph
height=250; width=400;
top=30; bottom=-40;
left=-7; right=7;
---
g(x)=-x^2-2|-10<x<10|dashed|#E9D8A6
-g(x)-4|-10<x<10|dashed|#E9D8A6

f(x)=x^2*1\sin(x*\pi-\pi/2)-2|#005F73
```
%%


