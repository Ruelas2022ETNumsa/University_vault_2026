---
galaxy_body: dropship
carrier: "[[_app/Tars/work/tars_conversion/tsk_carrier.md]]"
scope: opcion-B
status: activo
date: 2026-09-04
---

## Proposito

Documentar y probar la Opción B del carrier `tars-hpprgm-conversion` — generar el `.hpprgm` en formato G1 (antiguo), el mismo que usa Xprime. CASE acepta el archivo pero requiere abrir el editor y hacer "Check" una vez para que lo resave al formato moderno.

---

## Contenido

### Concepto

Xprime (editor macOS para HP Prime) genera `.hpprgm` en formato G1 — un formato más simple que el moderno, que CASE acepta con la condición de que el usuario abra el archivo en el editor y ejecute "Check" al menos una vez. Después de ese paso, el archivo queda en formato moderno y corre normalmente.

### Comportamiento esperado

1. Python genera el `.hpprgm` en formato G1 y lo copia a `HP Prime\Calculators\Prime`
2. CASE detecta el archivo
3. Usuario abre el programa en el editor de CASE → ejecuta "Check"
4. CASE resave el archivo al formato moderno
5. El programa corre normalmente

### Formato G1

Formato más simple — el contenido va directamente en UTF-16 LE sin el header named completo del formato moderno. La estructura exacta está en el código fuente de Xprime.

### Referencias

- [Xprime — GitHub](https://github.com/Insoft-UK/Xprime) — implementación de referencia en macOS
- Nota de Xprime: *"The HP Prime will initially accept the file, but it must be resaved by the calculator before it becomes a fully valid modern .hpprgm"*

### Preguntas abiertas

- ¿Cuál es la estructura exacta del header G1 según el código de Xprime?
- ¿El paso "Check" en CASE es suficiente o requiere ejecutar el programa?

### Resultados de prueba

- [ ] Prueba 1 — archivo existente `KMH_CONV.hpprgm`: pendiente
- [ ] Prueba 2 — archivo nuevo nunca cargado en CASE: pendiente

### Veredicto

Pendiente.
