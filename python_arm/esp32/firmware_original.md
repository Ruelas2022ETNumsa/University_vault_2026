# ESP32: documentación del firmware original (respaldo)

**Fecha:** 21 de noviembre de 2026
**Motivo:** guardar una copia completa de la flash antes de instalar MicroPython, para poder volver al estado original.

## 1. Hardware

| Dato | Valor |
| ---- | ----- |
| Placa | ESP32-WROOM-32, 38 pines |
| Chip | ESP32-D0WD-V3 (revisión v3.0) |
| Características | Wi-Fi, Bluetooth, doble núcleo, 240 MHz |
| Cristal | 40 MHz |
| MAC | `a8:42:e3:49:a4:90` |
| Flash: fabricante / dispositivo | `5e` / `4016` |
| Flash: tamaño | 4 MB |
| Voltaje de la flash | 3,3 V (por pin de strapping) |
| Chip USB-serie | CP2102 (Silicon Labs CP210x USB to UART Bridge) |
| Puerto en Windows | COM6 |
| Herramienta | esptool v5.6.0, Python 3.13.13 |

Los datos salen del comando `python -m esptool --port COM6 flash-id`.

## 2. Respaldo

- **Archivo:** `respaldo_esp32_original.bin` (en esta misma carpeta).
- **Contenido:** lectura completa de la flash, desde la dirección 0, 4 MB.
- **Comando usado:**

```
python -m esptool --port COM6 --baud 460800 read-flash 0 0x400000 respaldo_esp32_original.bin
```

- **Tamaño esperado:** 4194304 bytes.
- **Verificación del tamaño:** confirmada el 21-nov-2026, el archivo mide **4194304 bytes**.
- **Hash SHA-256:** [pendiente]. Se obtiene con:

```
Get-FileHash respaldo_esp32_original.bin -Algorithm SHA256
```

- **Qué traía la placa:** no se examinó. Se desconoce si tenía un programa de ejemplo o estaba vacía.

## 3. Cómo restaurar el firmware original

Escribe la copia completa desde la dirección 0. Esto **reemplaza** MicroPython (o lo que haya en la placa) por lo que se guardó:

```
python -m esptool --port COM6 --baud 460800 write-flash 0 respaldo_esp32_original.bin
```

Nota: comando con la sintaxis de esptool 5.x, **no probado** todavía en esta placa.

## 4. Problemas encontrados

- **Error `Wrong boot mode detected (0x13)`:** la placa no entró sola en modo de descarga. Solución: mantener apretado el botón **BOOT** mientras esptool muestra `Connecting......` y soltarlo cuando empiece el avance. Otra opción: mantener BOOT, pulsar y soltar EN, soltar BOOT y ejecutar el comando enseguida.
- Cerrar Thonny y cualquier terminal serial antes de usar esptool, porque ocupan el puerto.

## 5. Historial

| Fecha | Acción |
| ----- | ------ |
| 21-nov-2026 | Se leyó la información de la placa (`flash-id`) y se hizo el respaldo de la flash. |
| 21-nov-2026 | Se instaló MicroPython **v1.29.0** (`ESP32_GENERIC`, variante Espressif ESP32 / WROOM) con Thonny, borrando antes toda la flash. Escribió 1790544 bytes en `0x1000` y el hash de lo grabado se verificó. Hizo falta apretar BOOT al aparecer `Connecting`. |
| 21-nov-2026 | **Siguiente paso:** comprobar el mensaje de MicroPython en el Shell de Thonny y probar el Bluetooth. [pendiente] |
