```text
MODULE: TEST
MEMORY: AC; flag
OUTPUTS: done
INPUTS: go
COMBUS: DBUS

1. → (~go)/(1)
2. AC ← DBUS; flag ← 1
3. done = 1
4. DEAD END
END SEQUENCE
END
```

| Paso | Operación                                          | Condición           | Estado resultante                                                                                                        |
| ---- | -------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 1.   | \( \rightarrow (\overline{go})/(1) \)              | \( \overline{go} \) | Bucle de espera. Retorna mientras \( go = 0 \); sale al paso 2 cuando \( go = 1 \).                                      |
| 2.   | \( AC \leftarrow DBUS \) ; \( flag \leftarrow 1 \) | —                   | Transferencia síncrona al flanco de reloj. \( AC \) se carga desde \( DBUS \) y \( flag \) se pone en 1 simultáneamente. |
| 3.   | \( done = 1 \)                                     | —                   | Conexión combinacional. La salida \( done \) se activa sin reloj durante este paso.                                      |
| 4.   | \( DEAD\ END \)                                    | —                   | Fin de secuencia. El módulo se detiene.                                                                                  |
| 

---

copiar con puntero:


MODULE: TEST
MEMORY: AC[1]; flag
OUTPUTS: done
INPUTS: go
COMBUS: DBUS[1]

1. → (~go)/(1)
2. AC ← DBUS; flag ← 1
3. done = 1
4. DEAD END
END SEQUENCE
END
PasoOperaciónCondiciónEstado resultante1.$ \rightarrow (\overline{go})/(1) $$ \overline{go} $Bucle de espera. Retorna mientras $ go = 0 $; sale al paso 2 cuando $ go = 1 $.2.$ AC \leftarrow DBUS $ ; $ flag \leftarrow 1 $—Transferencia síncrona al flanco de reloj. $ AC$1$ $ se carga desde $ DBUS$1$ $ y $ flag $ se pone en 1 simultáneamente.3.$ done = 1 $—Conexión combinacional. La salida $ done $ se activa sin reloj durante este paso.4.$ DEAD\ END $—Fin de secuencia. El módulo se detiene.