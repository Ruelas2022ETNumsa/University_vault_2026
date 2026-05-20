
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

