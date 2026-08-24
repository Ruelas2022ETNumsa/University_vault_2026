> [!important]
> $$ 
> \frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_r}\right)
> -
> \frac{\partial T}{\partial q_r}
> =
> F_x\frac{\partial x}{\partial q_r}
> +
> F_y\frac{\partial y}{\partial q_r}
> +
> F_z\frac{\partial z}{\partial q_r}
> $$

## Ejercicios resueltos


### Ejercicio 1

![[paso607-24-08-2026_17-16-06.png]]



[figura 2.8]

$$
x=r\sin\theta
$$

$$
y=r\cos\theta
$$

$$
T=\frac{1}{2}mv^2
=
\frac{1}{2}m
\left(
\dot r^2+r^2\dot\theta^2+\dot z^2
\right)
$$

$$
\frac{d}{dt}
\left(
\frac{\partial T}{\partial\dot r}
\right)
-
\frac{\partial T}{\partial r}
=
F_x\frac{\partial x}{\partial r}
+
F_y\frac{\partial y}{\partial r}
+
F_z\frac{\partial z}{\partial r}
$$

$$
\frac{m}{2}2\ddot r=m\ddot r
$$

$$
\frac{m}{2}2\dot\theta^2r
=
mr\dot\theta^2
$$

$$
-F\cos\theta\sin^2\theta
$$

$$
-F\cos^2\theta+mg
$$

$$
m\ddot r-mr\dot\theta^2
=
-k(r-l_0)\sin^2\theta
-k(r-l_0)\cos^2\theta
+mg\cos\theta
$$

$$
m(\ddot r-r\dot\theta^2)
=
-k(r-l_0)+mg\cos\theta
$$

> [!important]
> $$
> \boxed{
> m(\ddot r-r\dot\theta^2)
> =
> -k(r-l_0)+mg\cos\theta
> }
> $$

$$
\text{Resorte:}\qquad
\frac{1}{2}k(r-l_0)^2
$$

---

### Continuación — Ejercicio 1

Si:

$$
r=0
$$

$$
-mr\dot\theta^2=mg\cos\theta
$$

$$
\frac{d}{dt}
\left(
\frac{\partial T}{\partial\dot\theta}
\right)
-
\frac{\partial T}{\partial\theta}
=
F_x\frac{\partial x}{\partial\theta}
+
F_y\frac{\partial y}{\partial\theta}
$$

$$
\frac{mr^2 2\dot\theta}{2}
$$

Entonces:

$$
m(2r\dot r\dot\theta+r^2\ddot\theta)
=
-mgr\sin\theta
$$

Si:

$$
r=l
$$

> [!important]
> $$
> \boxed{
> l^2\ddot\theta=-gl\sin\theta
> }
> $$

### Ejercicio 2

![[paso607-24-08-2026_17-16-22.png]]


[figura 2.9]

$$
z=0
$$

$$
N=2\quad(x,y)
$$

$$
T=
\frac{m}{2}
\left(
\dot x^2+\dot y^2+\dot z^2
\right)
$$

$$
\frac{d}{dt}
\left(
\frac{\partial T}{\partial\dot x}
\right)
-
\frac{\partial T}{\partial x}
=
F_x\frac{\partial x}{\partial x}
+
F_y\frac{\partial y}{\partial x}
+
F_z\frac{\partial z}{\partial x}
$$

$$
\frac{m}{2}2\ddot x
$$

Entonces:

> [!important]
> $$
> \boxed{
> m\ddot x=0
> }
> $$

Otro:

$$
\frac{d}{dt}
\left(
\frac{\partial T}{\partial\dot y}
\right)
-
\frac{\partial T}{\partial y}
=
F_x\frac{\partial x}{\partial y}
+
F_y\frac{\partial y}{\partial y}
$$

simplifacnado alguno elementos:
$$
\frac{m}{2}2\ddot y
$$

$$
F_y=-mg
$$

entonces :
$$\ddot y = - g$$



### Ejercicio 3 *

![[paso607-24-08-2026_17-16-32.png]]

[figura 2.7]

$$
z=0
$$

$$
N=2\quad(r,\theta,z)
$$

$$
x=r\cos\theta
$$

$$
y=r\sin\theta
$$

$$
N:\text{ Grados de libertad}
$$

$$
T=\frac{m}{2}\left(\dot r^2+r^2\dot\theta^2+\dot z^2\right)
$$

$$
\frac{d}{dt}
\left(
\frac{\partial T}{\partial\dot r}
\right)
-
\frac{\partial T}{\partial r}
=
F_x\frac{\partial x}{\partial r}
+
F_y\frac{\partial y}{\partial r}
+
F_z\frac{\partial z}{\partial r}
$$

$$
\frac{\partial x}{\partial r}=\cos\theta
$$

$$
\frac{\partial y}{\partial r}=\sin\theta
$$

$$
F_x=-F\cos\theta
$$

$$
F_y=-F\sin\theta
$$

$$
\frac{m}{2}2\ddot r
$$

$$
\frac{m}{2}2\dot\theta^2r
$$

$$
m\ddot r-mr\dot\theta^2
=
-\frac{GMm}{r^2}
\left(
\cos^2\theta+\sin^2\theta
\right)
$$

$$
\boxed{
\ddot r-r\dot\theta^2-\frac{GM}{r^2}=0
}
$$

$$
\frac{d}{dt}
\left(
\frac{\partial T}{\partial\dot\theta}
\right)
-
\frac{\partial T}{\partial\theta}
=
F_x\frac{\partial x}{\partial\theta}
+
F_y\frac{\partial y}{\partial\theta}
$$

$$
\frac{\partial x}{\partial\theta}
=
-r\sin\theta
$$

$$
\frac{\partial y}{\partial\theta}
=
r\cos\theta
$$

$$
F_x=-F\cos\theta
$$

$$
F_y=-F\sin\theta
$$

$$
\frac{m}{2}r^2 2\ddot\theta
$$

$$
m(2r\dot r\dot\theta+r^2\ddot\theta)=0
$$

$$
\boxed{
m(2r\dot r\dot\theta+r^2\ddot\theta)=0
}
$$
