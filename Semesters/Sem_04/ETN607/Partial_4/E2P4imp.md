# E2P4 — Circuito cúbico: sistema mecánico equivalente

## Enunciado

Hallar el sistema mecánico equivalente del circuito eléctrico, que tiene forma de cubo.

**Figura:** (dibujar a mano)

---

## Reglas

1. **Analogía de voltajes:** inductancia = cuerpo (masa), fuente = fuerza, capacitor C = resorte 1/C, resistencia R = amortiguador, corriente = velocidad.
2. **Grados de libertad:** número de mallas = N. Para un circuito conexo, N = aristas − nodos + 1.
3. **Cubo:** se dibuja plano eligiendo una de sus 6 caras como cara exterior. La cara exterior **no** es una malla; las otras 5 caras sí.
4. **Compartidos:** una inductancia (cuerpo) o una fuente (fuerza) no puede estar compartida entre dos mallas. Solo se analizan inductancias y fuentes. Si alguna está compartida, se elige otra cara exterior (se gira el circuito).
5. **Numeración:** las mallas con inductancia llevan el número de su inductancia (3, 4 y 5). Las mallas sin inductancia son 1 y 2. Una malla sin inductancia es un **cuerpo simulado** de masa 0, que se conecta igual que cualquier cuerpo.
6. **Corrientes:** una corriente de malla por malla (i₁ a i₅). Un elemento en una sola malla lleva la corriente de esa malla. Un elemento compartido por dos mallas lleva la diferencia de sus corrientes.
7. **Conversión a mecánico:** la corriente de una malla es la velocidad de su cuerpo. Un elemento en una sola malla va entre su cuerpo y la pared fija. Un elemento compartido va entre los dos cuerpos de sus mallas.
8. **Serie ↔ paralelo:** elementos en serie en el circuito pasan a paralelo en el sistema mecánico.

---

## Solución por pasos

### Paso 1. Grados de libertad y cara exterior

N = 12 − 8 + 1 = **5 mallas**.

**Cara exterior elegida: E–F–G–H.** Sus aristas E–F, F–G, G–H y E–H quedan cada una en una sola malla. Las inductancias L3, L4, L5 y la fuente S están todas en esas aristas, así que ninguna queda compartida.

**Mallas (las 5 caras restantes):**

| Malla | Cara | Aristas y elementos | Inductancia en la malla | Cuerpo en el mecánico |
|---|---|---|---|---|
| **1** | A-B-C-D | Rab, Rbc, Rcd, Rad | ninguna | **simulado L1** (masa 0) |
| **2** | A-B-F-E | Rab, Cbf, R_ef, Rae | ninguna | **simulado L2** (masa 0) |
| **3** | B-C-G-F | Rbc, Rcg, L3, Cbf | L3 | masa L3 |
| **4** | C-D-H-G | Rcd, Cdh, L4, Rcg | L4 | masa L4 |
| **5** | D-A-E-H | Rad, Rae, L5 con S, Cdh | L5 y S | masa L5 |

Las mallas 1 y 2 no tienen inductancia en el circuito real, pero igual son grados de libertad. Por eso en el sistema mecánico aparecen como cuerpos simulados L1 y L2, de masa 0.

### Paso 2. Inductancias y fuentes compartidas

| Elemento | Arista | Mallas | ¿Compartido? |
|---|---|---|---|
| L3 | F–G | 3 | No |
| L4 | G–H | 4 | No |
| L5 | E–H | 5 | No |
| S | E–H (en serie con L5) | 5 | No |

**Conclusión:** no hay inductancias ni fuentes compartidas. **No hace falta girar el cubo.**

### Paso 3. Corriente por cada uno de los 12 elementos

**Elementos en una sola malla (aristas de la cara exterior):**

| Elemento | Arista | Malla | Corriente |
|---|---|---|---|
| R_ef | E–F | 2 | i₂ |
| L3 | F–G | 3 | i₃ |
| L4 | G–H | 4 | i₄ |
| L5 y S (serie) | E–H | 5 | i₅ |

**Elementos compartidos por dos mallas:**

| Elemento | Arista | Mallas | Corriente |
|---|---|---|---|
| Rab | A–B | 1 y 2 | i₁ − i₂ |
| Rbc | B–C | 1 y 3 | i₁ − i₃ |
| Rcd | C–D | 1 y 4 | i₁ − i₄ |
| Rad | A–D | 1 y 5 | i₁ − i₅ |
| Cbf | B–F | 2 y 3 | i₂ − i₃ |
| Rcg | C–G | 3 y 4 | i₃ − i₄ |
| Cdh | D–H | 4 y 5 | i₄ − i₅ |
| Rae | A–E | 2 y 5 | i₂ − i₅ |

### Paso 4. Sistema mecánico equivalente

**Cuerpos:**

| Cuerpo | Malla | Masa | Velocidad |
|---|---|---|---|
| 1 (L1) | 1 (A-B-C-D) | 0 (simulado) | v₁ = i₁ |
| 2 (L2) | 2 (A-B-F-E) | 0 (simulado) | v₂ = i₂ |
| 3 | 3 (B-C-G-F) | L3 | v₃ = i₃ |
| 4 | 4 (C-D-H-G) | L4 | v₄ = i₄ |
| 5 | 5 (D-A-E-H) | L5 | v₅ = i₅ |

**Fuerzas:** una sola, **F₅ = S**, aplicada sobre el cuerpo 5. L5 y S están en serie en el circuito y quedan en paralelo sobre el cuerpo 5.

**Sentido de la fuerza:** lo fija la polaridad de la fuente respecto al sentido elegido para i₅. Si la fuente empuja la corriente en el sentido positivo de i₅, F₅ es positiva (empuja al cuerpo 5 en el sentido de v₅). Si la empuja en contra, F₅ = −S. El enunciado no da la polaridad de S, así que aquí solo se deja indicada F₅ = ±S sobre el cuerpo 5. Dibujarla a la izquierda o a la derecha del cuerpo no cambia nada, solo es una convención del dibujo.

**Elementos y conexiones:**

| Elemento | Se conecta entre | Velocidad relativa |
|---|---|---|
| Amortiguador **R_ef** | cuerpo 2 y pared fija | v₂ |
| Amortiguador **Rab** | cuerpos 1 y 2 | v₁ − v₂ |
| Amortiguador **Rbc** | cuerpos 1 y 3 | v₁ − v₃ |
| Amortiguador **Rcd** | cuerpos 1 y 4 | v₁ − v₄ |
| Amortiguador **Rad** | cuerpos 1 y 5 | v₁ − v₅ |
| Resorte **1/Cbf** | cuerpos 2 y 3 | v₂ − v₃ |
| Amortiguador **Rcg** | cuerpos 3 y 4 | v₃ − v₄ |
| Resorte **1/Cdh** | cuerpos 4 y 5 | v₄ − v₅ |
| Amortiguador **Rae** | cuerpos 2 y 5 | v₂ − v₅ |

Total: **7 amortiguadores** (R_ef, Rab, Rbc, Rcd, Rad, Rcg, Rae) y **2 resortes** (1/Cbf, 1/Cdh).

**Conexiones por cuerpo:**

- **Cuerpo 1 (masa 0):** Rab al cuerpo 2, Rbc al cuerpo 3, Rcd al cuerpo 4 y Rad al cuerpo 5.
- **Cuerpo 2 (masa 0):** R_ef a la pared, Rab al cuerpo 1, resorte 1/Cbf al cuerpo 3 y Rae al cuerpo 5.
- **Cuerpo 3 (masa L3):** Rbc al cuerpo 1, resorte 1/Cbf al cuerpo 2 y Rcg al cuerpo 4.
- **Cuerpo 4 (masa L4):** Rcd al cuerpo 1, Rcg al cuerpo 3 y resorte 1/Cdh al cuerpo 5.
- **Cuerpo 5 (masa L5):** Rad al cuerpo 1, Rae al cuerpo 2, resorte 1/Cdh al cuerpo 4 y la fuerza F₅ = S.

**Pared fija:** solo está unido a ella **R_ef**. Los cuerpos 3, 4 y 5 son masas libres (no son elementos de pared).

### Paso 5. Verificación de las 12 aristas

| Grupo | Aristas | Representación mecánica |
|---|---|---|
| Cara exterior E-F-G-H | E–F | amortiguador R_ef a la pared |
| | F–G | masa L3 (cuerpo 3) |
| | G–H | masa L4 (cuerpo 4) |
| | E–H | masa L5 (cuerpo 5) y fuerza S |
| Cara A-B-C-D (cuerpo 1 con 2, 3, 4, 5) | A–B, B–C, C–D, A–D | Rab, Rbc, Rcd, Rad |
| Aristas verticales | B–F, C–G, D–H, A–E | 1/Cbf, Rcg, 1/Cdh, Rae |

4 + 4 + 4 = **12 aristas representadas**.

**Correspondencias:**

| Circuito | Sistema mecánico |
|---|---|
| Mallas 1 y 2 | Cuerpos simulados de masa 0 |
| Mallas 3, 4, 5 | Cuerpos de masa L3, L4, L5 |
| S | Fuerza F₅ sobre el cuerpo 5 |
| Cbf, Cdh | Resortes 1/Cbf y 1/Cdh |
| Las 7 resistencias | 7 amortiguadores |
