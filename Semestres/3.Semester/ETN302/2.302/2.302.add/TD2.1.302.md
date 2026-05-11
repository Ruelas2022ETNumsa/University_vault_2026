---
Alias: [T2-Definicion]
Tags: [Leaves, Desmos]
---
- Def_ejem_1
```desmos-graph
height=150;width=400;
top=2.3; bottom=-2;
left=-0.8; right=6.5;
grid=true;
degreeMode=radians;
---
y=\cos(2x)|0<x<4|#005F73
y=\cos(2x)|4<x<10|dashed|#005F73

y=1.5*\sin(2x)|0<x<4|#BB3E03
y=1.5*\sin(2x)|4<x<10|dashed|#BB3E03

(0,1)|label: i(t)|#005F73
(0.75,1.5)|label: v(t)|#BB3E03

(6,0)|label: t[ms]|black
```

- Def_ejem_2
```desmos-graph
height=150;width=400;
top=1.2; bottom=-0.2;
left=-3; right=6;
---
y=0.01|-10<x<-2|dashed|#005F73
y=0.01|-2<x<-0.01|#005F73
(0,0.01)|open|#005F73

(0,1)|#005F73
y=1|0<x<4|#005F73
y=1|4<x<10|dashed|#005F73

(0,1)|label:x(t)|#005F73
(5.5,0)|label: t|black
```