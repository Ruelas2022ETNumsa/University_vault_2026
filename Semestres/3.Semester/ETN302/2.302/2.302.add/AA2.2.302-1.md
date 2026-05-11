---
Created: [09-June-22/19:44:48]
Title: [Tema_2-Ejercicio_1]
Alias: []
Tags: [Whorled, Ejercicios]
---

---

##### Sea la señal.
![[AAD2.2.302-1.svg]]

--- 
# Solucion
---

>- Para la recta $L_1$.
>$$L_{1}:\quad\dfrac{x-4}{2-4}=\dfrac{y-0}{3-0}$$
>
>$$\frac{\mbox{-}\,3}{2}·(x-4)=y$$
>
>$$f_{(t)}=\frac{\mbox{-}\,3}{2}·(t-4)$$

>- Para la rescta $L_2$.
>$$L_{2}:\quad\dfrac{x-12}{12-8}=\dfrac{y-0}{0-(\mbox{-}\,6)}$$
>
>$$\frac{3}{2}·(x-12)=y$$
>
>$$g_{(t)}=\frac{3}{2}·(t-12)$$

>- Para el periodo.
>$$T=12$$

>- Para el valor medio.

$$V_m=\dfrac{1}{12}\left[\,
\int^{8}_{2}\dfrac{\mbox{-}\,3}{2}·(t-4)dt+
\int^{14}_{8}\dfrac{3}{2}·(t-12)dt\right]$$

$$V_m=\dfrac{1}{12}\left[\,
\dfrac{\mbox{-}\,3}{2}·\left(\dfrac{1}{2}·t^2-4·t\right)\Bigg |^{8}_{2}+
\dfrac{3}{2}·\left(\dfrac{1}{2}·t^2-12·t\right)\Bigg |^{14}_{8}\,\right]$$

$$V_m=\dfrac{1}{8}\left[\,
\dfrac{1}{2}·(8^2-2^2)-4·(8-2)+
\dfrac{1}{2}·(14^2-8^2)-12·(14-8)\,\right]$$

$$V_m=\dfrac{1}{8}\left[\,
{\color{orange}\cancelto{{\color{orange}6}}{{\color{gray}(8-2)}}}\left[\,{\color{orange}\cancelto{{\color{orange}5}}{{\color{gray}\dfrac{1}{2}·(8+2)}}}-4\,\right]+
{\color{orange}\cancelto{{\color{orange}6}}{{\color{gray}(14-8)}}}\left[\,{\color{orange}\cancelto{{\color{orange}11}}{{\color{gray}\dfrac{1}{2}·(14+8)}}}-12\,\right]
\,\right]$$

$$V_m=\dfrac{1}{8}·[\,6·1+6·(\,\mbox{-}\,1)\,]\Rightarrow\quad V_m=0$$

>- Por otro método.
>$${\color{orange}V_m=\dfrac{\sum \mbox{Área}_{(+)}+\sum \mbox{Área}_{(-)}}{\mbox{Periodo}}}$$
>
>$$\hookrightarrow V_m=\dfrac{\tfrac{4·3}{2}+\tfrac{8·(\,\mbox{-}\,6)}{2}}{12}=\dfrac{6-24}{12}=\dfrac{-18}{12}$$
>
>$$V_m=-1.5$$

>- Para el valor eficaz.
>$$V_{\varepsilon}=\sqrt{\dfrac{1}{12}·
\left[\,\int^{8}_{2}\left(
\dfrac{\mbox{-}\,3}{2}·(t-4)
\right)^2dt+
\int^{14}_{8}\left(
\dfrac{3}{2}·(t-12)
\right)^2dt\,\right]}$$
>
>$$V_{\varepsilon}=\sqrt{\dfrac{3}{16}·
\left[\,\int^{8}_{2}
(t^2-8t+4^2)dt+
\int^{14}_{8}
(t^2-24t+12^2)^2dt\,\right]}$$
>
>$$V_{\varepsilon}=\sqrt{\dfrac{3}{16}·\left[\,
\left(\dfrac{1}{3}·t^3-\dfrac{8}{2}·t^2+4^2·t\right)\Bigg |^{8}_{2}+
\left(\dfrac{1}{3}·t^3-\dfrac{24}{2}·t^2+12^2·t\right)\Bigg |^{14}_{8}\,\right]}$$
>
>$$V_{\varepsilon}=\sqrt{\dfrac{3}{16}\left[\,
\left(
\dfrac{1}{3}(8^3\,\mbox{-}\,8)\,\mbox{-}\,
4(8^2\,\mbox{-}\,4)+4^2(8\,\mbox{-}\,2)
\right)+\left(
\dfrac{1}{3}(14^3\,\mbox{-}\,8^3)\,\mbox{-}\,
12(14^2\,\mbox{-}\,8^2)+12^2(14\,\mbox{-}\,8)
\right)\,\right]}$$
>
>$$V_{\varepsilon}=\sqrt{\dfrac{3}{16}\left[\,
\dfrac{{\color{orange}\bcancel{{\color{gray}8^3}}}\,\mbox{-}\,8+14^3\,\mbox{-}\,{\color{orange}\bcancel{{\color{gray}8^3}}}}{3}+
4({\color{orange}\cancelto{{\color{orange}6}}{{\color{gray}8\,\mbox{-}\,2}}})({\color{orange}\cancelto{{\color{orange}-6}}{{\color{gray}4\,\mbox{-}\,8\,\mbox{-}\,2}}})+
12({\color{orange}\cancelto{{\color{orange}6}}{{\color{gray}14\,\mbox{-}\,8}}})({\color{orange}\cancelto{{\color{orange}-10}}{{\color{gray}12\,\mbox{-}\,14\,\mbox{-}\,8}}})
\,\right]}$$
>
>$$V_{\varepsilon}=\sqrt{\dfrac{3}{16}\left[\,
\dfrac{\,\mbox{-}\,8+14^3}{3}-
4(6^2)+2(6)(6)(-10)
\,\right]}=
\sqrt{\dfrac{3}{16}\left[\,
\dfrac{\,\mbox{-}\,8+14^3}{3}-
6^2·(4+20)
\,\right]}$$
>
>$$V_{\varepsilon}=
\sqrt{\dfrac{3}{16}\left[\,
\dfrac{\,\mbox{-}\,8+14^3}{3}-
6^2·(4+20)
\,\right]}=
\sqrt{\dfrac{{\color{orange}\bcancel{{\color{gray}3}}}}{16}\left[\,
\dfrac{144}{{\color{orange}\bcancel{{\color{gray}3}}}}
\,\right]}=\dfrac{12}{4}$$
>
>$$V_{\varepsilon}=3$$

>- Finalmente para el factor de forma.
>$$f.f.=\dfrac{3}{\,\mbox{-}1.5}\Rightarrow\quad f.f.=\,\mbox{-}2$$