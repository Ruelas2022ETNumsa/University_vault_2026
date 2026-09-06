---
galaxy_body: dropship
carrier: "[[tsk_carrier.md]]"
scope: prueba-5
status: activo
date: 2026-09-05
---

## Propósito

Validar cálculo numérico intensivo en Python — el caso donde Python supera a PPL. Implementar Newton-Raphson para encontrar raíces de funciones y bisección como alternativa robusta. Comparar visualmente la velocidad vs un equivalente PPL si ya existe.

---

## Concepto

PPL es lento en loops con muchas iteraciones porque cada línea es interpretada por el CAS. MicroPython en la G2 compila a bytecode antes de ejecutar — en benchmarks de hpmuseum, Python es 3–5× más rápido que PPL en loops intensivos. Newton-Raphson con tolerancia 1e-10 y hasta 100 iteraciones es un buen stress test real con utilidad matemática directa.

---

## Programa propuesto — PY_NUMERICO

```python
#PYTHON numerico
from math import sqrt, sin, cos, log, exp, fabs

print("=== PY_NUMERICO ===")
print("Metodos numericos: raices de f(x)")
print("")

# --- Newton-Raphson ---
# f(x) = x^3 - 2x - 5  (raiz ~2.0946)
def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2

def newton(x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if fabs(fx) < tol:
            return x, i
        dfx = df(x)
        if dfx == 0:
            return None, i
        x = x - fx / dfx
    return x, max_iter

x0 = float(input("Newton-Raphson\nx0 inicial (sugerido: 2): "))
raiz, iters = newton(x0)

if raiz is not None:
    print("Raiz: " + str(round(raiz, 10)))
    print("Iteraciones: " + str(iters))
    print("f(raiz) = " + str(round(f(raiz), 15)))
else:
    print("Error: derivada = 0 en el proceso")

print("")

# --- Biseccion ---
def biseccion(a, b, tol=1e-10, max_iter=100):
    if f(a) * f(b) > 0:
        return None, 0
    for i in range(max_iter):
        c = (a + b) / 2
        if fabs(f(c)) < tol or (b - a) / 2 < tol:
            return c, i
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, max_iter

print("Biseccion en [1, 3]:")
raiz_b, iters_b = biseccion(1, 3)
if raiz_b is not None:
    print("Raiz: " + str(round(raiz_b, 10)))
    print("Iteraciones: " + str(iters_b))
else:
    print("Error: f(a) y f(b) tienen el mismo signo")

print("Listo.")
#end

EXPORT PY_NUMERICO()
BEGIN
  PRINT();
  PYTHON(numerico);
END;
```

---

## Checklist antes de subir

- [ ] `fabs()` de `math` — no usar `abs()` para flotantes en MicroPython (puede dar problemas)
- [ ] Funciones definidas con `def` dentro del bloque — disponible en MicroPython
- [ ] Tolerancia `1e-10` — notación científica soportada en MicroPython
- [ ] No usar f-strings — concatenar con `str()`

---

## Preguntas a validar

1. ¿`def` dentro de `#PYTHON` funciona correctamente?
2. ¿Recursión o loops de 100 iteraciones se completan sin timeout?
3. ¿`fabs()` y `1e-10` soportados?
4. ¿La velocidad es notablemente mejor que un PPL equivalente?
5. ¿El resultado numérico es correcto (raiz ≈ 2.0945514815)?

---

## Resultados

| # | Descripción | Estado | Fecha |
|---|-------------|--------|-------|
| 1 | def dentro de #PYTHON | ⬜ | — |
| 2 | Newton-Raphson completo sin error | ⬜ | — |
| 3 | Bisección completa sin error | ⬜ | — |
| 4 | fabs + 1e-10 soportados | ⬜ | — |
| 5 | Resultado correcto (2.0945514815) | ⬜ | — |

---

## Notas
