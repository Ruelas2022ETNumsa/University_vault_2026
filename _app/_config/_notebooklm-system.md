---
title: Sistema NotebookLM — University Vault
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
related_notes:
  - "[[_galaxy-system]]"
  - "[[MAT101-notebooklm-user_guide]]"
  - "[[_notebooklm-prompt]]"
  - "[[desmos_guide]]"
  - "[[tikzjax_guide]]"
tags:
  - beacon
  - notebooklm
  - infraestructura
date_created: 2026-06-03
date_updated: 2026-06-25
status: activo
---

# Sistema NotebookLM — University Vault

> Guía de modos y triggers: [[MAT101-notebooklm-user_guide]]
> Prompt de configuración: [[_notebooklm-prompt]]

NotebookLM es el tutor externo del vault. Recibe las notas `.md` del alumno
como fuente de contexto y las enriquece cruzándolas con los libros de la materia.
No reemplaza las notas — las mejora.

---

## Flujo de trabajo

```
1. Digitalizás tus apuntes en Obsidian
   → nota .md con LaTeX, Desmos y formato Cornell

2. Subís el .md a NotebookLM como fuente
   → NotebookLM lo interpreta según el prompt de configuración

3. Iterás con NotebookLM
   → Modo 4 para corregir errores matemáticos
   → Modo 1 para profundizar conceptos
   → Modo 3 para dictado de contenido nuevo listo para pegar

4. Actualizás la nota en Obsidian con el contenido mejorado

5. Cuando la nota esté completa, exportás a PDF con Better Export
   → el PDF es para leer, imprimir y estudiar fuera del vault
   → NO subir el PDF a NotebookLM — el .md es siempre mejor fuente

6. Si la nota cambia significativamente, resubís el .md a NotebookLM
   → NotebookLM no sincroniza automáticamente — hay que reemplazar
      la fuente manualmente
```

---

## Por qué .md y no PDF como fuente

| Aspecto | .md | PDF (Better Export) |
|---------|-----|---------------------|
| LaTeX | Texto legible — NotebookLM lo interpreta sin ambigüedad | Renderizado como imagen en algunos casos — puede perder contenido |
| Desmos | Código fuente visible — útil como referencia de sintaxis y contexto del tema | Imagen estática — NotebookLM lo ve como figura sin contenido matemático |
| Cornell (MCM) | Interpretado correctamente con el prompt de configuración | Flujo continuo — NotebookLM no distingue columnas |
| YAML | Ignorado naturalmente — no interfiere con el análisis | No presente |

---

## YAML en archivos .md

NotebookLM lee el bloque YAML como texto plano y no lo confunde con
contenido matemático. No requiere instrucción especial en el prompt.
Si en alguna consulta el YAML genera ruido, agregar al prompt:

```
El bloque entre los primeros "---" es YAML de metadatos —
ignoralo para el análisis matemático.
```

---

## Prompt de configuración

El prompt vive en [[_notebooklm-prompt]]. Define:

- 5 modos de respuesta (explicación, ejercicio, ejercicio rápido, dictado, revisión)
- Reglas de sintaxis Desmos y TikZJax
- Interpretación de notas Cornell (Multi-Column Markdown)
- Programa de la materia y mapeo tema → libro prioritario
- Restricción de fuentes: ejercicios solo de los libros del notebook

Un prompt por materia. Cada materia nueva requiere su propio archivo
`_notebooklm-prompt-ETNXXX.md` siguiendo el mismo modelo.
Ver tarea pendiente en [[_ToDo-system]].

---

## Registro de decisiones

| Decisión | Razón |
|----------|-------|
| .md como fuente principal, no PDF | El .md preserva LaTeX como texto y código Desmos como referencia — el PDF los convierte a imagen y pierde contenido matemático |
| PDF solo para lectura y estudio | Better Export genera un PDF de calidad para imprimir y estudiar, pero no aporta como fuente en NotebookLM |
| No agregar interpretación de YAML al prompt | NotebookLM ignora el YAML naturalmente — agregar instrucción solo si se confirma ruido en la práctica |
| Un prompt por materia | Cada materia tiene programa, libros y nivel de rigor distintos — un prompt genérico produce respuestas menos precisas |
| Resubida manual al actualizar la nota | NotebookLM no sincroniza con el vault — resubir el .md cuando la nota cambie significativamente |

%%
galaxy-links
[[_galaxy-system]]
[[MAT101-notebooklm-user_guide]]
[[_notebooklm-prompt]]
[[desmos_guide]]
[[tikzjax_guide]]
[[_ToDo-system]]
%%
