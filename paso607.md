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
