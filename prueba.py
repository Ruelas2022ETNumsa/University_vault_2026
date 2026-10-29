from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch

# ---- CONFIGURACION ----
PUERTOS = [Port.A, Port.B, Port.C, Port.D]
NOMBRES = ["A", "B", "C", "D"]
VELOCIDAD = 100        # deg/s
V_CORTE = 5000         # mV: si baja de esto, frena todo
PASO_MS = 250          # cada cuanto mide
ESPERA_MS = 1000       # tiempo entre arranque de un motor y el siguiente
FINAL_MS = 5000        # tiempo con los 4 motores andando
# -----------------------

hub = InventorHub()
motores = [Motor(p) for p in PUERTOS]
activos = []


def medir(duracion_ms, paso_ms):
    """Imprime lineas hasta cumplir duracion_ms. Devuelve False si cae el voltaje."""
    t = StopWatch()
    while t.time() < duracion_ms:
        v = hub.battery.voltage()
        print(len(activos), v, hub.battery.current(), [m.load() for m in activos])
        if v < V_CORTE:
            return False
        wait(paso_ms)
    return True


print("activos, mV, mA, cargas (mNm)")
ok = True
for nombre, m in zip(NOMBRES, motores):
    activos.append(m)
    m.run(VELOCIDAD)
    print("")
    print(">>> ARRANCA MOTOR", nombre, "->", len(activos), "activos a", VELOCIDAD, "deg/s")
    hub.speaker.beep()
    if len(activos) < len(motores):
        ok = medir(ESPERA_MS, PASO_MS)
    else:
        ok = medir(FINAL_MS, PASO_MS)
    if not ok:
        break

for m in motores:
    m.stop()

if not ok:
    print("!!! VOLTAJE BAJO: DETENIDO con", len(activos), "motores activos")
print("FIN")