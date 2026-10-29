from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# ---- CONFIGURACION ----
PUERTOS = [Port.A, Port.B]   # ej: [Port.A, Port.B, Port.C]
VELOCIDAD = 800              # deg/s
V_CORTE = 6500               # mV: si baja de esto, frena todo
# -----------------------

hub = InventorHub()
motores = [Motor(p) for p in PUERTOS]
print("Motores:", len(motores))
print("vel, mV, mA, cargas (mNm)")
print("")
print(">>> CAMBIO A VELOCIDAD:", VELOCIDAD, "deg/s con", len(motores), "motores")
hub.speaker.beep()

for m in motores:
    m.run(VELOCIDAD)
wait(1000)  # aceleracion

for i in range(10):  # 10 x 500 ms = 5 s
    v = hub.battery.voltage()
    print(VELOCIDAD, v, hub.battery.current(), [m.load() for m in motores])
    if v < V_CORTE:
        for m in motores:
            m.stop()
        print("!!! VOLTAJE BAJO (", v, "mV): DETENIDO")
        break
    wait(500)

for m in motores:
    m.stop()
print("--- fin de", VELOCIDAD, "deg/s ---")
print("FIN")