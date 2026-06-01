
````start-multi-column
ID: cornell-001
number of columns: 2
column size: [55%, 45%]
border: off
shadow: off
````

## 📝 Apuntes

Acá va el contenido principal — definiciones, 
desarrollo del tema, fórmulas, etc.
eraaer
aer
aer
aer
aer
aer
aer
aer

--- column-break ---

## ❓ Preguntas / Claves

- ¿Qué implica X?
- ¿Cómo se relaciona con Y?
- Palabra clave: **Z**

````end-multi-column```

> **Resumen:** Una o dos oraciones que capturen la idea central de esta sección.
````

---

### Dos cosas importantes para tu vault

**1. El `ID` debe ser único por nota.** Si ponés dos bloques Cornell en la misma nota (ej. un comet largo con varias secciones), usá `cornell-001`, `cornell-002`, etc.

**2. No va en el YAML.** El bloque va en el cuerpo de la nota, debajo del frontmatter, como cualquier otro contenido. Los campos YAML de `planet` y `comet` no cambian.

---

### Cómo integrarlo en tus plantillas existentes

En `tpl-planet.md` y `tpl-comet.md`, después del frontmatter actual, el cuerpo quedaría así:

````markdown
<%* tp.file.cursor() %>

```start-multi-column
ID: cornell-001
number of columns: 2
column size: [55%, 45%]
border: off
shadow: off
```

## 📝 Apuntes



--- column-break ---

## ❓ Preguntas / Claves



```end-multi-column```

> **Resumen:** 
```

El cursor de Templater cae antes del bloque, listo para escribir.

---

### ¿Querés que actualice los archivos `tpl-planet.md` y `tpl-comet.md` directamente en el vault con esto integrado?

También puedo crear una versión standalone — una plantilla `tpl-cornell-block.md` en `_templates/` que insertes con Templater dentro de cualquier nota cuando la necesitás, sin tocar las plantillas base.