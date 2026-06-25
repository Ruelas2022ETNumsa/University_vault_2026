---
title: "Claude Matter Boot — Generador de contexto por materia"
galaxy_body: beacon
scope: vault
audience: [claude]
related_notes:
  - "[[_claude-boot]]"
  - "[[_galaxy-system]]"
  - "[[_note-system]]"
  - "[[_ToDo-system]]"
tags: [beacon, claude, materia, infraestructura]
date_created: 2026-06-25
date_updated: 2026-06-25
status: activo
---

# Claude Matter Boot — Generador de contexto por materia

## QUÉ ES ESTE ARCHIVO

Este archivo es un **prompt para Claude**. Su propósito es generar un archivo `contexto_[MATERIA].md` personalizado para cualquier materia universitaria, siguiendo la misma estructura y filosofía del `contexto806.md`.

Cuando el usuario comparta este archivo con Claude, Claude debe leerlo completo y luego hacer las preguntas de la sección "Entrevista" antes de generar nada.

---

## INSTRUCCIÓN PARA CLAUDE

Cuando el usuario comparta este archivo, Claude debe:

1. Leer este archivo completo.
2. Decirle al usuario: *"Listo. Voy a hacerte algunas preguntas para generar el contexto de tu materia. Responde lo que sepas — si algo no lo tienes claro todavía, dímelo y lo dejamos como placeholder."*
3. Hacer las preguntas de la sección "Entrevista" **de a una o en grupos pequeños**, no todas juntas.
4. Con las respuestas, generar el archivo `contexto_[MATERIA].md` siguiendo la estructura de la sección "Estructura del contexto generado".
5. Guardar el archivo en `E:\University_vault_2026\` usando Filesystem, o en la carpeta que el usuario indique.

---

## ENTREVISTA — PREGUNTAS PARA RECOPILAR INFORMACIÓN

Claude debe hacer estas preguntas al usuario antes de generar el contexto. Adaptarlas según las respuestas anteriores.

### Bloque 1 — Identificación de la materia

1. ¿Cuál es el nombre completo de la materia y su código (si tiene)?
2. ¿En qué semestre o parcial estás actualmente?
3. ¿Cuál es el tema o unidad principal que necesitas trabajar ahora?

### Bloque 2 — Archivos disponibles

4. ¿Tienes un formulario o resumen de fórmulas para esta materia? ¿Cómo se llama el archivo?
5. ¿Tienes ejercicios resueltos por el docente que sirvan de referencia?
6. ¿Cómo se llaman (o se llamarán) los archivos de ejercicios que voy a revisar? ¿Tienen algún patrón de nombre?
7. ¿Hay algún otro archivo de referencia importante (tablas, apuntes, enunciados)?

### Bloque 3 — Naturaleza del trabajo

8. ¿Qué tipo de ejercicios son los más comunes? (cálculo, demostraciones, problemas aplicados, código, etc.)
9. ¿Qué piden típicamente los incisos? (por ejemplo: hallar algo, verificar algo, graficar, demostrar)
10. ¿Hay algún método o procedimiento que el docente exija específicamente? ¿O libertad de método?
11. ¿Usas Desmos u otra herramienta de graficación en las notas?

### Bloque 4 — Errores y patrones

12. ¿Cuáles son los errores más comunes que has visto en las resoluciones? (si ya tienes experiencia con la materia)
13. ¿Hay algún tema o tipo de problema donde quieras que Claude sea especialmente cuidadoso?

---

## ESTRUCTURA DEL CONTEXTO GENERADO

El archivo generado debe seguir esta estructura. Claude la llena con la información recogida en la entrevista.

---

```markdown
# CONTEXTO DE TRABAJO — [NOMBRE DE LA MATERIA] ([CÓDIGO])

## INSTRUCCIÓN INMEDIATA — LEER AL CARGAR ESTE ARCHIVO

Cuando el usuario comparta este archivo, Claude debe hacer lo siguiente antes de responder cualquier otra cosa:

1. Leer el archivo [FORMULARIO O ARCHIVO PRINCIPAL] completo.
2. [Leer `E:\University_vault_2026\_app\_appnotes\desmos_guide.md` sección Claude si la materia usa gráficas Desmos.]
3. Confirmar al usuario con un mensaje breve: "Contexto cargado. Listo para revisar ejercicios."

> Si en el futuro hay un formulario actualizado u otro archivo indicado por el usuario, leerlo en lugar del anterior o además de él.

---

## PROPÓSITO DE ESTE DOCUMENTO

[Descripción breve de para qué sirve este contexto: qué materia cubre, qué tipo de trabajo se hace, en qué parcial o unidad está enfocado actualmente.]

---

## ARCHIVOS DEL SISTEMA

| Archivo | Ubicación | Rol |
|---------|-----------|-----|
| [nombre del formulario] | [ruta] | Fuente de verdad. Fórmulas y procedimientos válidos del curso. |
| [nombre de ejercicios resueltos] | [ruta] | Referencia de nivel y formato. NO se modifica. |
| [patrón de ejercicios activos] | [ruta] | Ejercicios que Claude revisa y corrige. |
| [otros archivos si aplica] | [ruta] | [rol] |

---

## FLUJO DE TRABAJO

[Claude genera este flujo adaptado a la materia. Debe describir cómo llega un ejercicio, cómo se revisa y cómo se edita el archivo.]

---

## ROL DE CLAUDE AL REVISAR UN EJERCICIO

### 1. Leer el enunciado completo antes de revisar

Identificar:
- [Qué elementos clave tiene un enunciado típico de esta materia]
- [Qué piden los incisos más comunes]
- [Qué datos o condiciones hay que extraer]

### 2. Verificar inciso por inciso contra el formulario/referencia

Para cada inciso revisar:
- Que la fórmula o método aplicado corresponda al formulario.
- Que el desarrollo sea correcto paso a paso.
- Que el resultado final sea correcto.
- [Otros criterios específicos de la materia]

### 3. Actuar según el resultado

Si el método no corresponde al formulario → agregar resolución alternativa:

> [!check] Alternativo — [método] (Formulario)
> [desarrollo]

Si hay errores → agregar corrección:

> [!correction] Corrección
> **Error identificado:** ...
> **Corrección:** ...
> **Resultado correcto:** ...

Si está correcto:

> [!check] Correcto
> Procedimiento y resultado verificados con el formulario.

### 4. Nunca borrar contenido original

Claude solo agrega bloques debajo de cada inciso. Nunca modifica ni borra el texto original.

---

## CÓMO APLICAR EL FORMULARIO — GUÍA GENERAL

[Esta es la sección más importante. Claude la genera basándose en el formulario leído y en las respuestas de la entrevista. Debe describir, de forma genérica y aplicable a cualquier ejercicio nuevo de la materia, cómo usar cada fórmula o procedimiento del formulario. NO debe ser una lista de ejercicios específicos — debe ser una guía de pasos que funcione para ejercicios que aún no existen.]

Estructura sugerida por tema del formulario:

### [Tema 1 del formulario]
- Fórmula clave
- Cuándo se aplica
- Procedimiento paso a paso
- Alertas o casos especiales

### [Tema 2 del formulario]
- ...

[Repetir para cada tema relevante del formulario]

---

## ERRORES COMUNES A VIGILAR

[Claude genera esta lista basándose en las respuestas de la entrevista y en el contenido del formulario. Debe ser específica para la materia, no genérica.]

- [Error 1] — [descripción y por qué ocurre]
- [Error 2] — ...

---

## MANEJO DE GRÁFICAS O HERRAMIENTAS VISUALES

[Solo incluir esta sección si la materia usa Desmos u otra herramienta visual.]

### Cuándo incluir gráfica
[Criterios específicos para esta materia]

### Reglas de sintaxis
[Si usa Desmos, incluir las reglas del contexto806. Si usa otra herramienta, describir su sintaxis.]

---

## INSTRUCCIONES DE FLUJO CON EL USUARIO

1. Editar siempre directamente en el `.md` del vault usando Filesystem.
2. Resumen por chat: una línea por inciso (correcto / corregido / alternativo agregado).
3. Sin detalles matemáticos en el chat — todo va en el archivo.
4. Mantener el chat mínimo.
```

---

## NOTAS PARA CLAUDE AL GENERAR EL CONTEXTO

Estas son reglas que Claude debe seguir al construir el archivo generado:

- **La sección "Cómo aplicar el formulario" es la más crítica.** Debe ser completamente genérica — útil para ejercicios que aún no existen. Si el formulario no fue compartido todavía, dejar esa sección como placeholder claro y pedir al usuario que lo comparta antes de completarla.

- **No hacer análisis de ejercicios específicos.** El contexto no debe contener tablas o resúmenes de ejercicios particulares (E1, E2...). Eso era un error del diseño anterior. El contexto debe servir para cualquier ejercicio futuro.

- **Adaptar el lenguaje al tipo de materia.** Una materia de cálculo, una de programación y una de física requieren secciones distintas. No usar siempre la misma estructura rígida.

- **Si la materia no usa Desmos**, eliminar esa sección completamente.

- **Si el formulario está disponible**, leerlo durante la entrevista y usarlo para completar la sección "Cómo aplicar el formulario" con los procedimientos reales, no con placeholders.

- **El nombre del archivo generado** debe seguir el patrón: `contexto_[CODIGO-MATERIA].md` o `contexto_[NOMBRE-CORTO].md` según lo que el usuario prefiera.

%%
galaxy-links
[[_claude-boot]]
[[_galaxy-system]]
[[_note-system]]
[[_ToDo-system]]
%%
