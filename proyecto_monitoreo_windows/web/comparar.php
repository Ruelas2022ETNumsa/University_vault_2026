<?php
// ============================================================
//  comparar.php  — Comparacion de los 10 enlaces — VERSION PHP 7.1
//  Diagrama de quesos (pie chart) usando:
//  AVG(), MIN(), MAX(), COUNT(), STDDEV(), ROUND()
//  GROUP BY enlace, ORDER BY promedio ASC, HAVING
//
//  CAMBIOS vs original Linux:
//   1. "fn(...) => ..." (arrow function) reemplazado por function() {} normal
//      porque arrow functions existen recien desde PHP 7.4
//   2. "match()" reemplazado por switch porque match() existe recien desde PHP 8.0
// ============================================================

// ── Credenciales ─────────────────────────────────────────────
$DB_USER = "root";
$DB_PASS = "Mamacita.com921";
$DB_NAME = "monitoreo_red";

// ── Parametros del formulario ─────────────────────────────────
$fecha       = isset($_POST['fecha'])       ? $_POST['fecha']       : (isset($_GET['fecha'])       ? $_GET['fecha']       : date('Y-m-d'));
$hora_inicio = isset($_POST['hora_inicio']) ? $_POST['hora_inicio'] : (isset($_GET['hora_inicio']) ? $_GET['hora_inicio'] : '00:00');
$hora_fin    = isset($_POST['hora_fin'])    ? $_POST['hora_fin']    : (isset($_GET['hora_fin'])    ? $_GET['hora_fin']    : '23:59');
$enviado     = isset($_POST['fecha']) || isset($_GET['fecha']);

$datos_grafico = [];
$error_msg     = '';

if ($enviado) {
    $conn = new mysqli("localhost", $DB_USER, $DB_PASS, $DB_NAME);
    if ($conn->connect_error) {
        $error_msg = "Error de conexion: " . $conn->connect_error;
    } else {
        $hora_fin_completo = $hora_fin . ":59";

        // ══════════════════════════════════════════════════════
        //  CONSULTA PRINCIPAL — funciones MySQL de agregacion
        //  Uso de: AVG, MIN, MAX, COUNT, STDDEV, ROUND
        //          GROUP BY, ORDER BY, HAVING, IF, CASE
        // ══════════════════════════════════════════════════════
        $stmt = $conn->prepare(
            "SELECT
                enlace,
                ROUND(AVG(rtt_max), 2)    AS promedio,
                ROUND(MIN(rtt_max), 2)    AS minimo,
                ROUND(MAX(rtt_max), 2)    AS maximo,
                ROUND(STDDEV(rtt_max), 2) AS desviacion,
                COUNT(*)                   AS total,
                SUM(IF(rtt_max >= 0, 1, 0)) AS exitosos,
                SUM(IF(rtt_max  < 0, 1, 0)) AS fallidos,
                CASE
                    WHEN AVG(rtt_max) < 50  THEN 'Excelente'
                    WHEN AVG(rtt_max) < 100 THEN 'Bueno'
                    WHEN AVG(rtt_max) < 200 THEN 'Regular'
                    ELSE 'Malo'
                END AS calidad
             FROM muestras
             WHERE fecha = ?
               AND hora BETWEEN ? AND ?
               AND rtt_max >= 0
             GROUP BY enlace
             HAVING COUNT(*) > 0
             ORDER BY promedio ASC"
        );
        $stmt->bind_param("sss", $fecha, $hora_inicio, $hora_fin_completo);
        $stmt->execute();
        $res = $stmt->get_result();

        while ($f = $res->fetch_assoc()) {
            $datos_grafico[] = $f;
        }
        $conn->close();

        if (empty($datos_grafico)) {
            $error_msg = "No hay datos para esa fecha y rango de horas. Usa la Opcion 7 del menu para cargar datos de prueba.";
        }
    }
}

// ── Preparar arrays para Chart.js ────────────────────────────
$labels    = array_column($datos_grafico, 'enlace');
$promedios = array_column($datos_grafico, 'promedio');

// Paleta de colores para el pie chart (un color por enlace)
$colores = [
    'rgba(0,229,255,0.85)',   'rgba(124,58,237,0.85)',
    'rgba(16,185,129,0.85)',  'rgba(245,158,11,0.85)',
    'rgba(239,68,68,0.85)',   'rgba(59,130,246,0.85)',
    'rgba(236,72,153,0.85)',  'rgba(132,204,22,0.85)',
    'rgba(249,115,22,0.85)',  'rgba(20,184,166,0.85)',
];
// FIX PHP 7.1: en el original era "fn($c) => str_replace('0.85','1',$c)"
// Las arrow functions existen recien desde PHP 7.4. Usamos function() normal.
$borders = array_map(function($c) { return str_replace('0.85', '1', $c); }, $colores);

$labels_json    = json_encode($labels);
$promedios_json = json_encode($promedios);
$colores_json   = json_encode(array_slice($colores, 0, count($labels)));
$borders_json   = json_encode(array_slice($borders, 0, count($labels)));
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Comparacion de enlaces — ETN921</title>
    <link rel="stylesheet" href="estilos.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        .pie-wrap {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            align-items: start;
        }
        @media(max-width:700px){ .pie-wrap { grid-template-columns: 1fr; } }
        .ranking-tabla { width: 100%; border-collapse: collapse; font-size: 0.82rem; margin-top:0.5rem; }
        .ranking-tabla th {
            background: rgba(0,229,255,0.1); color: var(--acento);
            padding: 0.5rem 0.6rem; text-align:left;
            border-bottom: 1px solid var(--borde); font-family: var(--mono);
        }
        .ranking-tabla td { padding: 0.45rem 0.6rem; border-bottom: 1px solid rgba(30,58,95,0.4); }
        .ranking-tabla tr:hover td { background: rgba(0,229,255,0.04); }
        .medalla { font-size: 1rem; }
        .badge-cal {
            display: inline-block; padding: 1px 8px;
            border-radius: 10px; font-size: 0.72rem; font-weight: 600;
        }
        .cal-excelente { background:rgba(16,185,129,0.2); color:#10b981; }
        .cal-bueno     { background:rgba(59,130,246,0.2); color:#3b82f6; }
        .cal-regular   { background:rgba(245,158,11,0.2); color:#f59e0b; }
        .cal-malo      { background:rgba(239,68,68,0.2);  color:#ef4444; }
        .sql-badge {
            background: rgba(0,229,255,0.08); border: 1px solid rgba(0,229,255,0.3);
            border-radius: 6px; padding: 0.5rem 0.8rem;
            font-family: var(--mono); font-size: 0.75rem; color: var(--acento);
            margin-bottom: 1rem; line-height: 1.8;
        }
    </style>
</head>
<body>
<header>
    <div class="header-inner">
        <h1>&#9685; Comparacion de los 10 enlaces</h1>
        <p class="subtitulo">ETN921 &mdash; Diagrama de quesos con AVG() + GROUP BY de MySQL</p>
    </div>
</header>
<main>

    <!-- Formulario de filtro -->
    <section class="tarjeta">
        <h2>&#9998; Seleccionar rango para comparar</h2>
        <form method="POST" action="comparar.php" class="form-reporte">
            <div class="fila-form">
                <label>Fecha:</label>
                <input type="date" name="fecha" value="<?php echo htmlspecialchars($fecha); ?>" required>
            </div>
            <div class="fila-form">
                <label>Hora inicio:</label>
                <input type="time" name="hora_inicio" value="<?php echo htmlspecialchars($hora_inicio); ?>" required>
            </div>
            <div class="fila-form">
                <label>Hora fin:</label>
                <input type="time" name="hora_fin" value="<?php echo htmlspecialchars($hora_fin); ?>" required>
            </div>
            <button type="submit" class="btn-reporte">Generar comparacion</button>
        </form>

        <!-- Muestra las instrucciones SQL que se usaron -->
        <?php if ($enviado && !empty($datos_grafico)): ?>
        <div class="sql-badge">
            Consulta MySQL ejecutada:<br>
            SELECT enlace, <strong>ROUND(AVG(rtt_max),2)</strong>, <strong>MIN()</strong>,
            <strong>MAX()</strong>, <strong>STDDEV()</strong>, <strong>COUNT(*)</strong>,
            <strong>SUM(IF(...))</strong>, <strong>CASE...END</strong><br>
            FROM muestras WHERE fecha='<?php echo $fecha;?>' AND hora BETWEEN '<?php echo $hora_inicio;?>' AND '<?php echo $hora_fin;?>'<br>
            <strong>GROUP BY</strong> enlace <strong>HAVING</strong> COUNT(*) > 0
            <strong>ORDER BY</strong> promedio ASC
        </div>
        <?php endif; ?>
    </section>

    <?php if (!empty($error_msg)): ?>
    <section class="tarjeta">
        <div class="sin-datos"><?php echo htmlspecialchars($error_msg); ?></div>
    </section>

    <?php elseif (!empty($datos_grafico)): ?>
    <!-- Graficos y tabla de ranking -->
    <section class="tarjeta">
        <h2>&#9685; Diagrama de quesos — Promedio RTT por enlace</h2>
        <p style="font-size:0.85rem;color:var(--texto-dim);">
            El tamano de cada sector es proporcional al promedio de latencia (AVG).
            Un sector mas grande indica <strong>peor rendimiento</strong>.
            El enlace mas rapido aparece primero en la leyenda.
        </p>

        <div class="pie-wrap">
            <!-- Diagrama de quesos (Pie Chart) -->
            <div style="position:relative;max-width:420px;margin:0 auto;">
                <canvas id="pieChart"></canvas>
            </div>

            <!-- Grafico de barras horizontal para comparar -->
            <div>
                <p style="font-size:0.78rem;color:var(--texto-dim);margin-bottom:0.5rem;">
                    Barras ordenadas de menor a mayor RTT promedio (mejor -&gt; peor)
                </p>
                <canvas id="barChart" style="max-height:340px;"></canvas>
            </div>
        </div>

        <script>
        var labels    = <?php echo $labels_json; ?>;
        var promedios = <?php echo $promedios_json; ?>;
        var colores   = <?php echo $colores_json; ?>;
        var borders   = <?php echo $borders_json; ?>;

        // ── Pie Chart ─────────────────────────────────────────
        new Chart(document.getElementById('pieChart').getContext('2d'), {
            type: 'pie',
            data: {
                labels: labels,
                datasets: [{
                    data: promedios,
                    backgroundColor: colores,
                    borderColor: borders,
                    borderWidth: 1.5
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { color:'#ccc', font:{size:11}, padding:10 }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(ctx) {
                                var total = ctx.dataset.data.reduce(function(a,b){return a+b;},0);
                                var pct   = ((ctx.parsed / total) * 100).toFixed(1);
                                return ' ' + ctx.label + ': ' + ctx.parsed + ' ms (' + pct + '% del total)';
                            }
                        }
                    }
                }
            }
        });

        // ── Bar Chart horizontal ──────────────────────────────
        new Chart(document.getElementById('barChart').getContext('2d'), {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'RTT Promedio AVG() ms',
                    data: promedios,
                    backgroundColor: colores,
                    borderColor: borders,
                    borderWidth: 1
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                plugins: {
                    legend: { display: false },
                    tooltip: { callbacks: { label: function(c){ return ' ' + c.parsed.x + ' ms'; } } }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        ticks: { color:'#aaa', callback: function(v){ return v+' ms'; } },
                        grid: { color:'#2a2a2a' }
                    },
                    y: { ticks: { color:'#ccc', font:{size:11} }, grid:{color:'#1a1a2a'} }
                }
            }
        });
        </script>
    </section>

    <!-- Tabla de ranking detallado -->
    <section class="tarjeta">
        <h2>&#127942; Ranking de rendimiento — resultados de MySQL</h2>
        <p style="font-size:0.83rem;color:var(--texto-dim);">
            Ordenado por AVG(rtt_max) ASC — el primero es el mas rapido.
            La desviacion estandar (STDDEV) indica la inestabilidad: valores altos = conexion variable.
        </p>
        <table class="ranking-tabla">
            <thead>
                <tr>
                    <th>Pos.</th>
                    <th>Enlace</th>
                    <th>AVG() ms</th>
                    <th>MIN() ms</th>
                    <th>MAX() ms</th>
                    <th>STDDEV() ms</th>
                    <th>COUNT(*)</th>
                    <th>Fallidos</th>
                    <th>CASE calidad</th>
                </tr>
            </thead>
            <tbody>
            <?php foreach ($datos_grafico as $i => $d):
                // FIX PHP 7.1: el original era "match($i) { 0=>'🥇', 1=>'🥈', 2=>'🥉', default=>... }"
                // match() es PHP 8.0+. Aqui usamos switch.
                switch ($i) {
                    case 0:  $medal = '🥇'; break;
                    case 1:  $medal = '🥈'; break;
                    case 2:  $medal = '🥉'; break;
                    default: $medal = ($i + 1) . '.';
                }
                $cal_cls = 'cal-' . strtolower($d['calidad']);
            ?>
            <tr>
                <td class="medalla"><?php echo $medal; ?></td>
                <td style="font-family:var(--mono);font-size:0.8rem;color:var(--acento);">
                    <?php echo htmlspecialchars($d['enlace']); ?>
                </td>
                <td><strong><?php echo $d['promedio']; ?></strong></td>
                <td class="estado-ok"><?php echo $d['minimo']; ?></td>
                <td class="estado-error"><?php echo $d['maximo']; ?></td>
                <td style="color:#f59e0b;"><?php echo $d['desviacion']; ?></td>
                <td><?php echo $d['exitosos']; ?></td>
                <td class="<?php echo $d['fallidos']>0?'estado-error':'estado-ok'; ?>">
                    <?php echo $d['fallidos']; ?>
                </td>
                <td><span class="badge-cal <?php echo $cal_cls; ?>"><?php echo $d['calidad']; ?></span></td>
            </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
    </section>
    <?php endif; ?>

    <div style="text-align:center;margin-top:0.5rem;">
        <a href="index.php" class="btn-volver">&#8592; Volver al menu principal</a>
    </div>
</main>
<footer>
    <p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p>
</footer>
</body>
</html>
