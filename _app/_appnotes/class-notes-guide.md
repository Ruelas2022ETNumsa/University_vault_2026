---
title: "Class Notes Guide — Apuntes manuscritos a Markdown"
galaxy_body: beacon
scope: vault
audience: [usuario, claude, chatgpt, notebooklm]
tags: [beacon, convencion, apuntes, infraestructura]
date_created: 2026-05-31
date_updated: 2026-05-31
status: activo
---

# Class Notes Guide — Apuntes manuscritos a Markdown

> Esta guía define cómo transformar apuntes manuscritos (vía OCR) al formato `.md` del vault.
> Aplica exclusivamente a notas de tipo `planet` y `comet` del Sistema Galaxy.
> Cualquier IA que reciba esta guía debe seguir estas reglas sin apartarse de ellas.

---

## 1. FLUJO DE TRABAJO

```
Apunte manuscrito
      ↓
   OCR + LaTeX  (ChatGPT)
      ↓
   Texto crudo con fórmulas en $...$ o $$...$$
      ↓
   IA transforma a .md siguiendo esta guía
      ↓
   Archivo final en el vault
```

---

## 2. CABECERA YAML OBLIGATORIA

### Para `planet` (teoría, definiciones, propiedades)

```yaml
---
title: "MATXXX-nombre-descriptivo"
galaxy_body: planet
subject: MAT-XXX
semester: N
partial: N
topic: TNN_nombre-del-tema
star: ""
moons: []
comets: []
tags: [MAT-XXX, galaxy-planet, PN]
date_created: YYYY-MM-DD
status: activo
---
```

### Para `comet` (ejercicio resuelto)

```yaml
---
title: "MATXXX-TNN-nombre-del-ejercicio"
galaxy_body: comet
subject: MAT-XXX
semester: N
partial: N
topic: TNN_nombre-del-tema
source: ""
concepts_used: []
status: pendiente
tags: [MAT-XXX, galaxy-comet, PN]
date_created: YYYY-MM-DD
---
```

---

## 3. JERARQUÍA DE TÍTULOS

| Nivel | Uso | Ejemplo |
|-------|-----|---------|
| `#` | Título de la nota — solo uno por archivo | `# Números reales y desigualdades` |
| `##` | Sección principal del tema | `## Axiomas de cuerpo` |
| `###` | **No usar** para ítems individuales de una lista | — |

> **Regla clave:** si el contenido es una lista de axiomas, teoremas o propiedades numeradas, usar lista numerada bajo un `##` — no crear un `###` por cada ítem. Los `###` se reservan para subsecciones con desarrollo propio (párrafos, no listas).

---

## 4. FORMATO DE LISTAS DE AXIOMAS / TEOREMAS / PROPIEDADES

Estructura estándar — nombre en negrita, fórmula en línea siguiente con tab:

```markdown
1. **Nombre del axioma**
	- $formula_1$
	- $formula_2$
```

Si el ítem tiene una sola fórmula principal:

```markdown
1. **Nombre**
	$formula$
```

Si el ítem tiene explicación textual además de fórmula:

```markdown
1. **Nombre**
	- $formula$
	- Texto explicativo en español
```

**No usar** el símbolo `—` para separar nombre de fórmula en la misma línea.

---

## 5. FÓRMULAS — CUÁNDO USAR `$` vs `$$`

| Situación | Formato | Ejemplo |
|-----------|---------|---------|
| Fórmula dentro de texto corrido | `$...$` | `Sea $a \in \mathbb{R}$` |
| Fórmula corta en línea propia (dentro de lista) | `$...$` con tab | `	$a+b=b+a$` |
| Fórmula importante / resultado principal | `$$...$$` línea propia | definiciones, teoremas centrales |
| Fórmula con fracciones grandes, sumatorias, integrales | `$$...$$` siempre | evita que se vea comprimida |

---

## 6. SEPARADORES Y SECCIONES

Usar `---` para separar secciones principales (entre `##`). No usar `---` entre ítems de una misma lista.

---

## 7. TABLAS

Usar tabla cuando hay comparación de 3 o más elementos con atributos en común:

```markdown
| Tipo | Ejemplo | Descripción |
|------|---------|-------------|
| Igualdad | $2^3=8$ | Siempre verdadera |
| Ecuación | $x^2=4$ | Solo para algunos $x$ |
| Identidad | $x^2-4=(x-2)(x+2)$ | Para todo $x \in \mathbb{R}$ |
```

---

## 8. PIE DE NOTA — GALAXY LINKS

Toda nota debe cerrar con el bloque de enlaces galaxy (invisible en modo lectura):

```markdown
%%
galaxy-links
[[MATXXX-TNN-star]]
%%
```

---

## 9. INSTRUCCIONES PARA IA (ChatGPT / Claude)

Cuando recibas texto OCR de apuntes manuscritos con esta guía, debes:

1. Identificar si es teoría (`planet`) o ejercicio (`comet`) y usar el YAML correspondiente
2. Usar `#` para el título principal y `##` para secciones — nunca `###` para ítems de lista
3. Colocar cada axioma/teorema/propiedad como ítem numerado en negrita con su fórmula en la línea siguiente con tab
4. Convertir todo símbolo matemático a LaTeX — sin unicode matemático suelto (∀ → `$\forall$`, ∃ → `$\exists$`, ∈ → `$\in$`, ℝ → `$\mathbb{R}$`)
5. Usar `$$...$$` para fórmulas principales que merecen línea propia
6. No inventar contenido — si el OCR tiene texto ilegible marcarlo con `[ilegible]`
7. Cerrar con el bloque `%%galaxy-links%%`

---

## 10. EJEMPLO DE SALIDA ESPERADA

Entrada OCR:
```
Axiomas de cuerpo
1. Clausura: a+b ∈ ℝ, a·b ∈ ℝ
2. Conmutatividad: a+b=b+a, a·b=b·a
```

Salida correcta:
```markdown
## Axiomas de cuerpo

Sean $a, b \in \mathbb{R}$

1. **Clausura**
	- $a+b \in \mathbb{R}$
	- $a \cdot b \in \mathbb{R}$

2. **Conmutatividad**
	- $a+b=b+a$
	- $a \cdot b=b \cdot a$
```

---

%%
# galaxy-links
[[_app/_config/_note-system.md]]
[[_app/_config/_galaxy-system.md]]
%%
