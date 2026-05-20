<?php
// ============================================================
//  ping_helper.php  — Helper compartido para hacer ping en Windows
//
//  Arquitectura segun la especificacion del proyecto:
//
//      navegador --GET--> PHP --shell_exec--> ping_web.bat --> ping
//
//  Esto sustituye la cadena Linux original:
//      navegador --GET--> PHP --shell_exec--> bash ping_online.sh --> ping
//
//  Maneja la salida de ping en Espanol e Ingles de Windows:
//    Espanol:  "tiempo=15ms" / "tiempo<1ms"
//    Ingles:   "time=15ms"   / "time<1ms"
//
//  Compatible con PHP 7.1.11 (sin match(), sin arrow functions).
// ============================================================

/**
 * Ejecuta ping a $destino llamando al script ping_web.bat
 * y devuelve un array con la salida cruda y el RTT maximo (ms).
 *
 * @param string $destino  dominio o IP
 * @return array  ['salida' => string, 'rtt_max' => float|int]  (-1 si no responde)
 */
function hacer_ping($destino) {
    // Sanitizacion: solo letras, numeros, puntos y guiones (como en el sh original)
    $destino_limpio = preg_replace('/[^a-zA-Z0-9.\-]/', '', $destino);
    if ($destino_limpio === '') {
        return ['salida' => 'ERROR: Direccion invalida.', 'rtt_max' => -1];
    }

    // Ruta absoluta al .bat (en la misma carpeta que este PHP)
    $bat = __DIR__ . DIRECTORY_SEPARATOR . 'ping_web.bat';

    if (!file_exists($bat)) {
        return ['salida' => 'ERROR: No se encontro ping_web.bat en ' . __DIR__,
                'rtt_max' => -1];
    }

    // shell_exec del .bat con el destino como argumento.
    // Sobre IIS+FastCGI esto ejecuta el .bat bajo la identidad del
    // Application Pool. La carpeta del proyecto debe tener permisos
    // de lectura/ejecucion para IIS_IUSRS (lo hace menu.bat opcion 4).
    $cmd = '"' . $bat . '" ' . escapeshellarg($destino_limpio) . ' 2>&1';
    $salida = shell_exec($cmd);

    if ($salida === null) {
        return ['salida' => 'ERROR: shell_exec devolvio null. ' .
                            'Revisa permisos de ' . $bat,
                'rtt_max' => -1];
    }

    // Extraer todos los tiempos de cada respuesta.
    // Patron acepta:
    //   "tiempo=15ms" / "time=15ms" (separador =)
    //   "tiempo<1ms"  / "time<1ms"  (separador <, para latencias <1ms)
    //   coma o punto decimal segun el locale
    $rtt_max = -1;
    if (preg_match_all('/(?:tiempo|time)\s*[=<]\s*(\d+(?:[.,]\d+)?)\s*ms/i', $salida, $matches)) {
        $tiempos = [];
        foreach ($matches[1] as $t) {
            $tiempos[] = (float) str_replace(',', '.', $t);
        }
        if (!empty($tiempos)) {
            $rtt_max = max($tiempos);
        }
    }

    return ['salida' => $salida, 'rtt_max' => $rtt_max];
}
