# Guion de Exposición — ETN921
## Sistema de Monitoreo de Enlaces TCP/IP en Windows

<!--
IMÁGENES POR SECCIÓN — PERSONA 1 (Backend):

* Figura 9.1  → Arranque de servicios MySQL e IIS
* Figura 9.2  → Verificación de versiones MySQL y PHP
* Figura 9.3  → Menú principal (menu.bat)
* Figura 9.4  → Fix de autenticación MySQL 8 + PHP 7.1
* Figura 9.5  → Creación de la base de datos
* Figura 9.6  → Instalación de la interfaz web en IIS
* Figura 9.7  → Creación de tareas en Task Scheduler
* Figura 9.8  → Tareas registradas en el Programador de Tareas
* Figura 9.9  → Archivo muestras_temp.txt generado automáticamente

IMÁGENES POR SECCIÓN — PERSONA 2 (Frontend):
* `index.php`             → Figura 9.10
* `ping_online.php`       → Figura 9.11
* `estado_enlaces.php`    → Figura 9.12
* `gestionar_enlaces.php` → Figura 9.13
* Formulario reporte      → Figura 9.14
* `reporte.php` resultado → Figura 9.15 y 9.16
* `comparar.php` resultado → Figura 9.17
-->

---

# PERSONA 1 — Backend

## Introducción

*"El proyecto es un sistema que monitorea automáticamente 10 enlaces de red en Windows. Mi parte cubre todo lo que ocurre por debajo: cómo se recolectan los datos, cómo se guardan, y cómo se administra el sistema."*

*"El sistema tiene tres componentes de backend:"*

- **menu.bat** — consola de administración central
- **tomar_muestra.bat + cargar_bd.bat** — monitoreo automático vía Task Scheduler
- **Base de datos MySQL** — almacenamiento persistente de muestras

---

## 1. menu.bat — Consola de administración

Centraliza todas las operaciones del sistema. Debe ejecutarse como administrador.

```bat
set "DB_USER=root"
set "DB_PASS=..."
set "MYSQL_BIN=C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
set "WEB_DEST=C:\inetpub\wwwroot\monitoreo"
```

*"Las variables globales definen rutas y credenciales una sola vez. El resto del script las usa sin repetir valores."*

**Opciones principales:**

- **Opción 2** — Crea/elimina las tareas en el Task Scheduler
- **Opción 3** — Gestiona la base de datos (crear, vaciar, fix de auth)
- **Opción 4** — Copia los archivos PHP a IIS y aplica permisos
- **Opción 8** — Agrega o quita enlaces monitoreados

**Creación de tareas programadas:**

```bat
schtasks /Create /SC MINUTE /MO 5 /TN "MonitoreoRed_Muestra" /TR "tomar_muestra.bat" /F
schtasks /Create /SC HOURLY  /TN "MonitoreoRed_Carga"   /TR "cargar_bd.bat"      /F
```

*"/SC MINUTE /MO 5 = cada 5 minutos. /SC HOURLY = cada hora. /F fuerza el reemplazo si ya existe."*

**Instalación web — permisos IIS:**

```bat
xcopy /Y /E "%DIR%\web\*" "%WEB_DEST%\"
icacls "%WEB_DEST%" /grant "IIS_IUSRS:(OI)(CI)RX" /T
icacls "%WEB_DEST%\reportWEB" /grant "IIS_IUSRS:(OI)(CI)M" /T
```

*"IIS_IUSRS es el usuario virtual de IIS. RX = leer y ejecutar. M = modificar, necesario para que los .bat puedan escribir archivos."*

---

## 2. tomar_muestra.bat — Recolección cada 5 minutos

Invocado automáticamente por el Task Scheduler. Hace ping a cada enlace y guarda el resultado.

**Fecha y hora con PowerShell** (más confiable que `wmic`, ya deprecado):

```bat
for /f "delims=" %%D in ('powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd'"') do set "FECHA=%%D"
```

**Ping con Test-Connection:**

```bat
powershell -Command "try {
    $r = Test-Connection -ComputerName '%%E' -Count 5 -ErrorAction Stop;
    ($r | Measure-Object -Property ResponseTime -Maximum).Maximum
} catch { -1 }" > "_rtt_tmp.txt"
```

*"Envía 5 paquetes ICMP y devuelve el máximo. Si el host no responde, la excepción devuelve -1. El resultado se captura en un archivo temporal en lugar de usar pipes anidados, que son más frágiles entre cmd y PowerShell."*

**Salida al archivo de muestras:**

```bat
echo !FECHA!^|!HORA!^|%%E^|!RTT_MAX!>> muestras_temp.txt
```

Formato: `FECHA|HORA|ENLACE|RTT_MAX` — exactamente lo que espera `cargar_bd.bat`.

---

## 3. cargar_bd.bat — Carga a MySQL cada hora

Lee `muestras_temp.txt` e inserta cada línea en la base de datos.

```bat
for /f "usebackq tokens=1,2,3,4 delims=|" %%A in ("%ARCHIVO_TXT%") do (
    mysql -u root -p... monitoreo_red -e
    "INSERT INTO muestras (enlace, fecha, hora, rtt_max)
     VALUES ('%%C', '%%A', '%%B', '%%D');"
)
```

*"El for /f parte cada línea por el delimitador | y asigna las 4 partes a %%A %%B %%C %%D. Un INSERT por línea."*

**Rotación del archivo:**

```bat
type "%ARCHIVO_TXT%" >> muestras_procesadas.txt
type nul > "%ARCHIVO_TXT%"
```

*"Anexa al histórico permanente y deja el temporal vacío para la próxima ronda."*

---

## 4. Base de datos — crear_bd.sql

```sql
CREATE TABLE IF NOT EXISTS muestras (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    enlace  VARCHAR(100) NOT NULL,
    fecha   DATE         NOT NULL,
    hora    TIME         NOT NULL,
    rtt_max FLOAT        NOT NULL,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

ALTER TABLE muestras ADD INDEX idx_enlace_fecha (enlace, fecha);
```

*"rtt_max usa FLOAT y -1 para sin respuesta en vez de NULL, para que siempre sea comparable numéricamente. El índice compuesto en (enlace, fecha) acelera las consultas de los reportes, que siempre filtran por esos dos campos."*

**Fix de autenticación MySQL 8 + PHP 7.1:**

```sql
ALTER USER 'root'@'localhost'
IDENTIFIED WITH mysql_native_password BY '...';
FLUSH PRIVILEGES;
```

*"MySQL 8 cambió el plugin de autenticación por defecto a caching_sha2_password, que PHP 7.1 no entiende. Sin este fix, la web no puede conectar a la base de datos."*

---

## Transición

*"Eso es el backend: los datos se recolectan solos cada 5 minutos, se persisten cada hora, y todo se administra desde un solo menú. Ahora [nombre] explica cómo el usuario accede a esa información desde el navegador."*

---
---

# PERSONA 2 — Frontend

## Entrada

*"Mi parte cubre cómo el usuario accede al sistema desde el navegador. La carpeta `web\` está organizada en tres bloques:"*

- **Núcleo común** — funciones y estilos compartidos por toda la web. Sin lógica propia, solo utilidades.
- **Componente 2 (GET)** — ping en tiempo real desde el navegador.
- **Componente 3 (POST)** — reportes gráficos históricos consultando la base de datos.

---

## BLOQUE 1 — Núcleo común

### enlaces.php
Única fuente de verdad sobre qué dominios se monitorean. Lee `enlaces.txt`, ignora comentarios (`#`) y sanitiza la entrada. Todos los demás archivos la usan vía `require_once`.

```php
$lineas = file($archivo, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
if ($linea[0] === '#') continue;
$linea = preg_replace('/[^a-zA-Z0-9.\-]/', '', $linea);
```

`obtener_enlaces_numerados()` devuelve claves 1..N porque el Componente 2 recibe `?Equipo=1`, no `?Equipo=0`.

### ping_helper.php + ping_web.bat
La consigna exigía la cadena `Navegador → PHP → .bat → ping`. PHP no ejecuta el ping directamente, llama al `.bat` con `shell_exec()`.

```php
$destino_limpio = preg_replace('/[^a-zA-Z0-9.\-]/', '', $destino);
$cmd = '"' . $bat . '" ' . escapeshellarg($destino_limpio) . ' 2>&1';
$salida = shell_exec($cmd);
```

El parseo acepta español (`tiempo=15ms`) e inglés (`time=15ms`) con una sola expresión regular, toma el máximo. Si no hubo respuesta, devuelve `-1`.

### estilos.css
Todo el tema visual en variables CSS. Verde = OK, amarillo = Lento, rojo = error.

```css
:root {
    --fondo:  #0a0f1a;
    --acento: #00e5ff;
    --ok:     #10b981;
    --warn:   #f59e0b;
    --error:  #ef4444;
}
```

---

## BLOQUE 2 — Componente GET

### index.php
Página principal. Genera los botones de ping dinámicamente desde la lista, sin tocar el HTML:

```php
foreach ($enlaces as $i => $e) {
    echo "<a href='ping_online.php?Equipo=" . ($i+1) . "' class='btn-enlace'>$e</a>";
}
```

También contiene el formulario POST de reporte y el GET de comparación.

### ping_online.php
Recibe `?Equipo=N`, valida que el índice exista y ejecuta el ping. Si el número no existe, redirige al inicio.

```php
$equipo = isset($_GET['Equipo']) ? (int)$_GET['Equipo'] : 0;
if (!array_key_exists($equipo, $enlaces)) {
    header("Location: index.php"); exit;
}
$ping = hacer_ping($enlaces[$equipo]);
```

### ping_manual.php
Variante de `ping_online.php`. Recibe el dominio escrito por el usuario en lugar de un índice numérico.

### estado_enlaces.php
Se incluye dentro de `index.php`. Muestra el último RTT de cada enlace y lo clasifica con colores.

```php
if ($rtt < 0)       { $clase = "estado-error"; $texto = "Sin respuesta"; }
elseif ($rtt < 100) { $clase = "estado-ok";    $texto = "OK"; }
elseif ($rtt < 300) { $clase = "estado-warn";  $texto = "Lento"; }
else                { $clase = "estado-error";  $texto = "Muy lento"; }
```

### gestionar_enlaces.php
Agregar o quitar dominios desde el navegador. El cambio se refleja en la siguiente ejecución del Task Scheduler, sin reiniciar nada.

```php
if (!in_array($nuevo, $lista_actual)) {
    $lista_actual[] = $nuevo;
    guardar_lista($archivo, $lista_actual);
}
$nueva = array_values(array_filter($lista_actual,
    function($x) use ($a_quitar) { return $x !== $a_quitar; }
));
```

---

## BLOQUE 3 — Componente POST

### reporte.php
Recibe enlace, fecha y rango horario. MySQL calcula todo — PHP no hace aritmética, solo muestra resultados.

```sql
SELECT ROUND(AVG(rtt_max),3), ROUND(MAX(rtt_max),3), ROUND(MIN(rtt_max),3),
       ROUND(STDDEV(rtt_max),3),
       SUM(IF(rtt_max >= 0, 1, 0)) AS exitosos,
       CASE WHEN AVG(rtt_max) < 50  THEN 'Excelente'
            WHEN AVG(rtt_max) < 100 THEN 'Bueno'
            WHEN AVG(rtt_max) < 200 THEN 'Regular'
            ELSE 'Malo' END AS calidad
FROM muestras WHERE enlace=? AND fecha=? AND hora BETWEEN ? AND ?
```

Los datos se inyectan en Chart.js como JSON para dibujar el gráfico de línea.

**Fix PHP 7.1:** `match()` (PHP 8.0+) reemplazado por `switch`.

### comparar.php
Compara todos los enlaces en un rango usando `GROUP BY`. Ordena de más rápido a más lento.

```sql
SELECT enlace, ROUND(AVG(rtt_max),2) AS promedio, ...
FROM muestras WHERE fecha=? AND hora BETWEEN ? AND ?
GROUP BY enlace HAVING COUNT(*) > 0 ORDER BY promedio ASC
```

Produce un diagrama de quesos y un ranking con tabla.

**Fix PHP 7.1:** arrow functions `fn()` (PHP 7.4+) reemplazadas por funciones anónimas completas.

---

## Transición a Resultados

*"Siete archivos PHP, un .bat, un CSS, un .txt. Cada uno con una responsabilidad clara, todos leyendo la misma lista de enlaces, todos apuntando a la misma base de datos. Ahora lo vemos corriendo..."*

---

## Cierre conjunto

*"Los tres bloques que pedía la materia están implementados: monitoreo automático con Task Scheduler, consulta en tiempo real con GET siguiendo la cadena PHP → .bat → ping, y reportes históricos con POST usando funciones de agregación de MySQL."*

*"Los problemas reales que resolvimos — incompatibilidad MySQL 8 + PHP 7.1, parseo bilingüe del ping, permisos de IIS — son lo que aparece al montar un sistema así en Windows, no en un entorno de prueba limpio."*

*"¿Preguntas?"*
