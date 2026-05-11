---
Alias: [T2-Tipos de señales]
Tags: [Leaves, Desmos]
---

- Unitario
```desmos-graph
height=150; width=400;
top=1.7; bottom=-0.2;
left=-3; right=4.5;
---
\polygon( (0,0),(10,0),(10,1),(0,1) )|#0A9396
x=0|-1<y<10|black

y=0.01|-10<x<-2|dashed|#005F73
y=0.01|-2<x<0|#005F73
(0,0.01)|open|#005F73

y=1|-1<x<0|dashed|#94D2BD

(0,1)|#005F73
y=1|0<x<2|#005F73
y=1|2<x<10|dashed|#005F73

(-1,1)|label:A|#94D2BD
(1.5,1)|label:u(t)|#005F73
(3.5,0)|label: t|black
```

- Rampa
```desmos-graph
height=150; width=400;
top=4; bottom=-0.5;
left=-1.5; right=5;
---
\polygon( (1,0),(10,0),(11,10) ) |#0A9396
y=0|1<x<10|black
y=0.01|-10<x<-0.5|dashed|#005F73
y=0.01|-0.5<x<1|#005F73
x=y+1|0.01<y<2|#005F73
x=y+1|1<y<10|dashed|#005F73
x=1|-5<y<5|dashed|#94D2BD

(1,0)|label: x|#94D2BD
(3,2)|label:A·r(t-x)|#005F73
(4.5,0)|label: t|black
```

- Impulso unitario def-0
```desmos-graph
height=150; width=200;
top=1.2; bottom=-0.2;
left=-0.4; right=2.4;
grid=true;
---
y=1|0<x<1|dashed |#94D2BD
\polygon( (0.8,0.8),(1.2,0.8),(1,1) ) |#005F73
x=1|0<y<0.8|#005F73

(1,0.9)|label:D(t-x)|#005F73
(1,0)|label:x|#005F73
(0,1)|label:A|#94D2BD
(2,0)|label:t |black
```

- Impulso unitario def-1
```desmos-graph
height=150; width=250;
top=7; bottom=-1;
left=-0.5; right=5;
grid=false;
---
\polygon( (0,0),(1,0),(1,6.2),(0,6.2) )|#fdffb6
x=1  |0<y<6.2|dashed|#EE9B00
y=6.2|0<x<1|dashed|#EE9B00

\polygon( (0,0),(2,0),(2,5.5),(0,5.5) )|#e26d5c
x=2  |0<y<5.5|dashed|#AE2012
y=5.5|0<x<2|dashed|#AE2012

\polygon( (0,0),(3,0),(3,4.5),(0,4.5) )|#f3722c
x=3  |0<y<4.5|dashed|#BB3E03
y=4.5|0<x<3|dashed|#BB3E03

\polygon( (0,0),(4.5,0),(4.5,3.5),(0,3.5) ) |#0A9396
x=4.5|0<y<3.5|dashed|#005F73
y=3.5|0<x<4.5|dashed|#005F73

x=0|black
y=0|black

y=4|3.3<x<4.2||#94D2BD
\polygon( (3.3,3.8),(3.2,4),(3.3,4.2) ) |#94D2BD

(3.75,1.7)|label:Fp|#005F73
(4.5,0)|label:a|#005F73
(0,3.5)|label:1/a|#005F73
```

- Impulso unitario def-2
```desmos-graph
height=150; width=250;
top=1.2; bottom=-0.2;
left=-0.5; right=2.7;
grid=true;
---
\polygon( (-0.2,0.8),(0.2,0.8),(0,1) ) |#005F73
x=0.01|0<y<0.8|#005F73

(0,0.9)|label:Fp|#005F73
(2.3,0)|label:t |black
```