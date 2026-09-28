# 📡 Resumen de Sesión — Wireshark y Análisis de Tramas de Red

**Fecha de sesión:** Septiembre 2026  
**Contexto:** Laboratorio de redes — preparación para análisis de tramas con Wireshark  
**Próximo paso:** Conseguir diapositivas del docente y profundizar bibliografía

---

## 1. ¿Qué es Wireshark?

- Programa para capturar y analizar **tramas de red** (trenes de bits)
- Permite monitorear **direcciones MAC**, IPs, protocolos y más
- Es **gratuito y open source** — licencia GPLv2
- Sitio oficial: [wireshark.org](https://www.wireshark.org)

---

## 2. Instalación

### Versión instalada
- **Wireshark 4.6.9** — Windows x64 Installer

### Componentes seleccionados
| Componente | Estado | Motivo |
|---|---|---|
| Wireshark | ✅ Instalado | Interfaz gráfica principal |
| TShark | ✅ Instalado | Versión consola/terminal |
| ETWdump | ✅ Instalado | Viene por defecto |
| Npcap 1.88 | ✅ Instalado | **Obligatorio** — motor de captura |
| USBcap | ❌ No instalado | No necesario para laboratorio de red |

### Opciones de Npcap seleccionadas
| Opción | Estado |
|---|---|
| Restrict access to administrators only | ❌ No marcado |
| Support raw 802.11 / monitor mode (WiFi) | ✅ Marcado |
| WinPcap API-compatible mode | ❌ No marcado |

---

## 3. Consideraciones de hardware

- La laptop **no tiene puerto RJ45 nativo** — usa adaptador **USB-Ethernet**
- Wireshark detecta el adaptador USB-Ethernet sin problemas (lo maneja Npcap)
- La PC de escritorio tiene **2 puertos RJ45 en motherboard** — NO funcionan como switch, son interfaces independientes
- La PC de escritorio comparte internet via **antena WiFi** → funciona como router improvisado

### Topología actual
```
Internet → Cable RJ45 → PC escritorio → Antena WiFi → dispositivos
```

---

## 4. Escenarios de captura

| Escenario | Conexión | Filtro útil | Qué se aprende |
|---|---|---|---|
| PC a internet | RJ45 o WiFi | `arp`, `tcp` | Ver MACs propias y del router |
| Laptop a laptop | Cable directo | `icmp` | Ver tráfico puro entre 2 equipos |
| WiFi general | Inalámbrica | `arp` | Ver MACs de varios dispositivos |

> **Diferencia clave:** RJ45 a internet ≠ laptop a laptop. En laptop a laptop se ven las MACs de ambos equipos directamente y el tráfico es más limpio y didáctico.

---

## 5. Primer uso — Pasos

1. Abrir Wireshark como **Administrador**
2. Seleccionar la interfaz con línea de actividad moviéndose
3. Doble clic → empieza la captura
4. Generar tráfico (abrir navegador, hacer ping)
5. Aplicar filtros en la barra superior
6. Detener con botón ⏹️ o **Ctrl + E**

### Filtros básicos
```
arp       → tramas ARP (ver MACs)
icmp      → ping entre equipos
tcp       → tráfico TCP
ip        → todo tráfico IP
eth       → todo tráfico Ethernet
```

---

## 6. Interpretación de la captura

### Panel superior — columnas
| Columna | Significado |
|---|---|
| No. | Número de trama |
| Time | Tiempo desde inicio de captura |
| Source | IP/MAC de quien envía |
| Destination | IP/MAC de quien recibe |
| Protocol | Protocolo usado |
| Length | Tamaño en bytes |
| Info | Detalle del paquete |

### Colores
| Color | Significado |
|---|---|
| Verde | TCP normal y saludable |
| Azul claro | UDP |
| Negro | Errores o problemas |
| Amarillo | ARP / warnings |

### Flags TCP frecuentes
| Flag | Significado |
|---|---|
| ACK | Confirmación de recepción |
| PSH | Enviar datos inmediatamente |
| SYN | Inicio de conexión |
| FIN | Cierre de conexión |

---

## 7. Direcciones MAC — Conceptos clave

- La MAC es una dirección **física grabada en el hardware** — su valor nunca cambia
- Es **única en el mundo** para cada dispositivo
- Wireshark identifica el **fabricante automáticamente** por los primeros bytes (OUI)
- Puede aparecer como **Source o Destination** según quién envíe en ese momento
- **Solo viaja en la red local** — internet no transmite la MAC real

### MACs identificadas en la sesión
| Dispositivo | MAC | Fabricante |
|---|---|---|
| Router/Antena | `50:3e:aa:df:b6:60` | TP-Link |
| Tarjeta de red PC | `30:e3:...:1c:...` | Intel |

### ¿Hay que proteger la MAC?
- Riesgo principal: **MAC Spoofing** (alguien la clona en la misma red)
- Solo es visible dentro de la **red local**
- No permite acceso a cuentas ni internet remotamente
- Conviene no compartirla públicamente por buena práctica

---

## 8. Estructura de una trama (introducción)

```
┌─────────────────────────────┐
│        DATOS (mensaje)      │  Capa de Aplicación
├─────────────────────────────┤
│     TCP/UDP (transporte)    │  Puerto origen y destino
├─────────────────────────────┤
│         IP (red)            │  IP origen y destino
├─────────────────────────────┤
│     Ethernet (enlace)       │  MAC origen y destino
└─────────────────────────────┘
```

- Cada capa **envuelve** a la anterior → **encapsulamiento**
- Se lee de afuera hacia adentro al llegar al destino
- Wireshark muestra cada capa en el panel inferior al hacer clic en una trama

> ⚠️ **Tema pendiente de profundizar** — estructura detallada de tramas, cabeceras, campos específicos. Pedir diapositivas al docente para avanzar sobre los temas ya vistos en clase.

---

## 9. Bibliografía sugerida (a explorar)

| Recurso | Tipo | Nivel | Prioridad |
|---|---|---|---|
| **Forouzan — Transmisión de Datos y Redes** | Libro | Básico/Medio | ⭐ Primera opción |
| **Tanenbaum — Redes de Computadoras** | Libro clásico | Medio | ⭐ Segunda opción |
| **Cisco NetAcad** (netacad.com) | Curso online gratis | Básico | ⭐ Complemento gratis |
| **Professor Messer** (YouTube) | Videos | Básico | Complemento visual |
| **PowerCert Animated Videos** (YouTube) | Videos animados | Básico | Complemento visual |

> 📌 Confirmar con el docente si usa alguno de estos libros en la cátedra y pedir las diapositivas para alinear el estudio.

---

## 10. Pendientes para próxima sesión

- [ ] Conseguir diapositivas del docente
- [ ] Profundizar estructura de tramas (cabeceras, campos)
- [ ] Buscar más bibliografía específica según programa de la cátedra
- [ ] Realizar prueba de captura **laptop a laptop** por cable
- [ ] Practicar filtros ARP e ICMP en Wireshark
- [ ] Investigar modelo OSI y TCP/IP en detalle

---

*Resumen generado como contexto para sesiones futuras.*
