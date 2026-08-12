Classify the following continuous-time signals as periodic or aperiodic. If periodic, determine the period. 

i) $x(t) = \cos\left(\frac{2\pi}{3}t\right) + 2\sin\left(\frac{\pi}{2}t\right)$
ii) $x(t) = \cos(2\pi t) + \sin\left(\sqrt{2}\pi t\right)$
iii) $x(t) = \frac{1}{2} - \frac{1}{2}\cos(2t)$
iv) $x(t) = 1 + \sin(4t) + \cos\left(6t + \frac{\pi}{3}\right)$
v) $x(t) = e^{j(4t+\tfrac{\pi}{5})}$
vi) $x(t) = \cos\left(2t + \frac{\pi}{4}\right)$
vii) $x(t) = \cos(2\pi t)u(t)$
viii) $x(t) = \cos^2(t)$

---

### i) $x(t) = \cos\left(\frac{2\pi}{3}t\right) + 2\sin\left(\frac{\pi}{2}t\right)$

$$T_1 = \frac{2\pi}{2\pi/3} = 3 \text{ s}, \quad T_2 = \frac{2\pi}{\pi/2} = 4 \text{ s}$$

$$\frac{T_1}{T_2} = \frac{3}{4} \in \mathbb{Q} \implies \text{Periódica}$$

$$T_0 = \text{MCM}(3,4) = 12 \text{ s}$$

---

### ii) $x(t) = \cos(2\pi t) + \sin\left(\sqrt{2}\pi t\right)$

$$T_1 = \frac{2\pi}{2\pi} = 1 \text{ s}, \quad T_2 = \frac{2\pi}{\sqrt{2}\pi} = \sqrt{2} \text{ s}$$

$$\frac{T_1}{T_2} = \frac{1}{\sqrt{2}} \notin \mathbb{Q} \implies \textbf{Aperiódica}$$

---

### iii) $x(t) = \frac{1}{2} - \frac{1}{2}\cos(2t)$

La constante no afecta la periodicidad. Para $-\frac{1}{2}\cos(2t)$ con $\omega = 2$ rad/s:

$$T_0 = \frac{2\pi}{2} = \pi \text{ s} \implies \text{Periódica}$$

---

### iv) $x(t) = 1 + \sin(4t) + \cos\left(6t + \frac{\pi}{3}\right)$

La constante no afecta la periodicidad.

$$T_1 = \frac{2\pi}{4} = \frac{\pi}{2} \text{ s}, \quad T_2 = \frac{2\pi}{6} = \frac{\pi}{3} \text{ s}$$

$$\frac{T_1}{T_2} = \frac{3}{2} \in \mathbb{Q} \implies \text{Periódica}$$

$$T_0 = 2T_1 = 3T_2 = \pi \text{ s}$$

---

### v) $x(t) = e^{j\left(4t + \frac{\pi}{5}\right)}$

Exponencial compleja con $\omega_0 = 4$ rad/s, siempre periódica:

$$T_0 = \frac{2\pi}{4} = \frac{\pi}{2} \text{ s} \implies \text{Periódica}$$

---

### vi) $x(t) = \cos\left(2t + \frac{\pi}{4}\right)$

$\omega_0 = 2$ rad/s:

$$T_0 = \frac{2\pi}{2} = \pi \text{ s} \implies \text{Periódica}$$

---

### vii) $x(t) = \cos(2\pi t)u(t)$

$$x(t) = \begin{cases} \cos(2\pi t) & t \ge 0 \\ 0 & t < 0 \end{cases}$$

La señal vale $0$ para $t < 0$, por lo que no existe $T > 0$ tal que $x(t+T) = x(t)$ para todo $t$.

$$\implies \textbf{Aperiódica}$$

---

### viii) $x(t) = \cos^2(t)$

Por identidad trigonométrica:

$$\cos^2(t) = \frac{1}{2} + \frac{1}{2}\cos(2t)$$

$\omega_0 = 2$ rad/s:

$$T_0 = \frac{2\pi}{2} = \pi \text{ s} \implies \text{Periódica}$$
