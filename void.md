
---

## Caso 3 — Bloque `::cue` / `::note` (Cornell Notes) con marginalia

> Este bloque usa la sintaxis nativa de Cornell Notes (5 backticks).
> La marginalia se coloca dentro del `::cue` y del `::note`.

`````cornell
::cue
¿Qué es la transformada de Laplace A0?ajajajaja%%> ! Definición centralA0ajajajaja;; %%
::note
La transformada de Laplace se define como $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$.%%> F- Fórmula de examen A0peepepepep;;%% La condición de convergencia requiere $\text{Re}000000(s) > \sigma_0$.%%< V- Verificado Kreyszig p.218 A0piiipipipip ;;%%
`````

# caos55

`````cornell
::cue
```marginalia
¿Qué es la transformada de Laplace?A4 %%> F- Fórmula de examen A4wrwrwer;;%%
```
::note
```marginalia
La transformada de Laplace se define como $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$.%%< Definición centralxxxA4ertretert;; %%
.
.
La condición de convergencia requiere $\text{Re}(s) > \sigma_0$. %%< Verificado Kreyszig p.218A4 rrtyrtyrty ;;%%
.
.
.
```
`````



---

## Caso 4 — Múltiples marginalia con A3 (`[!cornell]` callout)

> A3 gestiona el espaciado automáticamente entre múltiples notas dentro del callout.

> [!cornell]
> El circuito RC en serie tiene constante de tiempo $\tau = RC$.%%> F- τ = RC — entra en parcial;; %%
> La respuesta natural decae exponencialmente: $v(t) = V_0 e^{-t/\tau}$.%%> ! Forma de la respuesta natural;; %%
> Para $t = \tau$ el voltaje cae al 36.8% de su valor inicial.%%< ? ¿Por qué 36.8%? — ver $e^{-1}$ %%




### Flashcards
! Definición centralA0ajajajaja :: ¿Qué es la transformada de Laplace A0?ajajajaja
F- Fórmula de examen A0peepepepep :: La transformada de Laplace se define como $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$.
F- Fórmula de examen A4wrwrwer :: ¿Qué es la transformada de Laplace?A4
Definición centralxxxA4ertretert :: La transformada de Laplace se define como $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$.
Verificado Kreyszig p.218A4 rrtyrtyrty :: La condición de convergencia requiere $\text{Re}(s) > \sigma_0$.
F- τ = RC — entra en parcial :: > El circuito RC en serie tiene constante de tiempo $\tau = RC$.
! Forma de la respuesta natural :: > La respuesta natural decae exponencialmente: $v(t) = V_0 e^{-t/\tau}$.