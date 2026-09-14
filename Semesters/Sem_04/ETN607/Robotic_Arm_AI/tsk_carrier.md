---
galaxy_body: carrier
project: "Robotic Arm AI — ETN607"
date: 2026-09-13
status: docking
fleet: Sem_04 / ETN607
---

## Handoff

**Última sesión:** 2026-09-13
**Retomar desde:** construir Robot Arm H25 base + planificar extensión con piezas de expansión 45560
**Completado esta sesión:**
- Reanálisis completo de hardware desde cero (sesión 2)
- Decisión revertida: Mould King Digger → EV3 Core 45544 + Expansion 45560
- Razón central: motores PF del Digger sin encoder → posición no reproducible → skills no deterministas
- EV3 confirmado: encoder nativo por motor, USB nativo, ev3dev + MicroPython, sin hardware extra
- Robot Arm H25 identificado como punto de partida oficial (3 motores: base, codo, garra)
- Muñeca confirmada como mecanismo pasivo (biela/rack) — no requiere motor extra
- Expansión 45560 confirmada: 853 piezas estructurales, sin motores ni sensores
- Stack IA definitivo: Claude (orquestador + visión) + Gemini Flash (traducción rápida a JSON)
- Comunicación: USB cable solamente, sin WiFi
- Fase 2 (cámara web + visión IA): viable sin cambios de hardware, se agrega en Python

**Próximo paso:** construir H25 base → evaluar extensión con piezas 45560 → definir skills MVP
**Preguntas abiertas:**
- ¿El docente tiene requisitos específicos de entrega (informe, video, diagrama)?
- ¿Cuántas skills para el MVP? Mínimo sugerido: saludo + trabajo (origen→destino)
- ¿Agregar cámara web al MVP o queda como fase 2?

---

## Tareas

- [x] Evaluar Mould King Digger vs LEGO Mindstorms EV3
- [x] Reanálisis completo de hardware con criterio de precisión
- [x] Confirmar EV3 Core 45544 + Expansion 45560 como plataforma definitiva
- [x] Definir comunicación (USB cable, sin WiFi)
- [x] Seleccionar stack IA (Claude + Gemini Flash)
- [x] Identificar punto de partida: Robot Arm H25
- [x] Confirmar viabilidad de muñeca pasiva (sin motor extra)
- [ ] Adquirir EV3 Core 45544 + Expansion 45560
- [ ] Construir Robot Arm H25 base
- [ ] Evaluar extensión del H25 con piezas de expansión 45560
- [ ] Definir skills MVP (cantidad y comportamiento)
- [ ] Instalar ev3dev o MicroPython en EV3 Brick
- [ ] Servidor Python: intermediario IA → USB Serial → EV3
- [ ] Archivo README de skills para system prompt de IA
- [ ] Código EV3: recibir JSON por USB + ejecutar skills
- [ ] Prueba de integración completa end-to-end
- [ ] Evaluar cámara web + visión IA (fase 2)
- [ ] Consultar al docente requisitos de entrega
- [ ] Documentar para entrega universitaria

---

## Archivos del carrier

| Archivo | Tipo | Estado | Descripción |
| ------- | ---- | ------ | ----------- |
| `tsk_carrier.md` | tsk | docking | archivo de trabajo activo |
| `logbook.md` | logbook | on-track | README histórico del proyecto |
| `chronicle.md` | chronicle | — | registro cronológico de sesiones |
| `robarm-config.md` | dropship | activo | configuración general de hardware y stack |
| `robarm-opc_A-arquitectura.md` | dropship | activo | arquitectura software EV3 + IA |
| `robarm-opc_B-garra.md` | dropship | activo | diseño de garra con piezas Technic del H25 |
| `blueprint.md` | blueprint | evaluando | ideas y decisiones pendientes del proyecto |
