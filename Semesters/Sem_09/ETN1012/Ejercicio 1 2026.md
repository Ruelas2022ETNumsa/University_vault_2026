# Ejercicio 1 2026

Si el código del país es 403 y el código de la ciudad es 33, para realizar una llamada internacional desde Bolivia cual es el procedimiento establecido para las llamadas al exterior, realizar la llamada.

---

## Solución

Se aplica el **Plan Fundamental de Numeración de 15 dígitos**. Según el formulario, la llamada internacional saliente es:

$$
00 + \text{Código Carrier} + \text{Código de País} + \text{Número de teléfono}
$$

donde el número de teléfono incluye el código de ciudad (dígitos 7 y 8) y el número de abonado (zona, central y usuario).

| Campo | Dígitos del plan | Cantidad | Valor |
| ----- | :--------------: | :------: | ----- |
| Acceso internacional | 14 y 15 | 2 | `00` |
| Código del Carrier | 12 y 13 | 2 | `10` (supuesto: ENTEL) |
| Código de país | 9, 10 y 11 | 3 | `403` |
| Código de ciudad / región | 7 y 8 | 2 | `33` |
| Zona | 6 | 1 | `1` (ej.) |
| Central | 5 | 1 | `2` (ej.) |
| Usuario | 1, 2, 3 y 4 | 4 | `3456` (ej.) |

Check: 2 + 2 + 3 + 2 + 1 + 1 + 4 = **15 dígitos**.

Supuestos: el enunciado no da el carrier ni el número de abonado; se toma ENTEL (`10`) y el abonado `123456` como ejemplo.

**Marcación:** `00 10 403 33 1 2 3456` → `001040333123456`

---

REFERENCIA (no es parte de la respuesta; fuentes de internet, verificar con las diapositivas)

Zona telefónica actual (Bolivia; ojo: no es el dígito 6 "zona" del plan de 15 dígitos del formulario, que es la zona dentro de la ciudad; el país del enunciado es 403, no Bolivia): 2 = La Paz, Oruro, Potosí | 3 = Santa Cruz, Beni, Pando | 4 = Cochabamba, Chuquisaca, Tarija

Código de ciudad (2 dígitos, plan anterior; las fuentes varían):

| Ciudad                  | Código                   |
| ----------------------- | ------------------------ |
| La Paz                  | 22                       |
| Oruro                   | 52                       |
| Potosí                  | 62                       |
| Sucre                   | 64                       |
| Cochabamba              | 44 (otra fuente: 42)     |
| Tarija                  | 66                       |
| Santa Cruz de la Sierra | 33 |
| Trinidad                | 46 (346 con zona 3)      |
| Cobija                  | 842 (3 dígitos)          |

Código de carrier / portador (formato 1X o XY):

| Operador        | Código |
| --------------- | ------ |
| Entel           | 10     |
| AXS             | 11     |
| COTAS           | 12     |
| Boliviatel      | 13     |
| Nuevatel (Viva) | 14     |
| ITS             | 15     |
| COTEL           | 16     |
| Telecel (Tigo)  | 17     |
| BossNet         | 20     |
| Unete           | 21     |
| Utecom          | 22     |

Nota: asignaciones antiguas (años 90) daban 11 = AES, 12 = Teledata, 13 = Boliviatel. Tigo marca hoy 0017 (00 + 17).
