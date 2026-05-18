---
Alias: [T2-Auxiliatura]
Tags: [Leaves, Desmos]
---

# Auxiliatura 2

## graficar
%%
-E 1
```desmos-graph
height=200;width=400;
top=4; bottom=-2;
left=-1; right=4;
grid=true;
---
u_1(x)=-1|-5<x<=0|#005F73
u_2(x)=3|5>x>=2|#005F73
y=0|0<x<2|#005F73

(0,-1)|label: -1|#005F73
(0,0)|open|#005F73
(2,0)|label: 2|open|#005F73
(2,3)|label: 3|#005F73
```

- E2
```desmos-graph
height=200;width=400;
top=6; bottom=-3;
left=-3; right=8;
grid=true;
---
u_1(x)=4|1.5<x<=8.2|#f1faee
u_2(x)=-2|5>x>=-5|#f1faee

u_1(x)|5<x|#005F73
u_2(x)|1.5>x|#005F73
u_1(x)+u_2(x)|#005F73


(1.5,-2)|open|label: (1.5,-2)|#005F73
(1.5,2)|label: (1.5,2)|#005F73
(5,2)|label: (1.5,2)|#005F73
(5,4)|open|label: (5,4)|#005F73
```

- E3
```desmos-graph
height=200;width=400;
top=3.5; bottom=-1.5;
left=-0.2; right=8;
grid=true;
---
r_1(x)=x-2|2<=x<10|dashed|#E9D8A6
r_2(x)=-2(x-4)|4<=x<10|dashed|#E9D8A6

y=1|-3<x<2|#005F73
1+r_1(x)|x<4|#005F73
1+r_1(x)+r_2(x)|#005F73

(0,1)|cross|label: 1|#005F73
(2,0)|cross|label: 2|#005F73
(4,0)|cross|label: 4|#005F73
(7,0)|cross|label: 7|#005F73
```

- E4
```desmos-graph
height=200;width=400;
top=4; bottom=-6.5;
left=-2; right=3;
grid=true;
---
x=1|-7.5<y<5|dashed|#94D2BD

u(x)=3|1<=x<5|dashed|#E9D8A6
r(x)=-2(x+1)|-1<=x<5|dashed|#E9D8A6

y=-1|-5<x<-1|#005F73
r(x)-1|-1<=x<1|#005F73
u(x)+r(x)-1||1<=x<5|#005F73

(-1,0)|cross|label: -1|#005F73
(1,0)|cross|label: 1|#005F73
(0,3)|cross|label: 3|#005F73
(0,-2)|cross|label: -2|#005F73
(0,-5)|cross|label: -5|#005F73
(1,-5)|open|#005F73
(1,-2)|#005F73

```

- E5
```desmos-graph
height=200;width=400;
top=4.5; bottom=-9;
left=-3; right=5;
grid=true;
---

u(x)=1|-5<x<4|dashed|#E9D8A6
r(x)=(x-1)|1<x<8|dashed|#E9D8A6

y=0|-5<x<1|#005F73
d_1(y)=-2|-8<y<0|#005F73
u(x)r(x)|#005F73
d_2(y)=3|2<y<3|#005F73
y=0|4<x<10|#005F73

(4,3)|label: (4,3)|#005F73
(4,0)|open|label: (4,0)|#005F73
(3,3)|label: d(t-3)|#005F73
(-2,-8)|label: -8d(t+2)|#005F73
(1,0)|cross|label: 1|#005F73
(0,3)|cross|label: 3|#005F73
(-2,0)|cross|label: -2|#005F73
(3,0)|cross|label: 3|#005F73
```

- E6
```desmos-graph
height=200;width=400;
top=4.5; bottom=-1.5;
left=-4; right=9;
grid=true;
---

r_1(x)=x-1|1<x<10|dashed|#E9D8A6
r_2(x)=-(x-4)|4<x<10|dashed|#E9D8A6

y=0|-5<x<-2|dashed|#005F73
y=0|-2<x<1|#005F73
r_1(x)|1<x<4|#005F73
r_1(x)+r_2(x)|x<7|#005F73
r_1(x)+r_2(x)|7<x<10|dashed|#005F73

(4,0)|cross|label: 4|#005F73
(1,0)|cross|label: 1|#005F73
(0,3)|cross|label: 3|#005F73



```

- Ej1
```desmos-graph
height=200;width=400;
top=4; bottom=-4;
left=-1.5; right=26;
grid=true;
---
f(x)=-3\sin(x/2)|-\pi<x<8\pi|#f1faee

f(x)|x<0|dashed|#005F73
f(x)|0<x<4\pi|#005F73
f(x)|4\pi<x|dashed|#005F73

(0,3)|cross|label: 3|#005F73
(0,-3)|cross|label: -3|#005F73
(4\pi,0)|cross|label: T|#005F73
(8\pi,0)|cross|label: 2T|#005F73
```

- Ej2
```desmos-graph
height=200;width=400;
top=2.5; bottom=-2.5;
left=-1.5; right=6;
grid=true;
---
f(x)=2\cos(x\pi-1)|-2<x<2\pi|#f1faee

f(x)|x<1/\pi|dashed|#005F73
f(x)|1/\pi<x<1/\pi+4|#005F73
f(x)|1/\pi+4<x|dashed|#005F73

(0,2)|cross|label: 2|#005F73
(0,-2)|cross|label: -2|#005F73
(1/\pi+2,0)|cross|label: T|#005F73
(1/\pi+4,0)|cross|label: 2T|#005F73
(1/\pi,0)|cross|label: to|#005F73
```

- E1
```desmos-graph
height=300;width=450;
top=12; bottom=-12;
left=-5; right=7;
grid=true;
---
h(x)=1-x|-5<x<7|#f1faee
f(x)=2\sin(x\pi)|1>x>-(1+4)|#f1faee
g(x)=\cos(x\pi)|1<x<1+6|#f1faee

h(x)|x>1|dashed|#E9D8A6
-h(x)|x>1|dashed|#E9D8A6
2h(x)|x<1|dashed|#E9D8A6
-2h(x)|x<1|dashed|#E9D8A6

(1-x)f(x)|x>-3|#005F73
(1-x)f(x)|x<-3|dashed|#005F73
(1-x)g(x)|x<5|#BB3E03
(1-x)g(x)|x>5||dashed|#BB3E03

(1,0)|open|label: 1|#005F73
```

- E2
```desmos-graph
height=200;width=400;
top=3.5; bottom=-6.5;
left=-4.5; right=20;
grid=true;
---
f(y)=(2/3)y|-6<y<3|#f1faee
f(1y)=x|-4<x<0|dashed|#005F73
f(1y)=x|0<x<2|#005F73

g(y)=(-2/3)y+4|-6<y<3|#005F73
f(1y)=x-12|#005F73
g(1y)=x-12|14<x<16|#005F73
g(1y)=x-12|x>16|dashed|#005F73

(0,3)|cross|label: 3|#005F73
(0,-6)|cross|label: -6|#005F73
(2,0)|cross|label: 2|#005F73
(4,0)|cross|label: 4|#005F73
(8,0)|cross|label: 8|#005F73
(12,0)|cross|label: 12|#005F73
(14,0)|cross|label: 14|#005F73
(16,0)|cross|label: 16|#005F73
```
%%




