from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()
motor = Motor(Port.A, Direction.CLOCKWISE)

VELOCIDAD = 300      # grados/segundo (fija)
UMBRAL_MIN = 5500    # si el minimo del movimiento es menor a esto, se termina el programa
PERIODO_MS = 50      # cada cuanto se mide durante el movimiento


def pedir_numero(mensaje):
    """Pide un numero por teclado. Devuelve None si se escribe 'q'."""
    while True:
        texto = input(mensaje).strip().lower()
        if texto == "q":
            return None
        try:
            return float(texto)
        except ValueError:
            print("Valor no valido, escribi un numero (o 'q' para salir).")


def mover_y_medir(objetivo):
    """Mueve al angulo absoluto 'objetivo' y devuelve el valor minimo medido en ese movimiento."""
    minimo = hub.battery.voltage()
    motor.run_target(VELOCIDAD, objetivo, wait=False)
    while not motor.done():
        v = hub.battery.voltage()
        if v < minimo:
            minimo = v
        wait(PERIODO_MS)
    # ultima lectura al llegar
    v = hub.battery.voltage()
    if v < minimo:
        minimo = v
    return minimo


motor.reset_angle(0)
print("Angulo inicial:", motor.angle(), "deg")
print("Escribi 'q' en cualquier momento para salir.")

multiplicador = pedir_numero("Multiplicador: ")
if multiplicador is None:
    motor.stop()
    print("Programa terminado.")
else:
    while True:
        angulo = pedir_numero("Angulo (deg): ")
        if angulo is None:
            break

        objetivo = int(angulo * multiplicador)
        print("Objetivo:", objetivo, "deg (", angulo, "x", multiplicador, ")")

        minimo = mover_y_medir(objetivo)

        print("Llego -> Angulo:", motor.angle(), "deg | Valor minimo:", minimo)

        if minimo < UMBRAL_MIN:
            motor.stop()
            print("Valor minimo", minimo, "< ", UMBRAL_MIN, "-> motor detenido, programa terminado.")
            break

    motor.stop()
    print("Programa terminado. Angulo final:", motor.angle(), "deg")
