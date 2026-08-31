
### N15. PATRÓN — SALIDA COMBINACIONAL PERMANENTE (fuera de secuencia)

> Contexto para NotebookLM: las expresiones después de `END SEQUENCE` y antes de `END` son salidas combinacionales que el módulo mantiene en todo momento, sin reloj. Se usan cuando una salida debe reflejar en tiempo real el contenido de un registro o una operación lógica sobre él. Pueden incluir transferencias condicionales con `*` y row catenation con `!`.

```AHPL
% Formato básico:
END SEQUENCE
SALIDA = expresión
END

% Ejemplo — CHAR siempre refleja CR:
END SEQUENCE
CHAR = CR
END

% Ejemplo con transferencia condicional y row catenation (Hill & Peterson 2ª ed., Example 9.3):
% ss toma el valor 1!0 (es decir, 1 o 0) condicionado por (start, stop)
END SEQUENCE
ss * (start \/ stop) ← (1!0) * (start, stop)
OPR = PR
END

% Ejemplo con selección de bits:
END SEQUENCE
CHAR = CR(0:7)
END
```

> **Diferencia con transferencia en paso:** `CR ← valor` ocurre una vez al borde de reloj. `CHAR = CR` es continuo — si CR cambia, CHAR cambia en el mismo instante.
>
> **Nota:** las expresiones fuera de secuencia pueden usar `←` (con reloj) o `=` (combinacional) según el tipo de operación. El ejemplo `ss * (start \/ stop) ← (1!0) * (start, stop)` usa `←` porque `ss` es un registro (MEMORY).
