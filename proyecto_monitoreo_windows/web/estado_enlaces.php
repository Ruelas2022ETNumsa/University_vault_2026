<?php
// ============================================================
//  estado_enlaces.php  — Incluido en index.php
//  Muestra la última muestra de cada enlace desde la BD
// ============================================================

$conn = @new mysqli("localhost", "root", "Mamacita.com921", "monitoreo_red");

if ($conn->connect_error) {
    echo "<p class='aviso'>Base de datos no disponible. Ejecuta primero la Opción 3 del menú.</p>";
    return;
}

require_once __DIR__ . '/enlaces.php';
$enlaces = obtener_enlaces();

echo "<table class='tabla-estado'>";
echo "<thead><tr><th>#</th><th>Enlace</th><th>Última muestra</th><th>Hora</th><th>RTT Máx (ms)</th><th>Estado</th></tr></thead>";
echo "<tbody>";

foreach ($enlaces as $i => $enlace) {
    $stmt = $conn->prepare(
        "SELECT fecha, hora, rtt_max FROM muestras
         WHERE enlace = ? ORDER BY fecha DESC, hora DESC LIMIT 1"
    );
    $stmt->bind_param("s", $enlace);
    $stmt->execute();
    $res = $stmt->get_result();
    $fila = $res->fetch_assoc();

    if ($fila) {
        $rtt = $fila['rtt_max'];
        if ($rtt < 0) {
            $clase = "estado-error"; $texto = "Sin respuesta";
        } elseif ($rtt < 100) {
            $clase = "estado-ok";   $texto = "OK";
        } elseif ($rtt < 300) {
            $clase = "estado-warn"; $texto = "Lento";
        } else {
            $clase = "estado-error"; $texto = "Muy lento";
        }
        echo "<tr>
            <td>" . ($i+1) . "</td>
            <td><a href='ping_online.php?Equipo=" . ($i+1) . "'>$enlace</a></td>
            <td>{$fila['fecha']}</td>
            <td>{$fila['hora']}</td>
            <td>{$rtt}</td>
            <td class='$clase'>$texto</td>
          </tr>";
    } else {
        echo "<tr>
            <td>" . ($i+1) . "</td>
            <td><a href='ping_online.php?Equipo=" . ($i+1) . "'>$enlace</a></td>
            <td colspan='3'>Sin datos aún</td>
            <td class='estado-warn'>Esperando</td>
          </tr>";
    }
}

echo "</tbody></table>";
$conn->close();
?>
