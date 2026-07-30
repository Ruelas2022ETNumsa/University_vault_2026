---
title: "rclone — Configuración del script de sync con Google Drive"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[Rclone_guide]]"
  - "[[_sync-system]]"
tags: [beacon, rclone, sync, google-drive, infraestructura, automatizacion]
date_created: 2026-07-18
date_updated: 2026-07-19
status: activo
---

# rclone — Configuración del script de sync con Google Drive

> Guía de uso y rol en el vault: [[Rclone_guide]]
> Sistema de sync general: [[_sync-system]]

Este archivo documenta el proceso de configuración realizado para que rclone
pueda sincronizar archivos del vault hacia Google Drive. Incluye la configuración
en Google Cloud Console, la configuración del remote en rclone, la automatización
vía Task Scheduler y los botones de sync manual en Obsidian.

> ⚠️ Este archivo se sincroniza con GitHub y Mega. No registrar valores de
> credenciales, tokens ni IDs. Para esos valores consultar los archivos en
> `E:\Programas\Rclone\datosclientemio\` — esa carpeta no se sincroniza con nada.

---

## 1. Archivos de credenciales

Todos los archivos sensibles viven exclusivamente en la PC. No se sincronizan con
Mega, GitHub ni ningún otro servicio.

| Archivo | Ubicación | Contenido |
|---|---|---|
| `backupdata.txt` | `E:\Programas\Rclone\datosclientemio\` | Client ID, Client Secret y output de configuración |
| `client_secret_(...).json` | `E:\Programas\Rclone\datosclientemio\` | Credenciales OAuth2 descargadas de Google Cloud Console. El nombre del archivo coincide con el Client ID |
| `rclone.conf` | `C:\Users\USUARIO\AppData\Roaming\rclone\` | Configuración del remote `gdrive` con token OAuth2 activo |
| `rclone.exe` | `E:\Programas\Rclone\` | Ejecutable de rclone v1.74.4 |

> En caso de reconfiguración futura (pérdida de token, cambio de cuenta, ampliación
> del sync), consultar `backupdata.txt` y el `.json` antes de correr `rclone config`.

---

## 2. Configuración en Google Cloud Console

Pasos realizados para crear el Client ID propio y evitar compartir cuota con
otros usuarios de rclone.

### 2.1 Crear proyecto y habilitar API

1. Ir a [Google Cloud Console](https://console.developers.google.com/) con la cuenta personal
2. Crear proyecto nuevo → nombre: `vault-notebooklm`
3. APIs y servicios → Buscar **Google Drive API** → Habilitar

### 2.2 Pantalla de consentimiento OAuth

1. APIs y servicios → Pantalla de consentimiento OAuth → Get started
2. Completar:
   - Nombre de app: `rclone`
   - Email de asistencia: email personal
   - Audience: **Usuarios externos**
   - Info de contacto: email personal
   - Aceptar política de datos → Crear
3. Acceso a datos → Agregar permisos → agregar manualmente:
   `https://www.googleapis.com/auth/drive` → Add to table → Update → Save
4. Público → Add users → agregar email personal → Guardar

### 2.3 Crear Client ID

1. Clientes → Crear cliente → tipo: **Aplicación de escritorio** → nombre: `rclone` → Crear
2. Copiar Client ID y Client Secret → guardar en `backupdata.txt`
3. Descargar JSON de credenciales → guardar en `datosclientemio\`

---

## 3. Configuración del remote en rclone

Comando usado para iniciar la configuración interactiva:

```bash
rclone config
```

Opciones seleccionadas:

| Pregunta | Valor elegido |
|---|---|
| Operación | `n` — nuevo remote |
| Nombre del remote | `gdrive` |
| Tipo de storage | `drive` (Google Drive) |
| client_id | Client ID propio (ver `backupdata.txt`) |
| client_secret | Client Secret propio (ver `backupdata.txt`) |
| scope | `drive` — acceso completo |
| service_account_file | (vacío — no aplica) |
| Edit advanced config | `n` |
| Autenticación por navegador | `y` — completada en navegador con la cuenta personal |
| Shared Drive | `n` — Drive personal |
| Confirmar remote | `y` |

Remote resultante guardado como `[gdrive]` en `rclone.conf`.

### Verificar conexión

```bash
rclone lsd gdrive:
```

---

## 4. PATH de Windows

Para que rclone sea invocable desde cualquier terminal y desde Task Scheduler
sin ruta absoluta:

Panel de control → sysdm.cpl → Opciones avanzadas → Variables de entorno
→ Variables del sistema → Path → Editar → Agregar: `E:\Programas\Rclone`

Verificar:
```bash
rclone version
```

---

## 5. Automatización — Task Scheduler

Tarea configurada para ejecutar el sync del vault automáticamente sin intervención manual.

| Campo | Valor |
|---|---|
| Nombre | `rclone sync vault` |
| Descripción | `Sincroniza vault completo con Google Drive (canal de lectura)` |
| Desencadenador | Diariamente a las 13:00, repite cada **5 horas** indefinidamente |
| Programa | `E:\Programas\Rclone\rclone.exe` |
| Argumentos | *(ver sección 8 — comando completo)* |
| Iniciar en | `E:\Programas\Rclone` |
| Configurado para | Windows 10 |
| Detener tarea al repetir | No |

Acceder: `Win + R` → `taskschd.msc` → buscar `rclone sync vault`

---

## 6. Shell Commands — botones de sync manual en Obsidian

Configurados vía Shell Commands + Commander para ejecutar el sync sin esperar
Task Scheduler.

### Sync vault completo → Drive

**Pestaña General**

| Campo | Valor |
|---|---|
| Alias | `Sync Vault → Drive` |
| Comando | *(ver sección 8 — comando completo con `--verbose`)* |

**Pestaña Output**

| Canal | Valor |
|---|---|
| stdout | Notification balloon |
| stderr | Error balloon |

**Ribbon:** agregado vía Commander.

---

## 7. Renovación de token

A partir de 2026-07-19 la app está publicada en Google Cloud Console (estado
**"En producción"**) — el refresh token no expira por tiempo.

**Si el token expira de todas formas** (por ejemplo por falta de uso prolongado):

**Síntoma:** error `invalid_grant: token expired` en el balloon de error.

**Solución:**
```bash
rclone config reconnect gdrive:
```
Abre el navegador, autenticarse con la cuenta personal, rclone actualiza el
token automáticamente en `rclone.conf`.

**Para publicar la app si se pierde el estado** (reconfiguración futura):

1. Ir a [Google Cloud Console](https://console.developers.google.com/)
2. Seleccionar proyecto `vault-notebooklm`
3. APIs y servicios → Pantalla de consentimiento OAuth
4. Estado de publicación → botón **Publicar app** → confirmar
5. Correr `rclone config reconnect gdrive:` una vez más para obtener token bajo app publicada

> Publicar no requiere verificación de Google para apps de uso personal con
> un solo usuario autorizado. El recuadro de verificación que aparece es una
> advertencia genérica — se ignora y se continúa con el flujo normal.

---

## 8. Comando completo — sync vault

```bash
rclone sync "E:\University_vault_2026" gdrive: --exclude "_PDF/**" --exclude "_assets/**" --exclude "Excalidraw/**" --exclude "_app/shellcommands/**" --exclude "_app/scripts/**" --exclude "_app/completr-words/**" --exclude "_app/_appnotes/tagroute_parche/**" --exclude "Borrar/**" --exclude "Rubbish/**" --exclude "Semestres/**" --exclude ".git/**" --exclude ".gitignore" --exclude ".gitattributes" --exclude ".cache/**" --exclude ".trash/**" --exclude ".obsidian/plugins/**" --exclude ".obsidian/scripts/**" --exclude ".obsidian/snippets/**" --exclude ".obsidian/themes/**" --exclude ".obsidian/cache/**" --exclude ".obsidian/workspace.json" --exclude ".obsidian/workspaces.json" --exclude ".obsidian/.trash/**" --filter "+ .obsidian/core-plugins.json" --filter "+ .obsidian/community-plugins.json" --verbose
```

**Notas:**
- Destino: raíz de `gdrive:` — preserva rutas relativas de los galaxy-links.
- Unidireccional: local → Drive. Drive nunca escribe hacia la PC.
- `--filter` antes de `--exclude` para `core-plugins.json` y `community-plugins.json`
  — única excepción dentro de `.obsidian/` que sí se sincroniza.
- Para dry-run (previsualización sin ejecutar): agregar `--dry-run` al comando.

---

%%
# galaxy-links
[[_app/_config/_sync-system.md]]
[[_app/_appnotes/Rclone_guide.md]]
%%
