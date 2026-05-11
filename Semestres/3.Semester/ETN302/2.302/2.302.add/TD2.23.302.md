---

Alias: [T2-Funciones exponenciales y por tramos]
Tags: [Leaves, Desmos]

---

- F. exponencial Creciente
```desmos-graph
height=200; width=400;
top=10; bottom=-0.5;
left=-25; right=15;
grid=true;
---
y-1=2* e^{x/10}|-30<x<30|#005F73
y=1|-30<x<20|dashed|#94D2BD

(0,3)|label: A|#005F73
(0,8)|label: f(t)|black
(12,0)|label: t|black
```

- F. exponencial Decreciente
```desmos-graph
height=200; width=400;
top=10; bottom=-0.5;
left=-15; right=25;
grid=true;
---
y-1=2* e^{-x/10}|-30<x<30|#005F73
y=1|-20<x<30|dashed|#94D2BD
(0,3)|label: A|#005F73
(0,8)|label: f(t)|black
(21,0)|label: t|black
```

- F. por tramos
```desmos-graph
height=250; width=550;
top= 3; bottom=-0.4;
left= -0.3; right= 4.6;
grid=true;
---
f(x)=\sin(2*x*\pi)+1|0<x<0.5|#005F73
0\le y\le f(x)\left\{(x)(0.5-x)>0\right\}|#005F73
x=0.5|0<y<1|dashed|#94D2BD
(0,1)|label: f1|#005F73
(0.5,1)|open|#005F73

g(x)=\exp(x/1.5)+0.2|0.5<x<1|#55a630
0\le y\le g(x)\left\{(4-x)(2-x)>0\right\}|#55a630
x=0.5|1<y<1.6|dashed|#55a630
x=1|0.5<y<2.1|dashed|#55a630
(0.5,1.6)|label: f2|#55a630
(1,2.15)|open|#55a630


h(x)=(x-0.3)^{2}+\sin(3(x+4))|1<x<2|#BB3E03
0\le y\le h(x)\left\{(4-x)(6-x)>0\right\}|#BB3E03
x=1|0<y<1.1|dashed|#BB3E03
x=2|0<y<2.1|dashed|#BB3E03
(1,1.15)|label: f3|#BB3E03
(2,2.15)|open|#BB3E03


k(x)=+1.5-(x-3)^3|2<x<4|#E9D8A6
0\le y\le k(x)\left\{(4-x)(6-x)>0\right\}|#E9D8A6

x=2|2.15<y<2.5|dashed|#f0b67f
x=4|0<y<0.5|dashed|#f0b67f
(2,2.5)|label: f4|#f0b67f
(4,0.5)|open|#f0b67f

(0.5,0)|cross|label: a|#005F73
(1,0)|cross|label: b|#BB3E03
(2,0)|cross|label: c|#AE2012
(4,0)|cross|label: d|#f0b67f

(0,2.5)|label: f(t)|black
(4.5,0)|label: t|black
y=0.5|dotted|4.1<x<4.3|#e9ecef
```