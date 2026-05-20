
```php
function obtener_enlaces_numerados() {
    $enlaces = obtener_enlaces();
    $numerados = [];
    foreach ($enlaces as $i => $e) {
        $numerados[$i + 1] = $e;
    }
    return $numerados;
}
```


### ping_online.php

```php
$equipo = isset($_GET['Equipo']) ? (int)$_GET['Equipo'] : 0;
if (!array_key_exists($equipo, $enlaces)) {
    header("Location: index.php"); exit;
}
$ping = hacer_ping($enlaces[$equipo]);
```

### estado_enlaces.php

**Consulta de última muestra por enlace:**

```php
$stmt = $conn->prepare(
    "SELECT fecha, hora, rtt_max FROM muestras
     WHERE enlace = ? ORDER BY fecha DESC, hora DESC LIMIT 1"
);
```

**Clasificación del RTT:**

```php
if ($rtt < 0)        { $clase = "estado-error"; $texto = "Sin respuesta"; }
elseif ($rtt < 100)  { $clase = "estado-ok";    $texto = "OK"; }
elseif ($rtt < 300)  { $clase = "estado-warn";  $texto = "Lento"; }
else                 { $clase = "estado-error";  $texto = "Muy lento"; }
```


### gestionar_enlaces.php

**Lógica de agregar:**
```php
if ($accion === 'agregar') {
    $nuevo = preg_replace('/[^a-zA-Z0-9.\-]/', '', trim($_POST['enlace']));
    if (!in_array($nuevo, $lista_actual)) {
        $lista_actual[] = $nuevo;
        guardar_lista($archivo, $lista_actual);
    }
}
```

**Lógica de quitar:**
```php
if ($accion === 'quitar') {
    $nueva = array_values(array_filter($lista_actual, function($x) use ($a_quitar) {
        return $x !== $a_quitar;
    }));
    guardar_lista($archivo, $nueva);
}
```
