<?php
// ============================================================
//  ping_manual.php  — Ping a direccion escrita por el usuario
//  Metodo GET: ?direccion=www.ejemplo.com  — IIS + WINDOWS
//  Flujo: GET -> PHP -> ping_web.bat -> ping (segun spec ETN921)
// ============================================================

require_once __DIR__ . '/ping_helper.php';

$direccion_raw = isset($_GET['direccion']) ? $_GET['direccion'] : '';

// Sanitizar: solo caracteres validos en un dominio o IP
$destino = preg_replace('/[^a-zA-Z0-9.\-]/', '', $direccion_raw);

if (empty($destino)) {
    header("Location: index.php");
    exit;
}

// Ejecutar ping a traves del .bat
$ping = hacer_ping($destino);
$resultado = $ping['salida'];
$rtt_max   = $ping['rtt_max'] >= 0 ? $ping['rtt_max'] . " ms" : "Sin respuesta";
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ping manual - ETN921</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
<header>
    <div class="header-inner">
        <h1>&#9001; Ping Manual &#9002;</h1>
        <p class="subtitulo">ETN921 &mdash; Direccion personalizada (GET)</p>
    </div>
</header>
<main>
    <section class="tarjeta">
        <h2>Ping a: <span class="resaltado"><?php echo htmlspecialchars($destino); ?></span></h2>
        <div class="resultado-ping">
            <div class="rtt-badge">RTT Max: <?php echo htmlspecialchars($rtt_max); ?></div>
            <pre><?php echo htmlspecialchars($resultado); ?></pre>
        </div>
        <form method="GET" action="ping_manual.php" class="form-inline" style="margin-top:1rem;">
            <input type="text" name="direccion" placeholder="Otra direccion..." value="<?php echo htmlspecialchars($destino); ?>">
            <button type="submit">Ping</button>
        </form>
        <a href="index.php" class="btn-volver">&#8592; Volver al menu</a>
    </section>
</main>
<footer>
    <p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p>
</footer>
</body>
</html>
