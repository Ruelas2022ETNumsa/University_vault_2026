Aquí van 10 ejemplos variados para probar:

1. $f(x) = x^3 - 6x^2 + 9x - 4$ — polinomio cúbico


**WolframAlpha:** $f(x) = x^3 - 6x^2 + 9x - 4$

**Gráfica:**
![[Untitled-14-07-2026_14-46-28.png]]

**Alternate form:**
$f(x) = (x - 4) (x - 1)^2$

**Roots:**
$x = 1 | x = 4$

**Properties as a real function:**
$R (all real numbers) | R (all real numbers) | surjective onto R$

**Derivative:**
$d/dx(x^3 - 6 x^2 + 9 x - 4) = 3 (x^2 - 4 x + 3)$

**Indefinite integral assuming all variables are real:**
$integral(x^3 - 6 x^2 + 9 x - 4) dx = x^4/4 - 2 x^3 + (9 x^2)/2 - 4 x + constant$

**Local minimum:**
$min{x^3 - 6 x^2 + 9 x - 4} = -4 at x = 3$

**Local maximum:**
$max{x^3 - 6 x^2 + 9 x - 4} = 0 at x = 1$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
f(x) = x^3 - 6x^2 + 9x - 4
Si aplica, graficá usando Desmos o TikZJax.
```



---

**WolframAlpha:** $integrate x^2 * sin(x) dx$

**Gráfica:**
![[Untitled-14-07-2026_15-22-20.png]]

**Indefinite integral:**
$integral x^2 sin(x) dx = 2 x sin(x) - (x^2 - 2) cos(x) + constant$

**Alternate forms of the integral:**
$(2 - x^2) cos(x) + 2 x sin(x) + constant | -1/2 e^(-i x) x^2 - 1/2 e^(i x) x^2 + i e^(-i x) x - i e^(i x) x + e^(-i x) + e^(i x) + constant$

**Reduced trigonometric form:**
$2 cos(x) - cos(x) x^2 + 2 x sin(x) + constant$

**Series expansion of the integral at x = 0:**
$2 + x^4/4 - x^6/36 + x^8/960 + O(x^9)
(Taylor series)$

**Definite integral:**
$integral_0^π x^2 sin(x) dx = π^2 - 4≈5.8696$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
integrate x^2 * sin(x) dx
Si aplica, graficá usando Desmos o TikZJax.
```


2. integrate x^2 * sin(x) dx — integral por partes

[ERROR] Wolfram Alpha no pudo interpretar la expresión.

**WolframAlpha:** $integrate x^2 * sin(x) dx$

**Gráfica:**
![[Untitled-14-07-2026_15-03-47.png]]

**Indefinite integral:**
$integral x^2 sin(x) dx = 2 x sin(x) - (x^2 - 2) cos(x) + constant$

**Alternate forms of the integral:**
$(2 - x^2) cos(x) + 2 x sin(x) + constant | -1/2 e^(-i x) x^2 - 1/2 e^(i x) x^2 + i e^(-i x) x - i e^(i x) x + e^(-i x) + e^(i x) + constant$

**Reduced trigonometric form:**
$2 cos(x) - cos(x) x^2 + 2 x sin(x) + constant$

**Series expansion of the integral at x = 0:**
$2 + x^4/4 - x^6/36 + x^8/960 + O(x^9)
(Taylor series)$

**Definite integral:**
$integral_0^π x^2 sin(x) dx = π^2 - 4≈5.8696$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
integrate x^2 * sin(x) dx
Si aplica, graficá usando Desmos o TikZJax.
```



3. `solve x^2 + 3x - 10 = 0` — ecuación cuadrática

**WolframAlpha:** $solve x^2 + 3x - 10 = 0$

**Gráfica:**
![[Untitled-14-07-2026_15-22-44.png]]

**Results:**
$x = -5 | x = 2$

**Sum of roots:**
$-3$

**Product of roots:**
$-10$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
solve x^2 + 3x - 10 = 0
Si aplica, graficá usando Desmos o TikZJax.
```


[ERROR] Wolfram Alpha no pudo interpretar la expresión.


4. `limit sin(x)/x as x->0` — límite clásico

**WolframAlpha:** $limit sin(x)/x as x->0$

**Gráfica:**
![[ima-1.png]]

**Limit:**
$lim_(x->0) sin(x)/x = 1$

**Series expansion at x = 0:**
$1 - x^2/6 + x^4/120 + O(x^6)
(Taylor series)$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
limit sin(x)/x as x->0
Si aplica, graficá usando Desmos o TikZJax.
```


[ERROR] Wolfram Alpha no pudo interpretar la expresión.


5. `y'' - 3y' + 2y = 0` — ecuación diferencial

**WolframAlpha:** $y'' - 3y' + 2y = 0$

**Gráfica:**
![[Untitled-14-07-2026_15-23-08.png]]

**ODE names:**
$y''(x) = -2 y(x) + 3 y'(x) | d/(dx) (e^(-3 x) y'(x)) + 2 e^(-3 x) y(x) = 0$

**ODE classification:**
$second-order linear ordinary differential equation$

**Alternate forms:**
$y''(x) = 3 y'(x) - 2 y(x) | y''(x) + 2 y(x) = 3 y'(x)$

**Differential equation solution:**
$y(x) = c_1 e^x + c_2 e^(2 x)$

**Differential equation series solution about x = 0:**
$c_1 + c_2 x + ((3 c_2)/2 - c_1) x^2 + ((7 c_2)/6 - c_1) x^3 + ((5 c_2)/8 - (7 c_1)/12) x^4 + ((31 c_2)/120 - c_1/4) x^5 + O(x^6)
(converges everywhere)$

**Differential equation infinite series expansion:**
$sum_(n=0)^∞ ((c_1 + 2^n c_2) x^n)/(n!)
(converges everywhere)$

**Differential equation series solution about x = -∞:**
$c_1 e^(2 x) + c_2 e^x
(converges everywhere)$

**Sample solution family:**
$  (sampling y(0) and y'(0))$

**Possible Lagrangian:**
$ℒ(y', y, x) = 1/2 (e^(-3 x) (y')^2 - 2 e^(-3 x) y^2)$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
y'' - 3y' + 2y = 0
Si aplica, graficá usando Desmos o TikZJax.
```


6. `matrix {{1,2},{3,4}} inverse` — matriz inversa


**WolframAlpha:** $matrix {{1,2},{3,4}} inverse$

**Gráfica:**
![[Untitled-14-07-2026_15-23-40.png]]

**Result:**
$1/2(-4 | 2
3 | -1)$

**Expanded form:**
$(-2 | 1
3/2 | -1/2)$

**Dimensions:**
$2 (rows) × 2 (columns)$

**Transpose:**
$(-2 | 3/2
1 | -1/2)$

**Cofactors:**
$(-1/2 | -3/2
-1 | -2)$

**Trace:**
$-5/2$

**Determinant:**
$-1/2$

**Characteristic polynomial:**
$λ^2 + (5 λ)/2 - 1/2$

**Eigenvalues:**
$λ_1 = 1/4 (-5 - sqrt(33)) | λ_2 = 1/4 (sqrt(33) - 5)$

**Eigenvectors:**
$v_1 = (1/6 (-3 - sqrt(33)), 1) | v_2 = (1/6 (-3 + sqrt(33)), 1)$

**Diagonalization:**
$(-2 | 1
3/2 | -1/2) = P.D.P^(-1)
where
P = 1/6(-3 - sqrt(33) | sqrt(33) - 3
6 | 6)
D = 1/4(-5 - sqrt(33) | 0
0 | sqrt(33) - 5)
P^(-1) = 1/22(-2 sqrt(33) | 11 - sqrt(33)
2 sqrt(33) | 11 + sqrt(33))$

**Condition number:**
$21$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
matrix {{1,2},{3,4}} inverse
Si aplica, graficá usando Desmos o TikZJax.
```


6. `100 km/h to m/s` — conversión de unidades

**WolframAlpha:** $100 km/h to m/s$

**Result:**
$27.78 m/s (meters per second)$

**Additional conversions:**
$1491 mi/d (miles per day) | 62.14 mph (miles per hour) | 1.036 mi/min (miles per minute) | 91.13 ft/s (feet per second) | 328084 ft/h (feet per hour)$

**Comparisons as speed:**
$ ≈ 0.91 × speed of the fastest water animal (sailfish) ( ≈ 110 km/h ) |  ≈ typical takeoff speed of a light aircraft like a Cessna 150 ( ≈ 63 mph ) |  ≈ (0.6 to 1.5) × instantaneous speed of air particles during an average human sneeze ( 40 to 100 mph )$

**Fujita tornado wind speed classification:**
$F0 (gale tornado)$

**Interpretations:**
$speed$

**Basic unit dimensions:**
$[length] [time]^(-1)$

**Corresponding quantities:**
$Time to travel 1 meter from t = d/v:
 | 36 ms (milliseconds) | Time to travel 1 kilometer from t = d/v:
 | 36 seconds
 | 0.6 minutes | Slowness from s = 1/v:
 | 36 s/km (seconds per kilometer)
 | 0.6 min/km (minutes per kilometer)
 | 0.011 s/ft (seconds per foot) | Corresponding Mach number under standard conditions:
 | 0.081
 | (assuming speed of sound ≈ 340 m/s) | Observed wind intensity from B = (v/(0.836 m/s))^(2/3):
 | 10 Beaufort scale numbers | Effective rocket exhaust speed from v_e = I_sp:
 | 28 m/s (meters per second) | Thrust specific fuel consumption from SFC = 1/I_sp:
 | 36000 g/(kN s) (grams per kilonewton second)$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
100 km/h to m/s
Si aplica, graficá usando Desmos o TikZJax.
```



7. `area of ellipse a=5 b=3` — geometría


**WolframAlpha:** $area of ellipse a=5 b=3$

**Result:**
$area | 47.12$

**Equation:**
$A = π a b | 
A | area
a | semimajor axis
b | semiminor axis$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
area of ellipse a=5 b=3
Si aplica, graficá usando Desmos o TikZJax.
```


7. `sin(45 degrees)` — trigonometría


**WolframAlpha:** $sin(45 degrees)$

**Result:**
$1/sqrt(2)$

**Decimal approximation:**
$0.7071067811865475244008443621048490392848359376884740365883398689...$

**Reference triangle for angle 45°:**
$
width | cos(45 °) = 1/sqrt(2)≈0.707107
height | sin(45 °) = 1/sqrt(2)≈0.707107$

**Alternate form:**
$sqrt(2)/2$

**Continued fraction:**
$[0; 1, 2^_]$

**Alternative representations:**
$sin(45 °) = cos(45 °) | sin(45 °) = -cos(135 °) | sin(45 °) = 1/csc(45 °)$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
sin(45 degrees)
Si aplica, graficá usando Desmos o TikZJax.
```



8. `simple interest principal=5000 rate=3% time=5 years` — finanzas
[ERROR] Wolfram Alpha no pudo interpretar la expresión.
[ERROR] Wolfram Alpha no pudo interpretar la expresión.



- `100 km/h to m/s` — conversión de unidades


**WolframAlpha:** $100 km/h to m/s$

**Result:**
$27.78 m/s (meters per second)$

**Additional conversions:**
$1491 mi/d (miles per day) | 62.14 mph (miles per hour) | 1.036 mi/min (miles per minute) | 91.13 ft/s (feet per second) | 328084 ft/h (feet per hour)$

**Comparisons as speed:**
$ ≈ 0.91 × speed of the fastest water animal (sailfish) ( ≈ 110 km/h ) |  ≈ typical takeoff speed of a light aircraft like a Cessna 150 ( ≈ 63 mph ) |  ≈ (0.6 to 1.5) × instantaneous speed of air particles during an average human sneeze ( 40 to 100 mph )$

**Fujita tornado wind speed classification:**
$F0 (gale tornado)$

**Interpretations:**
$speed$

**Basic unit dimensions:**
$[length] [time]^(-1)$

**Corresponding quantities:**
$Time to travel 1 meter from t = d/v:
 | 36 ms (milliseconds) | Time to travel 1 kilometer from t = d/v:
 | 36 seconds
 | 0.6 minutes | Slowness from s = 1/v:
 | 36 s/km (seconds per kilometer)
 | 0.6 min/km (minutes per kilometer)
 | 0.011 s/ft (seconds per foot) | Corresponding Mach number under standard conditions:
 | 0.081
 | (assuming speed of sound ≈ 340 m/s) | Observed wind intensity from B = (v/(0.836 m/s))^(2/3):
 | 10 Beaufort scale numbers | Effective rocket exhaust speed from v_e = I_sp:
 | 28 m/s (meters per second) | Thrust specific fuel consumption from SFC = 1/I_sp:
 | 36000 g/(kN s) (grams per kilonewton second)$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
100 km/h to m/s
Si aplica, graficá usando Desmos o TikZJax.
```






- `area of ellipse a=5 b=3` — geometría




**WolframAlpha:** $area of ellipse a=5 b=3$

**Result:**
$area | 47.12$

**Equation:**
$A = π a b | 
A | area
a | semimajor axis
b | semiminor axis$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
area of ellipse a=5 b=3
Si aplica, graficá usando Desmos o TikZJax.
```





- `sin(45 degrees)` — trigonometría



**WolframAlpha:** $sin(45 degrees)$

**Result:**
$1/sqrt(2)$

**Decimal approximation:**
$0.7071067811865475244008443621048490392848359376884740365883398689...$

**Reference triangle for angle 45°:**
$
width | cos(45 °) = 1/sqrt(2)≈0.707107
height | sin(45 °) = 1/sqrt(2)≈0.707107$

**Alternate form:**
$sqrt(2)/2$

**Continued fraction:**
$[0; 1, 2^_]$

**Alternative representations:**
$sin(45 °) = cos(45 °) | sin(45 °) = -cos(135 °) | sin(45 °) = 1/csc(45 °)$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
sin(45 degrees)
Si aplica, graficá usando Desmos o TikZJax.
```






- `simple interest principal=5000 rate=3% time=5 years` — finanzas



[ERROR] Wolfram Alpha no pudo interpretar la expresión.





----

Aquí van 10 en LaTeX:

1. $\int_0^1 x^2 dx$ — integral definida


**WolframAlpha:** $\int_0^1 x^2 dx$

**Riemann sums:**
$left sum | ((n - 1) (2 n - 1))/(6 n^2) = 1/3 - 1/(2 n) + O((1/n)^2)
(assuming subintervals of equal length)$

**Indefinite integral:**
$integral x^2 dx = x^3/3 + constant$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\int_0^1 x^2 dx
Si aplica, graficá usando Desmos o TikZJax.
```



2. $\frac{d}{dx} \sin(x^2)$ — derivada


**WolframAlpha:** $\frac{d}{dx} \sin(x^2)$

**Gráfica:**
![[Untitled-14-07-2026_15-27-46.png]]

**Alternate form:**
$e^(-i x^2) x + e^(i x^2) x$

**Real root:**
$x = 0$

**Roots:**
$x = sqrt(π/2) (-sqrt(2 n - 1)), n element Z | x = sqrt(π/2) sqrt(2 n - 1), n element Z$

**Properties as a real function:**
$R (all real numbers) | R (all real numbers) | surjective onto R | odd$

**Series expansion at x = 0:**
$2 x - x^5 + O(x^9)
(Taylor series)$

**Indefinite integral:**
$integral2 x cos(x^2) dx = sin(x^2) + constant$

**Definite integral:**
$integral_0^sqrt(π/2) 2 x cos(x^2) dx = 1$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\frac{d}{dx} \sin(x^2)
Si aplica, graficá usando Desmos o TikZJax.
```




3. $\lim_{x \to \infty} \frac{1}{x}$ — límite

[ERROR] Wolfram Alpha no pudo interpretar la expresión.


4. $\sum_{n=1}^{10} n^2$ — sumatoria

**WolframAlpha:** $\sum_{n=1}^{10} n^2$



```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\sum_{n=1}^{10} n^2
Si aplica, graficá usando Desmos o TikZJax.
```




5. $\sqrt{x^2 + y^2} = 5$ — ecuación con raíz

**WolframAlpha:** $\sqrt{x^2 + y^2} = 5$

**Gráfica:**
![[Untitled-14-07-2026_15-28-19.png]]

**Geometric figure:**
$circle$

**Alternate form:**
$x^2 + y^2 = 25$

**Solutions:**
$y = -sqrt(25 - x^2) | y = sqrt(25 - x^2)$

**Integer solutions:**
$x = ± 4, y = ± 3 | x = ± 3, y = ± 4 | x = ± 5, y = 0 | x = 0, y = ± 5$

**Number of integer solutions:**
$12$

**Implicit derivatives:**
$(dx(y))/(dy) = -y/x | (dy(x))/(dx) = -x/y$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\sqrt{x^2 + y^2} = 5
Si aplica, graficá usando Desmos o TikZJax.
```



6. $\int x e^x dx$ — integral por partes


**WolframAlpha:** $\int x e^x dx$

**Gráfica:**
![[ima-2.png]]

**Indefinite integral:**
$integral x e^x dx = e^x (x - 1) + constant$

**Alternate form of the integral:**
$e^x x - e^x$

**Expanded form of the integral:**
$e^x x - e^x + constant$

**Series expansion of the integral at x = 0:**
$-1 + x^2/2 + x^3/3 + x^4/8 + O(x^5)
(Taylor series)$

**Definite integral:**
$integral_(-∞)^0 e^x x dx = -1$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\int x e^x dx
Si aplica, graficá usando Desmos o TikZJax.
```



7. $\frac{x^2 - 4}{x - 2}$ — simplificación


**WolframAlpha:** $\frac{x^2 - 4}{x - 2}$

**Gráfica:**
![[Untitled-14-07-2026_15-28-36.png]]

**Result:**
$2 + x (for x!=2)$

**Expanded form:**
$x^2/(x - 2) - 4/(x - 2)$

**Alternate form:**
$x + 2 (for x!=2)$

**Quotient and remainder:**
$x^2 - 4 = (x + 2)(x - 2) + 0$

**Root:**
$x = -2$

**Properties as a real function:**
${x element R : x!=2} | {y element R : y!=4} | injective (one-to-one)$

**Derivative:**
$d/dx((x^2 - 4)/(x - 2)) = 1$

**Indefinite integral:**
$integral(x^2 - 4)/(x - 2) dx = 1/2 x (x + 4) + constant$

**Series representations:**
$(-4 + x^2)/(-2 + x) = sum_(n=-∞)^∞ ( piecewise | 1 | n = 1
2 | n = 0) x^n | (-4 + x^2)/(-2 + x) = sum_(n=-∞)^∞ ( piecewise | 1 | n = 1
4 | n = 0) (-2 + x)^n | (-4 + x^2)/(-2 + x) = sum_(n=-∞)^∞ ( piecewise | 1 | n = 1
3 | n = 0) (-1 + x)^n$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\frac{x^2 - 4}{x - 2}
Si aplica, graficá usando Desmos o TikZJax.
```



8. $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ — matriz


**WolframAlpha:** $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$

**Gráfica:**
![[Untitled-14-07-2026_15-28-57.png]]

**Dimensions:**
$2 (rows) × 2 (columns)$

**Transpose:**
$(1 | 3
2 | 4)$

**Cofactors:**
$(4 | -3
-2 | 1)$

**Trace:**
$5$

**Determinant:**
$-2$

**Inverse:**
$1/2(-4 | 2
3 | -1)$

**Characteristic polynomial:**
$λ^2 - 5 λ - 2$

**Eigenvalues:**
$λ_1 = 1/2 (5 + sqrt(33)) | λ_2 = 1/2 (5 - sqrt(33))$

**Eigenvectors:**
$v_1 = (1/6 (-3 + sqrt(33)), 1) | v_2 = (1/6 (-3 - sqrt(33)), 1)$

**Diagonalization:**
$(1 | 2
3 | 4) = P.D.P^(-1)
where
P = 1/6(-3 - sqrt(33) | sqrt(33) - 3
6 | 6)
D = 1/2(5 - sqrt(33) | 0
0 | 5 + sqrt(33))
P^(-1) = 1/22(-2 sqrt(33) | 11 - sqrt(33)
2 sqrt(33) | 11 + sqrt(33))$

**Condition number:**
$21$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
Si aplica, graficá usando Desmos o TikZJax.
```



9. $\sin^2(x) + \cos^2(x)$ — identidad trigonométrica


**WolframAlpha:** $\sin^2(x) + \cos^2(x)$

**Gráfica:**
![[Untitled-14-07-2026_15-29-25.png]]

**Expanded trigonometric form:**
$1$

**Roots:**
$(no roots exist)$

**Properties as a real function:**
$R (all real numbers) | {y element R : y = 1} | even$

**Indefinite integral:**
$integral(sin^2(x) + cos^2(x)) dx = x + constant$

**Global minimum:**
$min{sin^2(x) + cos^2(x)} = 1 at x = -49 π$

**Global maximum:**
$max{sin^2(x) + cos^2(x)} = 1 at x = -49 π$

**Limit:**
$lim_(x-> ± ∞)(cos^2(x) + sin^2(x)) = 1$

**Alternative representations:**
$sin^2(x) + cos^2(x) = cosh^2(i x) + cos^2(π/2 - x) | sin^2(x) + cos^2(x) = cosh^2(-i x) + cos^2(π/2 - x) | sin^2(x) + cos^2(x) = cosh^2(-i x) + (-cos(π/2 + x))^2$

**Series representations:**
$sin^2(x) + cos^2(x) = ( sum_(k=0)^∞ ((-1)^k x^(2 k))/((2 k)!))^2 + ( sum_(k=0)^∞ ((-1)^k (-π/2 + x)^(2 k))/((2 k)!))^2 | sin^2(x) + cos^2(x) = ( sum_(k=0)^∞ ((-1)^k x^(2 k))/((2 k)!))^2 + ( sum_(k=0)^∞ ((-1)^k x^(1 + 2 k))/((1 + 2 k)!))^2 | sin^2(x) + cos^2(x) = ( sum_(k=0)^∞ ((-1)^k x^(1 + 2 k))/((1 + 2 k)!))^2 + ( sum_(k=0)^∞ ((-1)^k (-π/2 + x)^(1 + 2 k))/((1 + 2 k)!))^2$

**Integral representations:**
$sin^2(x) + cos^2(x) = (-( integral_(-i ∞ + γ)^(i ∞ + γ) e^(s - x^2/(4 s))/sqrt(s) ds)^2 + 4 π x^2 ( integral_0^1 cos(t x) dt)^2)/(4 π) for γ>0 | sin^2(x) + cos^2(x) = (-x^2 ( integral_(-i ∞ + γ)^(i ∞ + γ) e^(s - x^2/(4 s))/s^(3/2) ds)^2 + 16 π ( integral_(π/2)^x sin(t) dt)^2)/(16 π) for γ>0 | sin^2(x) + cos^2(x) = -(x^2 ( integral_(-i ∞ + γ)^(i ∞ + γ) e^(s - x^2/(4 s))/s^(3/2) ds)^2 + 4 ( integral_(-i ∞ + γ)^(i ∞ + γ) e^(s - x^2/(4 s))/sqrt(s) ds)^2)/(16 π) for γ>0$

**Definite integral:**
$integral_0^(π/2) (cos^2(x) + sin^2(x)) dx = π/2≈1.5708$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\sin^2(x) + \cos^2(x)
Si aplica, graficá usando Desmos o TikZJax.
```



10. $\frac{d^2y}{dx^2} + y = 0$ — EDO segundo orden


**WolframAlpha:** $\frac{d^2y}{dx^2} + y = 0$

**Gráfica:**
![[ima-3.png]]

**ODE names:**
$y''(x) = -y(x) | y''(x) + y(x) = 0$

**ODE classification:**
$second-order linear ordinary differential equation$

**Alternate form:**
$y''(x) = -y(x)$

**Differential equation solution:**
$y(x) = c_2 sin(x) + c_1 cos(x)$

**Differential equation series solution about x = 0:**
$c_1 + c_2 x - (c_1 x^2)/2 - (c_2 x^3)/6 + (c_1 x^4)/24 + (c_2 x^5)/120 + O(x^6)
(converges everywhere)$

**Differential equation series solution about x = ∞:**
$c_1 e^(-i x) + c_2 e^(i x)
(converges everywhere)$

**Differential equation infinite series expansion:**
$sum_(n=0)^∞ ((((-i)^n + i^n) c_1 + i ((-i)^n - i^n) c_2) x^n)/(2 n!)
(converges everywhere)$

**Differential equation series solution about x = -∞:**
$c_1 e^(i x) + c_2 e^(-i x)
(converges everywhere)$

**Sample solution family:**
$  (sampling y(0) and y'(0))$

**Possible Lagrangian:**
$ℒ(y', y) = 1/2 ((y')^2 - y^2)$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\frac{d^2y}{dx^2} + y = 0
Si aplica, graficá usando Desmos o TikZJax.
```




\lim_{x \to \infty}


[ERROR] Wolfram Alpha no pudo interpretar la expresión.





limit 1/x as x->infinity


**WolframAlpha:** $limit 1/x as x->infinity$

**Limit:**
$lim_(x->∞) 1/x = 0$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
limit 1/x as x->infinity
Si aplica, graficá usando Desmos o TikZJax.
```




sum n^2 from n=1 to 10


**WolframAlpha:** sum n^2 from n=1 to 10



```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
sum n^2 from n=1 to 10
Si aplica, graficá usando Desmos o TikZJax.
```



simple interest 5000 at 3 percent for 5 years


**WolframAlpha:** $simple interest 5000 at 3 percent for 5 years$

**Result:**
$present value | Bs4347.83 (Bolivian bolivianos)$

**Equation:**
$FV = PV (1 + i n) | 
PV | present value
n | interest periods
FV | future value
i | interest rate$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
simple interest 5000 at 3 percent for 5 years
Si aplica, graficá usando Desmos o TikZJax.
```




{{1,2},{3,4}}

**WolframAlpha:** ${{1,2},{3,4}}$

**Gráfica:**
![[Untitled-14-07-2026_21-38-19.png]]

**Dimensions:**
$2 (rows) × 2 (columns)$

**Transpose:**
$(1 | 3
2 | 4)$

**Cofactors:**
$(4 | -3
-2 | 1)$

**Trace:**
$5$

**Determinant:**
$-2$

**Inverse:**
$1/2(-4 | 2
3 | -1)$

**Characteristic polynomial:**
$λ^2 - 5 λ - 2$

**Eigenvalues:**
$λ_1 = 1/2 (5 + sqrt(33)) | λ_2 = 1/2 (5 - sqrt(33))$

**Eigenvectors:**
$v_1 = (1/6 (-3 + sqrt(33)), 1) | v_2 = (1/6 (-3 - sqrt(33)), 1)$

**Diagonalization:**
$(1 | 2
3 | 4) = P.D.P^(-1)
where
P = 1/6(-3 - sqrt(33) | sqrt(33) - 3
6 | 6)
D = 1/2(5 - sqrt(33) | 0
0 | 5 + sqrt(33))
P^(-1) = 1/22(-2 sqrt(33) | 11 - sqrt(33)
2 sqrt(33) | 11 + sqrt(33))$

**Condition number:**
$21$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
{{1,2},{3,4}}
Si aplica, graficá usando Desmos o TikZJax.
```




sum of n^2 for n=1 to 10


**WolframAlpha:** $sum of n^2 for n=1 to 10$



```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
sum of n^2 for n=1 to 10
Si aplica, graficá usando Desmos o TikZJax.
```



$\sum_{n=1}^{10} n^2$


**WolframAlpha:** $\sum_{n=1}^{10} n^2$

**Sum:**
$sum_(n=1)^10 n^2 = 385$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\sum_{n=1}^{10} n^2
Si aplica, graficá usando Desmos o TikZJax.
```







---
$$\frac{x^2 - 4}{x - 2}
x^3 - 8
(x+2)^4
\sqrt[3]{27x^6}$$

**WolframAlpha:** $\frac{x^2 - 4}{x - 2}
x^3 - 8
(x+2)^4
\sqrt[3]{27x^6}$

**Gráfica:**
![[Untitled-14-07-2026_21-59-47.png]]

**Input:**
$(x^2 - 4)/(x - 2) x^3 - 8 (x + 2)^4 (27 x^6)^(1/3)$

**Result:**
$(x^3 (x^2 - 4))/(x - 2) - 24 (x^6)^(1/3) (x + 2)^4$

**Alternate form assuming x is real:**
$x^2 (x + 2) (x - 24 (x + 2)^3)$

**Alternate forms:**
$x^3 (x + 2) - 24 (x^6)^(1/3) (x + 2)^4 | (-x - 2) (24 (x^6)^(1/3) (x + 2)^3 - x^3) | -((x + 2) (288 (x^6)^(1/3) x + 192 (x^6)^(1/3) - x^3 + 24 (x^6)^(1/3) x^3 + 144 (x^6)^(1/3) x^2))$

**Expanded form:**
$-24 x^6 + x^5/(x - 2) - 192 x^5 - 576 x^4 - (4 x^3)/(x - 2) - 768 x^3 - 384 x^2$

**Alternate form assuming x>0:**
$x^2 (x (x + 2) - 24 (x + 2)^4) | (x^3 (x^2 - 4))/(x - 2) - 24 x^2 (x + 2)^4$

**Real roots:**
$x = -2 | x = 0 | x≈-2.4685$

**Complex roots:**
$x≈-1.7657 - 0.3507 i | x≈-1.7657 + 0.3507 i$

**Properties as a real function:**
${x element R : x!=2} | {y element R : y<=2.64203}$

**Series expansion at x = 0:**
$-(384 (x^6)^(1/3) x^2)/x^2 - (2 (384 (x^6)^(1/3) - x^2) x^3)/x^2 + ((x^2 - 576 (x^6)^(1/3)) x^4)/x^2 - (192 (x^6)^(1/3) x^5)/x^2 - (24 (x^6)^(1/3) x^6)/x^2 + O(x^7)
(generalized Puiseux series)$

**Series expansion at x = ∞:**
$-24 x^6 - 192 x^5 - 575 x^4 - 766 x^3 - 384 x^2 + O((1/x)^1)
(Taylor series)$

**Derivative:**
$d/dx(((x^2 - 4) x^3)/(x - 2) - 8 (x + 2)^4 (27 x^6)^(1/3)) = -(2 x^2 (72 x^7 + 480 x^6 - 2 (x^6)^(2/3) x - 3 (x^6)^(2/3) + 1152 x^5 + 1152 x^4 + 384 x^3))/(x^6)^(2/3)$

**Indefinite integral assuming all variables are real:**
$integral(((x^2 - 4) x^3)/(x - 2) - 8 (x + 2)^4 (27 x^6)^(1/3)) dx = -(24 x^7)/7 - 32 x^6 - 115 x^5 - (383 x^4)/2 - 128 x^3 + constant$

**Local minimum:**
$min{((x^2 - 4) x^3)/(x - 2) - 8 (x + 2)^4 (27 x^6)^(1/3)}≈-34.112 at x≈-0.67329$

**Local maxima:**
$max{((x^2 - 4) x^3)/(x - 2) - 8 (x + 2)^4 (27 x^6)^(1/3)} = 0 at x = 0 | max{((x^2 - 4) x^3)/(x - 2) - 8 (x + 2)^4 (27 x^6)^(1/3)}≈2.6420 at x≈-2.3170$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\frac{x^2 - 4}{x - 2}
x^3 - 8
(x+2)^4
\sqrt[3]{27x^6}
Si aplica, graficá usando Desmos o TikZJax.
```







---

$$x^2 + 5x + 6 = 0
x^3 - 6x^2 + 11x - 6 = 0
\frac{1}{x} + \frac{1}{x+1} = 1$$


**WolframAlpha:** $x^2 + 5x + 6 = 0
x^3 - 6x^2 + 11x - 6 = 0
\frac{1}{x} + \frac{1}{x+1} = 1$

**Input:**
$x^2 + 5 x + 6 = 0 x^3 - 6 x^2 + 11 x - 6 = 0 × 1/x + 1/(x + 1) = 1$

**Result:**
$x^2 + 5 x + 6 = -6 x^2 + 11 x - 6 = 1/(x + 1) = 1$

**Alternate forms:**
${4/5 (x + 5/2)^2 = 1, -144/47 (x - 11/12)^2 = 1, x = 0} | {x (x + 5) + 5 = 0, 6 x^2 + 7 = 11 x, 1/(x + 1) = 1} | {(x + 2) (x + 3) = 1, -6 x^2 + 11 x - 6 = 1, 1/(x + 1) = 1}$

**Solutions:**
$(no solutions exist)$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
x^2 + 5x + 6 = 0
x^3 - 6x^2 + 11x - 6 = 0
\frac{1}{x} + \frac{1}{x+1} = 1
Si aplica, graficá usando Desmos o TikZJax.
```





----

$$\lim_{x \to 0} \frac{\sin(x)}{x}
\lim_{x \to \infty} \frac{x^2 + 1}{x^2 - 1}
\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$$

[ERROR] Wolfram Alpha no pudo interpretar la expresión.

[ERROR] Wolfram Alpha no pudo interpretar la expresión.

[ERROR] Wolfram Alpha no pudo interpretar la expresión.

[ERROR] Wolfram Alpha no pudo interpretar la expresión.

[ERROR] Wolfram Alpha no pudo interpretar la expresión.


---

$$\frac{d}{dx} x^3 \cdot \ln(x)
\frac{d}{dx} \frac{\sin(x)}{x}
\frac{d^2}{dx^2} e^{x^2}$$

[ERROR] Wolfram Alpha no pudo interpretar la expresión.

[ERROR] Wolfram Alpha no pudo interpretar la expresión.


[ERROR] Wolfram Alpha no pudo interpretar la expresión.


**WolframAlpha:** $\frac{d}{dx} x^3 \cdot \ln(x)$

**Gráfica:**
![[Untitled-14-07-2026_22-04-59.png]]

**Derivative:**
$d/dx(x^3 log(x)) = x^2 (3 log(x) + 1)$

**Expanded form:**
$x^2 + 3 x^2 log(x)$

**Root:**
$x = 1/e^(1/3)$

**Properties as a real function:**
${x element R : x>0} (all positive real numbers) | {y element R : y>=-3/(2 e^(5/3))}$

**Indefinite integral:**
$integral x^2 (1 + 3 log(x)) dx = x^3 log(x) + constant
(assuming a complex-valued logarithm)$

**Global minimum:**
$min{x^2 (3 log(x) + 1)} = -3/(2 e^(5/3)) at x = 1/e^(5/6)$

**Definite integral:**
$integral_0^1 x^2 (1 + 3 log(x)) dx = 0$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\frac{d}{dx} x^3 \cdot \ln(x)
Si aplica, graficá usando Desmos o TikZJax.
```






[ERROR] Wolfram Alpha no pudo interpretar la expresión.

[ERROR] No se pudo conectar con Wolfram Alpha: The read operation timed out

[ERROR] Wolfram Alpha no pudo interpretar la expresión.


**WolframAlpha:** $\frac{d}{dx} \frac{\sin(x)}{x}$

**Gráfica:**
![[ima-5.png]]

**Derivative:**
$d/dx(sin(x)/x) = (x cos(x) - sin(x))/x^2$

**Expanded form:**
$cos(x)/x - sin(x)/x^2$

**Alternate form:**
$-(i e^(-i x))/(2 x^2) + (i e^(i x))/(2 x^2) + e^(-i x)/(2 x) + e^(i x)/(2 x)$

**Numerical roots:**
$x ≈ -14.0661939128315... | x ≈ ± 10.9041216594289... | x ≈ ± 7.72525183693771... | x ≈ ± 4.49340945790906...$

**Properties as a real function:**
${x element R : x!=0} | odd$

**Series expansion at x = 0:**
$-x/3 + x^3/30 - x^5/840 + O(x^6)
(Taylor series)$

**Indefinite integral:**
$integral(x cos(x) - sin(x))/x^2 dx = sin(x)/x + constant$

**Limit:**
$lim_(x-> ± ∞) (x cos(x) - sin(x))/x^2 = 0$

**Definite integrals:**
$integral_0^∞ (x cos(x) - sin(x))/x^2 dx≈-1.00000000000... | integral_(-π/2)^∞ (x cos(x) - sin(x))/x^2 dx≈-0.6366197723676... | integral_(π/2)^π (x cos(x) - sin(x))/x^2 dx≈-0.6366197723676...$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\frac{d}{dx} \frac{\sin(x)}{x}
Si aplica, graficá usando Desmos o TikZJax.
```





**WolframAlpha:** $\frac{d}{dx} x^3 \cdot \ln(x)$

**Gráfica:**
![[Untitled-14-07-2026_22-03-48.png]]

**Derivative:**
$d/dx(x^3 log(x)) = x^2 (3 log(x) + 1)$

**Expanded form:**
$x^2 + 3 x^2 log(x)$

**Root:**
$x = 1/e^(1/3)$

**Properties as a real function:**
${x element R : x>0} (all positive real numbers) | {y element R : y>=-3/(2 e^(5/3))}$

**Indefinite integral:**
$integral x^2 (1 + 3 log(x)) dx = x^3 log(x) + constant
(assuming a complex-valued logarithm)$

**Global minimum:**
$min{x^2 (3 log(x) + 1)} = -3/(2 e^(5/3)) at x = 1/e^(5/6)$

**Definite integral:**
$integral_0^1 x^2 (1 + 3 log(x)) dx = 0$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\frac{d}{dx} x^3 \cdot \ln(x)
Si aplica, graficá usando Desmos o TikZJax.
```






---

$$\int_0^{\pi} \sin(x) dx
\int x^2 e^x dx
\int \frac{1}{x^2 + 1} dx$$


**WolframAlpha:** $\int_0^{\pi} \sin(x) dx$

**Definite integral:**
$integral_0^π sin(x) dx = 2$

**Riemann sums:**
$left sum | (π cot(π/(2 n)))/n = 2 - π^2/(6 n^2) + O((1/n)^4)
(assuming subintervals of equal length)$

**Indefinite integral:**
$integral sin(x) dx = -cos(x) + constant$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\int_0^{\pi} \sin(x) dx
Si aplica, graficá usando Desmos o TikZJax.
```



---


$$\sum_{n=1}^{\infty} \frac{1}{n^2}
\sum_{n=0}^{5} 2^n
\prod_{n=1}^{4} n$$


**WolframAlpha:** $\sum_{n=1}^{\infty} \frac{1}{n^2}$

**Infinite sum:**
$sum_(n=1)^∞ 1/n^2 = π^2/6≈1.6449$

**Sum convergence:**
$sum_(n=1)^∞ 1/n^2 converges$

**Partial sum formula:**
$sum_(n=1)^k 1/n^2 = H_k^(2)$

**Series representations:**
$π^2/6 = sum_(k=1)^∞ 1/k^2 | π^2/6 = -2 sum_(k=1)^∞ (-1)^k/k^2 | π^2/6 = 4/3 sum_(k=0)^∞ 1/(1 + 2 k)^2 | π^2/6 = 8/3 ( sum_(k=0)^∞ (-1)^k/(1 + 2 k))^2$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\sum_{n=1}^{\infty} \frac{1}{n^2}
Si aplica, graficá usando Desmos o TikZJax.
```




---


$$
\sin(x)^2 + \cos(x)^2
\tan(\frac{\pi}{4})
\arcsin(\frac{\sqrt{2}}{2})
$$


**WolframAlpha:** $\sin(x)^2 + \cos(x)^2$

**Gráfica:**
![[Untitled-14-07-2026_22-02-35.png]]

**Input:**
$sin^2(x) + cos^2(x)$

**Expanded trigonometric form:**
$1$

**Roots:**
$(no roots exist)$

**Properties as a real function:**
$R (all real numbers) | {y element R : y = 1} | even$

**Indefinite integral:**
$integral(sin^2(x) + cos^2(x)) dx = x + constant$

**Global minimum:**
$min{sin^2(x) + cos^2(x)} = 1 at x = -49 π$

**Global maximum:**
$max{sin^2(x) + cos^2(x)} = 1 at x = -49 π$

**Limit:**
$lim_(x-> ± ∞)(cos^2(x) + sin^2(x)) = 1$

**Alternative representations:**
$sin^2(x) + cos^2(x) = cosh^2(i x) + cos^2(π/2 - x) | sin^2(x) + cos^2(x) = cosh^2(-i x) + cos^2(π/2 - x) | sin^2(x) + cos^2(x) = cosh^2(-i x) + (-cos(π/2 + x))^2$

**Series representations:**
$sin^2(x) + cos^2(x) = ( sum_(k=0)^∞ ((-1)^k x^(2 k))/((2 k)!))^2 + ( sum_(k=0)^∞ ((-1)^k (-π/2 + x)^(2 k))/((2 k)!))^2 | sin^2(x) + cos^2(x) = ( sum_(k=0)^∞ ((-1)^k x^(2 k))/((2 k)!))^2 + ( sum_(k=0)^∞ ((-1)^k x^(1 + 2 k))/((1 + 2 k)!))^2 | sin^2(x) + cos^2(x) = ( sum_(k=0)^∞ ((-1)^k x^(1 + 2 k))/((1 + 2 k)!))^2 + ( sum_(k=0)^∞ ((-1)^k (-π/2 + x)^(1 + 2 k))/((1 + 2 k)!))^2$

**Integral representations:**
$sin^2(x) + cos^2(x) = (-( integral_(-i ∞ + γ)^(i ∞ + γ) e^(s - x^2/(4 s))/sqrt(s) ds)^2 + 4 π x^2 ( integral_0^1 cos(t x) dt)^2)/(4 π) for γ>0 | sin^2(x) + cos^2(x) = (-x^2 ( integral_(-i ∞ + γ)^(i ∞ + γ) e^(s - x^2/(4 s))/s^(3/2) ds)^2 + 16 π ( integral_(π/2)^x sin(t) dt)^2)/(16 π) for γ>0 | sin^2(x) + cos^2(x) = -(x^2 ( integral_(-i ∞ + γ)^(i ∞ + γ) e^(s - x^2/(4 s))/s^(3/2) ds)^2 + 4 ( integral_(-i ∞ + γ)^(i ∞ + γ) e^(s - x^2/(4 s))/sqrt(s) ds)^2)/(16 π) for γ>0$

**Definite integral:**
$integral_0^(π/2) (cos^2(x) + sin^2(x)) dx = π/2≈1.5708$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
\sin(x)^2 + \cos(x)^2
Si aplica, graficá usando Desmos o TikZJax.
```





---


$$y'' + 4y = 0
y' = 2xy
y'' - y' - 6y = 0$$






**WolframAlpha:** $y'' + 4y = 0$

**Gráfica:**
![[ima-4.png]]

**Input:**
$y''(x) + 4 y(x) = 0$

**Autonomous equation:**
$y''(x) = -4 y(x)$

**ODE classification:**
$second-order linear ordinary differential equation$

**Alternate form:**
$y''(x) = -4 y(x)$

**Differential equation solution:**
$y(x) = c_2 sin(2 x) + c_1 cos(2 x)$

**Differential equation series solution about x = 0:**
$c_1 + c_2 x - 2 c_1 x^2 - (2 c_2 x^3)/3 + (2 c_1 x^4)/3 + (2 c_2 x^5)/15 + O(x^6)
(converges everywhere)$

**Differential equation series solution about x = ∞:**
$c_1 e^(-2 i x) + c_2 e^(2 i x)
(converges everywhere)$

**Differential equation infinite series expansion:**
$sum_(n=0)^∞ ((2^(-1 + n) (((-i)^n + i^n) c_1 + i ((-i)^n - i^n) c_2)) x^n)/(n!)
(converges everywhere)$

**Differential equation series solution about x = -∞:**
$c_1 e^(2 i x) + c_2 e^(-2 i x)
(converges everywhere)$

**Sample solution family:**
$  (sampling y(0) and y'(0))$

**Possible Lagrangian:**
$ℒ(y', y) = 1/2 ((y')^2 - 4 y^2)$

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
y'' + 4y = 0
Si aplica, graficá usando Desmos o TikZJax.
```






$url = "https://api.wolframalpha.com/v2/query?input=&appid=A3WL4X56LG&output=json"
$r = Invoke-WebRequest -Uri $url -UseBasicParsing
($r.Content | ConvertFrom-Json).queryresult.pods | Select-Object title, id




$url = "https://api.wolframalpha.com/v2/query?input=sum+of+n^2+for+n%3D1+to+10&appid=A3WL4X56LG&output=json"
$r = Invoke-WebRequest -Uri $url -UseBasicParsing
($r.Content | ConvertFrom-Json).queryresult.pods | Select-Object title, id











$url = "https://api.wolframalpha.com/v2/query?input=sum+of+n^2+for+n%3D1+to+10&appid=A3WL4X56LG&output=json"
$r = Invoke-WebRequest -Uri $url -UseBasicParsing
($r.Content | ConvertFrom-Json).queryresult.pods | Select-Object title, id, @{n='plaintext';e={$_.subpods[0].plaintext}}