---
galaxy_body: carrier
project: "Robotic Arm AI — ETN607"
date: 2026-09-13
status: docking
fleet: Sem_04 / ETN607
---

## Handoff

**Última sesión:** 2026-09-13
**Retomar desde:** definición de arquitectura técnica completa — ver `dropship-arquitectura.md`
**Completado esta sesión:**
- Selección de hardware (Mould King Digger + 2 sets simples + ESP32)
- Decisión de comunicación Serial USB (sin WiFi)
- Definición de stack de IA gratuito (Gemini / Groq API)
- Sistema de skills con README como system prompt
- Evaluación de cámara web opcional (Gemini Vision)
- Descarte temporal del FPGA Cyclone 5
- Confirmación de viabilidad de garra 3 dedos con piezas del Digger

**Próximo paso:** definir mecanismo de garra 3 dedos + esquema de conexión ESP32 ↔ motores
**Preguntas de cierre:**
- ¿Agregamos cámara web al MVP o queda como fase 2?
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
