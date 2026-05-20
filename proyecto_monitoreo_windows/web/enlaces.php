<?php
// enlaces.php
// Carga y procesa la lista de enlaces desde enlaces.txt

// Devuelve los enlaces válidos en un array
function obtener_enlaces() {
    $archivo = __DIR__ . '/enlaces.txt';
    $resultado = [];
	
	// Si el archivo no existe, retorna vacío
    if (!file_exists($archivo)) {
        return $resultado;
    }

	 // Lee líneas ignorando vacías
    $lineas = file($archivo, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    foreach ($lineas as $linea) {
        $linea = trim($linea);
        // Ignorar lineas vacias y comentarios
        if ($linea === '' || $linea[0] === '#') {
            continue;
        }
        //Permite  solo caracteres validos
        $linea = preg_replace('/[^a-zA-Z0-9.\-]/', '', $linea);
		// Guarda el enlace limpio
        if ($linea !== '') {
            $resultado[] = $linea;
        }
    }
    return $resultado;
}
// Devuelve enlaces numerados desde 1
function obtener_enlaces_numerados() {
    $enlaces = obtener_enlaces();
    $numerados = [];
    foreach ($enlaces as $i => $e) {
        $numerados[$i + 1] = $e;
    }
    return $numerados;
}



