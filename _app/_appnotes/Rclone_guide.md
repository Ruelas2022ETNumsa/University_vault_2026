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
date_updated: 2026-07-19
status: activo
---

# Rclone — Guía de configuración y uso

> Sistema de sync general: [[_sync-system]]
> Sistema NotebookLM: [[_notebooklm-system]]

Rclone es una herramienta de línea de comandos para sincronizar archivos hacia y
desde proveedores de almacenamiento en la nube. En este vault se usa para dos
propósitos: sincronizar el vault completo hacia Google Drive como canal de lectura
para Claude desde móvil/tablet, y mantener las fuentes de NotebookLM actualizadas
en Drive.

---

## Rol en el ecosistema del vault

Rclone no reemplaza a Mega ni a Git. Cada herramienta cumple un rol distinto:

| Herramienta | Rol | Destino |
|---|---|---|
| Mega + FolderSync | Sync del vault completo entre dispositivos | Todos los dispositivos |
| Obsidian Git | Control de versiones + escritura de Claude desde móvil | GitHub |
| **Rclone — vault sync** | Sync del vault completo como canal de lectura para Claude | Google Drive (raíz) |
| **Rclone — NotebookLM** | Sync de fuentes `.md` para NotebookLM | `gdrive:NotebookLM_sources/` *(eliminado 2026-07-19)* |

> A partir de 2026-07-19 el sync de NotebookLM fue absorbido por el sync general
> del vault. La carpeta `NotebookLM_sources/` fue eliminada de Drive y las fuentes
> vinculadas fueron dadas de baja en NotebookLM.

Rclone no corre en segundo plano de forma permanente — se ejecuta, sube los
cambios y termina. El consumo de CPU y memoria es mínimo y solo ocurre durante
los segundos que tarda la transferencia.

---

## Ubicaciones críticas

| Qué | Ruta |
|---|---|
| Ejecutable | `E:\Programas\Rclone\rclone.exe` |
| Credenciales OAuth2 (Client ID + Secret) | `E:\Programas\Rclone\datosclientemio\` |
| Archivo de configuración de rclone | `C:\Users\USUARIO\AppData\Roaming\rclone\rclone.conf` |
| Vault local sincronizado | `E:\University_vault_2026\` |
| Destino en Google Drive | Raíz de `gdrive:` |

> El archivo `rclone.conf` contiene el remote `gdrive` con el token OAuth2 activo.
> No compartir ni subir este archivo a GitHub — contiene credenciales de acceso.

### Archivos de credenciales

En `E:\Programas\Rclone\datosclientemio\` se encuentran dos archivos usados por
rclone para autenticación con Google Drive. No se sincronizan con ningún servicio
— viven únicamente en la PC. En caso de reconfiguración (pérdida de token, cambio
de cuenta, ampliación del sync), consultar esos archivos antes de correr
`rclone config`. Para el detalle completo del proceso de configuración:
[[rclone_script]]

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
2. Crear proyecto nuevo → nombre: `vault-notebooklm`
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

> **App publicada (2026-07-19):** el proyecto fue publicado en Google Cloud Console
> (estado "En producción") para evitar que el refresh token expire cada 7 días.
> Después de publicar se corrió `rclone config reconnect gdrive:` para obtener un
> token bajo la app publicada — el token ahora no expira por tiempo.

### Configuración del remote en rclone

Comando usado:
```bash
rclone config
```

Opciones seleccionadas durante la configuración interactiva:

| Pregunta | Valor elegido |
|---|---|
| Nombre del remote | `gdrive` |
| Tipo de storage | `drive` — Google Drive |
| client_id | Client ID propio (desde `datosclientemio/`) |
| client_secret | Client Secret propio (desde `datosclientemio/`) |
| scope | `drive` — acceso completo |
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

## Comando de sincronización — vault completo

Sincroniza el vault completo hacia la raíz de Drive, excluyendo archivos pesados,
carpetas de sistema local y contenido irrelevante para consulta.

```bash
rclone sync "E:\University_vault_2026" gdrive: --exclude "_PDF/**" --exclude "_assets/**" --exclude "_app/Excalidraw/**" --exclude "_app/shellcommands/**" --exclude "_app/scripts/**" --exclude "_app/completr-words/**" --exclude "_app/_appnotes/tagroute_parche/**" --exclude "Borrar/**" --exclude "Rubbish/**" --exclude "Semestres/**" --exclude ".git/**" --exclude ".gitignore" --exclude ".gitattributes" --exclude ".cache/**" --exclude ".trash/**" --exclude ".obsidian/plugins/**" --exclude ".obsidian/scripts/**" --exclude ".obsidian/snippets/**" --exclude ".obsidian/themes/**" --exclude ".obsidian/cache/**" --exclude ".obsidian/workspace.json" --exclude ".obsidian/workspaces.json" --exclude ".obsidian/.trash/**" --filter "+ .obsidian/core-plugins.json" --filter "+ .obsidian/community-plugins.json" --verbose
```

### Qué se excluye y por qué

| Excluido | Motivo |
|---|---|
| `_PDF/**` | Archivos pesados — cubiertos por Mega y Git |
| `_assets/**` | Imágenes exportadas — pesadas, no útiles para consulta de texto |
| `_app/Excalidraw/**` | Archivos `.excalidraw` (JSON pesado) — no legibles como texto |
| `_app/shellcommands/**` | Scripts con rutas locales y datos sensibles de la PC |
| `_app/scripts/**` | Scripts JS locales — sin uso en consulta desde Drive |
| `_app/completr-words/**` | Diccionario local del plugin Completr — irrelevante |
| `_app/_appnotes/tagroute_parche/**` | Carpeta de parche temporal — sin valor para consulta |
| `Borrar/**` | Zona de espera de archivos a eliminar |
| `Rubbish/**` | Carpeta de uso exclusivo en PC/laptop |
| `Semestres/**` | Carpeta legacy (ETN302 y otros) — fuera del Sistema Galaxy activo |
| `.git/**` | Control de versiones — innecesario en Drive |
| `.gitignore`, `.gitattributes` | Archivos de configuración Git — sin uso en Drive |
| `.cache/**` | Caché local |
| `.trash/**`, `.obsidian/.trash/**` | Papelera interna de Obsidian |
| `.obsidian/plugins/**` | Plugins instalados — cubiertos por Mega y Git |
| `.obsidian/scripts/**` | Scripts de Templater — solo útiles con Obsidian abierto |
| `.obsidian/snippets/**` | CSS local — irrelevante en Drive |
| `.obsidian/themes/**` | Temas visuales — irrelevante en Drive |
| `.obsidian/cache/**` | Caché de Obsidian |
| `.obsidian/workspace.json` | Estado de sesión — cambia constantemente, sin valor |
| `.obsidian/workspaces.json` | Estado de sesión — ídem |

### Qué se incluye de `.obsidian/`

| Incluido | Motivo |
|---|---|
| `core-plugins.json` | Permite saber qué plugins nativos están activos |
| `community-plugins.json` | Permite saber qué plugins de comunidad están instalados |

### Notas sobre el comportamiento de sync

- `sync` es **unidireccional**: local → Drive. La PC es siempre la fuente de verdad.
- Drive nunca escribe hacia la PC.
- Si un archivo fue eliminado localmente, `sync` lo elimina también en Drive.
- Si una carpeta es renombrada, rclone sube la carpeta nueva y elimina la vieja en Drive.
- Los galaxy-links usan rutas relativas desde la raíz del vault. El vault se sincroniza
  en la raíz de Drive para que esas rutas sean válidas también desde Drive MCP.

---

## Automatización — Task Scheduler

Dos tareas configuradas para ejecutar los syncs automáticamente.

### Tarea: `rclone sync vault`

| Campo | Valor |
|---|---|
| Nombre | `rclone sync vault` |
| Descripción | `Sincroniza vault completo con Google Drive (canal de lectura)` |
| Desencadenador | Diariamente a las 13:00, repite cada **5 horas** indefinidamente |
| Programa | `E:\Programas\Rclone\rclone.exe` |
| Argumentos | *(ver comando completo en sección anterior)* |
| Iniciar en | `E:\Programas\Rclone` |
| Configurado para | Windows 10 |
| Detener tarea al repetir | No |

### Cómo acceder a las tareas para editarlas

`Win + R` → `taskschd.msc` → buscar la tarea en la lista →
clic derecho → Propiedades → pestaña Desencadenadores → Editar.

### Ejecutar manualmente sin esperar la hora

Desde Task Scheduler: clic derecho sobre la tarea → **Ejecutar**.
Desde cmd: pegar el comando completo de la sección anterior con `--verbose`.
Desde Obsidian: botón `Sync Vault → Drive` en el ribbon → ver [[rclone_script]] sección 8.

---

## Flujo completo de uso

```
PC — edición normal del vault
        ↓
rclone sync vault corre automáticamente cada 5 horas (Task Scheduler)
o manualmente desde cmd o botón en Obsidian si no se quiere esperar
        ↓
Google Drive tiene el vault actualizado en su raíz
        ↓
Claude desde móvil/tablet lee el vault via Drive MCP
GitHub MCP permite crear/editar notas desde móvil → llegan al vault via Obsidian Git
```

---

## Registro de decisiones

| Decisión | Razón |
|---|---|
| Rclone en lugar de script Python | Rclone hace lo mismo sin escribir ni mantener código |
| Client ID propio en lugar del de rclone | El Client ID compartido de rclone tiene cuota limitada entre todos sus usuarios; el propio garantiza cuota exclusiva |
| App publicada en Google Cloud Console (2026-07-19) | Evita que el refresh token expire cada 7 días — con app "En prueba" los tokens duran solo 7 días |
| `sync` en lugar de `copy` | Los archivos eliminados localmente deben eliminarse también en Drive |
| Vault en raíz de Drive en lugar de subcarpeta | Los galaxy-links usan rutas relativas desde la raíz del vault — sincronizar en la raíz de Drive preserva esas rutas para Drive MCP |
| Drive unidireccional (solo lectura desde móvil) | La PC es la fuente de verdad; escritura desde móvil va por GitHub MCP → Obsidian Git |
| `NotebookLM_sources/` eliminada (2026-07-19) | El sync general del vault cubre `_app/notebooklm/` — carpeta dedicada redundante |
| `Semestres/` excluida | Carpeta legacy fuera del Sistema Galaxy activo |
| `.obsidian/plugins/` excluida | Pesada e irrelevante para consulta; cubierta por Mega y Git |
| Solo `core-plugins.json` y `community-plugins.json` de `.obsidian/` | Suficiente para saber qué plugins están activos sin subir configuración local innecesaria |
| `_app/shellcommands/` excluida | Contiene rutas locales de la PC y datos sensibles |
| rclone.conf excluido de GitHub | Contiene token OAuth2 activo — no debe exponerse en un repositorio |

---

## Solución de problemas

**Error `invalid_grant: token expired`:**
El refresh token expiró. Desde 2026-07-19 la app está publicada y esto no debería
ocurrir. Si ocurre de todas formas:
```bash
rclone config reconnect gdrive:
```

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
Correr el comando manualmente con `--verbose` para ver si hay errores de autenticación o conectividad.
Verificar contenido de Drive con `rclone lsd gdrive:`.

**Carpeta renombrada en el vault:**
Rclone no detecta renombres — sube la carpeta con el nombre nuevo y elimina la vieja en Drive
en el próximo sync. No hay pérdida de datos. Si se necesita el cambio en Drive antes del próximo
sync automático, ejecutar manualmente.

---

%%
# galaxy-links
[[_app/_config/_sync-system.md]]
[[_app/_config/_notebooklm-system.md]]
[[_app/shellcommands/rclone_script.md]]
%%
