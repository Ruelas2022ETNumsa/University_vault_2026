---
galaxy_body: chronicle
scope: robotic-arm-ai
date_updated: 2026-09-13
---

## 2026-09-13 — Sesión 01: Definición del proyecto

**Objetivo de la sesión:** evaluar opciones de hardware y definir stack técnico completo.

**Discutido:**
- Comparación Mould King Digger (~1800 Bs) vs LEGO Mindstorms + expansión (~3000 Bs)
- Viabilidad de ESP32 como reemplazo del controlador Mindstorms
- Comunicación WiFi vs Serial USB → elegido Serial USB
- Stack de IA gratuita: Gemini (Google AI Studio) y Groq como opciones principales
- Sistema de skills: README como system prompt + JSON por Serial
- Descarte de OTA firmware update por lentitud
- Evaluación de cámara web con Gemini Vision (postergado a fase 2)
- Rol del FPGA Cyclone 5 (descartado por ahora)
- Viabilidad de garra 3 dedos con piezas Technic del Digger

**Resultado:** todas las decisiones técnicas principales tomadas. Hardware y stack definidos.

**Presupuesto estimado:**
- Mould King Digger: ~1800 Bs
- 2 sets simples adicionales: ~600 Bs
- ESP32 + drivers L298N + cables: ~250 Bs
- **Total: ~2650 Bs**
- Software: 0 Bs

---
