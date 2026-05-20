
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

#