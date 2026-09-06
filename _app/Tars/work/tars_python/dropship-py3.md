---
galaxy_body: dropship
carrier: "[[tsk_carrier.md]]"
scope: prueba-3
status: activo
date: 2026-09-05
---

## Propósito

Validar `hpprime.eval()` — el puente entre Python y PPL. Confirmar que desde un bloque `#PYTHON` se puede llamar `MSGBOX`, `CHOOSE`, `INPUT` y leer variables PPL del sistema.

---

## Concepto

`hpprime.eval("expresion_ppl")` ejecuta cualquier expresión PPL y devuelve el resultado como objeto Python. Es el mecanismo central para usar la UI nativa de la calc (menús, popups) desde Python. La limitación conocida es que es lento dentro de loops — en este dropship se usa solo para llamadas puntuales de UI.

---

## Programa propuesto — PY_EVAL

```python
#PYTHON evaltest
from hpprime import eval as heval

# Mostrar mensaje desde Python
heval('MSGBOX("Hola desde Python via eval")')

# CHOOSE desde Python
op = int(heval('CHOOSE(op,"Selecciona","Opcion A","Opcion B","Opcion C"); op'))

if op == 1:
    print("Elegiste: Opcion A")
elif op == 2:
    print("Elegiste: Opcion B")
elif op == 3:
    print("Elegiste: Opcion C")
else:
    print("Cancelado")

# Leer variable del sistema PPL
ticks = heval("ticks")
print("Ticks actuales:", ticks)

# Pausa hasta tecla
heval("wait(0)")
#end

EXPORT PY_EVAL()
BEGIN
  PRINT();
  PYTHON(evaltest);
END;
```

---

## Checklist antes de subir

- [ ] `heval` importado como alias de `hpprime.eval` para no repetir el namespace
- [ ] El string que se pasa a eval debe ser PPL válido con `;` al final si devuelve valor
- [ ] `CHOOSE` devuelve el índice en la variable PPL declarada — leerla con `; var` al final del eval
- [ ] `wait(0)` congela hasta cualquier tecla — equivalente a PPL `WAIT(0)`

---

## Preguntas a validar

1. ¿`hpprime.eval()` ejecuta MSGBOX correctamente desde Python?
2. ¿`CHOOSE` vía eval devuelve el índice seleccionado usable en Python?
3. ¿Se pueden leer variables del sistema PPL (ticks, keyboard) desde Python?
4. ¿`wait(0)` vía eval congela la ejecución como se espera?

---

## Resultados

| # | Descripción | Estado | Fecha |
|---|-------------|--------|-------|
| 1 | MSGBOX vía eval | ⬜ | — |
| 2 | CHOOSE vía eval + retorno de índice | ⬜ | — |
| 3 | Lectura de variables PPL (ticks) | ⬜ | — |
| 4 | wait(0) vía eval | ⬜ | — |

---

## Notas
