from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()
motor = Motor(Port.A, Direction.CLOCKWISE)

VELOCIDAD = 300      # grados/segundo (fija)
MEDIDAS_MOSTRAR = 5  # cuantas medidas de voltaje se imprimen por movimiento
PERIODO = 50         # ms entre lecturas (se registran todas, se imprimen solo 5)

motor.reset_angle(0)
voltaje_min = hub.battery.voltage()  # minimo registrado en toda la sesion (mV)

print("Voltaje inicial:", voltaje_min, "mV")
print("Escribi un angulo y presiona Enter. Escribi 'q' para salir.")

while True:
    texto = input("Angulo objetivo (deg): ")

    if texto.strip().lower() == "q":
        break

    try:
        objetivo = int(float(texto))
    except ValueError:
        print("Valor no valido, escribi un numero.")
        continue

    motor.run_target(VELOCIDAD, objetivo, wait=False)
    mostradas = 0

    while not motor.done():
        voltaje = hub.battery.voltage()

        # Se registra el minimo con todas las lecturas
        if voltaje < voltaje_min:
            voltaje_min = voltaje

        # Solo se imprimen las primeras medidas del movimiento
        if mostradas < MEDIDAS_MOSTRAR:
            print("Voltaje:", voltaje, "mV")
            mostradas += 1

        wait(PERIODO)

    # Lectura al terminar el movimiento
    voltaje = hub.battery.voltage()
    if voltaje < voltaje_min:
        voltaje_min = voltaje

motor.stop()
print("Programa terminado.")
print("Voltaje minimo registrado:", voltaje_min, "mV")
