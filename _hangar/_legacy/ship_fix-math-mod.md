---
galaxy_body: ship
project: "fix-math mod — soporte doble backslash + salto de linea"
date: 2026-08-13
status: delivered
fleet: tools / obsidian
---

## Handoff

**Ultima sesion:** 2026-08-13
**Retomar desde:** no aplica — entregado
**Completado esta sesion:** modificacion de main.js, documentacion en _legacy
**Proximo paso:** ninguno — plugin funcional en PC y tablet
**Preguntas de cierre:** ninguna

---

## Resumen y objetivo

Modificar el plugin `Fix Math for Obsidian` (v1.0.33) para que funcione correctamente con el texto copiado desde la app de NotebookLM en Android/tablet, que entrega delimitadores LaTeX con doble backslash (`\\(` y `\\[`) en lugar del simple que espera Obsidian. Adicionalmente, se ajusto el formato de salida de ecuaciones centradas para incluir salto de linea antes y despues del bloque `$$`.

---

## Decisiones

| Fecha | Decision | Motivo |
| ---------- | -------- | ------ |
| 2026-08-13 | Modificar `main.js` directamente en lugar de crear un plugin nuevo | El codigo es simple y localizado — menos overhead |
| 2026-08-13 | Normalizar `\\(` a `\(` como paso previo al flujo original | No altera la logica existente; el flujo original corre intacto despues |
| 2026-08-13 | Agregar salto de linea antes y despues de cada bloque `$$` | Mejor legibilidad en Obsidian; la ecuacion en si no cambia |

> [!note]- Descartadas
> - **Opcion 1 — usar NotebookLM desde Chrome en tablet**: probado, no resolvio el problema del doble backslash.
> - **Opcion 2 — script Python externo de conversion**: valida pero mas compleja; descartada porque la mod directa al plugin es mas limpia y transparente.

---

## Planificacion

El plugin original busca `\(` y `\[` como delimitadores de ecuaciones LaTeX. La app de NotebookLM en Android escapa el backslash al copiar texto, entregando `\\(` y `\\[`. El plugin no los reconoce y reporta "no changes required" aunque haya ecuaciones en el archivo.

Restricciones: no romper el comportamiento en PC (donde el texto llega con `\(` simple), no modificar la logica de deteccion existente.

Enfoque elegido: agregar dos lineas de normalizacion antes de la deteccion, que convierten doble backslash a simple. Si el texto ya viene con simple, las lineas no tienen efecto.

---

## Flujo de pasos

1. Leer `main.js` del plugin instalado en `.obsidian/plugins/fix-math/`
2. Crear backup `main.js.bk` (hecho por el usuario manualmente)
3. Agregar cabecera de version al inicio del archivo
4. Agregar normalizacion de doble backslash antes de `displayBackslashRe`
5. Modificar los 4 puntos de generacion de bloques `$$` para incluir salto de linea
6. Recargar plugin en Obsidian y verificar

---

## Tareas

- [x] Identificar causa del doble backslash (app Android vs navegador)
- [x] Agregar comentario de version en cabecera de `main.js`
- [x] Agregar normalizacion `\\(` a `\(` y `\\[` a `\[`
- [x] Agregar salto de linea antes y despues de bloques `$$`
- [x] Documentar en `_legacy`

---

## Preguntas abiertas

ninguna

---

## Recursos

**Archivo modificado:** `E:\University_vault_2026\.obsidian\plugins\fix-math\main.js`
**Backup:** `E:\University_vault_2026\.obsidian\plugins\fix-math\main.js.bk`
**Plugin original:** https://github.com/loglux/fix-math-for-obsidian (v1.0.33)

### Cambios aplicados al main.js

**1 — Cabecera de version** (linea 2):

```js
// =============================================================================
// Fix Math for Obsidian — v1.0.33 (mod alx-rul)
// Modificacion: normaliza doble backslash (\\( y \\[) antes de procesar,
// para compatibilidad con NotebookLM app Android que entrega ecuaciones
// con delimitadores escapados. El flujo original no se altera.
// =============================================================================
```

**2 — Normalizacion de doble backslash** (antes de `displayBackslashRe`):

```js
text = text.replace(/\\\\\[/g, "\\[").replace(/\\\\\]/g, "\\]");
text = text.replace(/\\\\\(/g, "\\(").replace(/\\\\\)/g, "\\)");
```

**3 — Salto de linea en bloques `$$`** (4 puntos modificados):

Todos los lugares donde se generaba `$$\n{inner}\n$$` fueron cambiados a `\n$$\n{inner}\n$$\n`, agregando linea vacia al inicio y al final del bloque.
