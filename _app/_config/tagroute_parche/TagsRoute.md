# Obsidian TagsRoutes Patch System

## Objetivo

Crear un sistema manual de parche para el plugin `Tags Routes` de Obsidian que:

1. Detecte y migre la carpeta desde E:\University_vault_2026:

```text
E:\University_vault_2026/TagsRoutes/
```

hacia:

```text
E:\University_vault_2026/_app/TagsRoutes/
```

2. Mueva/copíe automáticamente todo el contenido generado por el plugin:
- `logMessage.md`
- `logs/`
- `reports/`
- otros archivos internos

3. Modifique automáticamente el archivo:

```text
.obsidian/plugins/tags-routes/main.js
```

para que el plugin use permanentemente la nueva ruta:

```js
var programDirectory = "_app/TagsRoutes";
```

en lugar de:

```js
var programDirectory = "TagsRoutes";
```

4. Ejecutarse manualmente después de actualizar plugins en Obsidian.

---

# Qué se encontró

Dentro de `main.js` del plugin existe (linea 69218-69221):

```js
var programDirectory = "TagsRoutes";
var logDirectory = `${programDirectory}/logs`;
var reportDirectory = `${programDirectory}/reports`;
var logFilePath = `${programDirectory}/logMessage.md`;
```

Esto confirma que:
- la carpeta raíz del plugin está hardcodeada,
- pero centralizada en una sola variable,
- por lo que el parche es sencillo y estable.

---

# Solución elegida

## Script manual de parche

Se usará un script externo:
- PowerShell (`.ps1`)
- ejecutado desde un `.bat`
O se busca otra solucion con obsidian de ser posible.

se reviso lo siguientes puntos pero se concideran malos (reevaluar):
- CSS Snippets,
- monkey patching runtime,
- plugins JS externos,
- modificaciones dinámicas dentro de Obsidian.

---

# Flujo del parche

## 1. Detectar carpeta vieja

Si existe:

```text
TagsRoutes/
```

---

## 2. Crear nueva ruta

Crear si no existe:

```text
_app/TagsRoutes/
```

---

## 3. Migrar contenido

Mover/copiar:
- archivos,
- logs,
- reportes,
- subcarpetas

desde:

```text
TagsRoutes/
```

hacia:

```text
_app/TagsRoutes/
```

---

## 4. Eliminar carpeta vieja

Si quedó vacía:

```text
TagsRoutes/
```

---

## 5. Parchear `main.js`

Buscar:

```js
var programDirectory = "TagsRoutes";
```

y reemplazar por:

```js
var programDirectory = "_app/TagsRoutes";
```

---

# Uso previsto

## Workflow
conciderar el 3. y 5. ya que hay casos en los que obsidian solo requiere una actualizacion y reconoce los cambios (evaluar esto)

```text
1. Abrir Obsidian
2. Actualizar plugins manualmente
3. Cerrar Obsidian (de ser necesario)
4. Ejecutar patcher
5. Abrir Obsidian nuevamente
```

---

# Razón para hacerlo así

El plugin:
- no se actualiza automáticamente,
- carga `main.js` al iniciar,
- por lo tanto el parche debe existir antes de que el plugin se ejecute nuevamente.

Modificar el archivo después de abrir Obsidian:
- no afecta la sesión actual,
- solo tendría efecto tras reiniciar.

---

# Ventajas de esta solución

| Característica | Resultado |
|---|---|
| Persistencia tras updates | ✅ |
| Mantener estructura limpia del vault | ✅ |
| Sin hacks runtime | ✅ |
| Fácil mantenimiento | ✅ |
| Compatible con Git | ✅ |
| Compatible con Remotely Save | ✅ |
| Escalable a otros plugins | ✅ |

---

# Archivos involucrados

## Plugin

```text
.obsidian/plugins/tags-routes/main.js
```

```text
.obsidian/plugins/tags-routes/manifest.json
```

---

## Script

```text
patch-obsidian.ps1
```

```text
patch-obsidian.bat
```

---

# Resultado final esperado

Después del parche:

```text
app/
└── TagsRoutes/
    ├── logMessage.md
    ├── logs/
    ├── reports/
    └── screenshots/
```

Y ya no debería regenerarse:

```text
TagsRoutes/
```

en la raíz del vault.