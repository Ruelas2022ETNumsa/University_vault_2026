# Mapa del proyecto LaTeX — `work/`

> Última actualización: 2026-08-23 — sesión alx-rul  
> Compilador objetivo: **Overleaf** (pdfLaTeX)  
> Punto de entrada: `Main_Include.tex`  
> Arquitectura multi-archivo: paquete `subfiles`

---

## Estructura general

```
work/
├── Main_Include.tex        ← punto de entrada del documento
├── Preambulo/              ← configuración global (paquetes, estilos, colores)
├── Capitulos/              ← contenido de cada informe/laboratorio
├── Graficos/               ← imágenes y figuras TikZ/circuitikz
└── Anexos/                 ← fragmentos de código para insertar en informes
```

---

## `Main_Include.tex`

Archivo raíz. Define la clase del documento y carga todo el preámbulo
antes de abrir `\begin{document}`.

**Cadena de carga:**

```
Main_Include.tex
  ├── Preambulo/Preambulo.tex
  │     ├── Preambulo/Colores.tex
  │     └── Preambulo/TikzEstilos.tex
  ├── Preambulo/PaginaEstilo.tex
  ├── Preambulo/EstiloSecciones.tex
  └── Preambulo/Entornos.tex
```

Para agregar un nuevo informe: añadir `\subfile{Capitulos/NombreArchivo}` después de la carátula y antes de `\end{document}`.

---

## `Preambulo/`

Configuración global. Ningún archivo de esta carpeta contiene contenido
del documento — solo paquetes, estilos y definiciones.

| Archivo | Responsabilidad |
|---|---|
| `Preambulo.tex` | Núcleo: todos los `\usepackage` (incluido `subfiles`), `\lstset`, `\lstdefinestyle`, comandos personalizados. Carga `Colores.tex` y `TikzEstilos.tex` internamente. |
| `Colores.tex` | Todas las paletas de color: matlab\_dark, diagramas de flujo, acento (c1–c9), tablas, informes. |
| `TikzEstilos.tex` | `\tikzset` para diagramas de bloques y diagramas de flujo. Depende de los colores de `Colores.tex`. |
| `PaginaEstilo.tex` | Extensión del `\lstset` global (`firstnumber`, `numberfirstline`). `\pagestyle{fancy}` comentado — se activa en `EstiloSecciones.tex`. |
| `EstiloSecciones.tex` | `\titleformat` para `\section` y `\subsection`. Activa `\pagestyle{fancy}` con encabezado dinámico (`\tituloinforme`). |
| `Entornos.tex` | Entornos personalizados reutilizables. Actualmente: `cuadropregunta` (caja con fondo azul para enunciados). |

**Para agregar un color nuevo:** editar `Colores.tex`.  
**Para agregar un estilo TikZ nuevo:** editar `TikzEstilos.tex`.  
**Para agregar un entorno nuevo:** editar `Entornos.tex`.

---

## `Capitulos/`

Un archivo `.tex` por informe o laboratorio. Cada archivo usa el paquete `subfiles` — puede compilarse solo en Overleaf o desde `Main_Include.tex`.

| Archivo | Descripción |
|---|---|
| `C00-Caratula.tex` | Carátula oficial reutilizable. Datos a editar: institución, materia, tema, nombres. Suprime el fondo (`\NoBgThispage`) durante la carátula. Se carga con `\input` (no `\subfile`). |
| `Laboratorio1_903.tex` | Laboratorio 1 — Digitalización de Señales. 5 secciones: señales periódicas, convolución, sistema recursivo, DTFT, DFT. |

**Estructura de cada archivo de capítulo (`subfiles`):**
```latex
\documentclass[../Main_Include.tex]{subfiles}
\begin{document}
\backgroundsetup{contents={}}  % suprime draft en compilación standalone
% ... contenido ...
\end{document}
```

**Convención para nuevos informes:**
1. Copiar `Laboratorio1_903.tex` como plantilla.
2. Cambiar `\newcommand{\tituloinforme}{...}` al inicio del archivo.
3. Registrar con `\subfile{Capitulos/LaboratorioN_XXX}` en `Main_Include.tex`.

---

## `Graficos/`

Imágenes e ilustraciones del proyecto.

| Elemento | Descripción |
|---|---|
| `logo_umsa.png` | Logo institucional — usado en `C00-Caratula.tex`. |
| `img_caratula_fonfo.jpg` | Imagen de fondo de carátula — usada con el paquete `background`. |
| `Legacy/` | Colección de figuras TikZ/circuitikz de referencia. útiles como ejemplos. Ver nota abajo. |

### `Legacy/` — nota

Contiene ~65 archivos `.tex` con fragmentos de figuras listos para `\input`.
Dos tipos de contenido:

- **circuitikz** — circuitos RC, bloques de transferencia (ej. `Fig31a.tex`):  
  fragmentos con `\begin{circuitikz}...\end{circuitikz}`, sin preámbulo.

- **tikzpicture** — diagramas de bloques en dominio $s$ (ej. `Fig31b.tex`):  
  fragmentos con `\tikzset{...}` local + `\begin{tikzpicture}...\end{tikzpicture}`.

> ⚠️ Los `\tikzset` locales dentro de `Legacy/` pueden colisionar con
> los estilos globales de `TikzEstilos.tex`. Revisar antes de usar en un informe nuevo.

También contiene `OldImage/` (subcarpeta con imágenes del proyecto original)
y un `.png` suelto (`Fig36.png`).

**Subcarpetas por laboratorio:**

| Carpeta | Contenido |
|---|---|
| `Lab1/` | Imágenes del Laboratorio 1 |
| `Lab2/` | Imágenes del Laboratorio 2 |
| `Lab3/` | Imágenes del Laboratorio 3 |
| `Lab4/` | Imágenes del Laboratorio 4 |
| `Lab5/` | Imágenes del Laboratorio 5 |

Todas las rutas están registradas en `\graphicspath` — basta usar el nombre del archivo en `\includegraphics{nombre}` sin especificar subcarpeta.

---

## `Anexos/`

Carpeta reservada para fragmentos de código (MATLAB, Python, etc.)
que luego se incorporan como listados en los informes vía `\lstinputlisting`
o como bloques `lstlisting` copiados manualmente.

> Vacía por el momento. Estructura a definir según necesidad.

---

## Flujo de trabajo típico para un nuevo informe

```
1. Copiar Capitulos/Laboratorio1_903.tex → Capitulos/LaboratorioN_XXX.tex
2. Editar \newcommand{\tituloinforme}{...} con el título del informe
3. Editar C00-Caratula.tex con los datos del nuevo informe
4. Agregar \subfile{Capitulos/LaboratorioN_XXX} en Main_Include.tex
5. Colocar imágenes en Graficos/ y código en Anexos/
6. Compilar desde Main_Include.tex (documento completo)
   o abrir LaboratorioN_XXX.tex directamente (solo ese informe)
```

---

## Notas de arquitectura

### Multi-archivo con `subfiles`

Cada archivo de `Capitulos/` (excepto la carátula) es un subfile independiente.
Al compilarlo solo en Overleaf hereda automáticamente el preámbulo de `Main_Include.tex`.

- `\subfile{}` en el main — equivale a `\input` pero activa la herencia de preámbulo
- `\input{}` se reserva para preámbulo y carátula
- `\setcounter{page}{1}` en el main tras la carátula — garantiza numeración correcta
- `\backgroundsetup{contents={}}` al inicio de cada capítulo — evita watermark draft en compilación standalone
