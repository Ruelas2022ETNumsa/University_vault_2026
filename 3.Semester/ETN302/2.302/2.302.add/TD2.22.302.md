---

Alias: [T2-Funciones periódicas]
Tags: [Leaves, Desmos]

---

- F. periodicas gral
```desmos-graph
height=250; width=450;
top=2.5; bottom=-1.4;
left=-2.5; right=4;
grid=true;
degreeMode=radians;
---
(0,2)|label:f(t)|black
y=\sin(x * \pi+\pi/2)|-0.5<x<1.5|#005F73

y=\sin(x * \pi+\pi/2)|-10<x<-0.5|dashed|#94D2BD
y=\sin(x * \pi+\pi/2)|1.5<x<10|dashed|#94D2BD

y=1|-1.5<x<0|dashed|#AE2012
y=-1|-1.5<x<0|dashed|#AE2012

y=-0.5|-0.5<x<0|dashed|#CA6702
x=0|-0.5<y<1.5|dashed|#CA6702
x=-0.5|-0.5<y<0|dashed|#CA6702
(-0.25,-0.5)|label: to|#CA6702

y=1.5|0<x<2|#CA6702
x=2|1<y<1.5|dashed|#CA6702
(1,1.5)|label: T|#CA6702

(0,1)|cross|label: A|#005F73
(-1.5,1)|label: Vmax|#AE2012
(-1.5,-1)|label: Vmax|#AE2012
(3.0,0)|label: t|black
```

- F. periodicas ej1
```desmos-graph
height=150; width=400;
top= 5; bottom=-4.5;
left= -1.5; right= 9.8;
grid=true;
---
-3*x=y-3|-3<y<3|#005F73
-3*x=y-9|-3<y<3|#005F73
-3*x=y-15|-3<y<3|#005F73
-3*x=y-21|-3<y<3|dashed|#005F73
-3*x=y-27|-3<y<3|dashed|#005F73
x=2|-3<y<3|dashed|#94D2BD
x=4|-3<y<3|dashed|#94D2BD
x=6|-3<y<3|dashed|#94D2BD
x=8|-3<y<3|dashed|#94D2BD
x=10|-3<y<3|dashed|#94D2BD
(0,4)|label: f(t)|black
(9,0)|label: t|black
(2,0)|label: T|cross|#BB3E03
(4,0)|label: 2·T|cross|#BB3E03
```

- F. periodicas ej2
```desmos-graph
height=150; width=400;
top= 3; bottom=-0.5;
left= -1.5; right= 10;
grid=true;
degreeMode=radians;
---
y-1=\sin((x * \pi+\pi*2)/2)|0<x<4|#005F73
y-1=\sin((x * \pi+\pi*2)/2)|4<x<10|dashed|#005F73

x=4|0<y<1|dashed|#94D2BD
x=8|0<y<1|dashed|#94D2BD

(4,0)|label: T|cross|#BB3E03
(8,0)|label: 2·T|cross|#BB3E03
(0,2.5)|label: f(t)|black
(9,0)|label: t|black
```

- F.periodicas ej3
```desmos-graph
height=150; width=400;
top= 3.5; bottom=-0.5;
left= -1.5; right= 10;
grid=true;
---
y-1=\sin(2*x*\pi)|0<x<0.5|#005F73
(y+0.5)^{2}+(x-0.5)^2=1.5^2|0.5<x<1|y>0|#005F73
x=1|0<y<0.914|#005F73
y=x-1|1<x<2|#005F73

y-1=\sin(2*x*\pi)|2<x<2.5|#005F73
(y+0.5)^{2}+(x-2.5)^2=1.5^2|2.5<x<3|0<y|#005F73
x=3|0<y<0.914|#005F73
y=x-3|3<x<4|#005F73

y-1=\sin(2*x*\pi)|4<x<4.5|dashed|#005F73
(y+0.5)^{2}+(x-4.5)^2=1.5^2|4.5<x<5|y>0|dashed|#005F73
x=5|0<y<0.914|dashed|#005F73
y=x-5|5<x<6|dashed|#005F73

y-1=\sin(2*x*\pi)|6<x<6.5|dashed|#005F73
(y+0.5)^{2}+(x-6.5)^2=1.5^2|6.5<x<7|y>0|dashed|#005F73
x=7|0<y<0.914|dashed|#005F73
y=x-7|7<x<8|dashed|#005F73

y-1=\sin(2*x*\pi)|8<x<8.5|dashed|#005F73
(y+0.5)^{2}+(x-8.5)^2=1.5^2|8.5<x<9|y>0|dashed|#005F73
x=9|0<y<0.914|dashed|#005F73
y=x-9|9<x<10|dashed|#005F73

x=2|0<y<1|dashed|#BB3E03
x=4|0<y<1|dashed|#BB3E03

(2,0)|label: T|cross|#BB3E03
(4,0)|label: 2·T|cross|#BB3E03
(0,3)|label: f(t)|black
(9,0)|label: t|black
```

- F. periodicas ej4
```desmos-graph
height=150; width=400;
top= 1.5; bottom=-3;
left= -1.5; right= 10;
grid=true;
---
y=-0.5|0<x<1|#005F73
y=-2|1<x<2|#005F73
y=-0.5|2<x<3|#005F73
y=-2|3<x<4|#005F73
y=-0.5|4<x<5|#005F73
y=-2|5<x<6|#005F73
y=-0.5|6<x<7|#005F73
y=-2|7<x<8|#005F73
y=-0.5|8<x<9|#005F73
y=-2|9<x<10|#005F73
y=-0.5|10<x<11|#005F73
x=1|-2<y<-0.5|dashed|#94D2BD
x=2|-2<y<-0.5|dashed|#94D2BD
x=3|-2<y<-0.5|dashed|#94D2BD
x=4|-2<y<-0.5|dashed|#94D2BD
x=5|-2<y<-0.5|dashed|#94D2BD
x=6|-2<y<-0.5|dashed|#94D2BD
x=7|-2<y<-0.5|dashed|#94D2BD
x=8|-2<y<-0.5|dashed|#94D2BD
x=9|-2<y<-0.5|dashed|#94D2BD
x=10|-2<y<-0.5|dashed|#94D2BD

(2,0)|label: T|cross|#BB3E03
(4,0)|label: 2·T|cross|#BB3E03
(0,0.2)|label: f(t)|black
(9,0)|label: t|black
```