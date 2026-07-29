---
title: _tmp_sync — Prueba Script 2 LaTeX → MathJax
status: temp
---

# Prueba Script 2 — latex_to_mathjax

Texto normal con $x^2$ fuera de un bloque — NO debe convertirse.

%%>
Esto es un bloque Marginalia.
Fórmula inline: \(f(x) = x^2 + 1\)
Fórmula display: \[\int_0^1 f(x)\,dx = \frac{1}{3}\]
Wikilink que no debe tocarse: [[ETN806-T01-joint-pdf-definition]]
Código inline que no debe tocarse: `$x$`
Otra fórmula: \(\mu = E[X]\) y \(\sigma^2 = \text{Var}(X)\)
%%

Texto entre bloques con $y = mx + b$ — NO debe convertirse.

%%>
Segundo bloque Marginalia.
Sistema de ecuaciones: \[\begin{cases} x + y = 1 \\ x - y = 0 \end{cases}\]
Inline: \(P(A \cap B) = P(A) \cdot P(B)\)
%%

Texto final con $z$ suelto — NO debe convertirse.
