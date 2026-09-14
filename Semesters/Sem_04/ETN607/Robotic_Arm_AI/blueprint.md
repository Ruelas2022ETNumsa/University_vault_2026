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

- [x] Mould King Digger vs LEGO Mindstorms → **decidido: EV3 Core 45544 + Expansion 45560**
- [x] Comunicación WiFi vs USB cable → **decidido: USB cable**
- [x] ESP32 como controlador → **descartado: EV3 Brick cubre todo sin ESP32**
- [x] Punto de partida de construcción → **Robot Arm H25 (oficial Core Set)**
- [x] Muñeca como mecanismo pasivo (sin motor extra) → **confirmado**
- [ ] ¿Extender el H25 con piezas de la expansión 45560? — evaluar largo del brazo y alcance
- [ ] ¿Plataforma giratoria del 45560 para la base? — puede reemplazar el mecanismo de engranajes del H25
- [ ] Garra: ¿mantener pinza 2 lados del H25 o construir garra 3 dedos con piezas del 45560?
- [ ] ¿Cuántos motores necesita el diseño final? — el H25 usa 3, verificar si alcanza para el alcance deseado

---

## Control e integración IA

- [x] Orquestador IA → **Claude (claude.ai free)**
- [x] Delegado traducción JSON → **Gemini Flash (Google AI Studio, tier gratuito)**
- [x] Protocolo de comando → **JSON por USB Serial**
- [x] Sistema de skills con README como system prompt → **confirmado**
- [ ] ¿Cuántas skills para el MVP? — mínimo: saludo + trabajo (origen→destino)
- [ ] Formato exacto del skill README — definir estructura y campos obligatorios
- [ ] Servidor Python intermediario — diseñar flujo completo chat → API → USB → EV3
- [ ] ¿Agregar skill de posición home/reset? — útil para demo y recuperación de errores
- [ ] Control por voz como alternativa al chat — factible con Whisper (gratis, local)
- [ ] ¿Claude delega a Gemini solo la traducción JSON o también el razonamiento de ruta?

---

## Visión (fase 2)

- [ ] Cámara web USB en PC + Claude Vision o Gemini Vision — detecta objeto y calcula posición
- [ ] ¿Qué tipo de objeto para la demo? — definir objeto estándar (cubo, pelota, bloque LEGO)
- [ ] Calibración de coordenadas — mapear posición reloj (1–12) a ángulos reales de motores EV3
- [ ] Con encoders EV3, la calibración coordenada→ángulo es directa y reproducible — ventaja clave vs Digger
- [ ] ¿Qué tipo de objeto para la demo? — definir algo que el Color Sensor del Core Set pueda detectar también

---

## Proyecto universitario

- [ ] Consultar al docente requisitos específicos de entrega — puede cambiar prioridades
- [ ] ¿Se necesita documentación formal? — informe, diagrama de bloques, video demo
- [ ] Fecha de entrega — definir para trabajar hacia atrás con hitos

---

## A depurar / descartado

- Mould King Digger — descartado: motores DC sin encoder, posición no reproducible
- ESP32 como controlador — descartado: EV3 Brick lo reemplaza completamente
- Drivers L298N — descartado: no necesarios con EV3
- Level shifters BSS138 — descartado: no necesarios con EV3
- WiFi en ESP32 — descartado: USB cable es suficiente y más confiable
- OTA firmware update — descartado por lentitud (30-60 seg)
- FPGA Cyclone 5 — descartado: overkill para el alcance actual
- Groq como API — reemplazado por Gemini Flash (más integrado con el ecosistema Google Vision)
