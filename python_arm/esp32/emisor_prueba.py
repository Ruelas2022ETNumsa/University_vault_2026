# emisor_prueba.py (ESP32, MicroPython)
#
# Etapa 1 de pruebas: el ESP32 emite por Bluetooth (broadcast de Pybricks, sin conexion) un mensaje
# de prueba para el hub LEGO. El hub lo recibe con el modo R de ha8.py, que SOLO lo muestra
# (no mueve motores).
#
# Formato del mensaje (el que espera ha8.py), una tupla de 3 enteros:
#       (articulacion, angulo, id_orden)
#   articulacion: -1 = ninguna | 0 = F base | 1 = D codo | 2 = A muneca | 3 = B garra
#   angulo:       grados de la ARTICULACION que marcaria el slider
#   id_orden:     contador que SUBE 1 cada vez que se "aprieta ACCIONAR"
#
# Requiere bleradio.py copiado en /lib del ESP32.
# Como usarlo: abrir este archivo en Thonny (con el interprete MicroPython ESP32) y ejecutarlo (F5).
# Para terminar: boton Stop de Thonny.

from time import sleep_ms
from bleradio import BLERadio

CANAL = 1             # debe ser igual a CANAL_ESP32 de ha8.py
PERIODO_MS = 100      # Pybricks emite cada 100 ms; no tiene sentido ir mas rapido
REPETICIONES = 30     # 30 x 100 ms = 3 segundos con cada mensaje

# (articulacion, angulo, accionar)
# accionar=True hace que id_orden suba 1 en ese paso (simula apretar el boton ACCIONAR).
# Hay pasos con valores FUERA DE RANGO a proposito para ver el recorte en el hub:
#   codo 200 (maximo 180) y garra 120 (maximo 90).
PASOS = [
    (-1, 0, False),    # ninguna articulacion activa
    (0, 45, False),    # base: slider en 45
    (0, 90, False),    # base: slider en 90
    (0, 90, True),     # base: ACCIONAR
    (1, -30, False),   # codo: slider en -30
    (1, 200, False),   # codo: fuera de rango (se recorta a 180)
    (1, 200, True),    # codo: ACCIONAR
    (2, 100, False),   # muneca: slider en 100
    (3, 90, False),    # garra: abierta
    (3, 120, False),   # garra: fuera de rango (se recorta a 90)
    (3, 0, True),      # garra: cerrar y ACCIONAR
]

radio = BLERadio(broadcast_channel=CANAL)
id_orden = 0

print("Emitiendo en el canal", CANAL, "- para terminar usa el boton Stop de Thonny")
try:
    while True:
        for articulacion, angulo, accionar in PASOS:
            if accionar:
                id_orden += 1
            mensaje = (articulacion, angulo, id_orden)
            print("Emito:", mensaje, "<<< ACCIONAR" if accionar else "")
            for _ in range(REPETICIONES):
                radio.broadcast(mensaje)
                sleep_ms(PERIODO_MS)
finally:
    radio.broadcast(None)   # detiene la emision
    print("Emision detenida")
