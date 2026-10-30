from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()
motor = Motor(Port.A, Direction.CLOCKWISE)

motor.reset_angle(0)

VELOCIDAD = 300   # grados/segundo
GIRO = 360        # grados por movimiento


def mover(grados):
    """Gira 'grados' sin bloquear y muestra angulo y voltaje mientras se mueve."""
    motor.run_angle(VELOCIDAD, grados, wait=False)
    while not motor.done():
        angulo = motor.angle()
        voltaje = hub.battery.voltage()  # mV
        print("Angulo:", angulo, "deg | Voltaje:", voltaje, "mV")
        wait(100)
    # Lectura final al terminar el movimiento
    print("FIN -> Angulo:", motor.angle(), "deg | Voltaje:", hub.battery.voltage(), "mV")


# 1ro hacia un lado
print("Giro en sentido horario")
mover(GIRO)
wait(500)

# Luego hacia el otro
print("Giro en sentido antihorario")
mover(-GIRO)

motor.stop()
print("Angulo final:", motor.angle(), "deg")
