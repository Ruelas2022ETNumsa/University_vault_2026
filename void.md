# A8 — Flashcard Generator

---

## Caso 1 — Básico (una marginalia `;;` por línea)

La transformada de Laplace convierte ecuaciones diferenciales al dominio $s$.%%> ! ¿A qué dominio convierte la Laplace?;; %%

El teorema de Bayes relaciona probabilidades condicionales.%%> ¿Qué relaciona Bayes?;; %%

---

## Caso 2 — Bug: dos marginalia en la misma línea

La segunda ley de Newton es $F = ma$.%%> ! Segunda ley — entra en parcial %% %%< ¿Cuál es la segunda ley de Newton?;; %%

> ⚠️ En este caso la sección Flashcards copia los `%%` intermedios en la tarjeta generada.

---

## Caso 3 — Bloque `::cue` / `::note` (Cornell Notes) con marginalia

> Este bloque usa la sintaxis nativa de Cornell Notes (5 backticks).
> La marginalia se coloca dentro del `::cue` y del `::note`.

`````cornell
::cue
¿Qué es la transformada de Laplace?%%> ! Definición central;; %%
::note
La transformada de Laplace se define como $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$.%%> F- Fórmula de examen %% La condición de convergencia requiere $\text{Re}(s) > \sigma_0$.%%< V- Verificado Kreyszig p.218 %%
`````

---

## Caso 4 — Múltiples marginalia con A3 (`[!cornell]` callout)

> A3 gestiona el espaciado automáticamente entre múltiples notas dentro del callout.

> [!cornell]
> El circuito RC en serie tiene constante de tiempo $\tau = RC$.%%> F- τ = RC — entra en parcial;; %%
> La respuesta natural decae exponencialmente: $v(t) = V_0 e^{-t/\tau}$.%%> ! Forma de la respuesta natural;; %%
> Para $t = \tau$ el voltaje cae al 36.8% de su valor inicial.%%< ? ¿Por qué 36.8%? — ver $e^{-1}$ %%

---

## Caso 5 — Imagen en margen con A3

> A3 con `img:[[...]]` para imagen al margen izquierdo.

> [!cornell]
> El diagrama muestra la respuesta al escalón de un sistema de segundo orden.%%> img:[[_assets/ima-1.png]] %%
> El sobrepico depende del coeficiente de amortiguamiento $\zeta$.%%< ! Sobrepico — parámetro clave;; %%


### Flashcards
! ¿A qué dominio convierte la Laplace? :: La transformada de Laplace convierte ecuaciones diferenciales al dominio $s$.
¿Qué relaciona Bayes? :: El teorema de Bayes relaciona probabilidades condicionales.
! Segunda ley — entra en parcial %% %%< ¿Cuál es la segunda ley de Newton? :: La segunda ley de Newton es $F = ma$.
! Definición central :: ¿Qué es la transformada de Laplace?
F- τ = RC — entra en parcial :: > El circuito RC en serie tiene constante de tiempo $\tau = RC$.
! Forma de la respuesta natural :: > La respuesta natural decae exponencialmente: $v(t) = V_0 e^{-t/\tau}$.
! Sobrepico — parámetro clave :: > El sobrepico depende del coeficiente de amortiguamiento $\zeta$.