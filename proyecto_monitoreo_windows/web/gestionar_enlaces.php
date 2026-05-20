<?php
// ============================================================
//  gestionar_enlaces.php
//
//  Pantalla web para agregar o quitar enlaces de la lista
//  que monitorea el sistema. Trabaja sobre el mismo archivo
//  enlaces.txt que usan los demas archivos PHP y el script
//  tomar_muestra.bat.
//
//  Equivalente web de la Opcion 8 del menu.bat de consola.
//
//  Los cambios se aplican:
//    - Inmediatamente en la pagina web (al refrescar)
//    - En la siguiente toma de muestras (max 5 minutos)
// ============================================================

require_once __DIR__ . '/enlaces.php';

// Ruta del archivo que vamos a editar (mismo que lee enlaces.php)
$archivo = __DIR__ . '/enlaces.txt';

$mensaje  = '';
$tipo_msg = '';   // 'ok' | 'err'

// ── Funcion local para escribir la lista ────────────────────
function guardar_lista($archivo, $lista) {
    $contenido  = "# ============================================================\n";
    $contenido .= "# enlaces.txt - Lista de enlaces a monitorear\n";
    $contenido .= "# Editado desde gestionar_enlaces.php\n";
    $contenido .= "# ============================================================\n\n";
    foreach ($lista as $e) {
        $e = trim($e);
        if ($e === '') continue;
        if (preg_match('/^[a-zA-Z0-9.\-]+$/', $e)) {
            $contenido .= $e . "\n";
        }
    }
    return @file_put_contents($archivo, $contenido) !== false;
}

// ── Procesar acciones POST ──────────────────────────────────
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $accion = isset($_POST['accion']) ? $_POST['accion'] : '';
    $lista_actual = obtener_enlaces();

    // AGREGAR
    if ($accion === 'agregar') {
        $nuevo = isset($_POST['enlace']) ? trim($_POST['enlace']) : '';
        $nuevo = preg_replace('/[^a-zA-Z0-9.\-]/', '', $nuevo);

        if ($nuevo === '') {
            $mensaje = 'Direccion vacia o invalida.';
            $tipo_msg = 'err';
        } elseif (in_array($nuevo, $lista_actual)) {
            $mensaje = "El enlace '$nuevo' ya esta en la lista.";
            $tipo_msg = 'err';
        } else {
            $lista_actual[] = $nuevo;
            if (guardar_lista($archivo, $lista_actual)) {
                $mensaje = "Enlace '$nuevo' agregado correctamente.";
                $tipo_msg = 'ok';
            } else {
                $mensaje = "No se pudo escribir el archivo enlaces.txt. "
                        . "Verifica permisos de escritura en " . dirname($archivo);
                $tipo_msg = 'err';
            }
        }
    }

    // QUITAR
    if ($accion === 'quitar') {
        $a_quitar = isset($_POST['enlace']) ? $_POST['enlace'] : '';
        $nueva = array_values(array_filter($lista_actual, function($x) use ($a_quitar) {
            return $x !== $a_quitar;
        }));
        if (count($nueva) === count($lista_actual)) {
            $mensaje = "No se encontro el enlace '$a_quitar'.";
            $tipo_msg = 'err';
        } elseif (guardar_lista($archivo, $nueva)) {
            $mensaje = "Enlace '$a_quitar' eliminado.";
            $tipo_msg = 'ok';
        } else {
            $mensaje = 'No se pudo escribir el archivo enlaces.txt. '
                    . 'Verifica permisos de escritura en ' . dirname($archivo);
            $tipo_msg = 'err';
        }
    }
}

// Releer la lista (puede haber cambiado tras un POST)
$enlaces = obtener_enlaces();
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Gestionar enlaces - ETN921</title>
    <link rel="stylesheet" href="estilos.css">
    <style>
        .lista-enlaces {
            list-style: none; padding: 0; margin: 1rem 0;
        }
        .lista-enlaces li {
            display: flex; justify-content: space-between; align-items: center;
            padding: 0.6rem 0.8rem; border-bottom: 1px solid var(--borde);
            font-family: var(--mono); font-size: 0.85rem;
        }
        .lista-enlaces li:hover { background: rgba(0,229,255,0.04); }
        .lista-enlaces .nombre { color: var(--acento); }
        .btn-quitar {
            background: rgba(239,68,68,0.15); color: #ef4444;
            border: 1px solid rgba(239,68,68,0.3);
            padding: 0.3rem 0.8rem; border-radius: 4px;
            font-family: var(--mono); font-size: 0.75rem;
            cursor: pointer;
        }
        .btn-quitar:hover { background: rgba(239,68,68,0.25); }
        .form-agregar {
            display: flex; gap: 0.5rem; margin: 1rem 0;
        }
        .form-agregar input { flex: 1; }
        .msg {
            padding: 0.7rem 1rem; border-radius: 6px;
            margin: 1rem 0; font-size: 0.9rem;
        }
        .msg-ok  { background: rgba(16,185,129,0.15); color: #10b981;
                   border: 1px solid rgba(16,185,129,0.3); }
        .msg-err { background: rgba(239,68,68,0.15); color: #ef4444;
                   border: 1px solid rgba(239,68,68,0.3); }
        .info-archivo {
            font-family: var(--mono); font-size: 0.75rem;
            color: var(--texto-dim); margin: 0.5rem 0 1rem;
            padding: 0.5rem; background: rgba(0,229,255,0.05);
            border-left: 2px solid var(--acento);
        }
    </style>
</head>
<body>
<header>
    <div class="header-inner">
        <h1>&#9881; Gestionar Enlaces Monitoreados</h1>
        <p class="subtitulo">ETN921 &mdash; Agregar o quitar dominios de la lista</p>
    </div>
</header>
<main>
    <section class="tarjeta">

        <?php if ($mensaje): ?>
            <div class="msg msg-<?php echo $tipo_msg; ?>"><?php echo htmlspecialchars($mensaje); ?></div>
        <?php endif; ?>

        <p>
            Estos son los enlaces que el sistema monitorea cada 5 minutos.
            Los cambios se aplican en la siguiente toma de muestras y se
            reflejan inmediatamente en la pagina principal.
        </p>

        <div class="info-archivo">
            Archivo: <?php echo htmlspecialchars($archivo); ?><br>
            Total de enlaces: <strong><?php echo count($enlaces); ?></strong>
        </div>

        <!-- Formulario para AGREGAR -->
        <h2>&#43; Agregar enlace</h2>
        <form method="POST" action="gestionar_enlaces.php" class="form-agregar">
            <input type="hidden" name="accion" value="agregar">
            <input type="text" name="enlace"
                   placeholder="Ejemplo: www.umsa.bo"
                   pattern="[a-zA-Z0-9.\-]+"
                   title="Solo letras, numeros, puntos y guiones."
                   required>
            <button type="submit">Agregar</button>
        </form>

        <!-- Lista de enlaces actuales con boton de quitar -->
        <h2>&#9776; Enlaces actuales</h2>
        <?php if (empty($enlaces)): ?>
            <p>La lista esta vacia.</p>
        <?php else: ?>
            <ul class="lista-enlaces">
                <?php foreach ($enlaces as $i => $e): ?>
                    <li>
                        <span><strong style="color:var(--texto-dim);"><?php echo $i+1; ?>.</strong>
                              &nbsp; <span class="nombre"><?php echo htmlspecialchars($e); ?></span></span>
                        <form method="POST" action="gestionar_enlaces.php" style="margin:0;"
                              onsubmit="return confirm('Quitar <?php echo htmlspecialchars($e); ?>?');">
                            <input type="hidden" name="accion" value="quitar">
                            <input type="hidden" name="enlace" value="<?php echo htmlspecialchars($e); ?>">
                            <button type="submit" class="btn-quitar">Quitar</button>
                        </form>
                    </li>
                <?php endforeach; ?>
            </ul>
        <?php endif; ?>

        <a href="index.php" class="btn-volver">&#8592; Volver al menu</a>
    </section>
</main>
<footer>
    <p>Sistema de Monitoreo TCP/IP &mdash; ETN921 &mdash; <?php echo date('Y'); ?></p>
</footer>
</body>
</html>
