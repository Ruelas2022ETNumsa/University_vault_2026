from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch

# Cambiar PrimeHub por tu hub: InventorHub, EssentialHub, CityHub, etc.
hub = PrimeHub()
motor = Motor(Port.A, Direction.CLOCKWISE)

VOLTAJE_MIN = 5500          # mV: si baja de este valor, el programa se detiene
VELOCIDADES = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]  # grados/segundo
TIEMPO_PASO = 5000          # ms que se mantiene cada velocidad (5 s)
PERIODO = 100               # ms entre mediciones

reloj = StopWatch()


def voltaje_ok():
    """Devuelve True si el voltaje es suficiente para seguir."""
    return hub.battery.voltage() >= VOLTAJE_MIN


def detener(motivo):
    motor.stop()
    print("DETENIDO:", motivo, "| Voltaje:", hub.battery.voltage(), "mV")


# Verificacion inicial antes de mover el motor
v0 = hub.battery.voltage()
print("Voltaje inicial:", v0, "mV (minimo:", VOLTAJE_MIN, "mV)")
if v0 < VOLTAJE_MIN:
    detener("voltaje inicial menor al minimo")
else:
    motor.reset_angle(0)
    completo = True

    for vel in VELOCIDADES:
        print("--- Velocidad:", vel, "deg/s ---")
        motor.run(vel)
        reloj.reset()

        while reloj.time() < TIEMPO_PASO:
            voltaje = hub.battery.voltage()
            print(
                "t:", reloj.time(), "ms | vel objetivo:", vel,
                "| vel real:", motor.speed(),
                "| angulo:", motor.angle(),
                "| voltaje:", voltaje, "mV",
            )
            if voltaje < VOLTAJE_MIN:
                detener("voltaje menor a " + str(VOLTAJE_MIN) + " mV a " + str(vel) + " deg/s")
                completo = False
                break
            wait(PERIODO)

        if not completo:
            break

    if completo:
        motor.stop()
        print("Prueba completa. Voltaje final:", hub.battery.voltage(), "mV")
