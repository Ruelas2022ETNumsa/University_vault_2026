<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monitor de Red - ETN921</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <div class="header-inner">
            <h1>&#9001; Monitor de Enlaces TCP/IP &#9002;</h1>
            <p class="subtitulo">ETN921 &mdash; Teoría de Sistemas Operativos</p>
        </div>
    </header>

    <main>
        <!-- ── Componente 2: Ping en tiempo real (GET) ── -->
        <section class="tarjeta">
            <h2>&#9654; Ping en tiempo real</h2>
            <p>Selecciona un enlace o escribe una dirección para hacer ping ahora mismo.</p>

            <div class="grid-enlaces">
                <?php
                require_once 'enlaces.php';
                $enlaces = obtener_enlaces();
                foreach ($enlaces as $i => $e) {
                    echo "<a href='ping_online.php?Equipo=" . ($i+1) . "' class='btn-enlace'>$e</a>";
                }
                ?>
            </div>

            <!-- Ping manual via GET -->
            <form method="GET" action="ping_manual.php" class="form-inline">
                <input type="text" name="direccion" placeholder="Escribe una dirección (ej: www.nasa.gov)" required>
                <button type="submit">Ping manual</button>
            </form>

            <p style="margin-top:1rem; font-size:0.85rem; text-align:right;">
                <a href="gestionar_enlaces.php" style="color:var(--acento); text-decoration:none;">
                    &#9881; Agregar o quitar enlaces de la lista &rarr;
                </a>
            </p>
        </section>

        <!-- ── Componente 3: Reportes gráficos (POST) ── -->
        <section class="tarjeta">
            <h2>&#9998; Generar reporte gráfico</h2>
            <p>Consulta el historial de RTT de cualquier enlace en un rango de fechas.</p>

            <form method="POST" action="reporte.php" class="form-reporte">
                <div class="fila-form">
                    <label>Enlace:</label>
                    <select name="enlace" required>
                        <option value="">-- Selecciona --</option>
                        <?php foreach ($enlaces as $e) echo "<option value='$e'>$e</option>"; ?>
                    </select>
                </div>
                <div class="fila-form">
                    <label>Fecha:</label>
                    <input type="date" name="fecha" value="<?php echo date('Y-m-d'); ?>" required>
                </div>
                <div class="fila-form">
                    <label>Hora inicio:</label>
                    <input type="time" name="hora_inicio" value="00:00" required>
                </div>
                <div class="fila-form">
                    <label>Hora fin:</label>
                    <input type="time" name="hora_fin" value="23:59" required>
                </div>
                <button type="submit" class="btn-reporte">Generar reporte</button>
            </form>
        </section>

        <!-- ── Comparación: Diagrama de quesos (nuevo) ── -->
        <section class="tarjeta">
            <h2>&#9685; Comparar los 10 enlaces (diagrama de quesos)</h2>
            <p>Genera un diagrama de quesos comparando el promedio de latencia de todos los enlaces
               en un rango de fecha y hora. Usa <strong>AVG() + GROUP BY</strong> de MySQL.</p>
            <form method="GET" action="comparar.php" class="form-reporte">
                <div class="fila-form">
                    <label>Fecha:</label>
                    <input type="date" name="fecha" value="<?php echo date('Y-m-d'); ?>" required>
                </div>
                <div class="fila-form">
                    <label>Hora inicio:</label>
                    <input type="time" name="hora_inicio" value="00:00" required>
                </div>
                <div class="fila-form">
                    <label>Hora fin:</label>
                    <input type="time" name="hora_fin" value="23:59" required>
                </div>
                <button type="submit" class="btn-reporte" style="background:#7c3aed;">Ver comparación</button>
            </form>
        </section>

        <!-- ── Estado de los 10 enlaces ── -->
        <section class="tarjeta">
            <h2>&#9632; Estado actual de los 10 enlaces</h2>
            <?php include 'estado_enlaces.php'; ?>
        </section>
    </main>

    <footer>
        <p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p>
    </footer>
</body>
</html>
