from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch

# ---------------- CONFIGURACION ----------------
PUERTOS = [Port.A, Port.B, Port.C, Port.D]

ACEL = 400        # deg/s^2: aceleracion maxima (mas baja = arranque mas suave)
TORQUE = 80       # mNm: tope de torque por motor (mas bajo = menos pico de corriente)

V_CORTE = 5500    # mV: si baja de esto, frena todo
PASO_MS = 250     # cada cuanto mide
PAUSA_MS = 1000   # pausa con motores parados entre etapas

# Etapa: (nombre, motores activos, vel inicial, vel final, duracion ms)
# La velocidad cambia en rampa lineal de vel inicial a vel final durante la etapa.
ETAPAS = [
    ("A",    [0],          800, 640, 5000),
    ("AB",   [0, 1],       600, 440, 5000),
    ("ABC",  [0, 1, 2],    200, 120, 5000),
    ("ABCD", [0, 1, 2, 3], 100, 100, 1000),
    ("BCD",  [1, 2, 3],    120, 200, 1000),
    ("CD",   [2, 3],       440, 600, 1000),
    ("D",    [3],          640, 800, 1000),
]
# -----------------------------------------------

hub = InventorHub()
motores = [Motor(p) for p in PUERTOS]
for m in motores:
    m.control.limits(acceleration=ACEL, torque=TORQUE)


def medir(activos, v_ini, v_fin, dur):
    """Rampa de velocidad + medicion. Devuelve False si el voltaje cae bajo V_CORTE."""
    t = StopWatch()
    while t.time() < dur:
        vel = v_ini + (v_fin - v_ini) * t.time() // dur
        for m in activos:
            m.run(vel)
        v = hub.battery.voltage()
        print(vel, v, hub.battery.current(), [m.load() for m in activos])
        if v < V_CORTE:
            return False
        wait(PASO_MS)
    return True


def pausa():
    """Motores parados; mide para ver cuanto se recupera el voltaje."""
    for m in motores:
        m.stop()
    print("--- pausa, motores parados ---")
    t = StopWatch()
    while t.time() < PAUSA_MS:
        print("pausa", hub.battery.voltage(), hub.battery.current())
        wait(PASO_MS)


print("vel_cmd, mV, mA, cargas (mNm) en el orden de los motores activos")
print("Limites: aceleracion", ACEL, "deg/s2, torque", TORQUE, "mNm, corte", V_CORTE, "mV")
ok = True
nombre = ""
for i in range(len(ETAPAS)):
    nombre, idx, v_ini, v_fin, dur = ETAPAS[i]
    activos = [motores[k] for k in idx]
    print("")
    print(">>> ETAPA", nombre, "-", len(idx), "motores,", v_ini, "->", v_fin,
          "deg/s,", dur // 1000, "s")
    hub.speaker.beep()
    for k in range(len(motores)):
        if k not in idx:
            motores[k].stop()
    ok = medir(activos, v_ini, v_fin, dur)
    if not ok:
        break
    if i < len(ETAPAS) - 1:
        pausa()

for m in motores:
    m.stop()

if not ok:
    print("!!! VOLTAJE BAJO: DETENIDO en la etapa", nombre)
hub.speaker.beep(1000, 300)
print("FIN")