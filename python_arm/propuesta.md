# Propuesta: brazo que recoge una pelota roja por cámara (coordenadas x, y, z)

Fecha: 8-nov-2026. Estado: **en discusión, nada implementado todavía**.
Base de código: `mejor.py` (copia de `ha5.py`, hecha por el usuario).

## 1. Objetivo

Que el brazo (hub LEGO Inventor 51515 con Pybricks) recoja una pelota roja y la deje en un recipiente.
- La pelota está quieta; en algún momento puede estar elevada.
- Se ingresan o detectan **coordenadas (x, y, z) en cm**, no ángulos. Internamente se calculan los ángulos y solo estos se envían al hub, como en el programa actual.
- Todo con software gratuito en lo posible.

## 2. Geometría real del brazo (corregida en esta sesión)

Los nombres de los motores en el código no coinciden con su función mecánica.

| Puerto | Nombre en el código | Función real |
| ------ | ------------------- | ------------ |
| A | hombro | **base giratoria**: gira todo el brazo sobre el plano horizontal (360° posibles, pero se limita por el cable USB) |
| D | codo | articulación que levanta el brazo (de una altura 0 a unos 120°, según el usuario) |
| C | muñeca | segundo eslabón, sirve para alcanzar el objeto |
| E | garra | abre y cierra |
| F | sensor de color | sin uso por ahora |
| B | vacío | libre |

Consecuencia: el espacio alcanzable es una **dona** y x, y, z sí se pueden ingresar.

**Ejes:** x = izquierda-derecha, y = frente-atrás, z = altura.
**Origen:** en la mesa, justo debajo del eje de la base. Un objeto sobre la mesa tiene z≈0.

## 3. Cinemática inversa (plan)

1. Base (A): `θ = atan2(x, y)` (frente = y positivo = θ 0).
2. Alcance horizontal: `r = √(x² + y²)`.
3. Con `r` y `z` se resuelve el brazo plano de dos eslabones (D y C) con la ley de cosenos.
4. Se envían al hub los 3 ángulos, con los multiplicadores y rangos actuales.

Decisiones pendientes:
- **Cable USB:** elegir dónde queda θ=0 dentro del rango de A (hoy 0–270) para alcanzar ambos lados sin enrollar el cable.
- **Dos soluciones** (codo arriba o abajo): elegir una fija.
- **Rango de D:** el usuario dice 0 a ~120°, el código tiene -180 a 45. Aclarar antes de escribir.
- **Orientación de la garra** al agarrar (hacia abajo, horizontal o según el punto) y qué hace exactamente la muñeca (flexiona o gira).
- Aproximación al objeto: pasar por un punto por encima antes de bajar.

### Medidas pendientes (en cm)

1. **H:** altura del eje de D sobre la mesa.
2. **d0:** desplazamiento horizontal entre el eje de la base y el eje de D (puede ser 0).
3. **L1:** eje de D al eje de C.
4. **L2:** eje de C a la punta de la garra (donde agarra).
5. **Pose de cero** de D y C tras `llevar_a_cero()` y hacia dónde crece cada ángulo.
6. **Rangos reales** de D y C sin chocar.
7. Diámetro de la pelota.

## 4. Flujo con cámara (opción a elegida)

1. Cámara fija (celular en trípode con app tipo IP Webcam, o webcam), mirando la mesa. Foto con el brazo en INICIO para que no tape la pelota.
2. **Calibración una vez:** 4 marcas en las esquinas de la zona de trabajo, medidas con regla desde el origen. Pueden ser puntos de color o marcadores ArUco (OpenCV). La grilla de ~5 cm sirve de ayuda visual y de verificación. Si la cámara se mueve, recalibrar.
3. **Enter:** la PC captura varios fotogramas y los promedia.
4. **Detección:** segmentación del rojo en HSV, filtro de contornos por tamaño y centro de la pelota → píxel.
5. **Conversión:** homografía píxel → cm (`getPerspectiveTransform` / `findHomography`) → (x, y).
6. **Cálculo:** cinemática inversa → ángulos.
7. **Envío** de los ángulos al hub; `mejor.py` ejecuta TAKE y LEFT.
8. **Destino:** el recipiente o base de LEGO tiene coordenadas fijas conocidas (puede estar suspendido); no necesita visión.

## 5. Riesgos y cómo tratarlos

- **Pelota elevada:** la homografía solo vale para el plano calibrado; una pelota más alta aparece desplazada. Opciones: (1) empezar con z conocida (pelota sobre la base café); (2) ingresar z a mano; (3) estimar la distancia por el tamaño aparente de la pelota (requiere diámetro real, precisión moderada); (4) segunda cámara de costado. Recomendación: empezar con z fija y dejar lo elevado para la segunda etapa.
- **Rojo contra base café:** puede confundirse en HSV según la luz. Probar con la iluminación real, saturación alta, evitar sombras.
- **Precisión:** sin sensores en el brazo se espera 1–2 cm (desvíos de 2–4° al soltar motores y holgura de engranajes). Mitigación: calibrar con puntos conocidos y, si hace falta, una segunda foto tras el primer intento.
- **Calibración de la cámara:** en proyectos similares es la parte difícil y la que causa pick-and-place poco fiable.

## 6. Comunicación PC → hub

- Pybricks permite que el hub lea datos por `stdin`/`stdout` y que un script en la PC los envíe. El tutorial oficial usa Bluetooth con la librería `bleak`; `pybricksdev` también sirve y automatiza la carga del programa.
- El hub quedaría con un programa tipo `mejor.py` que, en lugar de `input()`, recibe los ángulos de la PC.
- **Por verificar:** si el envío funciona de forma estable por USB con este hub. Camino documentado: Bluetooth, dejando el USB para la alimentación.

## 7. Cámara de Pybricks (aclaración)

- Pybricks no tiene un sensor-cámara físico. Tiene una función **beta de "smart sensors"** que usa la cámara de un teléfono mediante la app de Pybricks y entrega valores al hub.
- **No se confirmó** si entrega la posición (x, y) de un objeto; el ejemplo revisado usa color. Es beta y corre en el teléfono, con poca personalización.
- Por eso se eligió visión en la PC con OpenCV (gratis y personalizable).

## 8. Software (todo gratuito)

Python, OpenCV, NumPy, pybricksdev y/o bleak, Pybricks (firmware y Pybricks Code), app de celular tipo IP Webcam (si se usa celular).

## 9. Orden de trabajo

1. Medir el brazo y armar la cinemática inversa; mover por coordenadas escritas a mano en `mejor.py`.
2. Cámara: detectar la pelota y calibrar píxel → cm.
3. Comunicación PC ↔ hub (verificar USB/Bluetooth).
4. Unir todo con el Enter y probar.
5. Pelota elevada (z).
6. Mejoras: corrección con segunda foto, límites de seguridad.

## 10. Preguntas abiertas

- Las 7 medidas de la sección 3 y la pose de cero.
- ¿Celular o webcam? ¿Fija sobre la mesa o en trípode?
- ¿La pelota elevada estará siempre sobre una base de altura conocida?
- Rango real de D (0–120° vs -180 a 45°).
- Dónde queda el "frente" (θ=0) respecto al cable y la mesa.

## 11. Antecedentes consultados

- Homografía imagen → mesa con 4 puntos y cinemática inversa: https://github.com/nildo/organizer-baxter
- Pelota roja sobre un plano y homografía: https://www.github.com/nickoala/openrv
- Detección roja por HSV y filtro por tamaño: https://annguyen9461.github.io/poolinator
- Celular como cámara + OpenCV + brazo: https://github.com/roboSobia/Shell-Game
- Dificultad de calibración (pick-and-place poco fiable): https://github.com/dkusznir/baxter_shuffle
- Comunicación hub ↔ PC en Pybricks: https://pybricks.com/projects/tutorials/wireless/hub-to-device/pc-communication/
- Proyectos Pybricks (brazo SPIKE con cámara): https://pybricks.com/project/python/
- Distancia con tamaño conocido: https://kiwix.lema.org/stackoverflow.com_en_all_2023-11/questions/44322897/opencv-calculate-distance-from-object-with-known-size
