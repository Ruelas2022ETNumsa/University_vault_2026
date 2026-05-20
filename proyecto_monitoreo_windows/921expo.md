# Guion de Exposición — ETN921
## Sección 7: Interfaz Web (Persona 2)
> Tono: semi-formal, explicativo. Mostrar código en diapositivas mientras se narra.

---

## Entrada

 *"Gracias [nombre]. Entonces ya sabemos cómo el sistema recolecta datos y los guarda. Ahora viene mi parte: cómo el usuario accede a toda esa información desde el navegador, y cómo el código lo hace posible."*
 *"La carpeta `web\` está organizada en tres bloques:"*
 
 - **Núcleo común** — funciones y estilos compartidos por toda la web. Sin lógica propia, solo utilidades.
 - **Componente 2 (GET)** — ping en tiempo real desde el navegador.
 - **Componente 3 (POST)** — reportes gráficos históricos consultando la base de datos.

*"Archivos por bloque:"*
> - **Núcleo común**: `enlaces.php`, `ping_helper.php`, `ping_web.bat`, `estilos.css`
> - **Componente 2 (GET)**: `index.php`, `ping_online.php`, `ping_manual.php`, `estado_enlaces.php`, `gestionar_enlaces.php`
> - **Componente 3 (POST)**: `reporte.php`, `comparar.php`

---

## BLOQUE 1 — Núcleo común

### 7.1 — enlaces.php

> *"Empezamos por el archivo más pequeño pero más importante del sistema: `enlaces.php`. No muestra nada al usuario. Su único trabajo es leer `enlaces.txt` y devolver la lista de dominios como un array PHP."*

> *"La función clave es `obtener_enlaces()`. Hace tres cosas en orden:"*

**Leer el archivo completo:**
```php
$lineas = file($archivo, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
```
> *"Lee el archivo en un array, una línea por posición, ignorando líneas vacías automáticamente."*

**Descartar comentarios:**
```php
if ($linea === '' || $linea[0] === '#') continue;
```
> *"Cualquier línea que empiece con `#` se ignora. Así el archivo de texto puede tener comentarios explicativos sin romper nada."*

**Filtrar la entrada:**
```php
$linea = preg_replace('/[^a-zA-Z0-9.\-]/', '', $linea);
```
> *"Solo pasan letras, números, puntos y guiones. Si alguien escribió algo raro en el archivo, acá se elimina antes de que llegue al resto del sistema."*

> *"Hay una segunda función: `obtener_enlaces_numerados()`, que devuelve la misma lista pero con claves del 1 al N en lugar de 0 al N-1. Eso es porque el Componente 2 recibe `?Equipo=1`, no `?Equipo=0`. Un detalle pequeño que evita un bug silencioso."*

> *"Todos los demás archivos PHP hacen `require_once 'enlaces.php'` al inicio. Nadie lee `enlaces.txt` directamente. Este archivo es la única fuente de verdad del sistema."*

---

### 7.2 — ping_helper.php + ping_web.bat

> *"El siguiente archivo del núcleo es `ping_helper.php`, y acá hay una decisión de diseño importante que viene de la especificación misma del proyecto."*

> *"se exigía esta cadena exacta:"*

```
Navegador → PHP → .bat → ping
```

> *"No era opcional. PHP no puede ejecutar el ping directamente. Tiene que llamar a un archivo `.bat`, y ese `.bat` llama al ping de Windows. Dos archivos para una sola tarea, pero así lo pide la arquitectura."*

**filtración antes de tocar el sistema operativo:**
```php
$destino_limpio = preg_replace('/[^a-zA-Z0-9.\-]/', '', $destino);
```
> *"Si no hacemos esto, alguien podría escribir `google.com & del C:\Windows` y el .bat lo ejecutaría literalmente. Esto lo previene."*

**Invocación del .bat:**
```php
$bat = __DIR__ . DIRECTORY_SEPARATOR . 'ping_web.bat';
$cmd = '"' . $bat . '" ' . escapeshellarg($destino_limpio) . ' 2>&1';
$salida = shell_exec($cmd);
```
> *"`shell_exec()` invoca un comando del sistema operativo y captura su salida como string. `escapeshellarg()` agrega comillas alrededor del argumento para que los espacios no rompan el comando."*

**Procesamiento de resultados en español e inglés:**
```php
preg_match_all('/(?:tiempo|time)\s*[=<]\s*(\d+(?:[.,]\d+)?)\s*ms/i', $salida, $matches)
```
> *"La salida del ping varía según el idioma de Windows. En español dice `tiempo=15ms`, en inglés dice `time=15ms`. Esta expresión regular acepta los dos formatos, y también acepta coma o punto como separador decimal. Un solo patrón cubre todos los casos."*

> *"Después de capturar todos los tiempos, se toma el máximo con `max($tiempos)`. Si no hubo ninguna respuesta, devuelve -1."*

**El ping_web.bat en sí es casi trivial:**
```bat
set "DESTINO=%~1"
ping -n 3 -w 5000 %DESTINO%
```
> *"Recibe el dominio como argumento `%~1` y ejecuta ping con 3 paquetes y 5 segundos de timeout. Nada más. "Toda la lectura y procesamiento de la salida la hace PHP, porque manejar texto en un .bat es mucho más frágil."*

---

### 7.3 — estilos.css

> *"El último del núcleo es el CSS. Lo importante son las variables:"*

```css
:root {
    --fondo:   #0a0f1a;
    --acento:  #00e5ff;
    --ok:      #10b981;
    --warn:    #f59e0b;
    --error:   #ef4444;
}
```
> *"Todo el tema visual está definido acá. El cian `#00e5ff` es el acento principal. Verde es OK, amarillo es Lento, rojo es error. Si mañana queremos cambiar el tema, tocamos estas 5 líneas y se actualiza todo el sistema."*

---

## BLOQUE 2 — Componente GET

### 7.4 — index.php

> *"La página principal. Lo primero que ve el usuario al entrar a `http://localhost/monitoreo/`. Tiene cuatro secciones en una sola pantalla: botones de ping, formulario de reporte, formulario de comparación, y tabla de estado actual."*

**Generación dinámica de botones:**
```php
$enlaces = obtener_enlaces();
foreach ($enlaces as $i => $e) {
    echo "<a href='ping_online.php?Equipo=" . ($i+1) . "' class='btn-enlace'>$e</a>";
}
```
> *"Llama a `obtener_enlaces()`, recorre la lista, y por cada dominio genera un botón con el link correspondiente. Si mañana hay 15 enlaces en el archivo, aparecen 15 botones. El HTML se adapta solo al contenido del archivo de texto."*

> *"El formulario de reporte usa `method='POST'` y apunta a `reporte.php`. El de comparación usa `method='GET'` y apunta a `comparar.php`. Cada uno al componente que le corresponde."*

---

### 7.5 — ping_online.php

> *"Este es el Componente 2 propiamente dicho. Recibe `?Equipo=N` por GET y ejecuta el ping."*

```php
$enlaces = obtener_enlaces_numerados();
$equipo  = isset($_GET['Equipo']) ? (int)$_GET['Equipo'] : 0;

if (!array_key_exists($equipo, $enlaces)) {
    header("Location: index.php");
    exit;
}

$destino = $enlaces[$equipo];
$ping    = hacer_ping($destino);
```
> *"Tres pasos: carga la lista numerada, lee el parámetro GET casteándolo a entero para evitar inyecciones de texto, y valida que el número exista en la lista. Si alguien escribe `?Equipo=999` y ese índice no existe, redirige al inicio en lugar de mostrar un error feo."*

**Renderizado del resultado:**
```php
<div class="rtt-badge">RTT Max: <?php echo htmlspecialchars($rtt_max); ?></div>
<pre><?php echo htmlspecialchars($resultado); ?></pre>
```
> *"La salida cruda del ping va dentro de un `<pre>` para preservar el formato. `htmlspecialchars()` en ambos lugares previene que caracteres especiales del resultado rompan el HTML."*

---

### 7.6 — ping_manual.php

> *"Variante del anterior. La diferencia es que en lugar de recibir un número de equipo, recibe directamente el dominio que el usuario escribió en el campo de texto."*

```php
$destino = preg_replace('/[^a-zA-Z0-9.\-]/', '', $direccion_raw);
```
> *"Misma sanitización que en el núcleo. Después llama a `hacer_ping()` igual que `ping_online.php`. La lógica compartida está en el núcleo para no repetirla en cada archivo."*

---

### 7.7 — estado_enlaces.php

> *"Este archivo no tiene página propia. Se incluye dentro de `index.php` con un `include`. Genera la tabla de estado al final de la página principal."*

**Consulta de última muestra por enlace:**
```php
$stmt = $conn->prepare(
    "SELECT fecha, hora, rtt_max FROM muestras
     WHERE enlace = ? ORDER BY fecha DESC, hora DESC LIMIT 1"
);
```
> *"Para cada enlace busca la última muestra ordenando por fecha y hora descendente y tomando solo la primera fila."*

**Clasificación del RTT:**
```php
if ($rtt < 0)        { $clase = "estado-error"; $texto = "Sin respuesta"; }
elseif ($rtt < 100)  { $clase = "estado-ok";    $texto = "OK"; }
elseif ($rtt < 300)  { $clase = "estado-warn";  $texto = "Lento"; }
else                 { $clase = "estado-error";  $texto = "Muy lento"; }
```
> *"Cuatro rangos. Menos de 100ms es OK, menos de 300ms es Lento, más de eso es Muy lento, y -1 es Sin respuesta. La clase CSS que se aplica cambia el color automáticamente usando las variables del núcleo."*

---

### 7.8 — gestionar_enlaces.php

> *"Permite agregar o quitar enlaces desde el navegador sin tocar ningún archivo a mano. Es el equivalente web de la Opción 8 del menú de consola."*

**Lógica de agregar:**
```php
if ($accion === 'agregar') {
    $nuevo = preg_replace('/[^a-zA-Z0-9.\-]/', '', trim($_POST['enlace']));
    if (!in_array($nuevo, $lista_actual)) {
        $lista_actual[] = $nuevo;
        guardar_lista($archivo, $lista_actual);
    }
}
```
> *"Sanitiza, verifica que no esté duplicado con `in_array()`, lo agrega al array y guarda."*

**Lógica de quitar:**
```php
if ($accion === 'quitar') {
    $nueva = array_values(array_filter($lista_actual, function($x) use ($a_quitar) {
        return $x !== $a_quitar;
    }));
    guardar_lista($archivo, $nueva);
}
```
> *"`array_filter()` recorre el array descartando el elemento que coincide con el que se quiere quitar. `guardar_lista()` reescribe el archivo completo con la lista actualizada."*

> *"El cambio es inmediato. En la próxima ejecución del Task Scheduler, el script de monitoreo ya lee la lista nueva. Sin reiniciar nada."*

---

## BLOQUE 3 — Componente POST

### 7.9 — reporte.php

> *"Acá está el corazón del proyecto en cuanto a base de datos. Recibe enlace, fecha y rango horario por POST, y devuelve estadísticas completas más un gráfico."*

**Consulta 1 — estadísticas con funciones de agregación:**
```sql
SELECT
    ROUND(AVG(rtt_max), 3)      AS promedio,
    ROUND(MAX(rtt_max), 3)      AS maximo,
    ROUND(MIN(rtt_max), 3)      AS minimo,
    COUNT(*)                     AS total_muestras,
    SUM(IF(rtt_max >= 0, 1, 0)) AS pings_exitosos,
    SUM(IF(rtt_max <  0, 1, 0)) AS pings_fallidos,
    ROUND(STDDEV(rtt_max), 3)   AS desviacion_std,
    CASE
        WHEN AVG(rtt_max) < 50  THEN 'Excelente'
        WHEN AVG(rtt_max) < 100 THEN 'Bueno'
        WHEN AVG(rtt_max) < 200 THEN 'Regular'
        ELSE 'Malo'
    END AS calidad
FROM muestras
WHERE enlace = ? AND fecha = ?
  AND hora BETWEEN ? AND ?
  AND rtt_max >= 0
```
> *"PHP no calcula nada de esto. Le pide a MySQL que calcule el promedio, el máximo, el mínimo, la desviación estándar, cuántos pings fueron exitosos y cuántos fallaron, y que clasifique la calidad del enlace con un `CASE WHEN`. MySQL devuelve una sola fila con todo ya calculado."*

> *"El `SUM(IF(rtt_max >= 0, 1, 0))` es un truco elegante: suma 1 cuando la condición es verdadera y 0 cuando es falsa, lo que equivale a contar solo las filas que cumplen esa condición."*

**Consulta 2 — datos para el gráfico:**
```sql
SELECT DATE_FORMAT(hora, '%H:%i') AS hora_fmt,
       ROUND(rtt_max, 3) AS rtt,
       IF(rtt_max < 0, 'Sin respuesta',
          IF(rtt_max < 100, 'OK',
             IF(rtt_max < 200, 'Lento', 'Muy lento')
          )
       ) AS estado
FROM muestras
WHERE enlace = ? AND fecha = ?
  AND hora BETWEEN ? AND ?
ORDER BY hora ASC
```
> *"`DATE_FORMAT()` convierte la hora al formato `HH:MM` para que las etiquetas del gráfico sean legibles. Los `IF()` anidados calculan el estado de cada muestra directamente en MySQL."*

**Inyección de datos en Chart.js:**
```php
$horas_json   = json_encode($horas_json_arr);
$valores_json = json_encode($valores_json_arr);
```
```javascript
labels: <?php echo $horas_json; ?>,
data:   <?php echo $valores_json; ?>,
```
> *"PHP inyecta los arrays directamente en el JavaScript como JSON. Chart.js los recibe y dibuja la línea. No hay AJAX ni llamadas adicionales al servidor. Todo llega en una sola respuesta."*

**Fix de compatibilidad PHP 7.1:**
```php
// PHP 8.0+ (no funciona en 7.1):
// match($calidad) { 'Excelente' => '#10b981', ... }

// Fix PHP 7.1:
switch ($calidad) {
    case 'Excelente': $calidad_color = '#10b981'; break;
    case 'Bueno':     $calidad_color = '#3b82f6'; break;
    case 'Regular':   $calidad_color = '#f59e0b'; break;
    case 'Malo':      $calidad_color = '#ef4444'; break;
    default:          $calidad_color = '#6b7280';
}
```
> *"`match()` existe recién desde PHP 8.0. El servidor corre PHP 7.1, así que tuvimos que reemplazarlo por `switch`. Si no lo cambiábamos, la página daba error de parseo y no cargaba nada."*

---

### 7.10 — comparar.php

> *"El último archivo. En lugar de analizar un enlace, compara todos al mismo tiempo."*

**Consulta con GROUP BY:**
```sql
SELECT enlace,
       ROUND(AVG(rtt_max), 2)    AS promedio,
       ROUND(MIN(rtt_max), 2)    AS minimo,
       ROUND(MAX(rtt_max), 2)    AS maximo,
       ROUND(STDDEV(rtt_max), 2) AS desviacion,
       COUNT(*)                   AS total,
       SUM(IF(rtt_max >= 0, 1, 0)) AS exitosos,
       CASE WHEN AVG(rtt_max) < 50  THEN 'Excelente'
            WHEN AVG(rtt_max) < 100 THEN 'Bueno'
            WHEN AVG(rtt_max) < 200 THEN 'Regular'
            ELSE 'Malo' END AS calidad
FROM muestras
WHERE fecha = ? AND hora BETWEEN ? AND ?
  AND rtt_max >= 0
GROUP BY enlace
HAVING COUNT(*) > 0
ORDER BY promedio ASC
```
> *"`GROUP BY enlace` agrupa todas las filas del mismo dominio y aplica las funciones de agregación a cada grupo por separado. `ORDER BY promedio ASC` ordena de más rápido a más lento. El `HAVING COUNT(*) > 0` descarta enlaces sin muestras en ese rango para no mostrar filas vacías."*

**Fix de compatibilidad PHP 7.1 — arrow functions:**
```php
// PHP 7.4+ (no funciona en 7.1):
// $borders = array_map(fn($c) => str_replace('0.85', '1', $c), $colores);

// Fix PHP 7.1:
$borders = array_map(function($c) {
    return str_replace('0.85', '1', $c);
}, $colores);
```
> *"Las arrow functions con `fn()` son PHP 7.4. En 7.1 hay que escribir la función anónima completa. Mismo resultado, sintaxis más larga."*

> *"Los datos van a dos gráficos de Chart.js: el diagrama de quesos donde el tamaño de cada sector es proporcional al promedio de RTT — más grande significa peor rendimiento — y el gráfico de barras horizontal para comparar visualmente. Debajo, la tabla de ranking con medallas para los tres primeros."*

---

## Transición a Resultados (Sección 9)

> *"Eso cubre todos los archivos de la carpeta web. Siete archivos PHP, un .bat, un CSS, y un .txt. Cada uno con una responsabilidad clara, todos leyendo la misma lista de enlaces, todos apuntando a la misma base de datos."*

> *"Ahora voy a mostrar el sistema corriendo con las capturas reales..."*

---

## Cierre — Conclusiones

> *"Para cerrar: los tres bloques que pedía la materia están implementados. El monitoreo automático con Task Scheduler. La consulta en tiempo real con GET siguiendo la cadena PHP → .bat → ping. Y los reportes históricos con POST usando funciones de agregación de MySQL."*

> *"Los problemas reales que resolvimos — la incompatibilidad de autenticación entre MySQL 8 y PHP 7.1, el parseo bilingüe del ping, los permisos de IIS, las funciones de PHP 8 que tuvimos que bajar a 7.1 — son exactamente lo que aparece cuando montás un sistema así en Windows en producción, no en un entorno de prueba limpio."*

> *"Eso es todo de mi parte. ¿Preguntas?"*


ARREGLOS:
CAMBIAR LA PALABRA SANITIZA POR FLITRAR
