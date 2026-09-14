---
galaxy_body: blueprint
status: evaluando
priority: alta
date: 2026-09-13
---

# Ideas — Robotic Arm AI

> **Relación:** Decisiones de diseño, expansiones y alternativas aún no resueltas del brazo robótico ETN607 — hardware, control, visión e integración IA.

---

## Hardware

- [x] Mould King Digger vs LEGO Mindstorms → decidido: Digger
- [x] ESP32 como controlador principal → confirmado
- [x] Comunicación WiFi vs Serial USB → decidido: Serial USB
- [ ] EV3 para futuros proyectos — motores con encoder para control de posición preciso (PID)
- [ ] Level shifter BSS138 4ch (Bs 9 c/u en Sawers) — necesario si se usan encoders EV3
- [ ] ¿Cuántos motores necesitan encoder? — evaluar cuáles articulaciones requieren posición exacta
- [ ] Garra 3 dedos vs pinza 2 dedos — pendiente definir mecanismo final con piezas disponibles
- [ ] FPGA Cyclone 5 — descartado por ahora, revisar si el docente pide visión en hardware

---

## Control e integración IA

- [x] Stack IA gratuita → Gemini (Google AI Studio) o Groq
- [x] Sistema de skills con README como system prompt → confirmado
- [x] JSON por Serial como protocolo de comando → confirmado
- [ ] ¿Cuántas skills para el MVP? — mínimo: saludo + trabajo (origen→destino)
- [ ] Formato exacto del skill README — definir estructura y campos obligatorios
- [ ] Servidor Python intermediario — diseñar flujo completo chat → API → Serial → ESP32
- [ ] ¿Agregar skill de posición home/reset? — útil para demo y recuperación de errores
- [ ] Control por voz como alternativa al chat — factible con Whisper (gratis, local)

---

## Visión (fase 2)

- [ ] Cámara web USB en PC + Gemini Vision — detecta objeto y calcula posición automáticamente
- [ ] ¿Qué tipo de objeto para la demo? — definir objeto estándar (cubo, pelota, bloque LEGO)
- [ ] Gemini Robotics ER — modelo específico para robótica con razonamiento espacial, evaluar si el tier gratuito lo incluye
- [ ] ESP32-CAM como alternativa — requeriría mantener WiFi solo para cámara
- [ ] Calibración de coordenadas — mapear posición reloj (1–12) a ángulos reales de motores

---

## Proyecto universitario

- [ ] Consultar al docente requisitos específicos de entrega — puede cambiar prioridades
- [ ] ¿Se necesita documentación formal? — informe, diagrama de bloques, video demo
- [ ] Presupuesto final confirmado — Digger + 2 sets + ESP32 + drivers + level shifters ≈ 2700 Bs
- [ ] Fecha de entrega — definir para trabajar hacia atrás con hitos

---

## A depurar

- OTA firmware update — descartado por lentitud (30-60 seg), reemplazado por JSON Serial
- WiFi en ESP32 — descartado para comunicación principal, podría volver si se agrega cámara
- LEGO Mindstorms como plataforma principal — descartado por costo y complejidad ESP32
