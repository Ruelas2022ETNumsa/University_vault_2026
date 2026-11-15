# Pendientes del brazo: visión con OpenCV y toma de la pelota

Fecha: 13-nov-2026. Hanói queda para una segunda etapa. El foco ahora es **OpenCV + control del brazo** para que tome una pelota roja pequeña.

Relacionados: `ha6.py` (programa actual), `resumen_13_nov.md` (cableado y roles), `resumen_8_nov.md` y `propuesta.md` (coordenadas y cámara), `referencia.md` (proyectos y papers).

---

## 1. Punto de partida

- Brazo LEGO ya armado: base giratoria (F), hombro (D), muñeca rotacional (A) y garra (B). 4 motores, hub Inventor 51515 con Pybricks.
- `ha6.py` funciona y el cableado está bien.
- OpenCV disponible en la PC.

## 2. Costo estimado

| Concepto | Costo |
| -------- | ----- |
| Brazo, motores y hub | Ya lo tienes |
| Python, OpenCV, `pybricksdev` / `bleak` | Gratis |
| Cámara (celular o webcam que ya tengas) | Gratis |
| Webcam básica, si hace falta comprar | Pocas decenas de dólares (verificar precio local) |
| Soporte fijo para la cámara, marcas de calibración, pelota roja | Mínimo |
| API de un modelo de IA | **No hace falta** para ver y tomar la pelota. Solo si se agrega un agente con voz o texto; se paga por uso (revisar precios del proveedor) |

## 3. Pendientes, en orden

- [ ] **1. Comprobar el alcance real del brazo.** Con base giratoria, hombro y una muñeca que solo rota, puede que en el plano vertical haya un solo eslabón articulado. Entonces el brazo alcanza un radio por cada altura, no cualquier punto (x, y). Medirlo con el brazo y una regla antes de calibrar nada, porque puede cambiar el diseño.
- [ ] **2. Medir la geometría:** altura de la base, longitud de los eslabones, posición de cero de cada articulación, sentido de giro de cada motor y rangos reales (hombro -120 a 180, base 0-270, muñeca 0-190).
- [ ] **3. Cinemática inversa:** base con `atan2(x, y)` y hombro según la distancia al objeto, según lo que permita el punto 1.
- [ ] **4. Calibración cámara → mesa:** cámara fija, 4 marcas medidas con regla y homografía de OpenCV (píxeles → cm). Probar con puntos conocidos y corregir desvíos.
- [ ] **5. Detección de la pelota:** segmentación HSV y centroide. El rojo necesita dos rangos de color y es sensible a la luz, así que conviene iluminar siempre igual. Probar el contraste de la pelota contra la mesa.
- [ ] **6. Garra y pelota:** medir el diámetro de la pelota contra la apertura de la garra (`GARRA_ABIERTA = 90`), comprobar que la sujeta sin que ruede o resbale y probablemente poner `SOLTAR_GARRA_CERRADA = False` para que quede en hold durante el traslado.
- [ ] **7. Comunicación PC → hub:** sin verificar todavía. Opciones: Bluetooth con `bleak` / `pybricksdev` o stdin/stdout del hub. Mientras tanto, primera etapa manual: la PC calcula y muestra los ángulos, y se escriben en `ha6.py`.
- [ ] **8. Verificación con la cámara:** tras cada movimiento, comprobar dónde quedó la pelota o el brazo y corregir. Compensa los desvíos de unos pocos grados al soltar los motores.

## 4. Pendientes heredados de los resúmenes

- Rango del hombro (D) real contra lo declarado (-120 a 180) y si volver a 0 tras tomar el objeto es seguro.
- Rango y multiplicador de la muñeca (diseño no final y rotacional).
- Definir dónde queda el frente (θ = 0) respecto al cable USB y no forzar los 360° de la base.
- Orientación de la garra al agarrar.
- Decidir celular o webcam.

## 5. Etapas siguientes (después de la pelota)

1. Pelota automática: ver, calcular, tomar y soltar en un recipiente de posición fija.
2. Agente con herramientas (`mover`, `abrir_garra`, `cerrar_garra`, `ir_a_inicio`, `detectar_pelota`, `tomar_objeto`), primero por texto y luego con voz. El agente decide y el código valida rangos y voltaje antes de mover.
3. Torre de Hanói (2-3 discos): la lista de jugadas sale de una recursión exacta; la cámara verifica el estado. Riesgo principal: la precisión al soltar los discos.

## 6. Primer paso propuesto

Medir el alcance real del brazo (pendiente 1). Se puede preparar un script corto para mover cada articulación a posiciones conocidas y registrar dónde llega la garra.
