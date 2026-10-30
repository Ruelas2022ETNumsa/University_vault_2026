from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()
motor = Motor(Port.A, Direction.CLOCKWISE)

VELOCIDAD = 300  # grados/segundo
CAMINO_CORTO = True  # True: gira maximo 180 grados | False: va directo a 0 (angulo acumulado)


def esperar_y_medir():
    """Muestra angulo y voltaje hasta que el motor termine de moverse."""
    while not motor.done():
        print("Angulo:", motor.angle(), "deg | Voltaje:", hub.battery.voltage(), "mV")
        wait(100)
    print("FIN -> Angulo:", motor.angle(), "deg | Voltaje:", hub.battery.voltage(), "mV")


def ir_a_cero_directo():
    """Vuelve a 0 deshaciendo todas las vueltas acumuladas."""
    motor.run_target(VELOCIDAD, 0, wait=False)
    esperar_y_medir()


def ir_a_cero_corto():
    """Vuelve al 0 mas cercano (por ejemplo, de 350 deg va +10 deg)."""
    resto = motor.angle() % 360
    delta = -resto if resto <= 180 else 360 - resto
    motor.run_angle(VELOCIDAD, delta, wait=False)
    esperar_y_medir()


if CAMINO_CORTO:
    ir_a_cero_corto()
else:
    ir_a_cero_directo()

motor.stop()
