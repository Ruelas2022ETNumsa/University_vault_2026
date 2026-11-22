# web_control.py (ESP32, MicroPython)
#
# Etapa 4 adelantada (prueba): el ESP32 crea su PROPIA red Wi-Fi y sirve una pagina web con
# botones para elegir articulacion, un slider de angulo y un boton ACCIONAR.
# Lo que se hace en la pagina se emite por Bluetooth (broadcast de Pybricks) al hub en el mismo
# formato de siempre: (articulacion, angulo, id_orden).
#   articulacion: -1 ninguna | 0 F base | 1 D codo | 2 A muneca | 3 B garra
#   id_orden: sube 1 cada vez que se toca ACCIONAR
#
# Con esto el hub puede estar en el modo R de ha8.py (solo muestra, NO mueve motores).
#
# Como usarlo:
#   1) Thonny (interprete MicroPython ESP32, COM6): abrir este archivo y ejecutarlo (F5).
#   2) La consola imprime el nombre de la red, la clave y la direccion de la pagina.
#   3) En el celular: Ajustes > Wi-Fi > conectarse a la red SSID con la clave CLAVE.
#      Si Android avisa "sin internet", elegir MANTENER la conexion.
#   4) Abrir en el navegador del celular  http://192.168.4.1  (con http, NO https).
# Para terminar: boton Stop de Thonny (detiene la emision).
#
# Requiere bleradio.py en /lib del ESP32.

import network
import socket
import bluetooth
from bleradio import BLERadio

SSID = "BRAZO_LEGO"
CLAVE = "brazo1234"      # minimo 8 caracteres (WPA2)
CANAL = 1                # debe ser igual a CANAL_ESP32 de ha8.py
PUERTO = 80

# limites por articulacion (los mismos de ARTICULACIONES de ha7/ha8; el hub tambien recorta)
LIMITES = {0: (0, 360), 1: (-120, 180), 2: (0, 190), 3: (0, 90)}
NOMBRES = {-1: "ninguna", 0: "F base", 1: "D codo", 2: "A muneca", 3: "B garra"}

PAGINA = b"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Brazo LEGO</title>
<style>
body{font-family:sans-serif;margin:0;padding:16px;background:#111;color:#eee}
h1{font-size:20px;margin:0 0 12px 0}
.fila{display:flex;gap:8px;margin-bottom:14px}
.fila button{flex:1;padding:16px 0;font-size:18px;border:2px solid #555;border-radius:10px;background:#222;color:#eee}
.fila button.on{background:#1565c0;border-color:#90caf9}
#sl{width:100%;height:48px}
#val{font-size:44px;text-align:center;margin:8px 0}
#go{width:100%;padding:26px 0;font-size:26px;border:none;border-radius:12px;background:#2e7d32;color:#fff}
#go:disabled{background:#333;color:#777}
#est{margin-top:14px;font-size:15px;color:#aaa;min-height:40px}
#cero{margin-top:18px;width:100%;padding:12px 0;font-size:14px;border:1px solid #555;border-radius:8px;background:#222;color:#aaa}
small{font-size:13px;color:#cfd8dc}
</style></head><body>
<h1>Brazo LEGO - control</h1>
<div class="fila" id="fila">
<button onclick="sel(-1)" id="b-1">Ninguna</button>
<button onclick="sel(0)" id="b0">F base<br><small id="v0">0 deg</small></button>
<button onclick="sel(1)" id="b1">D codo<br><small id="v1">0 deg</small></button>
<button onclick="sel(2)" id="b2">A muneca<br><small id="v2">0 deg</small></button>
<button onclick="sel(3)" id="b3">B garra<br><small id="v3">0 deg</small></button>
</div>
<input type="range" id="sl" min="0" max="0" value="0" disabled>
<div id="val">0 deg</div>
<button id="go" disabled onclick="enviar('go')">ACCIONAR</button>
<div id="est">Elige una articulacion.</div>
<button id="cero" onclick="cero()">Poner valores guardados en 0 (brazo en inicio)</button>
<script>
var LIM={0:[0,360],1:[-120,180],2:[0,190],3:[0,90]};
var art=-1, ultimo=0, pos={0:0,1:0,2:0,3:0};
var sl=document.getElementById('sl'), val=document.getElementById('val');
var est=document.getElementById('est'), go=document.getElementById('go');
function enviar(ruta){
  fetch('/'+ruta+'?a='+art+'&v='+sl.value)
    .then(function(r){return r.text();})
    .then(function(t){est.textContent=t; if(ruta=='go'){cargar();}})
    .catch(function(){est.textContent='Sin conexion con el ESP32';});
}
function sel(n){
  art=n;
  for(var i=-1;i<=3;i++){document.getElementById('b'+i).className=(i==n)?'on':'';}
  if(n<0){sl.disabled=true;go.disabled=true;sl.min=0;sl.max=0;sl.value=0;}
  else{sl.disabled=false;go.disabled=false;sl.min=LIM[n][0];sl.max=LIM[n][1];sl.value=pos[n];}
  val.textContent=sl.value+' deg';
  enviar('s');
}
sl.oninput=function(){
  val.textContent=sl.value+' deg';
  var t=Date.now();
  if(t-ultimo>150){ultimo=t;enviar('s');}
};
sl.onchange=function(){enviar('s');};
function pintar(){
  for(var i=0;i<4;i++){document.getElementById('v'+i).textContent=pos[i]+' deg';}
}
function cargar(){
  fetch('/pos').then(function(r){return r.text();}).then(function(t){
    var a=t.split(',');
    for(var i=0;i<4;i++){pos[i]=parseInt(a[i]);}
    pintar();
    if(art>=0){sl.value=pos[art];val.textContent=sl.value+' deg';}
  }).catch(function(){});
}
function cero(){
  if(!confirm('Poner en 0 los valores guardados? Usalo solo si el brazo esta en inicio.')){return;}
  fetch('/cero').then(function(){cargar();});
}
cargar();
</script></body></html>
"""

estado = {"art": -1, "ang": 0, "id": 0, "pos": {0: 0, 1: 0, 2: 0, 3: 0}}

# --- Wi-Fi propio (punto de acceso) ---
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, password=CLAVE, authmode=network.AUTH_WPA2_PSK)

# --- Bluetooth: se pasa un BLE propio para que BLERadio NO deje un escaneo continuo
#     (el escaneo constante podria estorbar al Wi-Fi). Solo se necesita emitir.
ble = bluetooth.BLE()
ble.active(True)
radio = BLERadio(broadcast_channel=CANAL, ble=ble)


def emitir():
    radio.broadcast((estado["art"], estado["ang"], estado["id"]))


def responder(cl, cuerpo, tipo=b"text/plain"):
    cl.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: " + tipo +
               b"; charset=utf-8\r\nConnection: close\r\nCache-Control: no-store\r\n\r\n" + cuerpo)


def parametros(query):
    d = {}
    for par in query.split("&"):
        if "=" in par:
            k, v = par.split("=", 1)
            d[k] = v
    return d


def posiciones():
    """Ultimo angulo ORDENADO (accionado) de cada articulacion: 'f,d,a,b'. No es lectura del motor."""
    return ",".join(str(estado["pos"][i]) for i in range(4))


def atender(cl):
    peticion = cl.recv(1024)
    if not peticion:
        return
    linea = peticion.split(b"\r\n")[0].decode()
    partes = linea.split(" ")
    if len(partes) < 2:
        return
    ruta, _, query = partes[1].partition("?")

    if ruta == "/":
        responder(cl, PAGINA, b"text/html")
    elif ruta in ("/s", "/go"):
        p = parametros(query)
        try:
            art = int(p.get("a", "-1"))
            ang = int(float(p.get("v", "0")))
        except ValueError:
            art = -1
            ang = 0
        if art not in LIMITES:
            art = -1
            ang = 0
        else:
            ang = max(LIMITES[art][0], min(LIMITES[art][1], ang))
        cambio_art = art != estado["art"]
        estado["art"] = art
        estado["ang"] = ang
        if ruta == "/go":
            if art == -1:
                responder(cl, b"Elige una articulacion antes de accionar.")
                return
            estado["id"] += 1
            estado["pos"][art] = ang
            print("ACCIONAR orden #{} -> {} {} deg".format(estado["id"], NOMBRES[art], ang))
            texto = "Orden #{} enviada: {} {} deg".format(estado["id"], NOMBRES[art], ang)
        else:
            if cambio_art:
                print("Articulacion activa:", NOMBRES[art])
            texto = "Listo: {} {} deg (falta ACCIONAR)".format(NOMBRES[art], ang)
        emitir()
        responder(cl, texto.encode())
    elif ruta == "/pos":
        responder(cl, posiciones().encode())
    elif ruta == "/cero":
        for k in estado["pos"]:
            estado["pos"][k] = 0
        print("Valores guardados de la pagina puestos en 0")
        responder(cl, posiciones().encode())
    else:
        cl.sendall(b"HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n")


srv = socket.socket()
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("0.0.0.0", PUERTO))
srv.listen(3)
srv.settimeout(1)

emitir()   # el hub recibe ya la referencia de id_orden (articulacion -1 = no mueve nada)
print("Red Wi-Fi:", SSID, "| clave:", CLAVE)
print("Pagina: http://{}  (en el celular, con http)".format(ap.ifconfig()[0]))
print("Emitiendo al hub por Bluetooth en el canal", CANAL, "- para terminar usa Stop de Thonny")

try:
    while True:
        try:
            cl, _ = srv.accept()
        except OSError:
            continue   # timeout de 1 s: sigue esperando
        try:
            cl.settimeout(2)
            atender(cl)
        except Exception as e:
            print("Error en peticion:", e)
        finally:
            cl.close()
finally:
    radio.broadcast(None)
    srv.close()
    print("Servidor detenido")
