
**A1 — Sintaxis core**

Tres cosas para probar:

1. **Inline simple** — escribir %%> izquierda%% en medio de un párrafo .

2. **Inline simple** — escribir %%< derecha%% en medio de un párrafo .
   
3. **Con LaTeX** — ecuaciones %%> Ver fórmula $e^{j\theta}$ %% para confirmar que LaTeX dentro del margen renderiza bien.

4. **con comillas** — escribir `%%> algún texto %%` en medio de un párrafo 111111

5. **con comillas** — escribir `%%> 2222   algún texto %%` en medio de un párrafo 





bien la idea no es solo probar las caracteristicas del plugin sino tambien saber donde usarlos.

---

**A2 — Semantic Highlighting**

Cada línea prueba un tag. Verificar color en Reading View y Live Preview.

1. **`!` ámbar** — Texto de referencia %%< ! Esto es importante, entra en examen %% fin de línea.

2. **`?` azul petróleo** — Texto de referencia %%< ? ¿Por qué se cumple esta condición? %% fin de línea.

3. **`X-` naranja quemado** — Texto de referencia %%< X- Error de signo en esta fórmula %% fin de línea.

4. **`V-` verde oliva** — Texto de referencia %%< V- Verificado con Kreyszig p.218 %% fin de línea.

5. **`C-` gris antracita** — Texto de referencia %%< C- Comentario neutro sin carga semántica %% fin de línea.

6. **`F-` morado** — Texto de referencia %%< F- Fórmula clave del tema %% fin de línea.

7. **`R-` verde azulado** — Texto de referencia %%< R- Relación con ETN806 T03 %% fin de línea.

---

**A3 — Grouping Method A** (`[!cornell]` callout)

Uso: agrupar contenido mixto fuera del bloque cornell. Solo renderiza en Reading View.

Caso 1 — párrafo + lista:

> [!cornell]%%> ! Marginalia alineada con todo el grupo %%
> La transformada de Laplace convierte una EDO en una ecuación algebraica.
> - Condición: $\text{Re}(s) > \sigma_0$
> - Útil para sistemas LTI causales
> - Inversa mediante fracciones parciales

Caso 2 — párrafo + imagen (reemplazar con imagen real del vault para la prueba):

> [!cornell]%%> F- Ver diagrama de polos y ceros %%
> El plano $s$ representa la región de convergencia.
> ![[_assets/test_image.png]]

---

**A4 — Grouping Method B** (bloque `marginalia`)

Uso principal en Galaxy: se anida dentro de bloques `cornell` (::cue y ::note).
También funciona standalone para composición compleja o exportación PDF.

Caso 1 — standalone, composición compleja:

```marginalia
La transformada de Laplace se define como: %%> F- Ecuación central del tema %%
$\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$
- Converge para $\text{Re}(s) > \sigma_0$
- Lineal: $\mathcal{L}\{af+bg\} = aF+bG$
```

Caso 2 — anidado dentro de cornell (flujo Galaxy real):

`````cornell
::cue
````marginalia %%> %%
Transformada de Laplace %%> ? ¿Cuál es la condición de convergencia? %%
````

::note
````marginalia %%< %%
Convierte EDO en ecuación algebraica en el dominio $s$. %%< V- Kreyszig p.218 %%
Condición: $\text{Re}(s) > \sigma_0$
````
`````

Caso 3 — nota va ANTES del texto (buena nota Cornell):

```marginalia
%%> ! Entra en examen %% La región de convergencia determina la unicidad de la transformada.
```

%%
# galaxy linkds

%%