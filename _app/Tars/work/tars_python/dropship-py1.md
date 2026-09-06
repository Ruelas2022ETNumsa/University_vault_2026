---
galaxy_body: dropship
carrier: "[[tsk_carrier.md]]"
scope: prueba-1
status: activo
date: 2026-09-05
---

## Propósito

Validar que el pipeline `tars-sync` puede convertir un `.hpprgm` con bloque `#PYTHON` y que CASE lo ejecuta correctamente. Prueba mínima viable: `print`, `input()`, `math` básico — sin tocar `hpprime`.

---

## Concepto

El bloque `#PYTHON` convive con el wrapper PPL en el mismo archivo `.hpprgm`. El script `main.py` lo procesa igual que un programa PPL normal — no requiere cambios. CASE debe reconocer el bloque y ejecutarlo con MicroPython.

---

## Programa propuesto — PY_BASICO

```python
#PYTHON basico
from math import sqrt, pi, sin, cos

print("=== PY_BASICO ===")
x = float(input("Ingrese un numero: "))
print("Raiz cuadrada:", sqrt(x))
print("x * pi =", x * pi)
print("sin(x) =", round(sin(x), 6))
print("cos(x) =", round(cos(x), 6))
print("x^2 =", x**2)
print("Listo.")
#end

EXPORT PY_BASICO()
BEGIN
  PRINT();
  PYTHON(basico);
END;
```

---

## Checklist antes de subir

- [ ] Nombre del EXPORT coincide con nombre del archivo (`PY_BASICO.hpprgm`)
- [ ] `#PYTHON` y `#end` en minúsculas correctas
- [ ] No usar f-strings — usar concatenación o `.format()`
- [ ] `float(input(...))` para entrada numérica

---

## Preguntas a validar

1. ¿El pipeline genera el binario correctamente con el bloque #PYTHON incluido?
2. ¿CASE reconoce y ejecuta el bloque MicroPython?
3. ¿`input()` muestra prompt en consola de texto de la calc?
4. ¿`print()` muestra output en la consola correctamente?
5. ¿Las funciones de `math` funcionan sin problemas?

---

## Resultados

| # | Descripción | Estado | Fecha |
|---|-------------|--------|-------|
| 1 | Pipeline genera .hpprgm con #PYTHON | ⬜ | — |
| 2 | CASE ejecuta el bloque Python | ⬜ | — |
| 3 | input() + print() operativos | ⬜ | — |
| 4 | math (sqrt, pi, sin, cos) operativo | ⬜ | — |

---

## Notas
