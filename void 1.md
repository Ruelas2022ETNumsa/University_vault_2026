
**A2 — Semantic Highlighting**

Cada línea prueba un tag. Verificar color en Reading View y Live Preview.

1. **`!` ámbar** — Texto de referencia %%< ! Esto es importante, entra en examen 1730V1 #pep  ^x7y9tt %% fin de línea.

2. **`?` azul petróleo** — Texto de referencia %%< ? ¿Por qué se cumple esta condición?  V1%% fin de línea.

3. **`X-` naranja quemado** — Texto de referencia %%< X- Error de signo en esta fórmula  V1%% fin de línea.

4. **`V-` verde oliva** — Texto de referencia %%< V- Verificado con Kreyszig p.218  V1%% fin de línea.

5. **`C-` gris antracita** — Texto de referencia %%< C- Comentario neutro sin carga semántica  V1%% fin de línea.

6. **`F-` morado** — Texto de referencia %%< F- Fórmula clave del tema  V1%% fin de línea.

7. **`R-` verde azulado** — Texto de referencia %%< R- Relación con ETN806 T03  V1%% fin de línea.

---

**A4 — Grouping Method B** (bloque `marginalia`)

Caso 1 — párrafo simple:

```marginalia
La transformada de Laplace convierte una EDO en una ecuación algebraica. bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla%%> ! Concepto clave %%
```

Caso 2 — párrafo + lista:

```marginalia
La transformada de Laplace convierte una EDO en una ecuación algebraica. %%> ! Entra en examen %%
- Condición: $\text{Re}(s) > \sigma_0$
- Útil para sistemas LTI causales
- Inversa mediante fracciones parciales
```

Caso 3 — párrafo + imagen:

```marginalia
El plano $s$ representa la región de convergencia. %%> F- Ver diagrama %%
![[_assets/test_image.png]]
```

Caso 4 — párrafo + LaTeX:

```marginalia
$\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$ %%> F- Ecuación central %%
- Converge para $\text{Re}(s) > \sigma_0$
- Lineal: $\mathcal{L}\{af+bg\} = aF+bG$
```

Caso 5 — nota antes del texto:

```marginalia
%%> ! Entra en examen %% La región de convergencia determina la unicidad de la transformada.
```

Caso 6 — nota después del texto:

```marginalia
La región de convergencia determina la unicidad de la transformada. %%> ! Entra en examen %%
```

Caso 7 — múltiples marginalia en el mismo bloque:

```marginalia
La transformada de Laplace convierte una EDO en una ecuación algebraica. %%> ! Entra en examen %%

$\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$ %%> F- Ecuación central %%

- Converge para $\text{Re}(s) > \sigma_0$ %%> ? ¿Qué pasa si no converge? %% .
```


123123123
> [!cornell]
> %%> ! Concepto clave %%
> La transformada de Laplace convierte una EDO en una ecuación algebraica.%%> ! Entra en examen %%
> $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$%%> F- Ecuación central %%
> La condición de convergencia es $\text{Re}(s) > \sigma_0$%%> ? ¿Qué pasa si no converge? %%





123123123


---




Caso 8 — anidado dentro de cornell (flujo Galaxy real):







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

````marginalia
La transformada de Laplace convierte una EDO en una ecuación algebraica. %%> ! Entra en examen %%

$\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$ %%> F- Ecuación central %%

- Converge para $\text{Re}(s) > \sigma_0$ %%> ? ¿Qué pasa si no converge? %% .
````




> [!cornell]
> %%> ! Concepto clave %%
> ppppLa transformada de Laplace convierte una EDO en una ecuación algebraica.%%> ! Entra en examen %%
> $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t)\, dt$%%> F- Ecuación central %%
> La condición de convergencia es $\text{Re}(s) > \sigma_0$%%> ? ¿Qué pasa si no converge? %%


`````
---




Primero busco imágenes disponibles en assets:Bien, uso `ima-1.png` que tiene nombre limpio. Los 4 casos:

**Caso 1 — inline simple izquierda:**


Texto de referencia antes de la imagen. %%> ! Imagen al margen izquierdo %%
![[_assets/ima-1.png]]


**Caso 2 — tag `C-` derecha:**


Texto de referencia antes de la imagen. %%< C- Comentario sobre el diagrama %%
![[_assets/ima-1.png]]


**Caso 3 — A3 (callout `[!cornell]`):**


> [!cornell]%%> ! Imagen agrupada en callout %%
> ![[_assets/ima-1.png]]
> %%< C- Comentario derecho sobre la misma imagen %%
> Descripción del diagrama debajo.


**Caso 4 — A4 (bloque `marginalia`):**


```marginalia
Descripción del diagrama. %%> ! Imagen en bloque marginalia %%
![[_assets/ima-1.png]]
```












ammamamama


---

**A5 — Imágenes en el margen**

Sintaxis: `%%> img:[[imagen.png]] %%` / `%%< img:[[imagen.png]] %%`

Caso 1 — inline simple izquierda:

Texto de referencia. %%> img:[[_assets/ima-1.png]] %%
bLA blA bla
bLA blA bLAbLA blA bLAbLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA


---

Caso 2 — tag `C-` derecha:
bLA blA bLA

Texto de referencia. %%< C- img:[[_assets/ima-1.png]] %%
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA


---

Caso 3 — A3 callout con imagen:

> [!cornell]
> Descripción del diagrama. %%> img:[[_assets/ima-1.png]] %%
> %%< C- ww Comentario derecho sobre la imagen %%

bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA




---

Caso 4 — A4 bloque marginalia con imagen:

```marginalia
Descripción del diagrama. %%> img:[[_assets/ima-1.png]] %%
Detalle adicional debajo de la imagen.

bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLA
bLA blA bLAbLA blA bLA
```

bLA blA bLA
bLA blA bLA
bLA blA bLA


amamam








%%
# galaxy linkds

%%