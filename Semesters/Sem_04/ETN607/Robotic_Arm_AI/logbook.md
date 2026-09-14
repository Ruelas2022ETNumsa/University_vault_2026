---
galaxy_body: logbook
scope: robotic-arm-ai
status: on-track
date_updated: 2026-09-13
---

## Visión general

Brazo robótico construido con piezas Mould King Digger (compatible Technic), controlado por ESP32 vía Serial USB, con integración de IA gratuita (Gemini/Groq) como capa de interpretación de comandos en lenguaje natural. El sistema ejecuta skills predefinidas (saludo, trabajo de agarre) enviando JSON por Serial desde un servidor Python en PC. Proyecto académico para ETN607, Semestre 4.

El criterio de éxito es: el brazo ejecuta al menos 2 skills funcionales controladas por lenguaje natural desde chat, sin costos de software, con un retraso total menor a 5 segundos.

---

## Estado actual

**Salud:** on-track
**Resumen:** fase de diseño y decisiones técnicas completada. Hardware seleccionado, stack definido, arquitectura acordada.
**Último avance:** selección completa de hardware y stack técnico en sesión inicial 2026-09-13.
**Próximo hito:** diseño de garra 3 dedos + esquema de conexión electrónica.

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | :--: | :----: | ----------- |
| `logbook.md` | logbook | — | este archivo — README histórico del proyecto |
| `tsk_carrier.md` | tsk | — | archivo de trabajo activo por sesión |
| `chronicle.md` | chronicle | — | registro cronológico de sesiones y pruebas |
| `robarm-config.md` | dropship | activo | configuración general de hardware y stack |
| `robarm-opc_A-arquitectura.md` | dropship | activo | arquitectura software ESP32 + IA |
| `robarm-opc_B-garra.md` | dropship | activo | diseño de garra 3 dedos con piezas Technic |

---

## Hitos

- 2026-09-13 — Decisión de hardware: Mould King Digger + 2 sets simples + ESP32
- 2026-09-13 — Stack técnico definido: Serial USB + Gemini/Groq gratis + Python intermediario
- 2026-09-13 — Sistema de skills con README como system prompt acordado

---

## Riesgos y dependencias

- Las piezas del Digger pueden no ser suficientes para garra 3 dedos → mitigado con 2 sets simples adicionales
- Gemini/Groq API tier gratuito tiene límites de requests por minuto → aceptable para demo universitaria
- El docente podría pedir requisitos específicos no contemplados → pendiente consultar
- Cámara web (Gemini Vision) no incluida en MVP → fase 2 si el tiempo lo permite

---

## Decisiones clave

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-09-13 | Mould King Digger sobre LEGO Mindstorms | 500 Bs menos, 6 motores, integración ESP32 más simple |
| 2026-09-13 | ESP32 como controlador | WiFi nativo, precio (~80 Bs), potencia suficiente |
| 2026-09-13 | Serial USB en lugar de WiFi | Menor latencia, más confiable en demo, sin dependencia de red |
| 2026-09-13 | Gemini/Groq API gratuita | Cero costo de software, tier gratuito suficiente para el proyecto |
| 2026-09-13 | Skills como JSON predefinido | Elimina OTA (lento), respuesta en 2-5 seg, más confiable |
| 2026-09-13 | FPGA Cyclone 5 descartado por ahora | Overkill para el alcance actual, agrega complejidad innecesaria |
| 2026-09-13 | Garra 3 dedos en lugar de pala original | Requisito funcional del brazo robótico |

> [!note]- Descartadas
> - WiFi en ESP32 — descartado por latencia y dependencia de red en demo
> - OTA firmware update — descartado por tiempo (30-60 seg) vs JSON Serial (ms)
> - LEGO Mindstorms — descartado por costo y complejidad de integración ESP32
