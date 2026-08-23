# Sistema LaTeX — Vault

> Compilador objetivo: **Overleaf** (pdfLaTeX)  
> Arquitectura multi-archivo: paquete `subfiles`

---

## Estructura del vault

```
Latex/
  Preambulo/          ← preámbulo compartido entre materias (fuente de verdad)
  Graficos_legacy/    ← figuras TikZ/circuitikz de referencia (ejemplos reutilizables)
  ETN1015/            ← proyecto Laboratorios ETN1015
  ETN_XXX/            ← próximas materias, misma estructura
```

---

## Preambulo/ — fuente de verdad

Configuración global compartida. Al crear un proyecto nuevo en Overleaf,
este preámbulo se usa como base.

| Archivo | Responsabilidad |
|---|---|
| `Preambulo.tex` | Núcleo: paquetes, estilos de código, `subfiles`, `graphicspath`. Carga `Colores.tex` y `TikzEstilos.tex`. |
| `Colores.tex` | Paletas de color: matlab\_dark, diagramas de flujo, acento, tablas. |
| `TikzEstilos.tex` | `\tikzset` para diagramas de bloques y flujo. |
| `PaginaEstilo.tex` | Extensión del `\lstset` global. |
| `EstiloSecciones.tex` | `\titleformat` para secciones. Activa `fancyhdr`. |
| `Entornos.tex` | Entornos personalizados (`cuadropregunta`, etc.). |

---

## Graficos_legacy/

Colección de figuras TikZ/circuitikz de un proyecto anterior. No se copian
a los proyectos de materia — están aquí como referencia y ejemplos reutilizables.

> ⚠️ Los `\tikzset` locales pueden colisionar con `TikzEstilos.tex`.
> Revisar antes de usar en un informe.

---

## Estructura de cada materia

Cada carpeta de materia replica la estructura que va a Overleaf:

```
ETN_XXX/
  Main_Include.tex    ← raíz del proyecto, específico por materia
  Capitulos/          ← un .tex por laboratorio (formato subfiles)
  Graficos/
    Lab1/ … LabN/     ← imágenes por laboratorio
  Anexos/
    Lab1/ … LabN/     ← archivos .m, .py, etc. por laboratorio
```

Ver `README.md` dentro de cada carpeta de materia para el detalle de sus archivos.

---

## Flujo para crear un nuevo proyecto en Overleaf

```
1. Comprimí Preambulo/ como .zip
2. Overleaf → New Project → Upload Project → subí el zip
3. Arrastrá a Overleaf:
     - Main_Include.tex  (de la carpeta de la materia)
     - Capitulos/        (con C00-Caratula.tex y el primer laboratorio)
     - Graficos/         (con subcarpetas Lab1…LabN vacías)
     - Anexos/           (con subcarpetas Lab1…LabN vacías)
4. Compilar Main_Include.tex — debe producir PDF sin errores
```

## Flujo de trabajo diario

```
Editar .tex en Obsidian
  → arrastrar el archivo modificado a Overleaf (reemplazar)
  → compilar y verificar PDF
```

Solo se arrastra el archivo que cambió — no hace falta re-subir todo.

---

## Convenciones

| Elemento | Convención | Ejemplo |
|---|---|---|
| Carpeta de materia | sigla oficial | `ETN1015/` |
| Archivo de capítulo | `LaboratorioN_SIGLA.tex` | `Laboratorio1_1015.tex` |
| Subcarpetas gráficos y anexos | `LabN/` | `Lab1/` |
| Carátula | `C00-Caratula.tex` | fijo |
