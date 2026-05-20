<?php
// ============================================================
//  ping_online.php  — Componente 2 (metodo GET)  — IIS + WINDOWS
//  Recibe ?Equipo=N y ejecuta ping al enlace correspondiente
//  Flujo: GET -> PHP -> ping_web.bat -> ping (segun spec ETN921)
// ============================================================

require_once __DIR__ . '/ping_helper.php';
require_once __DIR__ . '/enlaces.php';

// Cargar la lista de enlaces desde enlaces.txt (keys 1..N para que
// coincida con el parametro GET ?Equipo=N)
$enlaces = obtener_enlaces_numerados();

// Obtener parametro GET (como en el ejemplo del PDF del docente)
$equipo = isset($_GET['Equipo']) ? (int)$_GET['Equipo'] : 0;

if (!array_key_exists($equipo, $enlaces)) {
    header("Location: index.php");
    exit;
}

$destino = $enlaces[$equipo];

// Ejecutar ping a traves del .bat (ping_helper -> ping_web.bat -> ping)
$ping = hacer_ping($destino);
$resultado = $ping['salida'];
$rtt_max   = $ping['rtt_max'] >= 0 ? $ping['rtt_max'] . " ms" : "Sin respuesta";
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ping a <?php echo htmlspecialchars($destino); ?> - ETN921</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
<header>
    <div class="header-inner">
        <h1>&#9001; Resultado de Ping &#9002;</h1>
        <p class="subtitulo">ETN921 &mdash; Ping en tiempo real (GET)</p>
    </div>
</header>
<main>
    <section class="tarjeta">
        <h2>Ping a: <span class="resaltado"><?php echo htmlspecialchars($destino); ?></span></h2>
        <div class="resultado-ping">
            <div class="rtt-badge">RTT Max: <?php echo htmlspecialchars($rtt_max); ?></div>
            <pre><?php echo htmlspecialchars($resultado); ?></pre>
        </div>
        <a href="index.php" class="btn-volver">&#8592; Volver al menu</a>
    </section>
</main>
<footer>
    <p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p>
</footer>
</body>
</html>
