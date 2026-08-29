
### N11. MÓDULO COMPLETO — PRINTER INTERFACE

> Contexto para NotebookLM: módulo AHPL completo de la interface de impresora. Cubre el protocolo completo: espera de dirección en CSBUS, handshake con IOBUS (datavalid/accept), carga de DR, acumulación en CR con `first`, envío a impresora (feed/print), y espera de `wait`. Fuente: Hill & Peterson Digital Systems 2ª ed., material del docente ETN825.

```
MODULE: PRINTER INTERFACE
MEMORY: DR[18]; CR[8]; busy; first
OUTPUTS: CHAR[8]; print; feed
INPUTS: wait; csrdy
COMBUSES: IOBUS[18]; CSBUS[12]; ready; datavalid; accept

1.  → (csrdy ∧ ~CSBUS₀ ∧ CSBUS₁ ∧ ~CSBUS₂)/(1)
2.  accept = 1;
    → (~CSBUS₃, ~CSBUS₃, CSBUS₃)/(1, 1A, 3)

3.  → (readȳ)/(3)
4.  CSBUS₀ = busy; datavalid = 1;
    → (~accept, accept)/(4, 1)

1A. ready = 1;
    → (~datavalid)/(1A)
2A. DR ← IOBUS; busy ← 1; accept = 1; first ← 1
3A. CR ← (D₁₀:₁₇!) * (first, ~first)
4A. feed = RETURN(CR); print = RETURN(CR);
5A. Null
6A. → (wait)/(6A)
7A. first ← 0; busy * ~first ← 0
    → (first, ~first)/(3A, 8A)
8A. DEAD END

END SEQUENCE
CHAR = CR
END
```

#### Lectura paso a paso

| Paso | Qué hace |
|---|---|
| `1.` | Bucle de espera: sale cuando \( csrdy = 1 \) y la dirección CSBUS coincide. |
| `2.` | \( accept = 1 \) en el bus CS. Bifurca según \( CSBUS_3 \). |
| `3.` | Espera mientras \( \overline{ready} \) — sale cuando \( ready = 1 \). |
| `4.` | \( CSBUS_0 = busy \), \( datavalid = 1 \). Bucle hasta \( accept = 1 \). |
| `1A.` | \( ready = 1 \). Espera mientras \( \overline{datavalid} \). |
| `2A.` | \( DR \leftarrow IOBUS;\; busy \leftarrow 1;\; accept = 1;\; first \leftarrow 1 \) — todo simultáneo. |
| `3A.` | \( CR \leftarrow (D_{10:17}!) * (first,\, \overline{first}) \). |
| `4A.` | \( feed = RETURN(CR);\; print = RETURN(CR) \) — combinacional. |
| `5A.` | Paso nulo — sincronización. |
| `6A.` | Espera mientras \( wait = 1 \). |
| `7A.` | \( first \leftarrow 0;\; busy * \overline{first} \leftarrow 0 \). Bifurca: \( first = 1 \rightarrow 3A \), si no \( \rightarrow 8A \). |
| `8A.` | DEAD END. |
| `CHAR = CR` | Salida combinacional permanente: \( CHAR = CR \) en todo momento. |
