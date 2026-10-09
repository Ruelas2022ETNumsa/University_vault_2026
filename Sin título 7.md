
$$
\begin{aligned}
&\textbf{MODULE: PRINTER INTERFACE 1K}\\
&\textbf{MEMORY: } DR(18);\ CR(8);\ BUFFER(1024,18);\ cnt(10);\ limit(10);\ empty(10);\ busy;\ first;\ has\_data\\
&\textbf{OUTPUTS: } CHAR(8);\ print;\ feed\\
&\textbf{INPUTS: } wait;\ csrdy\\
&\textbf{COMBUS: } IOBUS(18);\ CSBUS(12);\ ready;\ datavalid;\ accept\\[1.2em]
1.\ \ &\rightarrow \overline{(csrdy \land \overline{CSBUS_{0}} \land CSBUS_{1} \land \overline{CSBUS_{2}})}\ /\ (1)\\[0.6em]
2.\ \ &accept = 1;\\
&\rightarrow (\overline{CSBUS_{3}} \land busy,\ \overline{CSBUS_{3}} \land \overline{busy},\ CSBUS_{3})\ /\ (1,\ 1A,\ 3)\\[0.6em]
3.\ \ &\rightarrow (\overline{ready})\ /\ (3)\\[0.6em]
4.\ \ &CSBUS_{0} = busy;\ datavalid = 1;\\
&\rightarrow (\overline{accept},\ accept)\ /\ (4,\ 1)\\[0.6em]
1A.\ \ &cnt \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash;\ empty \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash;\ limit \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash;\ has\_data \leftarrow 0;\ busy \leftarrow 1\\[0.6em]
2A.\ \ &ready = 1;\ accept = 0\\
&\rightarrow (\overline{datavalid})\ /\ (2A)\\[0.6em]
3A.\ \ &DR \leftarrow IOBUS;\ BUFFER * DCD(cnt) \leftarrow IOBUS;\ accept = 1\\[0.6em]
4A.\ \ &\rightarrow (datavalid)\ /\ (4A)\\[0.6em]
5A.\ \ &has\_data * (\bigvee / DR_{10:17} \lor \bigvee / DR_{1:8}) \leftarrow 1\\
&limit * (\bigvee / DR_{10:17} \lor \bigvee / DR_{1:8}) \leftarrow cnt\\
&empty * (\bigvee / DR_{10:17} \lor \bigvee / DR_{1:8}) \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash\\
&empty * \overline{(\bigvee / DR_{10:17} \lor \bigvee / DR_{1:8})} \leftarrow INC(empty)\\[0.6em]
6A.\ \ &cnt \leftarrow INC(cnt)\\
&\rightarrow (empty_{0} \lor \bigwedge / cnt,\ \overline{empty_{0} \lor \bigwedge / cnt})\ /\ (1B,\ 2A)\\[0.6em]
1B.\ \ &cnt \leftarrow \backslash 0,0,0,0,0,0,0,0,0,0 \backslash\\
&\rightarrow (\overline{has\_data},\ has\_data)\ /\ (9B,\ 2B)\\[0.6em]
2B.\ \ &DR \leftarrow BUSFN(BUFFER;\ DCD(cnt));\ first \leftarrow 1\\[0.6em]
3B.\ \ &CR \leftarrow (DR_{10:17}\ !\ DR_{1:8}) * (first,\ \overline{first})\\[0.6em]
4B.\ \ &feed = RETURN(CR);\ print = \overline{RETURN(CR)}\\[0.6em]
5B.\ \ &Null\\[0.6em]
6B.\ \ &\rightarrow (wait)\ /\ (6B)\\[0.6em]
7B.\ \ &first \leftarrow 0\\
&\rightarrow (first,\ \overline{first})\ /\ (3B,\ 8B)\\[0.6em]
8B.\ \ &cnt \leftarrow INC(cnt)\\
&\rightarrow (cnt\ EQ\ limit,\ \overline{cnt\ EQ\ limit})\ /\ (9B,\ 2B)\\[0.6em]
9B.\ \ &busy \leftarrow 0;\ accept = 0\\[0.6em]
10B.\ \ &\rightarrow (1)\ /\ (1)\\[1.2em]
&\textbf{END SEQUENCE}\\
&CHAR = CR\\
&\textbf{END}
\end{aligned}
$$
