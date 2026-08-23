# ETN1015 — Laboratorios LaTeX

> Última actualización: 2026-08-23 — sesión alx-rul  
> Compilador: **Overleaf** (pdfLaTeX) · Punto de entrada: `Main_Include.tex`

---

## Archivos y carpetas

```
ETN1015/
  Main_Include.tex    ← raíz del proyecto
  Capitulos/
    C00-Caratula.tex
    Laboratorio1_1015.tex
  Graficos/
    Lab1/ … Lab5/
    logo_umsa.png
    img_caratula_fonfo.jpg
  Anexos/
    Lab1/ … Lab5/
```

---

## Capitulos/

| Archivo | Contenido |
|---|---|
| `C00-Caratula.tex` | Carátula. Cargada con `\input` desde el main. |
| `Laboratorio1_1015.tex` | Lab 1 — Digitalización de Señales. 5 secciones. |

**Estructura de cada laboratorio (`subfiles`):**
```latex
\documentclass[../Main_Include.tex]{subfiles}
\begin{document}
\backgroundsetup{contents={}}  % evita draft en compilación standalone
\newcommand{\tituloinforme}{Título del informe}
% ... contenido ...
\end{document}
```

**Para agregar un laboratorio nuevo:**
1. Copiar `Laboratorio1_1015.tex` → `Laboratorio2_1015.tex`
2. Cambiar `\tituloinforme`
3. Agregar `\subfile{Capitulos/Laboratorio2_1015}` en `Main_Include.tex`

---

## Graficos/

Imágenes del proyecto. Todas las rutas están en `\graphicspath` — usar
`\includegraphics{nombre}` sin especificar subcarpeta.

| Carpeta | Uso |
|---|---|
| `Lab1/` … `Lab5/` | Imágenes por laboratorio |

---

## Anexos/

Archivos de código fuente (`.m`, `.py`) referenciados desde los laboratorios
con `\lstinputlisting`.

| Carpeta | Uso |
|---|---|
| `Lab1/` … `Lab5/` | Código por laboratorio |

```latex
% Ejemplo de uso en un laboratorio:
\lstinputlisting[style=matlab_dark, caption={Ejercicio 1}]{Anexos/Lab1/ej1.m}
```

---

## Main_Include.tex — notas

- Preámbulo cargado con `\input` desde `../Preambulo/`
- Carátula con `\input`, luego `\setcounter{page}{1}`
- Capítulos con `\subfile`
