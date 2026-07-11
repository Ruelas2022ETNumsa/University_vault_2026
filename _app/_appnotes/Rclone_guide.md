---
title: Rclone — Guía de configuración y uso
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
related_notes:
  - "[[_sync-system]]"
  - "[[_notebooklm-system]]"
tags:
  - beacon
  - rclone
  - sync
  - google-drive
  - infraestructura
date_created: 2026-07-10
date_updated: 2026-07-10
status: activo
---

# Rclone — Guía de configuración y uso

> Sistema de sync general: [[_sync-system]]
> Sistema NotebookLM: [[_notebooklm-system]]

Rclone es una herramienta de línea de comandos para sincronizar archivos hacia y
desde proveedores de almacenamiento en la nube. En este vault se usa exclusivamente
para sincronizar las fuentes `.md` del vault hacia Google Drive, de donde
NotebookLM las lee como fuentes vinculadas.

---

## Rol en el ecosistema del vault

Rclone no reemplaza a Mega ni a Git. Cada herramienta cumple un rol distinto:

| Herramienta | Rol | Destino |
|---|---|---|
| Mega + FolderSync | Sync del vault completo entre dispositivos | Todos los dispositivos |
| Obsidian Git | Control de versiones + acceso de Claude | GitHub |
| **Rclone** | Sync de fuentes NotebookLM hacia Drive | Google Drive |

Rclone no corre en segundo plano de forma permanente — se ejecuta, sube los
cambios y termina. El consumo de CPU y memoria es mínimo y solo ocurre durante
los segundos que tarda la transferencia.

---

## Ubicaciones críticas

| Qué | Ruta |
|---|---|
| Ejecutable | `E:\Programas\Rclone\rclone.exe` |
| Credenciales OAuth2 (Client ID + Secret) | `E:\Programas\Rclone\datosclientemio\` (.txt y .json) |
| Archivo de configuración de rclone | `C:\Users\USUARIO\AppData\Roaming\rclone\rclone.conf` |
| Carpeta local sincronizada | `E:\University_vault_2026\_app\notebooklm\` |
| Carpeta destino en Google Drive | `NotebookLM_sources/` |

> El archivo `rclone.conf` contiene el remote `gdrive` con el token OAuth2 activo.
> No compartir ni subir este archivo a GitHub — contiene credenciales de acceso.

---

## Instalación realizada

- Versión instalada: **rclone v1.74.4**
- Sistema: Windows 10 Pro 22H2 (64 bit / amd64)
- Descargado desde: https://rclone.org/downloads/ → archivo `rclone-v1.74.4-windows-amd64.zip`
- Instalación: extracción del `.zip`, `rclone.exe` colocado en `E:\Programas\Rclone\`
- PATH de Windows: `E:\Programas\Rclone` agregado en Variables del sistema → Path
  (Panel de control → sysdm.cpl → Opciones avanzadas → Variables de entorno → Variables del sistema)

Verificación de instalación:
```bash
rclone version
```

---

## Configuración del remote Google Drive

El remote se llama `gdrive` y fue configurado con Client ID propio para evitar
compartir cuota con otros usuarios de rclone.

### Pasos realizados para crear el Client ID en Google Cloud Console

1. Ir a https://console.developers.google.com/ con la cuenta de Google personal
2. Crear proyecto nuevo → nombre: `rclone-personal`
3. Habilitar **Google Drive API** (+ APIs y servicios → buscar "Google Drive API" → Habilitar)
4. Pantalla de consentimiento OAuth → Descripción general → Get started:
   - Nombre de app: `rclone`
   - Email de asistencia: email personal
   - Audience: **Usuarios externos**
   - Info de contacto: email personal
   - Aceptar política de datos → Crear
5. Acceso a datos → Agregar o quitar permisos → agregar manualmente:
   `https://www.googleapis.com/auth/drive` → Add to table → Update → Save
6. Público → Add users → agregar email personal → Guardar
7. Clientes → Crear cliente → tipo: **Aplicación de escritorio** → nombre: `rclone` → Crear
8. Copiar **Client ID** y **Client Secret** → guardados en `E:\Programas\Rclone\datosclientemio\`
9. Descargar JSON de credenciales → guardado en la misma carpeta

### Configuración del remote en rclone

Comando usado:
```bash
rclone config
```

Opciones seleccionadas durante la configuración interactiva:

| Pregunta | Valor elegido |
|---|---|
| Nombre del remote | `gdrive` |
| Tipo de storage | `24` — Google Drive |
| client_id | Client ID propio (desde `datosclientemio/`) |
| client_secret | Client Secret propio (desde `datosclientemio/`) |
| scope | `1` — Full access all files |
| service_account_file | (vacío — no aplica) |
| Edit advanced config | `n` |
| Autenticación por navegador | `y` — autenticación completada en navegador |
| Shared Drive | `n` — Drive personal |

Remote resultante guardado en `rclone.conf` como `[gdrive]`.

### Verificar conexión y listar Drive

```bash
rclone lsd gdrive:
```

---

## Carpeta en Drive

Carpeta creada durante la configuración:
```bash
rclone mkdir gdrive:NotebookLM_sources
```

Contenido sincronizado: las subcarpetas `general/` y `guides/` de
`E:\University_vault_2026\_app\notebooklm\`, con un total inicial de 18 archivos `.md`.

---

## Comando de sincronización

```bash
rclone sync "E:\University_vault_2026\_app\notebooklm" gdrive:NotebookLM_sources --progress
```

- `sync` — sincroniza en un sentido: local → Drive. Lo que está en local es la fuente de verdad.
- `--progress` — muestra transferencias en tiempo real (opcional, útil para diagnóstico).
- Si un archivo fue eliminado localmente, `sync` lo elimina también en Drive.
- Si solo se quiere subir sin eliminar nada en Drive, usar `copy` en lugar de `sync`.

---

## Automatización — Task Scheduler

Se configuró una tarea en el Programador de tareas de Windows para ejecutar el
sync automáticamente cada hora sin intervención manual.

### Configuración de la tarea

| Campo | Valor |
|---|---|
| Nombre | `rclone sync notebooklm` |
| Descripción | `Sincroniza vault con Google Drive` |
| Desencadenador | Diariamente a las 14:29, repite cada **1 hora** indefinidamente |
| Acción | Iniciar un programa |
| Programa | `E:\Programas\Rclone\rclone.exe` |
| Argumentos | `sync "E:\University_vault_2026\_app\notebooklm" gdrive:NotebookLM_sources` |
| Iniciar en | `E:\Programas\Rclone` |
| Detener tarea en ejecución al repetir | No — para no cortar transferencias en curso |

### Cómo acceder a la tarea para editarla

`Win + R` → `taskschd.msc` → buscar `rclone sync notebooklm` en la lista →
clic derecho → Propiedades → pestaña Desencadenadores → Editar.

### Ejecutar manualmente sin esperar la hora

Desde Task Scheduler: clic derecho sobre la tarea → **Ejecutar**.
Desde cmd:
```bash
rclone sync "E:\University_vault_2026\_app\notebooklm" gdrive:NotebookLM_sources --progress
```

Desde Obsidian: botón `upload-cloud` en el ribbon → ver [[plugin_guide]] sección 8. Shell Commands.

---

## Flujo completo de uso

```
1. Editar o crear archivo .md en _app/notebooklm/ (guides/, general/, prompts/)
        ↓
2. rclone sync corre automáticamente cada hora (Task Scheduler)
   o manualmente desde cmd o Task Scheduler si no se quiere esperar
        ↓
3. Google Drive tiene los archivos actualizados en NotebookLM_sources/
        ↓
4. Abrir NotebookLM → fuente vinculada → botón refresh
   (único paso manual — NotebookLM no detecta cambios automáticamente)
```

---

## Registro de decisiones

| Decisión | Razón |
|---|---|
| Rclone en lugar de script Python | Rclone hace lo mismo sin escribir ni mantener código |
| Client ID propio en lugar del de rclone | El Client ID compartido de rclone tiene cuota limitada entre todos sus usuarios; el propio garantiza cuota exclusiva |
| `sync` en lugar de `copy` | Los archivos eliminados localmente deben eliminarse también en Drive para que NotebookLM no lea fuentes obsoletas |
| Task Scheduler cada 1 hora | Las guías de NotebookLM cambian con poca frecuencia — cada hora es suficiente sin consumir recursos innecesariamente |
| Solo carpeta `_app/notebooklm/` sincronizada con Drive | Drive es exclusivo para fuentes de NotebookLM — el vault completo ya tiene Mega y GitHub como respaldo |
| rclone.conf excluido de GitHub | Contiene token OAuth2 activo — no debe exponerse en un repositorio |
| Drive no reemplaza a Mega | Roles distintos: Mega sincroniza el vault completo entre dispositivos; Drive es solo el canal hacia NotebookLM |

---

## Solución de problemas

**Error `invalid_client` al autenticar:**
El Client Secret fue copiado incorrectamente. Correr `rclone config` → editar remote `gdrive` →
corregir el secret. Los credenciales correctos están en `E:\Programas\Rclone\datosclientemio\`.

**El remote `gdrive` no aparece:**
Verificar que `rclone.conf` existe en `C:\Users\USUARIO\AppData\Roaming\rclone\`.
Si fue borrado accidentalmente, repetir `rclone config` con los credenciales de `datosclientemio/`.

**Task Scheduler no ejecuta la tarea:**
Verificar que el PATH de Windows incluye `E:\Programas\Rclone`.
Alternativamente, en el campo "Programa" de la tarea usar la ruta completa `E:\Programas\Rclone\rclone.exe`
(ya está configurado así — no debería ser problema).

**Archivos no aparecen en Drive después del sync:**
Correr el comando manualmente con `--progress` para ver si hay errores de autenticación o conectividad.
Verificar que la carpeta `NotebookLM_sources` existe en Drive con `rclone lsd gdrive:`.

%%
galaxy-links
[[_sync-system]]
[[_notebooklm-system]]
%%
