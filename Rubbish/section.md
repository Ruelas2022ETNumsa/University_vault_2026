
### N12. PATRÓN — BUCLE DE ESPERA CON SEÑAL

> Contexto para NotebookLM: patrón de polling. El módulo permanece en el mismo paso hasta que una señal cambia de estado. Se usa para esperar `datavalid`, `wait`, `ready`, `accept`. El paso bifurca hacia sí mismo mientras la condición de vuelta sea verdadera.

**Regla de lectura:** la condición dentro de `→ (cond)/(N)` es la condición de **retorno** — cuando es verdadera, vuelve al mismo paso. El módulo sale cuando esa condición es falsa y continúa al paso siguiente.

```
% Espera mientras la señal es 0 (retorna si ~señal=1, sale cuando señal=1):
N.  → (~señal)/(N)

% Espera mientras la señal es 1 (retorna si señal=1, sale cuando señal=0):
N.  → (señal)/(N)

% Ejemplo concreto — esperar que datavalid sea 1:
% retorna a (1) mientras datavalid=0; sale al paso 2 cuando datavalid=1
1.  → (~datavalid)/(1)

% Ejemplo concreto — esperar que wait sea 0:
% retorna a (6) mientras wait=1; sale al paso 7 cuando wait=0
6.  → (wait)/(6)
```
