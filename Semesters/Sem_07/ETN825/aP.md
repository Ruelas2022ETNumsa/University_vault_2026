## Nombre: Ruelas Machicado Mijahel Alexander

---

# a) Modificar la interface para que reciba 1K de datos cada vez

---

## Módulo AHPL

$$
\begin{array}{l}
\text{MODULE: INTERFACE 1K} \\
\text{MEMORY: } DR[18];\ BUFFER[1024,\,18];\ cnt[10];\ busy \\
\text{INPUTS: } csrdy \\
\text{COMBUSES: } IOBUS[18];\ CSBUS[12];\ ready;\ datavalid;\ accept
\end{array}
$$

$$
\begin{array}{rl}
1. & \rightarrow \overline{\left(csrdy \land \overline{CSBUS_{0}} \land CSBUS_{1} \land \overline{CSBUS_{2}}\right)} \,/\, (1) \\[6pt]
2. & accept = 1; \\
   & \rightarrow \left(\overline{CSBUS_{3}},\ \overline{CSBUS_{3}},\ CSBUS_{3}\right) \,/\, (1,\ 1A,\ 3) \\[6pt]
3. & \rightarrow \left(\overline{ready}\right) \,/\, (3) \\[6pt]
4. & CSBUS_{0} = busy;\ datavalid = 1; \\
   & \rightarrow \left(\overline{accept},\ accept\right) \,/\, (4,\ 1) \\[6pt]
1A. & cnt \leftarrow 0,0,0,0,0,0,0,0,0,0;\ busy \leftarrow 1 \\[6pt]
2A. & ready = 1; \\
    & \rightarrow \left(\overline{datavalid}\right) \,/\, (2A) \\[6pt]
3A. & DR \leftarrow IOBUS;\ BUFFER * DCD(cnt) \leftarrow IOBUS;\ accept = 1 \\[6pt]
4A. & \rightarrow \left(datavalid\right) \,/\, (4A) \\[6pt]
5A. & cnt \leftarrow INC(cnt); \\
    & \rightarrow \left(\bigwedge / cnt,\ \overline{\bigwedge / cnt}\right) \,/\, (6A,\ 2A) \\[6pt]
6A. & busy \leftarrow 0 \\[6pt]
7A. & \text{DEAD END}
\end{array}
$$

$$
\text{END SEQUENCE} \qquad \text{END}
$$
