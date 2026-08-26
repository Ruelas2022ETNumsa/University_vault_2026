



##### Ej. Una partícula se encuentra en la posición final $(x_f, y_f, z_f)$ luego de una rotación de $\gamma°$ alrededor del eje $z$. Hallar la posición inicial $(x, y, z)$.

**Resolución**
Determinación de la posición inicial mediante el producto de la matriz de rotación transpuesta por el vector de posición final.


$$
\begin{array}{rcl}
\vec{r}_0 & = & R_z^T(\gamma) \cdot \vec{r}_f \[4pt]
\begin{bmatrix} x \\ y \\ z \end{bmatrix} & = & \begin{bmatrix} \cos\gamma & -\sin\gamma & 0 \\ \sin\gamma & \cos\gamma & 0 \\ 0 & 0 & 1 \end{bmatrix}^T \begin{bmatrix} x_f \\ y_f \\ z_f \end{bmatrix} \[16pt]
\begin{bmatrix} x \\ y \\ z \end{bmatrix} & = & \begin{bmatrix} \cos\gamma & \sin\gamma & 0 \\ -\sin\gamma & \cos\gamma & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x_f \\ y_f \\ z_f \end{bmatrix} \[16pt]
x & = & x_f \cos\gamma + y_f \sin\gamma \[4pt]
y & = & -x_f \sin\gamma + y_f \cos\gamma \[4pt]
z & = & z_f \[10pt]
\therefore\quad (x, y, z) & = & \color{orange}{(x_f \cos\gamma + y_f \sin\gamma,\ -x_f \sin\gamma + y_f \cos\gamma,\ z_f)}
\end{array}
$$

