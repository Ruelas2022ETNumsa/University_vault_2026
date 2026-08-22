Leído todo — el documento y el library. Acá está mi análisis completo de complementos necesarios por sección:

---

**Secciones que NO necesitan complemento**
- `## Introducción` — enumeración limpia, completa para el nivel T1.
- `### b) Lagrange` y `### c) Conservación` — el desarrollo está bien detallado, el libro lo repetiría.
- `### d) Simulink` — es software, no hay complemento de libro útil.
- `### c) Rotacion Z γ` y `### d) Traslacion Z` / `### e) Rotaciones Sucesivas` — están completas y son algebraicas.
- `## Energia Cinetica` — una línea, definición cerrada, nada que agregar.

---

**Secciones que SÍ necesitan complemento — con nivel y posición exacta:**

---

**1. `## Objetivo` — después del `>[!summary]`**
Nivel B. El apunte solo dice "hallar EDO eliminando fuerzas de ligadura". Falta: qué son las fuerzas de ligadura, por qué son problemáticas en Newton, y por qué las funciones escalares las eliminan. Taylor Cap. 1 lo explica bien.

```
Complemento nivel B: Objetivo — fuerzas de ligadura y funciones escalares de energía. Buscar en Taylor Cap. 1.
```

---

**2. `### a) Newton` — después del `>[!summary]`**
Nivel C. El apunte aplica Newton al péndulo pero sin enunciar formalmente las condiciones del método (sistema de referencia inercial, segunda ley vectorial). Nelson Schaum's Cap. 11 tiene ejercicio de péndulo en cilíndricas con resolución paso a paso, más difícil que el del apunte.

```
Complemento nivel C: Newton — condiciones formales del método (referencia inercial, segunda ley vectorial) y ejercicio de péndulo en coordenadas cilíndricas más complejo que el del apunte. Buscar en Nelson Cap. 11.
```

---

**3. `## Condiciones (Masa, Velocidad, Tiempo)` — después del `>[!summary]`**
Nivel B. El apunte da los límites como listas pero sin explicar por qué cada uno falla. Taylor Cap. 1 tiene la justificación formal de cada límite. Falta también la definición de "mecánica clásica" como el rango válido entre esos extremos.

```
Complemento nivel B: Condiciones (Masa, Velocidad, Tiempo) — justificación formal de por qué falla la mecánica clásica en cada extremo y definición del rango válido. Buscar en Taylor Cap. 1.
```

---

**4. `## Sistemas de coordenadas` (intro) — después del `>[!summary]`**
Nivel B. El apunte define coordenadas como "variables de posición respecto al origen" pero no dice qué propiedad hace a un sistema de coordenadas útil (independencia, completitud). Taylor o Alonso.

```
Complemento nivel B: Sistemas de coordenadas (introducción) — propiedades que hacen útil a un sistema de coordenadas (independencia, completitud). Buscar en Taylor Cap. 1 o Alonso & Finn Vol. 1.
```

---

**5. `### b) Cilíndrico` — ya tiene el complemento de versores, OK.**

---

**6. `### c) Esférico` — después del `>[!summary]`**
Nivel C. El apunte tiene las ecuaciones de transformación y la definición de R, pero falta un ejercicio de conversión de coordenadas entre los tres sistemas. Nelson Cap. 12 tiene ejercicios de este tipo.

```
Complemento nivel C: Esférico 3D — ejercicio de conversión de coordenadas entre los tres sistemas (rectangular, cilíndrico, esférico) de mayor dificultad que el ejemplo x=4, y=3, z=0 del apunte. Buscar en Nelson Cap. 12.
```

---

**7. `### d) Parabólicas Cilíndricas` — después del título**
Nivel B mínimo. Está vacía. Al menos ecuaciones de transformación y figura geométrica. Si no hay en los libros, dejar nota de que el docente no la desarrolló.

```
Complemento nivel B: Parabólicas Cilíndricas — ecuaciones de transformación y figura geométrica del sistema. Buscar en Taylor Cap. 1 o Alonso & Finn Vol. 1. Si no existe en las fuentes, indicarlo sin inventar.
```

---

**7b. `### e) Hiperbólicas Cilíndricas` — después del título**
Nivel B mínimo. Está vacía. Misma situación que d).

```
Complemento nivel B: Hiperbólicas Cilíndricas — ecuaciones de transformación y figura geométrica del sistema. Buscar en Taylor Cap. 1 o Alonso & Finn Vol. 1. Si no existe en las fuentes, indicarlo sin inventar.
```

---

**7c. `### f) Otros` — después del título**
Nivel B mínimo. Está vacía. Si hay otros sistemas en los libros, listarlos brevemente.

```
Complemento nivel B: Otros sistemas de coordenadas — listar brevemente otros sistemas ortogonales que aparezcan en Taylor Cap. 1 o Alonso & Finn Vol. 1 además de los ya vistos. Si no hay nada relevante, indicarlo sin inventar.
```

---

**8. `## Rotacion y traslacion Ejes cartesianos` (intro) — después del `>[!summary]`**
Nivel B. El apunte da las matrices directamente sin motivación geométrica. Taylor Cap. 1 o Goldstein Cap. 1 lo tienen.

```
Complemento nivel B: Rotacion y traslacion Ejes cartesianos (introducción) — motivación geométrica de por qué se necesita rotar y trasladar ejes, previa a las matrices. Buscar en Taylor Cap. 1 o Goldstein Cap. 1.
```

---

**9. `## Grados de libertad DOF` — después del `>[!summary]`**
Nivel C. Falta la fórmula general N = 3n - k y un ejemplo de cálculo de DOF de un sistema con varias piezas. Wells Cap. 1 o Taylor tienen esto.

```
Complemento nivel C: Grados de libertad DOF — fórmula general N = 3n - k para n partículas con k restricciones, y ejemplo de cálculo de DOF de un sistema con varias piezas. Buscar en Wells Cap. 1 o Taylor Cap. 1.
```

---

**10. `## Velocidad - Vector` (intro) — después del `>[!summary]`**
Nivel B mínimo. El apunte tiene solo `v = dR/dt` sin ningún contexto de por qué se define así como límite de un cociente incremental. Taylor Cap. 1 lo justifica formalmente.

```
Complemento nivel B: Velocidad - Vector (introducción) — justificación formal de la definición de velocidad como límite del cociente incremental de posición. Buscar en Taylor Cap. 1.
```

---

**11. `### a) Coordenadas rectangulares` (Velocidad) — después del `>[!summary]`**
Nivel B. Tiene R, v y módulo pero le falta la aceleración en cartesianas — las secciones de cilíndricas y esféricas sí la incluyen, queda inconsistente. Taylor Cap. 1.

```
Complemento nivel B: Velocidad coordenadas rectangulares — expresión de la aceleración en cartesianas para completar la sección, consistente con cilíndricas y esféricas. Buscar en Taylor Cap. 1.
```

---

**12. `## Velocidad escalar` — subsección c) esférica — dentro del ::note**
Nivel B. El desarrollo de `dx` está pero `dy` y `dz` están vacíos en el apunte (solo dice "y" y "z" sin expandir). Falta completar las tres derivadas y el resultado final de v². Taylor Cap. 1 o Alonso.

```
Complemento nivel B: Velocidad escalar en coordenadas esféricas — expansión completa de dy y dz con sus derivadas temporales y resultado final de v² = rho_dot² + rho²*theta_dot² + rho²*phi_dot²*sin²(theta). Buscar en Taylor Cap. 1 o Alonso & Finn Vol. 1.
```

---

**Resumen ordenado por prioridad:**

| # | Sección | Nivel | Fuente sugerida |
|---|---|---|---|
| 1 | Objetivo | B | Taylor Cap. 1 |
| 2 | Newton | C | Nelson Cap. 11 |
| 3 | Condiciones | B | Taylor Cap. 1 |
| 4 | Sistemas de coordenadas (intro) | B | Taylor Cap. 1 / Alonso |
| 5 | Esférico | C | Nelson Cap. 12 |
| 6 | d) Parabólicas | B mínimo | Taylor / Alonso |
| 7 | e) Hiperbólicas | B mínimo | Taylor / Alonso |
| 8 | f) Otros | B mínimo | Taylor / Alonso |
| 9 | Rotacion y traslacion (intro) | B | Taylor / Goldstein Cap. 1 |
| 10 | DOF | C | Wells Cap. 1 / Taylor |
| 11 | Velocidad - Vector (intro) | B mínimo | Taylor Cap. 1 |
| 12 | Velocidad rectangular (aceleración) | B | Taylor Cap. 1 |
| 13 | Velocidad escalar c) esférica | B | Taylor Cap. 1 / Alonso |
