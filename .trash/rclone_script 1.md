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
date_updated: 2026-07-18
status: activo
---

# rclone — Configuración del script de sync con Google Drive

> Guía de uso y rol en el vault: [[Rclone_guide]]
> Sistema de sync general: [[_sync-system]]

Este archivo documenta el proceso de configuración realizado para que rclone
pueda sincronizar archivos del vault hacia Google Drive. Incluye la configuración
en Google Cloud Console, la configuración del remote en rclone, la automatización
vía Task Scheduler y el botón de sync manual en Obsidian.

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
2. Crear proyecto nuevo → nombre: `rclone-personal`
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

> ⚠️ Con audience "Usuarios externos" y estado "En prueba", el refresh token
> expira cada 7 días. Para evitar reconexiones semanales, publicar la app
> (botón **Publicar**) antes de reconectar. Ver sección 6.

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

### Crear carpeta destino en Drive

```bash
rclone mkdir gdrive:NotebookLM_sources
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

Tarea configurada para ejecutar el sync automáticamente sin intervención manual.

| Campo | Valor |
|---|---|
| Nombre | `rclone sync notebooklm` |
| Desencadenador | Diariamente a las 12:00, repite cada **5 horas** indefinidamente |
| Programa | `E:\Programas\Rclone\rclone.exe` |
| Argumentos | `sync "E:\University_vault_2026\_app\notebooklm" gdrive:NotebookLM_sources` |
| Iniciar en | `E:\Programas\Rclone` |
| Detener tarea al repetir | No |

Acceder: `Win + R` → `taskschd.msc` → buscar `rclone sync notebooklm`

---

## 6. Shell Command — botón de sync manual en Obsidian

Configurado vía Shell Commands + Commander para ejecutar el sync sin esperar
Task Scheduler.

**Pestaña General**

| Campo | Valor |
|---|---|
| Alias | `Sync NotebookLM → Drive` |
| Comando | `rclone sync "E:\University_vault_2026\_app\notebooklm" gdrive:NotebookLM_sources --verbose` |

**Pestaña Output**

| Canal | Valor |
|---|---|
| stdout | Notification balloon |
| stderr | Error balloon |

**Ribbon:** agregado vía Commander. Icono: pendiente documentar.

---

## 7. Renovación de token

El token en `rclone.conf` puede expirar si la app está en estado **"En prueba"**
en Google Cloud Console (expira cada 7 días) o si no se usa rclone por un
período prolongado.

**Síntoma:** error `invalid_grant: token expired` en el balloon de error.

**Solución — reconectar:**
```bash
rclone config reconnect gdrive:
```
Abre el navegador, autenticarse con la cuenta personal, rclone actualiza el
token automáticamente en `rclone.conf`.

**Solución permanente — publicar la app:**

Para que el refresh token no expire nunca, publicar la app en Google Cloud Console:

1. Ir a [Google Cloud Console](https://console.developers.google.com/)
2. APIs y servicios → Pantalla de consentimiento OAuth
3. Estado de publicación → botón **Publicar app**
4. Confirmar
5. Después de publicar, correr `rclone config reconnect gdrive:` una vez más
   para obtener un token bajo la app publicada

> Publicar no requiere verificación de Google para apps de uso personal con
> un solo usuario autorizado.

---

%%
# galaxy-links
[[_app/_config/_sync-system.md]]
[[_app/_appnotes/Rclone_guide.md]]
%%
