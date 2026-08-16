---
Created: [10-June-22/20:54:29]
Title: [Tema_3]
Alias: [grafico resistencia]
Tags: [Whorled]
---
%%

---

# Tema 3 Desmos

---
2. Resistencias.
```desmos-graph
height=250; width=350;
top=5; bottom=-0.5;
left=-0.5; right=5;
---
y=x|0<x<5|#005F73

f(x)=4|0<x<4|dashed|#0A9396
f(x)-1|0<x<3|dashed|#0A9396
f(x)-2|0<x<2|dashed|#0A9396
f(x)-3|0<x<1|dashed|#0A9396

g(y)=4|0<y<4|dashed|#0A9396
x=g(y)-1|0<y<3|dashed|#0A9396
x=g(y)-2|0<y<2|dashed|#0A9396
x=g(y)-3|0<y<1|dashed|#0A9396

(0,4.5)|label: VR|#AE2012
(4.5,0)|label: i|#AE2012
```

3. Inductores ejemplo
- sea el grafico
```desmos-graph
height=200; width=450;
top=11.5; bottom=-11.5;
left=-1.5; right=7.5;
---
f(y)=y/10|-10<y<10|#f1faee
f(1y)=x|0>y|dashed|#005F73
f(1y)=x|0<y|#005F73
y=10|1<x<2|#005F73
f(-1y)=x-3|#005F73
y=-10|4<x<5|#005F73
f(1y)=x-6|0>y|#005F73
f(1y)=x-6|0<y|dashed|#005F73

(0,10)|label: 10|cross|#0A9396
(0,-10)|label: -10|cross|#0A9396
(-1,0)|label: -1|cross|#0A9396
(1,0)|label: 1|cross|#0A9396
(2,0)|label: 2|cross|#0A9396
(3,0)|label: 3|cross|#0A9396
(4,0)|label: 4|cross|#0A9396
(5,0)|label: 5|cross|#0A9396
(6,0)|label: 6|cross|#0A9396
(7,0)|label: 7|cross|#0A9396
(2.5,5)|label: L1|#005F73
(5.5,-5)|label: L2|#005F73
```



%%
- sea el resultado
```desmos-graph
height=200; width=450;
top=25; bottom=-25;
left=-0.5; right=6.5;
grid=true;
---
y=0|0.04<x<6|#f1faee
y_1=20|0<x<6|#f1faee
y_1|x<1|#AE2012
y_1|1<x<5|dashed|#E9D8A6
y_1|x>5|#AE2012

y_2=0|1<x<5|#f1faee
y_2|x<2|#AE2012
y_2|2<x<5|dashed|#E9D8A6
y_2|x>4|#AE2012

y=-20|2<x<4|#AE2012
y=-20|0<x<2|dashed|#E9D8A6

x_1=1|0<y<20|dashed|#CA6702
x=x_1+4|dashed|#CA6702
x=x_1+5|dashed|#CA6702
x_2=2|-20<y<0|dashed|#CA6702
x=x_2+2|dashed|#CA6702

(0,20)|label: 20|cross|#EE9B00
(0,-20)|label: -20|cross|#EE9B00
(1,0)|label: 1|cross|#EE9B00
(2,0)|label: 2|cross|#EE9B00
(4,0)|label: 4|cross|#EE9B00
(5,0)|label: 5|cross|#EE9B00
(6,0)|label: 6|cross|#EE9B00
```