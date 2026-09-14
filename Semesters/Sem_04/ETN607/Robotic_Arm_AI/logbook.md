---
galaxy_body: logbook
scope: robotic-arm-ai
status: on-track
date_updated: 2026-09-13
---

## Visión general

Brazo robótico construido sobre LEGO Mindstorms EV3 Education Core Set (45544) + Expansion Set (45560), controlado por el EV3 Brick vía cable USB, con integración de IA (Claude como orquestador + Gemini Flash como delegado de traducción rápida) como capa de interpretación de comandos en lenguaje natural. El sistema ejecuta skills predefinidas enviando JSON por Serial USB desde un servidor Python en PC. Proyecto académico para ETN607, Semestre 4.

Punto de partida de construcción: Robot Arm H25 (modelo oficial del Core Set 45544), que usa 3 motores EV3 con encoder para base, codo y garra mediante mecanismos Technic. La expansión 45560 provee piezas estructurales adicionales para escalar el diseño.

El criterio de éxito es: el brazo ejecuta al menos 2 skills funcionales controladas por lenguaje natural desde chat, con posición reproducible gracias a los encoders EV3, sin costos de software, con un retraso total menor a 5 segundos.

---

## Estado actual

**Salud:** on-track
**Resumen:** hardware definitivo seleccionado tras reanálisis completo en sesión 2. Decisión revertida del Digger al EV3+expansión por razones técnicas de precisión y disponibilidad de componentes en Bolivia.
**Último avance:** decisión de hardware cerrada, arquitectura de IA definida, stack técnico confirmado — 2026-09-13.
**Próximo hito:** construir Robot Arm H25 base + planificar extensión con piezas de expansión.

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `tsk_carrier.md` | tsk | — | archivo de trabajo activo por sesión |
| `chronicle.md` | chronicle | — | registro cronológico de sesiones y pruebas |
| `robarm-config.md` | dropship | activo | configuración general de hardware y stack |
| `robarm-opc_A-arquitectura.md` | dropship | activo | arquitectura software EV3 + IA |
| `robarm-opc_B-garra.md` | dropship | activo | diseño de garra con piezas Technic del H25 |
| `blueprint.md` | blueprint | evaluando | ideas y decisiones pendientes del proyecto |

---

## Hitos

- 2026-09-13 — Sesión 1: Decisión inicial de hardware: Mould King Digger + ESP32 (luego revertida)
- 2026-09-13 — Sesión 2: Reanálisis completo — decisión revertida a EV3 Core 45544 + Expansion 45560
- 2026-09-13 — Stack técnico definitivo: USB cable + Python + Claude/Gemini + JSON → EV3 Brick
- 2026-09-13 — Punto de partida de construcción: Robot Arm H25 oficial del Core Set

---

## Riesgos y dependencias

- EV3 + expansión encontrados en tienda Facebook — no en tiendas físicas; verificar disponibilidad antes de comprar
- El docente podría pedir requisitos específicos no contemplados → pendiente consultar
- Cámara web (visión IA) no incluida en MVP → fase 2, viable sin cambios de hardware
- Motores EV3 adicionales difíciles de conseguir en Bolivia → no necesarios, H25 usa 3 motores del Core Set

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-09-13 | **EV3 Core 45544 + Expansion 45560** sobre Mould King Digger | Ver nota de decisión abajo |
| 2026-09-13 | USB cable (no WiFi) como canal de comunicación | Menor latencia, confiable en demo, sin dependencia de red |
| 2026-09-13 | Claude como orquestador + Gemini Flash como delegado | Claude free para razonamiento y visión; Gemini para traducción rápida a JSON |
| 2026-09-13 | Robot Arm H25 como base de construcción | Modelo oficial del Core Set, usa 3 motores EV3, código MicroPython ya existente |
| 2026-09-13 | Muñeca como mecanismo pasivo (no motor extra) | El H25 demuestra que la muñeca se controla por biela/rack desde el codo — ahorra 1 motor |
| 2026-09-13 | FPGA Cyclone 5 descartado | Overkill para el alcance actual |

> [!note]- Por qué EV3+expansión y no el Digger
> El Digger fue la decisión inicial (sesión 1) basada en precio (Bs 1800 vs 3000) y cantidad de motores (6 vs 3). Sin embargo, el reanálisis en sesión 2 reveló el problema central: los motores PF del Digger son DC sin encoder — el ESP32 controla por tiempo ("girar 500ms") sin saber la posición real del brazo. Esto hace que las skills sean no reproducibles y la integración con visión IA sea inviable sin agregar encoders externos por articulación (mayor costo + complejidad de montaje en Technic + firmware adicional).
>
> El EV3 resuelve esto de forma nativa: cada servomotor tiene encoder integrado, Python lee `motor.position` en grados reales, y el control es determinista. Además, el Robot Arm H25 demuestra que 3 motores son suficientes para un brazo funcional de 3 GDL + garra, porque la muñeca se implementa como mecanismo pasivo. El EV3 Brick tiene USB nativo con protocolo abierto, compatible con ev3dev y MicroPython. No se necesitan drivers L298N, level shifters, ni ESP32. La expansión 45560 aporta 853 piezas estructurales (engranajes, plataforma giratoria, beams) sin motores adicionales — suficiente para escalar el H25.
>
> En Bolivia, conseguir motores EV3 individuales o encoders externos es igual de difícil. La ventaja del EV3 es que todo lo necesario viene en los dos sets que ya están disponibles en una sola compra.

> [!note]- Descartadas
> - Mould King Digger — descartado por motores sin encoder (precisión no reproducible sin hardware adicional)
> - ESP32 como controlador principal — descartado (reemplazado por EV3 Brick que ya tiene USB + compute)
> - WiFi — descartado, USB cable es suficiente y más confiable
> - Drivers L298N — no necesarios con EV3
> - Level shifters BSS138 — no necesarios con EV3
> - FPGA Cyclone 5 — descartado por complejidad innecesaria
