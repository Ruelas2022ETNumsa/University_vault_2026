<?php
// ping_helper.php
// Ejecuta pings en Windows usando ping_web.bat
// y devuelve la salida junto al tiempo máximo de respuesta.
function hacer_ping($destino) {
    // Filtra caracteres no válidos
    $destino_limpio = preg_replace('/[^a-zA-Z0-9.\-]/', '', $destino);
	// Verifica dirección válida
    if ($destino_limpio === '') {
        return ['salida' => 'ERROR: Direccion invalida.', 'rtt_max' => -1];
    }
    // Ruta del script batch
    $bat = __DIR__ . DIRECTORY_SEPARATOR . 'ping_web.bat';
	// Verifica existencia del .bat
    if (!file_exists($bat)) {
        return ['salida' => 'ERROR: No se encontro ping_web.bat en ' . __DIR__,
                'rtt_max' => -1];
    }
	// Ejecuta el ping desde PHP
    $cmd = '"' . $bat . '" ' . escapeshellarg($destino_limpio) . ' 2>&1';
    $salida = shell_exec($cmd);

	// Verifica error de ejecución
    if ($salida === null) {
        return ['salida' => 'ERROR: shell_exec devolvio null. ' .
                            'Revisa permisos de ' . $bat,
                'rtt_max' => -1];
    }
    // Extrae tiempos de respuesta del ping
    $rtt_max = -1;
    if (preg_match_all('/(?:tiempo|time)\s*[=<]\s*(\d+(?:[.,]\d+)?)\s*ms/i', $salida, $matches)) {
        $tiempos = [];
        foreach ($matches[1] as $t) {
            $tiempos[] = (float) str_replace(',', '.', $t);
        }
		// Obtiene el mayor tiempo registrado
        if (!empty($tiempos)) {
            $rtt_max = max($tiempos);
        }
    }
	// Retorna salida y tiempo máximo
    return ['salida' => $salida, 'rtt_max' => $rtt_max];
}





