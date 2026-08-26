


##### Ej. Una partícula se encuentra en la posición final $(x_f, y_f, z_f)$ luego de una rotación de $\alpha°$ alrededor del eje $x$. Hallar la posición inicial $(x, y, z)$.

**Resolución**
Determinación de la posición inicial mediante el producto de la matriz de rotación transpuesta por el vector de posición final.


$$
\begin{array}{rcl}
\vec{r}_0 & = & R_x^T(\alpha) \cdot \vec{r}_f \[4pt]
\begin{bmatrix} x \\ y \\ z \end{bmatrix} & = & \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\alpha & -\sin\alpha \\ 0 & \sin\alpha & \cos\alpha \end{bmatrix}^T \begin{bmatrix} x_f \\ y_f \\ z_f \end{bmatrix} \[16pt]
\begin{bmatrix} x \\ y \\ z \end{bmatrix} & = & \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\alpha & \sin\alpha \\ 0 & -\sin\alpha & \cos\alpha \end{bmatrix} \begin{bmatrix} x_f \\ y_f \\ z_f \end{bmatrix} \[16pt]
x & = & x_f \[4pt]
y & = & y_f \cos\alpha + z_f \sin\alpha \[4pt]
z & = & -y_f \sin\alpha + z_f \cos\alpha \[10pt]
\therefore\quad (x, y, z) & = & \color{orange}{(x_f,\ y_f \cos\alpha + z_f \sin\alpha,\ -y_f \sin\alpha + z_f \cos\alpha)}
\end{array}
$$

