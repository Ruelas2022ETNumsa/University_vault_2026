---
galaxy_body: blueprint
status: idea
priority: baja
date: 2026-09-02
---

# Ideas TARS × ESP32 WiFi Bridge

> **Relación:** Construir un adaptador DIY basado en ESP32 que permita conectar TARS (HP Prime G2) a una red WiFi estándar, reemplazando el adaptador propietario de HP usando el protocolo USB HID ya reverseado por la comunidad.

---

## Contexto del problema

El módulo inalámbrico de la HP Prime G2 opera en 2.4GHz pero NO es WiFi estándar IEEE 802.11.
Usa un chip Nordic propietario que se comunica via USB HID con paquetes de 64 bytes.
Los adaptadores oficiales de HP son caros y solo sirven para comunicación entre calculadoras en aula.
El protocolo USB HID ya fue parcialmente reverseado por la comunidad (PrimeComm, libhpcalcs).

---

## Hardware considerado

- [ ] **ESP32-S2 o ESP32-S3** — tienen USB OTG integrado, necesario para actuar como USB Host y leer TARS directamente sin adaptadores adicionales
- [ ] **ESP32 clásico + MAX3421E** — chip USB Host externo, fue el enfoque del primer experimento DIY documentado en hpmuseum.org (2014)
- [ ] **Módulo de nivel lógico (level shifter)** — necesario si el ESP32 opera a 3.3V y el bus USB de TARS requiere conversión
- [ ] **PCB personalizada** — el experimento original (eried, 2014) requirió fabricar una PCB custom para cablear todos los componentes sin errores

---

## Software / protocolo

- [ ] **PrimeComm** (eried) — librería C# que reverseó el protocolo USB HID de la HP Prime. Envía y recibe archivos .hpprgm. Base de código disponible en GitHub.
- [ ] **libhpcalcs** (debrouxl) — librería portable C (Windows/Linux/macOS) con soporte para enviar archivos, recibir backups, capturas de pantalla y consultar info del firmware. Más robusta que PrimeComm.
- [ ] **hplp** (debrouxl) — proyecto relacionado, más reciente, con comunicación básica funcional vía WebUSB
- [ ] **Firmware ESP32** — a desarrollar: implementar el lado USB Host del protocolo HID de HP Prime, luego hacer puente hacia WiFi 802.11 para que el Connectivity Kit lo vea como una calculadora virtual

---

## Flujo objetivo

- [ ] Definir el flujo completo:
```
TARS (física)
    ↓ USB micro
ESP32-S3 (USB Host)
    ↓ protocolo HID HP Prime → traducción
ESP32-S3 (WiFi 802.11)
    ↓ red local
PC — Connectivity Kit
    (ve a TARS como si fuera una calc virtual por red IP)
```
- [ ] Estudiar los paquetes HID de 64 bytes que usa el protocolo HP Prime
- [ ] Implementar el parsing en ESP32 (C++ / ESP-IDF o Arduino framework)
- [ ] Implementar el puente WiFi → servidor en PC que el Connectivity Kit pueda detectar

---

## Prerequisitos de conocimiento

- [ ] USB HID protocol (host/device, endpoints, paquetes)
- [ ] ESP32-S3 USB OTG como USB Host
- [ ] Protocolo HP Prime (estudiar PrimeComm y libhpcalcs)
- [ ] Networking básico (sockets, servidor local que imite el protocolo de la calc virtual)
- [ ] Fabricación de PCB si se opta por hardware custom

---

## A depurar

- ¿El Connectivity Kit acepta una calc física que se conecta por red IP igual que una virtual? (no confirmado)
- ¿El ESP32-S3 puede actuar como USB Host con TARS sin adaptadores adicionales?
- ¿PrimeComm / libhpcalcs siguen siendo compatibles con firmware 2.4 (2025)?
- ¿El protocolo HID cambió en el G2 respecto al G1 con dongle?

---

## Referencias

**Protocolo HP Prime (USB HID reverseado)**
- PrimeComm — librería C# con protocolo USB reverseado: https://github.com/eried/PrimeComm
- libhpcalcs — librería C portable (Windows/Linux/macOS): https://github.com/debrouxl/hplp
- Experimento DIY original ESP32+MAX3421E (2014): https://www.hpmuseum.org/forum/post-4747.html
- Detalles del protocolo Nordic/HID (Tim Wessman, HP): https://www.hpmuseum.org/forum/post-42434.html

**ESP32 como USB Host**
- ESP32-S3 USB OTG docs: https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/usb_host.html
- ESP32 WiFi bridge (Rust): https://github.com/owenthewizard/esp32-wifi-bridge
