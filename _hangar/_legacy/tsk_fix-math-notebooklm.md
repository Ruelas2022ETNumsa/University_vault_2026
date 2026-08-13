---
galaxy_body: ship
project: "fix-math-for-obsidian — integración NotebookLM"
date: 2026-08-12
status: delivered
fleet: herramientas-vault
---

## Handoff

**Última sesión:** 2026-08-12
**Retomar desde:** —
**Completado esta sesión:** Investigación del problema, evaluación de soluciones, instalación y configuración del plugin.
**Próximo paso:** — (delivered, no requiere acción)
**Preguntas de cierre:** —

---

## Resumen y objetivo

Resolver el problema de incompatibilidad de notación LaTeX al copiar respuestas de NotebookLM (NBLM) a notas `.md` en Obsidian. NBLM entrega fórmulas con delimitadores `\(...\)` y `\[...\]`; Obsidian requiere `$...$` y `$$...$$`. El objetivo era encontrar e instalar una solución que automatice la conversión sin fricción.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-12 | Usar plugin **fix-math-for-obsidian** (instalación manual) | Solución liviana, de un solo comando, sin dependencias externas. No está en el marketplace oficial pero es open source y activo. |
| 2026-08-12 | Desactivar "Convert HTML content to Markdown on paste" en Obsidian | Preserva la estructura original del contenido pegado desde NBLM; el plugin lo convierte limpiamente después. |
| 2026-08-12 | No usar instrucción de prompt en NBLM para forzar `$$` | Inconsistente en respuestas largas; el plugin es más confiable. |

> [!note]- Descartadas
> - **Instrucción de chat en NBLM**: pedirle a Gemini que use `$$` directamente. Funciona a veces pero no es confiable — vuelve a la notación LaTeX estándar en respuestas largas.
> - **Extensión Chrome "NotebookLM to LaTeX & MD"**: válida, pero agrega fricción (extensión de browser + paso extra de descarga). El plugin de Obsidian es más directo para el flujo de trabajo.

---

## Planificación

El problema raíz es que NBLM usa la notación LaTeX estándar (`\[...\]`, `\(...\)`) mientras Obsidian usa notación Markdown/MathJax (`$$...$$`, `$...$`). No existe configuración en NBLM para cambiar esto.

La solución elegida opera del lado de Obsidian: un plugin que detecta y convierte los delimitadores en el archivo activo, con soporte para selección parcial. No requiere conexión a internet, no modifica código blocks, y es seguro de ejecutar múltiples veces.

Restricciones consideradas: gratuito, sin dependencias de servicios externos, compatible con el vault actual.

---

## Flujo de pasos

1. Copiar la respuesta de NBLM usando el **botón Copy** de la interfaz (no selección manual de texto — preserva mejor los delimitadores).
2. Pegar en la nota `.md` de Obsidian.
3. *(Opcional)* Seleccionar solo el bloque pegado si no se quiere procesar toda la nota.
4. Ejecutar el comando con el hotkey asignado → las fórmulas quedan en formato Obsidian.

---

## Tareas

- [x] Investigar si NBLM tiene configuración de formato LaTeX → No existe.
- [x] Evaluar soluciones disponibles (plugin, extensión Chrome, prompt engineering).
- [x] Descargar `manifest.json` y `main.js` del repo.
- [x] Crear carpeta `.obsidian/plugins/fix-math/` en el vault.
- [x] Copiar los archivos al plugin folder.
- [x] Reiniciar Obsidian y activar el plugin en Settings → Community plugins.
- [x] Desactivar "Convert HTML content to Markdown on paste" en Settings → Editor.
- [x] Asignar hotkey en Settings → Hotkeys → "Fix math (current file)".
- [x] Verificar funcionamiento con fórmula de prueba pegada desde NBLM.

---

## Preguntas abiertas

—

---

## Recursos

**Plugin:**
- Repo: https://github.com/loglux/fix-math-for-obsidian
- Archivos necesarios: `manifest.json` + `main.js` (desde Releases)
- Carpeta destino: `.obsidian/plugins/fix-math/`

**Configuración de Obsidian:**
- Settings → Editor → desactivar **"Convert HTML content to Markdown on paste"**
- Settings → Hotkeys → buscar **"Fix math (current file)"** → asignar atajo

**Conversiones que realiza el plugin:**

| Input (NBLM / AI) | Output (Obsidian) |
| --- | --- |
| `\( ... \)` | `$ ... $` (inline) |
| `\[ ... \]` | `$$ ... $$` (display) |
| `( x=y )` con contenido matemático | `$ x=y $` (detección inteligente) |
| Bloques entre comillas `> \[...\]` | `> $$ ... $$` |
| Code blocks ` ``` ``` ` | sin cambios |
