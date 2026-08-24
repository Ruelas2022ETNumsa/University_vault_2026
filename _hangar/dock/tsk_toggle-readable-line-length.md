---
galaxy_body: ship
project: "toggle-readable-line-length"
date: 2026-08-24
status: docked
fleet: _app
blocked_by:
---

## Handoff

**Última sesión:** 2026-08-24
**Retomar desde:** sección Planificación
**Completado esta sesión:** idea definida, plugins elegidos, limitación móvil identificada
**Próximo paso:** implementar script en Shell Commands + botón en Commander
**Preguntas de cierre:** —

---

## Resumen y objetivo

Crear un botón accesible (ribbon o toolbar vía Commander) que haga toggle de la opción **Readable Line Length** de Obsidian. Necesario porque Marginalia requiere línea ancha (OFF) y el resto del vault funciona mejor con línea legible (ON).

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-08-24 | Shell Commands + Commander | Shell Commands permite ejecutar scripts externos; Commander expone el comando como botón en ribbon/toolbar sin tecla de atajo |
| 2026-08-24 | Descartar Templater y QuickAdd | Shell Commands es más limpio para un toggle de config sin crear archivos de nota intermedios |

> [!note]- Descartadas
> Templater y QuickAdd considerados — funcionan, pero crean ruido (archivos `.md` de script o macros en config). Shell Commands encapsula el script fuera del vault.

---

## Planificación

Usar **Shell Commands** para ejecutar un script que lea y modifique `app.json` (donde Obsidian persiste `readableLineLength`) y luego refresque la vista. Commander crea el botón de acceso rápido que dispara el comando registrado en Shell Commands.

Restricciones:
- Sin dependencias externas pagas
- Debe funcionar en Windows (vault en `E:\`)
- El script puede ser Python o PowerShell

---

## Limitación móvil

**Shell Commands no funciona en Obsidian móvil (iOS / Android).** El plugin depende del sistema operativo del host para ejecutar comandos de shell — en móvil no hay acceso a shell. El botón de Commander aparece en el ribbon pero al presionarlo no ocurre nada o da error silencioso.

Alternativa móvil si se necesita en el futuro: reemplazar Shell Commands por un plugin que use la API interna de Obsidian (como QuickAdd Macro o un plugin custom), que sí corre en móvil. Quedará como blueprint separado si se decide avanzar.

---

## Flujo de pasos

1. Instalar Shell Commands si no está instalado
2. Escribir script (Python o PowerShell) que lea `readableLineLength` de `.obsidian/app.json`, invierta el valor y lo escriba de vuelta
3. Registrar el script como comando en Shell Commands
4. Abrir Commander → agregar el comando al ribbon o toolbar con ícono descriptivo
5. Probar toggle desde el botón

---

## Tareas

- [ ] Escribir script toggle (Python o PowerShell)
- [ ] Registrar en Shell Commands
- [ ] Crear botón en Commander
- [ ] Probar en desktop

---

## Recursos

- Plugin: Shell Commands (`obsidian-shellcommands`)
- Plugin: Commander (`cmdr`)
- Archivo a modificar: `E:\University_vault_2026\.obsidian\app.json` → campo `readableLineLength`
- API interna alternativa (móvil): `app.vault.setConfig('readableLineLength', bool)` + `app.workspace.updateOptions()`
