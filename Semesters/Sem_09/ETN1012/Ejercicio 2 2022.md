# Ejercicio 2 2022
Explicar el concepto del plan de numeración con un ejemplo para una llamada internacional a cualquier país de Bolivia. (10 puntos).

---

El **plan de numeración** es un plan técnico que identifica inequívocamente a cada abonado y permite el enrutamiento jerárquico de las llamadas a nivel local, nacional e internacional. Usa una estructura de 15 dígitos:

| Dígitos | Significado |
| :-----: | ----------- |
| 14 y 15 | Ceros de acceso de red (`0` nacional, `00` internacional) |
| 12 y 13 | Código del Carrier (ej. `10` ENTEL, `16` COTEL) |
| 9, 10 y 11 | Código de país (`591` Bolivia) |
| 7 y 8 | Departamento o región |
| 6 | Zona |
| 5 | Central |
| 1, 2, 3 y 4 | Usuario |

Llamada internacional:

$$
00 + \text{Código Carrier} + \text{Código de País} + \text{Número de teléfono}
$$

**Ejemplo** (supuestos: destino La Paz, carrier ENTEL, código de ciudad `22`, abonado `794040`):

`00 + 10 + 591 + 22 + 794040` → **001059122794040**

Check: 2 + 2 + 3 + 2 + 6 = 15 dígitos.
