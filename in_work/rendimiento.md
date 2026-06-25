# Optimización PC - Contexto y Progreso

## Specs
- Win 10, 16GB RAM, GPU GTX 1050 Ti, HDD mecánico 1TB (partición C: ~260GB)

## Objetivo general
Optimizar la PC desde distintos ángulos:
1. Limpieza de archivos basura / espacio en disco
2. Programas que inician con Windows
3. Revisar procesos que consumen mucha RAM/CPU
4. Optimizar el HDD (mecánico, no SSD) ← **rama en la que avanzamos hoy**
5. Revisar problemas puntuales (lentitud general, tiempos de inicio)

---

## 🔴 PENDIENTE / EN PAUSA

### Problema de suspensión (issue original, en pausa)
- **Síntoma:** Al volver de suspensión (sea 3 min o 6 horas, da igual), la PC responde muy lento o el monitor muestra "no señal/comprobar cable" y hay que reiniciar con el botón de encendido.
- **Ya hecho:**
  - ✅ Actualizado driver NVIDIA a Game Ready 581.80 (instalación limpia, sin Nvidia App)
  - ✅ Fast Startup ya estaba desactivado (no era la causa)
  - ✅ Desactivado "reactivar el equipo" (Wake) en los 3 adaptadores de red (Realtek PCIe GbE, TP-Link Wireless, Microsoft WiFi Direct Virtual Adapter)
  - ⚠️ La 1050 Ti no tiene pestaña "Administración de energía" en Administrador de dispositivos (se saltó ese paso)
- **Pendiente para retomar:**
  - Hacer la prueba real de suspensión (10-15 min) y confirmar si mejoró
  - Si sigue: revisar Visor de Eventos (IDs 1, 41, 6008) cerca del momento de reanudación
  - Revisar cable/puerto del monitor (HDMI/DisplayPort directo a la GPU, probar otro cable/puerto)

### TODO - Otras ramas de optimización (no iniciadas)
- [ ] Programas que inician con Windows → **Ya se hizo parcialmente**: se desactivaron todos en Administrador de tareas > Inicio excepto Mega (se deja porque se usa)
- [ ] Revisar procesos que consumen mucha RAM/CPU (Administrador de tareas, pestaña Procesos/Rendimiento)
- [ ] Revisar lentitud general / tiempo de inicio puntual si persiste

---

## ✅ HECHO HOY - Rama: Optimizar el HDD

1. **Driver NVIDIA actualizado** a 581.80 (Game Ready, instalación limpia, sin Nvidia App, sin Wake-on-LAN)
2. **Desfragmentación** del disco C: realizada
3. **Liberador de espacio en disco** ejecutado (sin marcar "archivos temporales de internet" para no afectar sesiones/cookies activas)
4. **Indexación desactivada** en disco C: (Propiedades > desmarcar "permitir contenido indexado") — búsquedas de archivos un poco más lentas, pero menos actividad de disco en background
5. **Programas de inicio limpiados**: desactivados todos en Administrador de tareas excepto Mega
6. **ReadyBoost**: salteado por ahora (no había pendrive a mano)
7. **SysMain (ex Superfetch) desactivado**: servicio detenido y tipo de inicio cambiado a Deshabilitado (`services.msc`)
8. **Salud del disco verificada** con estado S.M.A.R.T: 45°C, sin errores, 20,942 horas de uso, 5400 RPM — disco sano, no es la causa de lentitud
9. **Efectos visuales reducidos**: Opciones de rendimiento > "Ajustar para obtener el mejor rendimiento"
10. **Antivirus**: examen completo ya se había hecho recientemente (no repetido)
11. **Memoria virtual**: se dejó en automático (correcto con 16GB RAM, no se tocó)
12. **Storage Sense**: ya estaba activado (limpieza automática cuando hay poco espacio)
13. **SFC /scannow ejecutado**: encontró y reparó archivos corruptos del sistema (detalles en `C:\Windows\Logs\CBS\CBS.log`)
14. **DISM /Online /Cleanup-Image /RestoreHealth ejecutado**: "The restore operation completed successfully" — reparación profunda OK, sin errores
15. **Reinicio final**: pendiente de confirmar si se hizo tras todos los cambios

### Limpieza de aplicaciones (Aplicaciones y características, ~134GB)
Revisadas y decisiones tomadas:
- Adobe AIR → desinstalar (no usado)
- Digilent software → **dejar** si se usa o se va a usar hardware de laboratorio (Analog Discovery, etc.) en electrónica. Confirmar con el usuario.
- HI-TECH C51-Lite (compilador 8051) → dejar si sigue cursando microcontroladores, sino borrar
- Microsoft Visio → desinstalado (nunca usado, hay alternativas online: draw.io, etc.)
- Windows SDK (2 versiones: 10.0.26100.4654 y 10.0.19041.685) → desinstalar ambas (no se usa Visual Studio completo ni compilación nativa de Windows)
- UI.Vision RPA → desinstalado (no usado, era para automatización de navegador/RPA)
- Winget (Windows Package Manager) → **NO desinstalar**, es componente del sistema
- Google Drive (3 versiones instaladas: 126.0.50 vigente + dos versiones 1.0 viejas) → desinstalar las viejas, dejar solo la más reciente (hacerlo de a una, verificando que Drive siga sincronizando bien)
- Microsoft Edge → **NO desinstalar**, integrado al sistema, no vale la pena el riesgo
- Microsoft Update Health Tools → **NO desinstalar**, ayuda con Windows Update, pesa muy poco
- Microsoft Windows 10 SDK Installer → desinstalar (resto del SDK ya descartado)
- Microsoft XNA Framework 4.0 → desinstalar si no se juegan juegos viejos/indie que lo requieran
- OpenAL → desinstalar si no se juegan juegos que lo requieran (dependencia de audio 3D para juegos)
- Visual Studio 2022 (completo) → el usuario decidió desinstalarlo completo vía Visual Studio Installer > botón "..." > Desinstalar (se lleva todos los componentes/workloads)

### Nota sobre programación en C/C++
El Windows SDK standalone NO es necesario para compilar C/C++. Para retomar programación en C:
- Opción simple: reinstalar **Dev-C++** (incluye compilador MinGW)
- Opción alterna: VS Code + compilador **MinGW-w64** + extensión C/C++
- Opción pesada: Visual Studio Community (trae compilador MSVC integrado)

---

## Notas generales
- Usuario es estudiante de ingeniería, usa la PC también para materias (microcontroladores, electrónica con hardware Digilent posiblemente, assembler con DOSBox en la facultad)
- Antes usaba Dev-C++ para C/C++, ya no lo tiene instalado
- Hubo un corto con un ESP32 que dañó un puerto USB (anterior al problema de suspensión, no relacionado)
