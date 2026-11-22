from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait, StopWatch
from ustruct import unpack

# AppData: en la version actual vive en pybricks.messaging (el proyecto oficial lo importa de ahi).
# Si tu firmware es mas viejo, queda el respaldo en pybricks.tools.
try:
    from pybricks.messaging import AppData
except ImportError:
    from pybricks.tools import AppData

# BLERadio (recibir mensajes de otro dispositivo por Bluetooth, sin conexion): vive en pybricks.messaging.
# Si el firmware no lo tiene, el modo REMOTO avisa y no se usa.
try:
    from pybricks.messaging import BLERadio
except ImportError:
    BLERadio = None

# ha9.py = ha8.py + el MODO REMOTO (R) AHORA MUEVE EL BRAZO (etapa 2).
#   - Los modos C (calibracion manual) y A (automatico) son los de ha7/ha8, sin cambios.
#   - Todos los parametros calibrados (VELOCIDAD, UMBRAL_MV, limites de ARTICULACIONES, timeouts) y la
#     funcion mover() son los de ha7/ha8: NO se cambio ninguno.
#   - Modo R: al entrar pide confirmacion, lleva el brazo a los valores iniciales (A muneca -> D codo ->
#     F base -> B garra a 0, igual que el modo automatico), fija los ceros y queda ARMADO.
#     Cada vez que el ESP32 manda una ORDEN NUEVA (id_orden cambia = se toco ACCIONAR en el celular) se
#     mueve UNA sola articulacion al angulo recibido, recortado a los limites, con mover():
#       * un solo motor energizado, se SUELTA al llegar;
#       * vigila voltaje/corriente; si baja de UMBRAL_MV 3 muestras seguidas, se suelta el motor y se PAUSA
#         (g + Enter = continuar | x = abortar y salir del modo R).
#     Mientras el brazo se mueve, las ordenes que lleguen se DESCARTAN (se avisa).
#     Con articulacion -1 (ninguna) o sin senal del ESP32 no se mueve nada.
#
# MENSAJE que emite el ESP32 (broadcast de Pybricks, canal CANAL_ESP32): una tupla de 3 enteros
#       (articulacion, angulo, id_orden)
#   articulacion: -1 = ninguna activa | 0 = F base | 1 = D codo | 2 = A muneca | 3 = B garra
#   angulo:       grados de la ARTICULACION que marca el slider (garra: 0 cerrada a 90 abierta)
#   id_orden:     contador que el ESP32 SUMA 1 cada vez que se aprieta ACCIONAR.
#   La primera lectura al entrar al modo R es solo la referencia de id_orden (no cuenta como orden).
#
# Pantalla: la terminal de Pybricks muestra los mensajes y la matriz del hub la letra de la articulacion
#   activa (F, D, A, B), "-" si no hay ninguna o "?" si no llega senal.
# Salir del modo R: botones IZQUIERDO y DERECHO del hub a la vez (mantener ~1 s). Los motores quedan sueltos.
#
# OJO: segun la documentacion de Pybricks, recibir por Bluetooth es MAS CONFIABLE cuando el hub no esta
#   conectado a la compu ni a otros dispositivos al mismo tiempo. Aqui el hub esta conectado a la compu
#   (terminal) y quiza al celular (camara), asi que puede haber lecturas perdidas.

# ha7.py = ha6.py + camara del celular (Pybricks smart sensor) + modo de CALIBRACION MANUAL.
#
# Nombres CORREGIDOS (los puertos y multiplicadores son los mismos de ha6.py):
#   F = BASE   (giro horizontal; multiplicador x3; se permite el giro completo de 360)
#   D = CODO   (levanta el brazo; x3; rango -120 a 180)      <- en ha6 se llamaba "hombro"
#   A = MUNECA (x1; rango 0 a 190)
#   B = GARRA  (0 = cerrada, 90 = abierta)
#   C y E libres.
#
# Lo que se mantiene de ha6.py: velocidad 200, umbral 5500 mV (pausa g/x), UN solo motor energizado
# a la vez (cada motor se SUELTA con stop() al llegar), descansos entre fases, inicio a 0.
#
# MODOS (menu):
#   C = CALIBRACION MANUAL: los motores quedan SUELTOS; vos mueves el brazo a mano y el programa imprime
#       motores (crudo>articulacion), IMU del hub y lo que ve la camara (pelota roja y cubo cafe).
#       Botones del hub: IZQUIERDO = guardar VISTA (camara) | DERECHO = guardar POSE (motores)
#                        ambos a la vez (mantener ~1 s) = salir.
#       La POSE imprime lineas listas para pegar en TABLA_TOMAR / TABLA_SOLTAR.
#   A = AUTOMATICO: barre la base buscando el CUBO y despues la PELOTA, guarda las coordenadas de ambos,
#       toma la pelota y la deja en el cubo. Codo y muneca salen de las tablas; con la tabla vacia
#       los pide por teclado (como en ha6).
#   R = REMOTO (ha9): recibe ordenes del ESP32 y mueve una articulacion por cada ACCIONAR (ver arriba).
#
# IMPORTANTE para la camara (como en el proyecto oficial):
#   - Conectar el hub desde la compu, SIN abrir camara; apretar el boton Bluetooth del hub;
#     abrir Pybricks en el celular, conectarse al mismo hub y tocar el icono del telefono (camara).
#   - El rastreador de color sigue UN solo color a la vez y entrega x, y, width, height como % (0-100)
#     del lado largo de la imagen. Si no ve nada entrega 0. Para ver los 2 objetos, el programa
#     CAMBIA el color con app.configure() entre lecturas (esto no esta verificado: revisar en
#     calibracion que las filas PELOTA y CUBO no salgan iguales).
#   - La camara va montada como en el proyecto oficial (gira con la base). Los datos de la camara para
#     la tabla se toman con el brazo en la POSE DE BUSQUEDA (todo en 0), antes de extender codo/muneca.

hub = InventorHub()

base = Motor(Port.F, Direction.CLOCKWISE)
muneca = Motor(Port.A, Direction.CLOCKWISE)
codo = Motor(Port.D, Direction.CLOCKWISE)
garra = Motor(Port.B, Direction.CLOCKWISE)

# ---------------- Parametros de ha6.py (sin cambios) ----------------

VELOCIDAD = 200          # grados/segundo del MOTOR (todos los motores)
UMBRAL_MV = 5500         # si el voltaje baja de esto (3 muestras seguidas), se PAUSA el programa
UMBRAL_AVISO_MV = 6000   # por debajo de esto se imprime un aviso (no pausa)
MUESTRAS_CORTE = 3       # muestras SEGUIDAS bajo UMBRAL_MV para pausar (filtra picos de 1 muestra)
PERIODO_MS = 20          # cada cuanto se mide durante el movimiento
TIMEOUT_ART_MS = 10000   # tiempo maximo por movimiento de articulacion
TIMEOUT_GARRA_MS = 3000  # tiempo maximo para la garra
ESPERA_INICIO_MS = 500   # espera antes de volver a inicio (tiempo para alejarse)
DESCANSO_FASES_MS = 1000 # pausa con motores sueltos entre fases (recupera bateria)

MOSTRAR_INCLINACION_POR_MOVIMIENTO = False
SOLTAR_GARRA_CERRADA = True
ACELERACION = None
TORQUE_MAX = None

GARRA_ABIERTA = 90
GARRA_CERRADA = 0

# clave = PUERTO: (motor, multiplicador, minimo, maximo) -> rangos en grados de la ARTICULACION
ARTICULACIONES = {
    "F": (base, 3, 0, 360),
    "D": (codo, 3, -120, 180),
    "A": (muneca, 1, 0, 190),
}
ORDEN = ["F", "D", "A"]  # base -> codo -> muneca
NOMBRES = {"F": "base", "D": "codo", "A": "muneca"}

# Secuencia de inicio: (nombre, motor, timeout) en orden muneca -> codo -> base -> garra
SECUENCIA_INICIO = [
    ("A muneca", muneca, TIMEOUT_ART_MS),
    ("D codo", codo, TIMEOUT_ART_MS),
    ("F base", base, TIMEOUT_ART_MS),
    ("B garra", garra, TIMEOUT_GARRA_MS),
]

# ---------------- Parametros NUEVOS: camara y busqueda ----------------

# Tono (hue, 0-359 grados) de cada objeto. La camara recibe tono // 2.
# Pelota roja: 8 en vez de 0 para no confundirla con magenta (igual que el proyecto oficial).
# Cubo cafe: 25 es un valor inicial A AJUSTAR (el cafe es un naranja oscuro y puede confundirse con la pelota).
TONOS = {"pelota": 8, "cubo": 25}
CAMBIO_COLOR_MS = 300      # espera tras cambiar de color para que la camara actualice
MUESTRAS_CAMARA = 3        # lecturas que se promedian en cada medicion
PERIODO_CAMARA_MS = 40     # pausa entre lecturas

# Criterio de "objeto en posicion" durante el barrido (valores del proyecto oficial, a calibrar)
ANCHO_MIN = {"pelota": 8, "cubo": 8}   # width minimo (% de la imagen)
X_MIN = 70                 # el objeto debe quedar con x entre X_MIN y X_MAX
X_MAX = 80
CONFIRMACIONES = 2         # lecturas seguidas que cumplen el criterio para frenar

VELOCIDAD_BARRIDO = 100    # grados/s del MOTOR de la base SOLO durante la busqueda (la camara necesita tiempo)
BASE_BARRIDO_MAX = 360     # grados de articulacion hasta donde barre la base (despues vuelve a 0 y desenreda el cable)
ESPERA_ASENTAR_MS = 400    # tras frenar la base, espera antes de medir

# Que valor de la camara se usa para estimar la distancia en las tablas: 0=x 1=y 2=width 3=height
CLAVE_DISTANCIA = 1

# Tablas de calibracion (se llenan con las lineas que imprime la calibracion manual).
# Cada fila: (valor_de_camara, codo_grados_articulacion, muneca_grados_articulacion)
# Se interpola entre filas. Con menos de 2 filas, el modo automatico pide codo y muneca por teclado.
TABLA_TOMAR = [
    # (y, codo, muneca),
]
TABLA_SOLTAR = [
    # (y, codo, muneca),
]

# ---------------- Parametros del modo remoto con el ESP32 (de ha8, sin cambios) ----------------

CANAL_ESP32 = 1            # canal de Bluetooth (0 a 255) por el que emite el ESP32; debe ser el mismo en el ESP32
PERIODO_REMOTO_MS = 50     # cada cuanto se revisan los botones y el mensaje (el ESP32 emite cada 100 ms)
PERIODO_IMPRESION_MS = 300 # minimo entre dos lineas del slider (las ordenes de ACCIONAR se imprimen siempre)

# numero de articulacion que manda el ESP32 -> clave de puerto de ha7 (la garra, 3, se trata aparte)
ID_ARTICULACION = {0: "F", 1: "D", 2: "A"}
ID_GARRA = 3

# ---------------- Camara ----------------

app = AppData([(0, 4)])
COLOR = {"actual": "pelota"}
app.configure(0, 0, bytes([TONOS["pelota"] // 2]))


def leer_bytes():
    """Una lectura cruda de la camara: (x, y, width, height). (0,0,0,0) si no ve nada o no hay datos."""
    try:
        datos = app.get_bytes(0)
        if datos is None or len(datos) < 4:
            return (0, 0, 0, 0)
        return unpack("BBBB", datos)
    except Exception:
        return (0, 0, 0, 0)


def poner_color(nombre):
    """Cambia el color que sigue la camara ('pelota' o 'cubo'). Solo reconfigura si hace falta."""
    if COLOR["actual"] == nombre:
        return
    app.configure(0, 0, bytes([TONOS[nombre] // 2]))
    COLOR["actual"] = nombre
    wait(CAMBIO_COLOR_MS)


def ver(nombre, muestras=MUESTRAS_CAMARA):
    """Promedia varias lecturas (solo las que ven el objeto). Devuelve (x, y, width, height)."""
    poner_color(nombre)
    sx = sy = sw = sh = n = 0
    for _ in range(muestras):
        x, y, w, h = leer_bytes()
        if w > 0:
            sx += x
            sy += y
            sw += w
            sh += h
            n += 1
        wait(PERIODO_CAMARA_MS)
    if n == 0:
        return (0, 0, 0, 0)
    return (round(sx / n, 1), round(sy / n, 1), round(sw / n, 1), round(sh / n, 1))


def txt_cam(etiqueta, c):
    return "{} x={} y={} w={} h={}".format(etiqueta, c[0], c[1], c[2], c[3])


# ---------------- IMU del hub ----------------

def imu_valores():
    """(cabeceo, balanceo, rumbo) del hub en grados. El rumbo es el giro horizontal (el hub va sobre la base)."""
    try:
        pitch, roll = hub.imu.tilt()
    except Exception:
        pitch = roll = "-"
    try:
        rumbo = round(hub.imu.heading(), 1)
    except Exception:
        rumbo = "-"
    return pitch, roll, rumbo


def inclinacion():
    p, r, h = imu_valores()
    return "cabeceo {} deg | balanceo {} deg | rumbo {} deg".format(p, r, h)


def reiniciar_ceros():
    """El brazo esta en inicio: esa posicion es el nuevo 0 de todos los motores y del rumbo del hub."""
    for m in (base, codo, muneca, garra):
        m.reset_angle(0)
    try:
        hub.imu.reset_heading(0)
    except Exception:
        pass


# ---------------- Utilidades comunes (de ha6.py) ----------------

def detener_todo(incluir_garra=True):
    """Suelta los motores (stop = sin alimentacion)."""
    for m in (base, codo, muneca):
        m.stop()
    if incluir_garra:
        garra.stop()


def descanso(etiqueta):
    """Entre fases: todo suelto y espera a que la bateria se recupere."""
    v_antes = hub.battery.voltage()
    i_antes = hub.battery.current()
    detener_todo(SOLTAR_GARRA_CERRADA)
    print("-- Descanso {} ({} ms, motores sueltos) | antes: {} mV, {} mA".format(
        etiqueta, DESCANSO_FASES_MS, v_antes, i_antes))
    wait(DESCANSO_FASES_MS)
    print("   despues: {} mV, {} mA".format(hub.battery.voltage(), hub.battery.current()))


def a_articulacion(motor, mult):
    """Convierte los grados medidos por el motor a grados de la articulacion."""
    return round(motor.angle() / mult, 1)


def nombre_motor(motor):
    if motor is base:
        return "F base"
    if motor is codo:
        return "D codo"
    if motor is muneca:
        return "A muneca"
    return "B garra"


STATS = {"vmin": 99999, "vmin_en": "-", "imax": 0, "imax_en": "-", "pausas": 0}


def pausar(etapa, motor, v, i):
    """Voltaje bajo sostenido: SUELTA el motor activo y espera 'g' + Enter para continuar.
    Devuelve True si se continua, False si el usuario escribe 'x' (abortar)."""
    STATS["pausas"] += 1
    motor.stop()
    print("  !! VOLTAJE BAJO en {}: {} mV con {} mA (motor soltado)".format(etapa, v, i))
    while True:
        texto = input("  PAUSA. 'g' + Enter = continuar | 'x' = abortar: ").strip().lower()
        if texto == "g":
            print("  Continuando... bateria: {} mV, {} mA".format(
                hub.battery.voltage(), hub.battery.current()))
            return True
        if texto == "x":
            detener_todo()
            return False
        print("  Escribi 'g' para continuar o 'x' para abortar.")


def muestrear(st, etapa, motor):
    """Lee voltaje (mV) y corriente (mA) del hub y actualiza minimos/maximos.
    Devuelve 0 = normal | 1 = hubo pausa y el usuario continuo (g) | 2 = abortar (x)."""
    v = hub.battery.voltage()
    i = hub.battery.current()
    if v < st["vmin"]:
        st["vmin"] = v
    if i > st["imax"]:
        st["imax"] = i
    if v < STATS["vmin"]:
        STATS["vmin"] = v
        STATS["vmin_en"] = etapa
    if i > STATS["imax"]:
        STATS["imax"] = i
        STATS["imax_en"] = etapa
    if v < UMBRAL_AVISO_MV and not st["avisado"]:
        st["avisado"] = True
        print("  ! aviso {}: {} mV con {} mA".format(etapa, v, i))
    if v < UMBRAL_MV:
        st["bajos"] += 1
        if st["bajos"] >= MUESTRAS_CORTE:
            st["bajos"] = 0
            if pausar(etapa, motor, v, i):
                return 1
            return 2
    else:
        st["bajos"] = 0
    return 0


def mover(motor, objetivo, timeout_ms, mantener=False):
    """Mueve al angulo absoluto del MOTOR vigilando voltaje y corriente.
    Al terminar (llegada, timeout o aborto) el motor se SUELTA con stop(), salvo mantener=True (hold).
    Devuelve (ok, minimo_mV). ok=False solo si el usuario aborta ('x') durante una pausa."""
    etapa = nombre_motor(motor)
    st = {"vmin": hub.battery.voltage(), "imax": hub.battery.current(), "bajos": 0, "avisado": False}
    ok = True
    reloj = StopWatch()
    motor.run_target(VELOCIDAD, objetivo, wait=False)
    while not motor.done():
        r = muestrear(st, etapa, motor)
        if r == 2:
            ok = False
            break
        if r == 1:
            motor.run_target(VELOCIDAD, objetivo, wait=False)
            reloj = StopWatch()
            continue
        if reloj.time() > timeout_ms:
            print("  ! timeout en", etapa)
            break
        wait(PERIODO_MS)

    if mantener and ok:
        motor.hold()
    else:
        motor.stop()
    print("  mon {}: Vmin {} mV | Imax mov {} mA | {}".format(
        etapa, st["vmin"], st["imax"], "hold" if (mantener and ok) else "soltado"))
    if MOSTRAR_INCLINACION_POR_MOVIMIENTO:
        print("  inclinacion hub: " + inclinacion())
    return ok, st["vmin"]


def pedir_angulo(titulo, clave):
    """Pide el angulo de una articulacion hasta que este en rango. Devuelve None si escribe X."""
    motor, mult, vmin, vmax = ARTICULACIONES[clave]
    while True:
        texto = input("[{}] {} ({}) [{} a {}]: ".format(
            titulo, clave, NOMBRES[clave], vmin, vmax)).strip().lower()
        if texto == "x":
            return None
        try:
            valor = float(texto)
        except ValueError:
            print("Valor no valido, escribi un numero (o 'x' para salir).")
            continue
        if valor < vmin or valor > vmax:
            print("Fuera de rango [{} a {}].".format(vmin, vmax))
            continue
        return valor


def mover_articulaciones(angulos):
    """Mueve base -> codo -> muneca, UNO A LA VEZ, soltando cada uno al llegar."""
    for k in ORDEN:
        motor, mult, vmin, vmax = ARTICULACIONES[k]
        objetivo = int(angulos[k] * mult)
        ok, minimo = mover(motor, objetivo, TIMEOUT_ART_MS)
        print("{} -> {} deg articulacion (motor {} deg) | minimo: {} mV".format(
            k, a_articulacion(motor, mult), motor.angle(), minimo))
        if not ok:
            return False
    return True


def llevar_a_cero():
    """A -> D -> F -> garra, todos a 0 (posicion de calibracion), uno por uno.
    Devuelve False si el usuario aborta ('x') durante una pausa por voltaje."""
    for nombre, motor, timeout in SECUENCIA_INICIO:
        ok, minimo = mover(motor, 0, timeout)
        print("{} -> {} deg | minimo: {} mV".format(nombre, motor.angle(), minimo))
        if not ok:
            return False
    return True


# ---------------- Fases (de ha6.py) ----------------

def ejecutar_take(angulos):
    """Garra abre -> F -> D -> A -> garra cierra -> muneca a 0 -> codo a 0 (no arrastrar el objeto)."""
    ok, minimo = mover(garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS)
    print("Garra abierta | minimo:", minimo, "mV")
    if not ok:
        return False

    if not mover_articulaciones(angulos):
        return False

    ok, minimo = mover(garra, GARRA_CERRADA, TIMEOUT_GARRA_MS, mantener=not SOLTAR_GARRA_CERRADA)
    print("Garra cerrada | minimo:", minimo, "mV")
    if not ok:
        return False

    ok, minimo = mover(muneca, 0, TIMEOUT_ART_MS)
    print("A muneca -> 0 (retirada) | motor {} deg | minimo: {} mV".format(muneca.angle(), minimo))
    if not ok:
        return False

    ok, minimo = mover(codo, 0, TIMEOUT_ART_MS)
    print("D codo -> 0 (retirada) | motor {} deg | minimo: {} mV".format(codo.angle(), minimo))
    return ok


def ejecutar_left(angulos):
    """F -> D -> A -> garra abre (suelta el objeto)."""
    if not mover_articulaciones(angulos):
        return False

    ok, minimo = mover(garra, GARRA_ABIERTA, TIMEOUT_GARRA_MS)
    print("Garra abierta | minimo:", minimo, "mV")
    return ok


def ejecutar_inicio():
    """A -> D -> F -> garra, todos a 0 (tras una espera para alejarse del objeto)."""
    wait(ESPERA_INICIO_MS)
    return llevar_a_cero()


def ejecutar_secuencia(ang_take, ang_left):
    """TAKE -> descanso -> LEFT -> descanso -> INICIO. Devuelve True si completo todo."""
    ok = ejecutar_take(ang_take)
    if ok:
        print("Toma del objeto terminada.")
        descanso("TAKE -> LEFT")
        ok = ejecutar_left(ang_left)
    if ok:
        print("Objeto soltado.")
        descanso("LEFT -> INICIO")
        ok = ejecutar_inicio()
    return ok


# ---------------- Tablas de calibracion ----------------

def interpolar(tabla, valor):
    """tabla: filas (clave, codo, muneca). Interpola linealmente (se queda en los extremos fuera de rango)."""
    filas = sorted(tabla)
    if valor <= filas[0][0]:
        return filas[0][1], filas[0][2]
    if valor >= filas[-1][0]:
        return filas[-1][1], filas[-1][2]
    for i in range(1, len(filas)):
        k0, d0, a0 = filas[i - 1]
        k1, d1, a1 = filas[i]
        if valor <= k1:
            if k1 == k0:
                return d1, a1
            f = (valor - k0) / (k1 - k0)
            return d0 + (d1 - d0) * f, a0 + (a1 - a0) * f
    return filas[-1][1], filas[-1][2]


def limitar(clave, valor):
    vmin = ARTICULACIONES[clave][2]
    vmax = ARTICULACIONES[clave][3]
    return max(vmin, min(vmax, valor))


def armar_angulos(titulo, ref, tabla):
    """Base = angulo medido por la camara; codo y muneca = de la tabla (o por teclado si la tabla esta vacia).
    Devuelve el dict {F, D, A} o None si el usuario escribe 'x'."""
    angulos = {"F": limitar("F", ref["F"])}
    if len(tabla) >= 2:
        d, a = interpolar(tabla, ref["cam"][CLAVE_DISTANCIA])
        angulos["D"] = limitar("D", d)
        angulos["A"] = limitar("A", a)
        print("[{}] codo y muneca desde la tabla (clave {} = {}): D {} | A {}".format(
            titulo, CLAVE_DISTANCIA, ref["cam"][CLAVE_DISTANCIA],
            round(angulos["D"], 1), round(angulos["A"], 1)))
    else:
        print("[{}] tabla con menos de 2 filas -> ingresa codo y muneca a mano.".format(titulo))
        for k in ("D", "A"):
            valor = pedir_angulo(titulo, k)
            if valor is None:
                return None
            angulos[k] = valor
    return angulos


# ---------------- Calibracion manual ----------------

def txt_motores():
    """F/D/A = motor>articulacion (ya dividido por el multiplicador) | B = garra (motor)."""
    partes = []
    for k in ORDEN:
        motor, mult, vmin, vmax = ARTICULACIONES[k]
        partes.append("{} {}>{}".format(k, motor.angle(), a_articulacion(motor, mult)))
    partes.append("B {}".format(garra.angle()))
    return " | ".join(partes)


def leer_botones(acum):
    b = hub.buttons.pressed()
    if Button.LEFT in b and Button.RIGHT in b:
        acum["salir"] = True
    if Button.LEFT in b:
        acum["izq"] = True
    if Button.RIGHT in b:
        acum["der"] = True


def calibracion():
    print("=== CALIBRACION MANUAL ===")
    print("Los motores quedan SUELTOS: mueve el brazo a mano.")
    print("Formato de cada linea: F/D/A = motor>articulacion (grados ya divididos por el multiplicador) | B = garra (motor)")
    print("   | IMU = cabeceo balanceo rumbo | PELOTA y CUBO = x y width height (% de la imagen, 0 = no lo ve) | voltaje, corriente")
    print("Botones del hub: IZQUIERDO = guardar VISTA (camara)  |  DERECHO = guardar POSE (motores)")
    print("   Mantene el boton ~1 s hasta ver el mensaje. Ambos a la vez = salir.")
    print("Por cada punto: 1) brazo en POSE DE BUSQUEDA (todo en 0) con la pelota/cubo a la vista -> IZQUIERDO")
    print("                2) mueve el brazo a mano hasta agarrar la pelota (o quedar sobre el cubo) -> DERECHO")
    texto = input("Pone el brazo en la posicion inicial (todo en 0, garra cerrada) y Enter para fijar ese 0 (x = volver): ")
    if texto.strip().lower() == "x":
        return
    detener_todo()
    reiniciar_ceros()
    print("Ceros fijados. Camara: pelota tono {} | cubo tono {} (grados).".format(TONOS["pelota"], TONOS["cubo"]))

    vista = None
    n_vista = 0
    n_pose = 0
    previo = {"izq": False, "der": False}
    while True:
        acum = {"izq": False, "der": False, "salir": False}
        leer_botones(acum)
        pelota = ver("pelota")
        leer_botones(acum)
        cubo = ver("cubo")
        leer_botones(acum)
        p, r, h = imu_valores()
        print("{} | IMU {} {} {} | {} | {} | {} mV {} mA".format(
            txt_motores(), p, r, h, txt_cam("PELOTA", pelota), txt_cam("CUBO", cubo),
            hub.battery.voltage(), hub.battery.current()))
        # ventana corta para leer botones sin perder pulsaciones
        for _ in range(10):
            leer_botones(acum)
            wait(20)

        if acum["salir"]:
            break

        if acum["izq"] and not previo["izq"]:
            n_vista += 1
            vista = {"n": n_vista, "pelota": pelota, "cubo": cubo,
                     "F": a_articulacion(base, ARTICULACIONES["F"][1])}
            print(">>> VISTA #{} guardada | F base {} deg | {} | {} | IMU {} {} {}".format(
                n_vista, vista["F"], txt_cam("PELOTA", pelota), txt_cam("CUBO", cubo), p, r, h))

        if acum["der"] and not previo["der"]:
            n_pose += 1
            dd = a_articulacion(codo, ARTICULACIONES["D"][1])
            aa = a_articulacion(muneca, ARTICULACIONES["A"][1])
            ff = a_articulacion(base, ARTICULACIONES["F"][1])
            print(">>> POSE #{} | {} | IMU {} {} {}".format(n_pose, txt_motores(), p, r, h))
            if vista is None:
                print("    (no hay VISTA guardada: guarda una con el boton IZQUIERDO para tener la clave de camara)")
                kp = None
                kc = None
            else:
                print("    usa VISTA #{} | F base de la vista {} deg | {} | {}".format(
                    vista["n"], vista["F"], txt_cam("PELOTA", vista["pelota"]), txt_cam("CUBO", vista["cubo"])))
                kp = vista["pelota"][CLAVE_DISTANCIA]
                kc = vista["cubo"][CLAVE_DISTANCIA]
            print("    TABLA_TOMAR : ({}, {}, {}),   # pelota en la garra (clave {} de la vista)".format(
                kp, dd, aa, CLAVE_DISTANCIA))
            print("    TABLA_SOLTAR: ({}, {}, {}),   # garra sobre el cubo (clave {} de la vista)".format(
                kc, dd, aa, CLAVE_DISTANCIA))
            print("    (base F en esta pose: {} deg | garra: {} deg)".format(ff, garra.angle()))

        previo["izq"] = acum["izq"]
        previo["der"] = acum["der"]

    detener_todo()
    print("Calibracion terminada. Inclinacion hub: " + inclinacion())


# ---------------- Busqueda automatica con la camara ----------------

def buscar(nombre):
    """Barre la base desde 0 hacia BASE_BARRIDO_MAX hasta ver 'nombre' en la ventana x (X_MIN..X_MAX)
    con ancho suficiente. Frena la base, espera a que asiente y mide de nuevo.
    Devuelve (estado, ref): estado 'ok' | 'no' (no lo encontro) | 'abortar' (x tras voltaje bajo).
    ref = {"F": grados de articulacion de la base, "cam": (x, y, w, h), "imu": (cabeceo, balanceo, rumbo)}"""
    etapa = "barrido " + nombre
    print("Buscando {} (base 0 -> {} deg, motor a {} deg/s)...".format(nombre, BASE_BARRIDO_MAX, VELOCIDAD_BARRIDO))
    poner_color(nombre)
    mult = ARTICULACIONES["F"][1]
    limite_motor = BASE_BARRIDO_MAX * mult
    st = {"vmin": hub.battery.voltage(), "imax": hub.battery.current(), "bajos": 0, "avisado": False}
    seguidas = 0
    ultimo = (0, 0, 0, 0)
    estado = "no"
    base.run(VELOCIDAD_BARRIDO)
    while base.angle() < limite_motor:
        r = muestrear(st, etapa, base)
        if r == 2:
            estado = "abortar"
            break
        if r == 1:
            base.run(VELOCIDAD_BARRIDO)
            seguidas = 0
            continue
        x, y, w, h = leer_bytes()
        if w > ANCHO_MIN[nombre] and X_MIN <= x <= X_MAX:
            ultimo = (x, y, w, h)
            seguidas += 1
            if seguidas >= CONFIRMACIONES:
                estado = "ok"
                break
        else:
            seguidas = 0
        wait(PERIODO_CAMARA_MS)
    base.stop()
    print("  mon {}: Vmin {} mV | Imax mov {} mA | soltado".format(etapa, st["vmin"], st["imax"]))

    if estado != "ok":
        return estado, None

    wait(ESPERA_ASENTAR_MS)
    cam = ver(nombre)
    if cam[2] == 0:
        print("  (al asentar la base no lo ve; se usan los valores del instante de frenado)")
        cam = ultimo
    ref = {"F": a_articulacion(base, mult), "cam": cam, "imu": imu_valores()}
    print("{} encontrado: base F {} deg (motor {}) | {} | IMU {} {} {}".format(
        nombre.upper(), ref["F"], base.angle(), txt_cam("cam", cam), ref["imu"][0], ref["imu"][1], ref["imu"][2]))
    if not (X_MIN <= cam[0] <= X_MAX):
        print("  ! x={} quedo fuera de la ventana {}-{} tras asentar (la base se paso al frenar)".format(
            cam[0], X_MIN, X_MAX))
    return "ok", ref


# ---------------- Interfaz del modo automatico ----------------

def mostrar_resumen(ang_take, ang_left, ref_pelota, ref_cubo):
    print("--- Resumen ---")
    print("PELOTA vista en base {} deg | {}".format(ref_pelota["F"], txt_cam("cam", ref_pelota["cam"])))
    print("CUBO   visto  en base {} deg | {}".format(ref_cubo["F"], txt_cam("cam", ref_cubo["cam"])))
    print("TAKE: garra abre a", GARRA_ABIERTA, "al inicio, cierra a", GARRA_CERRADA,
          "y luego muneca y codo vuelven a 0")
    for k in ORDEN:
        mult = ARTICULACIONES[k][1]
        print("  T{} ({}): {} deg articulacion -> motor {} deg (x{})".format(
            k, NOMBRES[k], round(ang_take[k], 1), int(ang_take[k] * mult), mult))
    print("LEFT: traslado al cubo y la garra abre a", GARRA_ABIERTA, "al llegar")
    for k in ORDEN:
        mult = ARTICULACIONES[k][1]
        print("  L{} ({}): {} deg articulacion -> motor {} deg (x{})".format(
            k, NOMBRES[k], round(ang_left[k], 1), int(ang_left[k] * mult), mult))
    print("INICIO: vuelve a 0 (A muneca -> D codo -> F base -> B garra)")
    print("Cada motor se suelta al llegar. Descanso entre fases: {} ms".format(DESCANSO_FASES_MS))


def mostrar_monitoreo():
    if STATS["vmin_en"] != "-":
        print("=== Monitoreo (acumulado) ===")
        print("Voltaje minimo: {} mV en {}".format(STATS["vmin"], STATS["vmin_en"]))
        print("Corriente maxima: {} mA en {}".format(STATS["imax"], STATS["imax_en"]))
        print("Pausas por voltaje bajo: {}".format(STATS["pausas"]))
        print("Bateria: {} mV".format(hub.battery.voltage()))


def automatico():
    print("=== AUTOMATICO ===")
    print("Bateria en reposo: {} mV, {} mA".format(hub.battery.voltage(), hub.battery.current()))
    print("Inclinacion hub INICIAL: " + inclinacion())
    print("Camara del celular encendida? (hub conectado, icono del telefono activo)")

    print("Estado inicial: motores a 0 (muneca -> codo -> base -> garra)...")
    if not llevar_a_cero():
        print("Calibracion abortada por el usuario (x) tras voltaje bajo -> motores detenidos.")
        return
    reiniciar_ceros()
    print("Calibracion completa: todos los motores en 0.")

    texto = input("Enter = empezar la busqueda (x = volver al menu): ").strip().lower()
    if texto == "x":
        return

    # 1) Cubo cafe
    estado, ref_cubo = buscar("cubo")
    if estado == "abortar":
        detener_todo()
        print("Abortado (x) tras voltaje bajo -> motores detenidos.")
        return
    if estado == "no":
        print("No se vio el cubo cafe en el barrido. Revisa el tono del cubo (TONOS) y la ventana x.")
        mover(base, 0, TIMEOUT_ART_MS)
        return
    ok, minimo = mover(base, 0, TIMEOUT_ART_MS)   # vuelve a 0: desenreda el cable
    if not ok:
        detener_todo()
        return
    descanso("CUBO -> PELOTA")

    # 2) Pelota roja
    estado, ref_pelota = buscar("pelota")
    if estado == "abortar":
        detener_todo()
        print("Abortado (x) tras voltaje bajo -> motores detenidos.")
        return
    if estado == "no":
        print("No se vio la pelota roja en el barrido. Revisa el tono (TONOS) y la ventana x.")
        mover(base, 0, TIMEOUT_ART_MS)
        return

    # 3) Angulos de TAKE y LEFT
    ang_take = armar_angulos("TAKE", ref_pelota, TABLA_TOMAR)
    if ang_take is None:
        detener_todo()
        mover(base, 0, TIMEOUT_ART_MS)
        return
    ang_left = armar_angulos("LEFT", ref_cubo, TABLA_SOLTAR)
    if ang_left is None:
        detener_todo()
        mover(base, 0, TIMEOUT_ART_MS)
        return

    while True:
        mostrar_resumen(ang_take, ang_left, ref_pelota, ref_cubo)
        cmd = input("Y=iniciar | X=cancelar | TF/TD/TA o LF/LD/LA=reingresar: ").strip().lower()

        if cmd == "x":
            detener_todo()
            mover(base, 0, TIMEOUT_ART_MS)
            return
        elif cmd in ("tf", "td", "ta"):
            valor = pedir_angulo("TAKE", cmd[1].upper())
            if valor is None:
                detener_todo()
                mover(base, 0, TIMEOUT_ART_MS)
                return
            ang_take[cmd[1].upper()] = valor
        elif cmd in ("lf", "ld", "la"):
            valor = pedir_angulo("LEFT", cmd[1].upper())
            if valor is None:
                detener_todo()
                mover(base, 0, TIMEOUT_ART_MS)
                return
            ang_left[cmd[1].upper()] = valor
        elif cmd == "y":
            ok = ejecutar_secuencia(ang_take, ang_left)
            detener_todo()
            if ok:
                print("Brazo en posicion inicial. Secuencia completa.")
            else:
                print("Secuencia abortada por el usuario (x) tras voltaje bajo -> motores detenidos.")
                print("En el siguiente modo automatico los motores volveran a 0 (calibracion).")
            print("Inclinacion hub FINAL: " + inclinacion())
            mostrar_monitoreo()
            return
        else:
            print("Comando no valido.")


# ---------------- Modo remoto (ESP32): RECIBE Y MUEVE UNA ARTICULACION POR CADA ACCIONAR ----------------

def pantalla(caracter):
    """Muestra un caracter en la matriz de luces del hub (si falla, se ignora)."""
    try:
        hub.display.char(caracter)
    except Exception:
        pass


def letra_articulacion(articulacion):
    """Letra que se muestra en el hub: F, D, A, B | '-' ninguna | '?' numero desconocido."""
    if articulacion == -1:
        return "-"
    if articulacion == ID_GARRA:
        return "B"
    if articulacion in ID_ARTICULACION:
        return ID_ARTICULACION[articulacion]
    return "?"


def interpretar(datos):
    """datos = lo que entrego observe(). Devuelve (articulacion, angulo, id_orden) o None si el formato no es valido.
    Formato esperado: tupla de 3 enteros."""
    if not isinstance(datos, tuple) or len(datos) != 3:
        return None
    for v in datos:
        if not isinstance(v, int):
            return None
    return datos


def simular(articulacion, angulo):
    """Calcula SIN MOVER NADA a donde iria la articulacion con los mismos rangos de ARTICULACIONES.
    Devuelve un texto."""
    if articulacion == -1:
        return "ninguna articulacion activa"
    if articulacion == ID_GARRA:
        objetivo = max(GARRA_CERRADA, min(GARRA_ABIERTA, angulo))
        aviso = " (recortado a [{} a {}])".format(GARRA_CERRADA, GARRA_ABIERTA) if objetivo != angulo else ""
        return "B garra -> {} deg{} | ahora: motor {} deg".format(objetivo, aviso, garra.angle())
    clave = ID_ARTICULACION.get(articulacion)
    if clave is None:
        return "articulacion {} no existe (usa -1, 0, 1, 2 o 3)".format(articulacion)
    motor, mult, vmin, vmax = ARTICULACIONES[clave]
    objetivo = limitar(clave, angulo)
    aviso = " (recortado a [{} a {}])".format(vmin, vmax) if objetivo != angulo else ""
    return "{} {} -> {} deg articulacion{} = motor {} deg | ahora: {} deg articulacion".format(
        clave, NOMBRES[clave], objetivo, aviso, int(objetivo * mult), a_articulacion(motor, mult))


def ejecutar_orden(articulacion, angulo):
    """Mueve UNA articulacion al angulo pedido, recortado a sus limites (los de ha7), con mover():
    un solo motor energizado, vigila el voltaje y se SUELTA al llegar.
    Devuelve False si el usuario aborta ('x') durante una pausa por voltaje bajo."""
    if articulacion == ID_GARRA:
        objetivo = max(GARRA_CERRADA, min(GARRA_ABIERTA, angulo))
        mantener = (objetivo == GARRA_CERRADA) and not SOLTAR_GARRA_CERRADA
        ok, minimo = mover(garra, objetivo, TIMEOUT_GARRA_MS, mantener)
        print("B garra -> {} deg | motor {} deg | minimo: {} mV".format(objetivo, garra.angle(), minimo))
        return ok
    clave = ID_ARTICULACION.get(articulacion)
    if clave is None:
        print("  articulacion {} no existe: no se mueve nada".format(articulacion))
        return True
    motor, mult, vmin, vmax = ARTICULACIONES[clave]
    objetivo = limitar(clave, angulo)
    ok, minimo = mover(motor, int(objetivo * mult), TIMEOUT_ART_MS)
    print("{} {} -> {} deg articulacion (motor {} deg) | minimo: {} mV".format(
        clave, NOMBRES[clave], a_articulacion(motor, mult), motor.angle(), minimo))
    return ok


RADIO = {"obj": None}


def obtener_radio():
    """Crea el BLERadio UNA sola vez y lo reutiliza si se vuelve a entrar al modo R."""
    if RADIO["obj"] is None:
        RADIO["obj"] = BLERadio(observe_channels=[CANAL_ESP32])
    return RADIO["obj"]


def remoto():
    print("=== REMOTO (ESP32) === MUEVE el brazo: una articulacion por cada ACCIONAR")
    if BLERadio is None:
        print("Este firmware no tiene pybricks.messaging.BLERadio: actualiza Pybricks e intenta de nuevo.")
        return
    print("Bateria en reposo: {} mV, {} mA".format(hub.battery.voltage(), hub.battery.current()))
    print("Escucha el canal {}. Mensaje esperado: (articulacion, angulo, id_orden)".format(CANAL_ESP32))
    print("  articulacion: -1 ninguna | 0 F base | 1 D codo | 2 A muneca | 3 B garra")
    print("Salir: botones IZQUIERDO y DERECHO del hub a la vez (mantener ~1 s).")
    texto = input("Enter = llevar el brazo a 0 (muneca -> codo -> base -> garra) y ARMAR | x = volver: ").strip().lower()
    if texto == "x":
        return

    print("Estado inicial: motores a 0 (muneca -> codo -> base -> garra)...")
    if not llevar_a_cero():
        detener_todo()
        print("Abortado por el usuario (x) tras voltaje bajo -> motores detenidos.")
        return
    reiniciar_ceros()
    print("Ceros fijados. Modo remoto ARMADO: cada ACCIONAR mueve una articulacion.")

    radio = obtener_radio()
    ultimo = None       # ultimo mensaje ya procesado
    id_ref = None       # id_orden de referencia (cambia = orden nueva de ACCIONAR)
    con_senal = None    # None = sin estado | True | False
    n_rx = 0
    n_ordenes = 0       # ordenes ACCIONAR detectadas
    n_mov = 0           # ordenes ejecutadas (con articulacion valida)
    reloj = StopWatch()
    t_impreso = -PERIODO_IMPRESION_MS
    pantalla("?")
    try:
        while True:
            b = hub.buttons.pressed()
            if Button.LEFT in b and Button.RIGHT in b:
                break

            datos = radio.observe(CANAL_ESP32)
            if datos is None:
                # observe() entrega None si no llega nada hace mas de 1 segundo
                if con_senal is not False:
                    con_senal = False
                    ultimo = None   # al volver la senal se vuelve a mostrar el mensaje y la letra
                    print("[ESP32] sin senal (no llega nada hace mas de 1 s): no se mueve nada")
                    pantalla("?")
            else:
                if con_senal is False:
                    print("[ESP32] senal recuperada")
                con_senal = True
                if datos != ultimo:
                    msg = interpretar(datos)
                    if msg is None:
                        ultimo = datos
                        print("[ESP32] mensaje con formato no valido (se espera tupla de 3 enteros): {}".format(datos))
                    else:
                        articulacion, angulo, id_orden = msg
                        orden_nueva = id_ref is not None and id_orden != id_ref
                        ahora = reloj.time()
                        # las ordenes de ACCIONAR se procesan siempre; el slider se imprime como maximo cada PERIODO_IMPRESION_MS
                        if orden_nueva or ahora - t_impreso >= PERIODO_IMPRESION_MS:
                            ultimo = datos
                            t_impreso = ahora
                            n_rx += 1
                            marca = ""
                            if id_ref is None:
                                marca = " (id_orden de referencia)"
                            elif orden_nueva:
                                n_ordenes += 1
                                marca = " <<< ACCIONAR (orden nueva)"
                            id_ref = id_orden
                            pantalla(letra_articulacion(articulacion))
                            print("[ESP32 #{}] art={} ang={} id_orden={}{}".format(
                                n_rx, articulacion, angulo, id_orden, marca))
                            if not orden_nueva:
                                print("    si accionas: {} | {} mV".format(
                                    simular(articulacion, angulo), hub.battery.voltage()))
                            elif articulacion == -1:
                                print("    orden sin articulacion: no se mueve nada")
                            else:
                                print("    EJECUTANDO: {} | {} mV".format(
                                    simular(articulacion, angulo), hub.battery.voltage()))
                                n_mov += 1
                                ok = ejecutar_orden(articulacion, angulo)
                                if not ok:
                                    detener_todo()
                                    print("    TAREA ABORTADA (x): motores sueltos. El brazo sigue armado; manda otra orden.")
                                # las ordenes que llegaron durante el movimiento se descartan:
                                # el mensaje actual pasa a ser la nueva referencia
                                despues = radio.observe(CANAL_ESP32)
                                msg2 = interpretar(despues) if despues is not None else None
                                if msg2 is not None:
                                    if msg2[2] != id_orden:
                                        print("    (se descartaron ordenes recibidas durante el movimiento)")
                                    id_ref = msg2[2]
                                    ultimo = despues
                                    pantalla(letra_articulacion(msg2[0]))
                                t_impreso = reloj.time()
                                print("    motor suelto, esperando la siguiente orden")
            wait(PERIODO_REMOTO_MS)
    finally:
        detener_todo()
        pantalla("-")
    print("Remoto terminado. Mensajes mostrados: {} | ordenes ACCIONAR: {} | movimientos ejecutados: {}".format(
        n_rx, n_ordenes, n_mov))
    mostrar_monitoreo()


# --- Programa principal ---
# Limites opcionales (una sola vez)
for m in (base, codo, muneca, garra):
    if ACELERACION is not None:
        m.control.limits(acceleration=ACELERACION)
    if TORQUE_MAX is not None:
        m.control.limits(torque=TORQUE_MAX)

print("ha9 | puertos: F base | D codo | A muneca | B garra | C y E libres")
while True:
    print("===== MENU =====")
    print("Bateria en reposo: {} mV, {} mA | Inclinacion hub: {}".format(
        hub.battery.voltage(), hub.battery.current(), inclinacion()))
    cmd = input("C = calibracion manual | A = automatico | R = remoto (ESP32, MUEVE el brazo) | X = salir: ").strip().lower()
    if cmd == "c":
        calibracion()
    elif cmd == "a":
        automatico()
    elif cmd == "r":
        remoto()
    elif cmd == "x":
        break
    else:
        print("Comando no valido.")

detener_todo()
print("Inclinacion hub al salir: " + inclinacion())
mostrar_monitoreo()
print("Programa terminado.")
