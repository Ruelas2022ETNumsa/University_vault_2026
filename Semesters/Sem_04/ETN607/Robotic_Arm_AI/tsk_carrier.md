---
galaxy_body: carrier
project: "Robotic Arm AI — ETN607"
date: 2026-09-13
status: docking
fleet: Sem_04 / ETN607
---

## Handoff

**Última sesión:** 2026-09-13
**Retomar desde:** diseño de garra 3 dedos + esquema de conexión ESP32 ↔ drivers ↔ motores
**Completado esta sesión:**
- Selección de hardware: Mould King Digger + 2 sets simples + ESP32
- Decisión de comunicación: Serial USB (sin WiFi)
- Stack IA gratuita: Gemini (Google AI Studio) o Groq — tier gratuito, sin tarjeta
- Sistema de skills: README como system prompt + JSON por Serial
- Evaluación de cámara web con Gemini Vision → postergado a fase 2
- FPGA Cyclone 5 descartado por ahora
- Garra 3 dedos: viable con piezas Technic del Digger + sets adicionales
- Análisis técnico de conectores: EV3 (6 pines, encoder integrado) vs PF/Mould King (4 pines, sin encoder)
- EV3 requiere level shifter 4ch BSS138 por motor con encoder — encontrado en Sawers Bs 9 c/u
- Mould King PF: conexión directa C1/C2 al H-bridge, sin level shifter
- LEGO EV3 sigue en evaluación para futuros proyectos por ventaja del encoder

**Próximo paso:** diseñar mecanismo de garra 3 dedos + esquema de conexión ESP32 ↔ L298N ↔ motores
**Preguntas de cierre:**
- ¿Cuántos motores del brazo necesitan encoder (posición precisa)?
- ¿Agregar cámara web al MVP o queda como fase 2?
- ¿El docente tiene requisitos específicos de entrega?

---

## Tareas

- [x] Evaluar Mould King Digger vs LEGO Mindstorms
- [x] Confirmar ESP32 como controlador
- [x] Definir comunicación (Serial USB sin WiFi)
- [x] Seleccionar stack IA gratuito
- [x] Definir sistema de skills con README
- [x] Evaluar viabilidad de garra 3 dedos
- [ ] Diseñar mecanismo de garra 3 dedos con piezas Technic
- [ ] Esquema de conexión ESP32 ↔ drivers L298N ↔ motores
- [ ] Código ESP32: servidor Serial + skills hardcodeados
- [ ] Servidor Python: intermediario IA → Serial
- [ ] Archivo README de skills para system prompt
- [ ] Prueba de integración completa
- [ ] Documentar para entrega universitaria
- [ ] Evaluar cámara web (fase 2)

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | ---- | ------ | ----------- |
| `tsk_carrier.md` | tsk | docking | archivo de trabajo activo |
| `logbook.md` | logbook | on-track | README histórico del proyecto |
| `chronicle.md` | chronicle | — | registro cronológico de sesiones |
| `robarm-config.md` | dropship | activo | configuración general de hardware y stack |
| `robarm-opc_A-arquitectura.md` | dropship | activo | arquitectura software ESP32 + IA |
| `robarm-opc_B-garra.md` | dropship | activo | diseño de garra 3 dedos con piezas Technic |
| `blueprint.md` | blueprint | evaluando | ideas y decisiones pendientes del proyecto |
