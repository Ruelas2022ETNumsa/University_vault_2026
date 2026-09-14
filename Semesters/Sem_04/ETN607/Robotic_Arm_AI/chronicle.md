---
galaxy_body: chronicle
scope: robotic-arm-ai
date_updated: 2026-09-13
---

## 2026-09-13 — Sesión 01: Definición inicial del proyecto

**Objetivo:** evaluar opciones de hardware y definir stack técnico.

**Discutido:**
- Comparación Mould King Digger (~1800 Bs) vs LEGO Mindstorms + expansión (~3000 Bs)
- Viabilidad de ESP32 como reemplazo del controlador Mindstorms
- Comunicación WiFi vs Serial USB → elegido Serial USB
- Stack de IA gratuita: Gemini (Google AI Studio) y Groq como opciones principales
- Sistema de skills: README como system prompt + JSON por Serial
- Descarte de OTA firmware update por lentitud
- Evaluación de cámara web con Gemini Vision (postergado a fase 2)
- Rol del FPGA Cyclone 5 (descartado)
- Viabilidad de garra 3 dedos con piezas Technic del Digger

**Resultado (sesión 1):** Decisión inicial: Mould King Digger + ESP32. Luego revertida en sesión 2.

**Presupuesto estimado sesión 1 (no ejecutado):**
- Mould King Digger: ~1800 Bs + 2 sets simples ~600 Bs + ESP32 + drivers: ~250 Bs → Total ~2650 Bs

---

## 2026-09-13 — Sesión 02: Reanálisis completo — decisión de hardware revertida

**Objetivo:** reanálisis desde cero con criterio de precisión y viabilidad en Bolivia.

**Problema identificado con el Digger:**
- Los motores PF (Power Functions) del Digger son DC sin encoder
- El ESP32 controla por tiempo de giro ("girar 500ms") sin conocer la posición real del brazo
- Esto hace que las skills sean no reproducibles: la misma instrucción puede terminar en posiciones distintas según voltaje, carga y fricción
- Para agregar precisión se necesitarían encoders externos o potenciómetros por articulación → mayor costo, complejidad de montaje en piezas Technic, y firmware adicional
- En Bolivia conseguir encoders externos o motores EV3 individuales es igualmente difícil

**Por qué el EV3 resuelve el problema:**
- Cada servomotor EV3 tiene encoder integrado → Python lee posición en grados reales
- Control determinista: `motor.run_angle(200, 90)` mueve exactamente 90° siempre
- EV3 Brick tiene USB nativo con protocolo abierto → Python se conecta directamente sin drivers adicionales
- Compatible con ev3dev (Linux) y MicroPython (Pybricks) → código ya existente para el Robot Arm H25
- No se necesitan L298N, level shifters, ni ESP32

**Robot Arm H25 identificado como base:**
- Modelo oficial del Core Set 45544 con instrucciones y código MicroPython publicado por LEGO/Pybricks
- Usa 3 motores: Port A (garra Medium), Port B (codo Large 8t→40t), Port C (base Large 12t→36t)
- La muñeca es un mecanismo pasivo (biela/rack) → no requiere motor extra
- Touch Sensors para homing de posición inicial

**Expansión 45560 aclarada:**
- 853 piezas estructurales: beams, engranajes, plataforma giratoria, conectores
- NO incluye motores ni sensores
- Suficiente para escalar el H25 con estructura adicional

**Stack IA definitivo:**
- Claude (claude.ai free) como orquestador principal — razonamiento, visión en fase 2
- Gemini Flash (Google AI Studio, tier gratuito) como delegado de traducción rápida a JSON
- Python intermediario en PC como puente USB → EV3

**Resultado:** Hardware definitivo cerrado. EV3 Core 45544 + Expansion 45560. Sin componentes adicionales necesarios para el MVP.

**Presupuesto confirmado:**
- EV3 Core 45544 + Expansion 45560: ~Bs 3000 (tienda Facebook)
- Software: Bs 0
