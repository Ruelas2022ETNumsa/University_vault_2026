He generado la transcripción y corrección completa del ejercicio de **E1P2.pdf** (página 2) en el documento **`etn607-e1p2-corregido.md`**.

```markdown
%%< correcciones hechas: Se corrigió el signo de la energía potencial elástica del resorte K' (debe ser siempre positivo +1/2 K' Δl²), el signo de la contribución gravitacional de m2 al derivar V respecto a X1 (al ser y2 = C - X1, la gravedad de m2 se opone a X1 aportando -m2 g), la expresión de deformación del resorte K' (y3 - y2 = y3 + X1 - C) y el planteamiento riguroso de las ecuaciones diferenciales de Lagrange para N = 2 grados de libertad. %%

## Resumen solo T y V

##### Ej. Planteamiento de energías T, V y ecuaciones del movimiento de Lagrange para sistema de tres masas con dos resortes.

![[pegar_imagen]]
*Figura 1.1 · Sistema mecánico formado por bloque $m_1$ con resorte $K$ sobre superficie horizontal y masas colgantes $m_2, m_3$ unidas por resorte $K'$.*

**Grados de libertad y ligadura del cable:**

$$N = (X_1, y_2, y_3) \quad \Rightarrow \quad \text{Grados de libertad } N = 2$$

$$\text{Cable inextensible: } \dot{X}_1 = \dot{y}_2 \implies X_1 + y_2 = C \implies y_2 = C - X_1$$

**Energía Cinética $T$:**

$$T = \frac{1}{2} m_1 \dot{X}_1^2 + \frac{1}{2} m_2 \dot{y}_2^2 + \frac{1}{2} m_3 \dot{y}_3^2$$

$$T = \frac{1}{2} (m_1 + m_2) \dot{X}_1^2 + \frac{1}{2} m_3 \dot{y}_3^2$$

**Energía Potencial $V$:**

$$V = \frac{K}{2}\left(X_1 - \frac{b_1}{2} - l_0\right)^2 - m_2 g y_2 - m_3 g y_3 + \frac{K'}{2}\left(y_3 - y_2 - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)^2$$

Sustituyendo la ecuación de ligadura $y_2 = C - X_1$:

$$V = \frac{K}{2}\left(X_1 - \frac{b_1}{2} - l_0\right)^2 - m_2 g (C - X_1) - m_3 g y_3 + \frac{K'}{2}\left(y_3 + X_1 - C - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)^2$$

**Ecuaciones del Movimiento de Lagrange:**

Aplicando $\dfrac{d}{dt}\left(\dfrac{\partial T}{\partial \dot{q}_i}\right) - \dfrac{\partial T}{\partial q_i} = -\dfrac{\partial V}{\partial q_i}$:

- **Para la coordenada $X_1$:**
  $$(m_1 + m_2)\ddot{X}_1 = -K\left(X_1 - \frac{b_1}{2} - l_0\right) - m_2 g - K'\left(y_3 + X_1 - C - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)$$

- **Para la coordenada $y_3$:**
  $$m_3 \ddot{y}_3 = m_3 g - K'\left(y_3 + X_1 - C - \frac{b_2}{2} - \frac{b_3}{2} - l_0'\right)$$

>[!note]
> **Notas de corrección sobre el apunte original:**
> 1. **Signo de la energía elástica**: En el apunte original se escribió un signo negativo para la energía potencial del resorte $K'$. La energía potencial elástica debe ser positiva $+\frac{1}{2}K'(\Delta l)^2$.
> 2. **Efecto de ligadura en la gravedad de $m_2$**: Puesto que $y_2 = C - X_1$, el término $-m_2 g y_2 = -m_2 g C + m_2 g X_1$. Al tomar $-\frac{\partial V}{\partial X_1}$, la contribución es $-m_2 g$, reflejando que el peso de $m_2$ tira hacia abajo y se opone al avance de $m_1$ hacia la derecha.
> 3. **Deformación del resorte $K'$**: La separación entre $m_2$ y $m_3$ es $y_3 - y_2 = y_3 + X_1 - C$.

IMA | fuente: E1P2.pdf | página: 2 | id: Figura 1.1 | posición: arriba
```

---

💡 **Siguiente paso sugerido:** ¿Quieres que expresemos las ecuaciones en forma matricial \\(M\ddot{\mathbf{q}} + K\mathbf{q} = \mathbf{F}_0\\) o que determinemos las posiciones de equilibrio estático del sistema?