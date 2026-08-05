---
galaxy_body: ship
project: "TABnote — Plantilla de apuntes tablet"
date: 2026-08-03
status: in-orbit
fleet: sistema-movil
blocked_by:
---

> [!warning] alx_gml — Sesión incompleta
> Diseño TABnote en curso. Preguntas abiertas sin responder. Retomar a las **23:03**.

## Handoff

**Última sesión:** 2026-08-03 18:03 → pausa por tokens a las 21:00 aprox
**Retomar desde:** Sección "Preguntas abiertas" — responder antes de continuar
**Completado esta sesión:** Diseño visual de la plantilla TABnote v4, catálogo de callouts, sugerencias de mejora, convenciones de imagen
**Próximo paso:** Responder preguntas abiertas → documentar plantilla final → crear prompt de transcripción para NotebookLM

---

## Resumen y objetivo

Diseñar una plantilla estándar para tomar apuntes en Samsung Notes (tablet S6 Lite, S Pen) que permita a NotebookLM extraer y transcribir el contenido sin fricción, enriquecido con fuentes. La plantilla debe ser adoptable en clase sin interrumpir el ritmo de escritura.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-03 | Un solo color para apuntes: #005F73 | Consistencia y legibilidad OCR |
| 2026-08-03 | Título centrado con resaltado simétrico a ambos lados | Así ya lo usa el usuario — confirmado con PDF real |
| 2026-08-03 | Subtítulo: texto + resaltado mismo color hasta borde derecho | Señal visual clara para NLM independiente del color usado |
| 2026-08-03 | Callout = caja cerrada 4 lados, cualquier color | Todos se transcriben como [!note]- note-tab |
| 2026-08-03 | Imagen = subtítulo en gris + área vacía | Señal para NLM de omitir, screenshot va directo al vault |
| 2026-08-03 | Encabezado simple: una línea `MAT101 · T01 · fecha` | Sin caja grande, solo referencia mínima |
| 2026-08-03 | Numeración de subtítulos (1. 2. 3.) | Ancla de orden para NLM |
| 2026-08-03 | Renglón en blanco entre subtítulos | NLM corta bloques sin mezclar temas |
| 2026-08-03 | `>` dentro del callout como señal de título | Facilita transcripción: `> titulo` + desarrollo |

> [!note]- Descartadas
> Cornell de 2 columnas — el usuario casi nunca la usa, se descartó como plantilla base. El resaltado horizontal es suficiente separador visual sin columnas.

---

## Planificación

Flujo final del sistema:
1. Apuntes en Samsung Notes (S Pen, plantilla TABnote)
2. Export a PDF vía Samsung Account sync → Samsung Notes PC
3. PDF sube a NotebookLM como fuente
4. Prompt de transcripción solicita subtítulo específico → NLM entrega supernova enriquecida con fuentes

Restricciones:
- Debe funcionar en clase sin interrumpir escritura
- Fórmulas siempre a mano (ya probado que NLM las extrae bien)
- Imágenes se omiten en transcripción — screenshot va al vault manualmente
- Sin Cornell: plantilla lineal simple con jerarquía por color + resaltado

---

## Sugerencias

- Documentación web confirma que layouts con etiquetas claras y separación visual por zonas producen mejores resultados en extracción con IA
- El S Pen (digitalizador activo) mejora precisión de reconocimiento vs stylus pasivo
- Espaciado consistente y tamaño de letra uniforme son los factores más importantes para OCR en manuscrito
- Separación visual entre bloques (renglón vacío) es crítica para que NLM no mezcle contenido de subtítulos distintos

---

## Flujo de pasos

1. [x] Relevar sistema actual del usuario (colores, export, flujo NLM)
2. [x] Definir jerarquía visual: título / subtítulo / apunte / énfasis
3. [x] Definir convención de callouts (caja + > título)
4. [x] Definir convención de imágenes (subtítulo gris + área vacía)
5. [x] Crear catálogo de tipos de callout para ingeniería electrónica
6. [x] Diseñar plantilla visual v4 con todas las convenciones
7. [ ] Responder preguntas abiertas
8. [ ] Documentar plantilla final como archivo de referencia en el vault
9. [ ] El usuario prueba la plantilla en clase real
10. [ ] Ajustes post-prueba
11. [ ] Crear prompt de transcripción para NLM (basado en MAT101-transcription.md adaptado a tablet)

---

## Tareas

- [x] Leer archivos de configuración del sistema
- [x] Diseño plantilla v1, v2, v3, v4
- [x] Catálogo de callouts universitarios — ingeniería electrónica
- [x] Sugerencias de mejora de apuntes
- [ ] Responder preguntas abiertas (ver sección)
- [ ] Archivo de referencia final `_TABnote-ref.md` en vault
- [ ] Prueba real en clase
- [ ] Prompt NLM para tablet

---

## Preguntas abiertas

*(Responder estas antes de continuar — son lo primero al retomar)*

1. Los callouts tienen título con `> titulo`. ¿El título lo escribís a mano libre según el momento, o preferís usar siempre uno del catálogo definido (Definición, Fórmula clave, Para el parcial, etc.)?

2. Las sugerencias de mejora (unidades en `[V]`, flecha de referencia cruzada `→ ver T02`, síntesis con `∴`, marca de estado `✓/?` al margen) — ¿cuál ves más adoptable para implementar primero en clase?

3. ¿El encabezado `MAT101 · T01 · fecha` va escrito a mano al inicio de cada nota, o preferís que sea parte de la plantilla preconfigurada en Samsung Notes (texto fijo que borrás/editás)?

4. ¿Querés que la plantilla final se documente como archivo `.md` de referencia en el vault, o alcanza con este tsk como documentación?

---

## Recursos

- `E:\University_vault_2026\_app\_config\_notebooklm-system.md`
- `E:\University_vault_2026\_app\_config\_TAB_note-system.md`
- `E:\University_vault_2026\_app\_config\_note-system.md`
- `E:\University_vault_2026\_app\_appnotes\cornell_guide.md`
- `E:\University_vault_2026\_app\notebooklm\prompts\MAT101\MAT101-transcription.md` ← base para el futuro prompt tablet
- Plantilla visual: diseñada en sesión (TABnote v1→v4), pendiente exportar como referencia
