from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()
motor = Motor(Port.A, Direction.CLOCKWISE)

VELOCIDAD = 300  # grados/segundo (fija)

motor.reset_angle(0)
print("Angulo inicial:", motor.angle(), "deg")
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

    # Movimiento al angulo absoluto indicado, mostrando el angulo en vivo
    motor.run_target(VELOCIDAD, objetivo, wait=False)
    while not motor.done():
        print("Angulo:", motor.angle(), "deg")
        wait(100)

    print("Llegó -> Angulo:", motor.angle(), "deg (objetivo:", objetivo, "deg)")

motor.stop()
print("Programa terminado. Angulo final:", motor.angle(), "deg")
