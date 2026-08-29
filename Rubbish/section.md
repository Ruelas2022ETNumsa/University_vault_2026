
### N4. OPERADORES AHPL

#### Transferencia y conexión

| Operador | LaTeX | Nombre | Reloj |
|---|---|---|---|
| \( \leftarrow \) | `\leftarrow` | Transferencia — \( AC \leftarrow DR \) copia DR en AC al borde de reloj | Sí |
| \( = \) | `=` | Conexión de bus — \( IBUS = AC \) conecta AC al bus | No |
| \( * \) | `*` | Transferencia condicional — \( A * \overline{a} \leftarrow B \) (si \( a=0 \), transfiere B a A); \( D \leftarrow (A \mathop{!} B \mathop{!} C) * (f,\, g,\, h) \) (selecciona origen según control) | Sí |

#### Operadores lógicos

| Símbolo | LaTeX | Operación | Alternativa texto | Ejemplo |
|---|---|---|---|---|
| \( \land \) | `\land` | AND | `AND`, `&` | \( csrdy \land \overline{CSBUS_0} \) |
| \( \lor \) | `\lor` | OR | `OR`, `+` | \( busy \lor first \) |
| \( \oplus \) | `\oplus` | XOR | `XOR`, `@` | \( AC \oplus DR \) |
| \( \overline{X} \) | `\overline{X}` | NOT | `NOT`, `~` prefijo | \( \overline{CSBUS_0} \), \( \overline{accept} \) |

#### Selección de bits

| Notación | LaTeX | Significado | Ejemplo |
|---|---|---|---|
| \( REG_i \) | `REG_i` | Bit i del registro | \( IR_0 \), \( CR_7 \) |
| \( REG_{i:j} \) | `REG_{i:j}` | Bits i a j | \( IR_{8:17} \), \( D_{10:17} \) |

#### Operaciones aritméticas

| Notación | LaTeX | Operación | Ejemplo |
|---|---|---|---|
| \( INC(REG) \) | `INC(REG)` | Incremento | \( PC \leftarrow INC(PC) \) |
| \( ADD(A,B) \) | `ADD(A,B)` | Suma | \( AC \leftarrow ADD(AC, DR) \) |
| \( BUSFN(M;\ DCD(AR)) \) | `BUSFN(M; DCD(AR))` | Acceso a ROM/tabla combinacional — lee datos de memoria M direccionada por DCD(AR) | \( MD \leftarrow BUSFN(M;\ DCD(AR)) \) |
| `RETURN(REG)` | `RETURN(REG)` | Combinational logic unit definida en el ejemplo — no es operador estándar de AHPL (no aparece en operador set, p. 118). En Example 9.3 actúa como detector booleano: evalúa si REG contiene un código específico y devuelve 1 bit. Equivalente estándar: `(CR = código)`. Ver: Using Combinational Logic Units, p. 128-132. | \( feed = RETURN(CR) \) |
