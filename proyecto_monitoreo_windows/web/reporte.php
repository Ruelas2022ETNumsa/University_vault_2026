<?php
// ============================================================
//  reporte.php  — Componente 3 (metodo POST) — VERSION PHP 7.1
//  Usa funciones de agregacion de MySQL: AVG, MAX, MIN,
//  COUNT, STDDEV, DATE_FORMAT, IF, CASE, GROUP BY, ORDER BY
//
//  CAMBIO vs original Linux: el bloque "match()" se reemplazo
//  por "switch" porque match() existe a partir de PHP 8.0
//  y este servidor corre PHP 7.1.11.
// ============================================================

if ($_SERVER['REQUEST_METHOD'] !== 'POST' && !isset($_GET['descargar'])) {
    header("Location: index.php");
    exit;
}

// ── Credenciales ─────────────────────────────────────────────
$DB_USER = "root";
$DB_PASS = "Mamacita.com921";
$DB_NAME = "monitoreo_red";

// ── Parametros del formulario ─────────────────────────────────
$enlace      = isset($_POST['enlace'])      ? $_POST['enlace']      : (isset($_GET['enlace'])      ? $_GET['enlace']      : '');
$fecha       = isset($_POST['fecha'])       ? $_POST['fecha']       : (isset($_GET['fecha'])       ? $_GET['fecha']       : date('Y-m-d'));
$hora_inicio = isset($_POST['hora_inicio']) ? $_POST['hora_inicio'] : (isset($_GET['hora_inicio']) ? $_GET['hora_inicio'] : '00:00');
$hora_fin    = isset($_POST['hora_fin'])    ? $_POST['hora_fin']    : (isset($_GET['hora_fin'])    ? $_GET['hora_fin']    : '23:59');
$formato_dl  = isset($_GET['descargar'])    ? $_GET['descargar']    : '';

// ── Conexion ─────────────────────────────────────────────────
$conn = new mysqli("localhost", $DB_USER, $DB_PASS, $DB_NAME);
if ($conn->connect_error) {
    die("<p style='color:red'>Error de conexion: " . $conn->connect_error . "</p>");
}

$hora_fin_completo = $hora_fin . ":59";

// ══════════════════════════════════════════════════════════════
//  CONSULTA 1: Estadisticas con funciones de agregacion MySQL
//  Usa: AVG, MAX, MIN, COUNT, STDDEV, IF, CASE
//  Todo calculado directamente en el motor de base de datos
// ══════════════════════════════════════════════════════════════
$stmt_stats = $conn->prepare(
    "SELECT
        ROUND(AVG(rtt_max), 3)    AS promedio,
        ROUND(MAX(rtt_max), 3)    AS maximo,
        ROUND(MIN(rtt_max), 3)    AS minimo,
        COUNT(*)                   AS total_muestras,
        SUM(IF(rtt_max >= 0, 1, 0)) AS pings_exitosos,
        SUM(IF(rtt_max < 0,  1, 0)) AS pings_fallidos,
        ROUND(STDDEV(rtt_max), 3) AS desviacion_std,
        CASE
            WHEN AVG(rtt_max) < 50  THEN 'Excelente'
            WHEN AVG(rtt_max) < 100 THEN 'Bueno'
            WHEN AVG(rtt_max) < 200 THEN 'Regular'
            ELSE 'Malo'
        END AS calidad
     FROM muestras
     WHERE enlace = ? AND fecha = ?
       AND hora BETWEEN ? AND ?
       AND rtt_max >= 0"
);
$stmt_stats->bind_param("ssss", $enlace, $fecha, $hora_inicio, $hora_fin_completo);
$stmt_stats->execute();
$stats = $stmt_stats->get_result()->fetch_assoc();

$promedio       = isset($stats['promedio'])       ? $stats['promedio']       : 0;
$maximo         = isset($stats['maximo'])         ? $stats['maximo']         : 0;
$minimo         = isset($stats['minimo'])         ? $stats['minimo']         : 0;
$total_muestras = isset($stats['total_muestras']) ? $stats['total_muestras'] : 0;
$pings_ok       = isset($stats['pings_exitosos']) ? $stats['pings_exitosos'] : 0;
$pings_fail     = isset($stats['pings_fallidos']) ? $stats['pings_fallidos'] : 0;
$stddev         = isset($stats['desviacion_std']) ? $stats['desviacion_std'] : 0;
$calidad        = isset($stats['calidad'])        ? $stats['calidad']        : 'Sin datos';

// ══════════════════════════════════════════════════════════════
//  CONSULTA 2: Datos para la grafica de linea
//  Usa: DATE_FORMAT para etiquetas de hora legibles, IF, ORDER BY
// ══════════════════════════════════════════════════════════════
$stmt_datos = $conn->prepare(
    "SELECT
        DATE_FORMAT(hora, '%H:%i') AS hora_fmt,
        ROUND(rtt_max, 3)          AS rtt,
        IF(rtt_max < 0,  'Sin respuesta',
           IF(rtt_max < 100, 'OK',
              IF(rtt_max < 200, 'Lento', 'Muy lento')
           )
        ) AS estado
     FROM muestras
     WHERE enlace = ? AND fecha = ?
       AND hora BETWEEN ? AND ?
     ORDER BY hora ASC"
);
$stmt_datos->bind_param("ssss", $enlace, $fecha, $hora_inicio, $hora_fin_completo);
$stmt_datos->execute();
$res_datos = $stmt_datos->get_result();

$filas = [];
$horas_json_arr = [];
$valores_json_arr = [];
while ($f = $res_datos->fetch_assoc()) {
    $filas[] = $f;
    if ($f['rtt'] >= 0) {
        $horas_json_arr[]   = $f['hora_fmt'];
        $valores_json_arr[] = (float)$f['rtt'];
    }
}
$cnt = count($valores_json_arr);
$conn->close();

// ── Arrays JSON para Chart.js ─────────────────────────────────
$horas_json   = json_encode($horas_json_arr);
$valores_json = json_encode($valores_json_arr);
$params_dl    = http_build_query(compact('enlace','fecha','hora_inicio','hora_fin'));

// ══════════════════════════════════════════════════════════════
//  DESCARGA TXT
// ══════════════════════════════════════════════════════════════
if ($formato_dl === 'txt') {
    header('Content-Type: text/plain; charset=utf-8');
    header('Content-Disposition: attachment; filename="reporte_' . preg_replace('/[^a-z0-9]/i','_',$enlace) . '_' . $fecha . '.txt"');
    echo "REPORTE DE MONITOREO - ETN921\n";
    echo "=====================================\n";
    echo "Enlace        : $enlace\n";
    echo "Fecha         : $fecha\n";
    echo "Rango horas   : $hora_inicio - $hora_fin\n";
    echo "Total muestras: $total_muestras\n";
    echo "Pings exitosos: $pings_ok\n";
    echo "Pings fallidos: $pings_fail\n";
    echo "RTT Maximo    : $maximo ms\n";
    echo "RTT Promedio  : $promedio ms\n";
    echo "RTT Minimo    : $minimo ms\n";
    echo "Desv. Estandar: $stddev ms\n";
    echo "Calidad       : $calidad\n";
    echo "=====================================\n\n";
    echo str_pad("Hora",8).str_pad("RTT(ms)",12).str_pad("Estado",16)."\n";
    echo str_repeat("-",36)."\n";
    foreach ($filas as $f) {
        echo str_pad($f['hora_fmt'],8).str_pad($f['rtt'],12).$f['estado']."\n";
    }
    exit;
}

// ══════════════════════════════════════════════════════════════
//  DESCARGA EXCEL (.csv con BOM)
// ══════════════════════════════════════════════════════════════
if ($formato_dl === 'excel') {
    header('Content-Type: text/csv; charset=utf-8');
    header('Content-Disposition: attachment; filename="reporte_' . preg_replace('/[^a-z0-9]/i','_',$enlace) . '_' . $fecha . '.csv"');
    echo "\xEF\xBB\xBF";
    echo "Enlace;Fecha;Hora;RTT (ms);Estado\n";
    foreach ($filas as $f) {
        echo "$enlace;$fecha;{$f['hora_fmt']};{$f['rtt']};{$f['estado']}\n";
    }
    echo "\n;ESTADISTICAS (calculadas con MySQL);;;;\n";
    echo ";Total muestras;$total_muestras;;;\n";
    echo ";Pings exitosos;$pings_ok;;;\n";
    echo ";Pings fallidos;$pings_fail;;;\n";
    echo ";RTT Maximo;$maximo ms;;;\n";
    echo ";RTT Promedio;$promedio ms;;;\n";
    echo ";RTT Minimo;$minimo ms;;;\n";
    echo ";Desv. Estandar;$stddev ms;;;\n";
    echo ";Calidad;$calidad;;;\n";
    exit;
}

// ── Color de calidad para badge ───────────────────────────────
// FIX PHP 7.1: el codigo original usaba "match()" que es PHP 8.0+.
// Lo reemplazamos por switch.
switch ($calidad) {
    case 'Excelente': $calidad_color = '#10b981'; break;
    case 'Bueno':     $calidad_color = '#3b82f6'; break;
    case 'Regular':   $calidad_color = '#f59e0b'; break;
    case 'Malo':      $calidad_color = '#ef4444'; break;
    default:          $calidad_color = '#6b7280';
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte: <?php echo htmlspecialchars($enlace); ?></title>
    <link rel="stylesheet" href="estilos.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
</head>
<body>
<header>
    <div class="header-inner">
        <h1>&#9001; Reporte Grafico &#9002;</h1>
        <p class="subtitulo">ETN921 &mdash; Historial de RTT — Estadisticas calculadas con MySQL</p>
    </div>
</header>
<main>
    <section class="tarjeta">
        <h2>Enlace: <span class="resaltado"><?php echo htmlspecialchars($enlace); ?></span>
            <span style="float:right;background:<?php echo $calidad_color;?>;color:#000;font-size:0.75rem;padding:3px 12px;border-radius:20px;font-family:var(--mono);">
                <?php echo $calidad; ?>
            </span>
        </h2>
        <p>Fecha: <strong><?php echo $fecha; ?></strong>
           &nbsp;|&nbsp; Rango: <strong><?php echo $hora_inicio; ?> – <?php echo $hora_fin; ?></strong>
           &nbsp;|&nbsp; Calculado con: <span style="color:var(--acento);font-family:var(--mono);font-size:0.8rem;">AVG() MAX() MIN() COUNT() STDDEV() IF() CASE</span>
        </p>

        <!-- Estadisticas calculadas 100% en MySQL -->
        <div class="stats-grid">
            <div class="stat">
                <span class="stat-num"><?php echo $maximo; ?></span>
                <span class="stat-lbl">MAX() ms</span>
            </div>
            <div class="stat">
                <span class="stat-num"><?php echo $promedio; ?></span>
                <span class="stat-lbl">AVG() ms</span>
            </div>
            <div class="stat">
                <span class="stat-num"><?php echo $minimo; ?></span>
                <span class="stat-lbl">MIN() ms</span>
            </div>
            <div class="stat">
                <span class="stat-num"><?php echo $stddev; ?></span>
                <span class="stat-lbl">STDDEV() ms</span>
            </div>
            <div class="stat">
                <span class="stat-num"><?php echo $pings_ok; ?></span>
                <span class="stat-lbl">COUNT exitosos</span>
            </div>
            <div class="stat">
                <span class="stat-num"><?php echo $pings_fail; ?></span>
                <span class="stat-lbl">COUNT fallidos</span>
            </div>
        </div>

        <!-- Botones de descarga -->
        <div class="botones-descarga">
            <a href="reporte.php?descargar=txt&<?php echo $params_dl; ?>" class="btn-dl btn-txt">
                &#8595;&nbsp; Descargar TXT
            </a>
            <a href="reporte.php?descargar=excel&<?php echo $params_dl; ?>" class="btn-dl btn-excel">
                &#8595;&nbsp; Descargar Excel (.csv)
            </a>
        </div>

        <?php if ($cnt === 0): ?>
            <div class="sin-datos">Sin datos para este rango. Usa la Opcion 7 del menu para cargar datos de prueba.</div>
        <?php else: ?>

        <!-- Grafico de linea -->
        <div class="grafico-contenedor">
            <canvas id="grafico"></canvas>
        </div>
        <script>
        new Chart(document.getElementById('grafico').getContext('2d'), {
            type: 'line',
            data: {
                labels: <?php echo $horas_json; ?>,
                datasets: [{
                    label: 'RTT Maximo (ms) — <?php echo htmlspecialchars($enlace); ?>',
                    data: <?php echo $valores_json; ?>,
                    borderColor: '#00e5ff',
                    backgroundColor: 'rgba(0,229,255,0.10)',
                    borderWidth: 2,
                    pointRadius: 4,
                    pointBackgroundColor: '#00e5ff',
                    tension: 0.3,
                    fill: true
                }, {
                    label: 'Promedio AVG() = <?php echo $promedio; ?> ms',
                    data: Array(<?php echo $cnt; ?>).fill(<?php echo $promedio; ?>),
                    borderColor: '#f59e0b',
                    borderWidth: 1,
                    borderDash: [6, 4],
                    pointRadius: 0,
                    fill: false
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { labels: { color:'#ccc', font:{size:12} } },
                    tooltip: { callbacks: { label: function(c) { return c.dataset.label.split('—')[0].trim() + ': ' + c.parsed.y + ' ms'; } } }
                },
                scales: {
                    x: { ticks:{color:'#aaa'}, grid:{color:'#2a2a2a'} },
                    y: {
                        beginAtZero: true,
                        ticks:{color:'#aaa', callback: function(v) { return v+' ms'; } },
                        grid:{color:'#2a2a2a'}
                    }
                }
            }
        });
        </script>

        <!-- Tabla con estado generado por IF() de MySQL -->
        <h3 style="color:var(--acento);font-family:var(--mono);margin:1.5rem 0 0.6rem;font-size:0.9rem;">
            Datos — estado calculado con IF() en MySQL
        </h3>
        <div style="overflow-x:auto;">
            <table class="tabla-estado">
                <thead>
                    <tr><th>#</th><th>Hora (DATE_FORMAT)</th><th>RTT (ms)</th><th>Estado (IF)</th></tr>
                </thead>
                <tbody>
                <?php foreach ($filas as $i => $f):
                    $c = $f['rtt'] < 0 ? 'estado-error' :
                         ($f['rtt'] < 100 ? 'estado-ok' :
                         ($f['rtt'] < 200 ? 'estado-warn' : 'estado-error'));
                ?>
                <tr>
                    <td><?php echo $i+1; ?></td>
                    <td><?php echo $f['hora_fmt']; ?></td>
                    <td><?php echo $f['rtt']; ?></td>
                    <td class="<?php echo $c; ?>"><?php echo $f['estado']; ?></td>
                </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
        </div>
        <?php endif; ?>

        <a href="index.php" class="btn-volver">&#8592; Nuevo reporte</a>
    </section>
</main>
<footer>
    <p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p>
</footer>
</body>
</html>
