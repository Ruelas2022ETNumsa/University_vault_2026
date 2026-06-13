---
title: "Sistema Sync — Vault y Acceso Claude"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
  - "[[_ToDo-system]]"
tags: [beacon, sync, github, infraestructura]
date_created: 2026-05-28
date_updated: 2026-06-13
status: activo
---

# Sistema Sync — Vault y Acceso Claude

> Sistema Galaxy: [[_galaxy-system]]
> Pendientes: [[_ToDo-system]]

## Objetivo

Que Claude pueda leer, crear y editar notas `.md` del vault de Obsidian directamente desde GitHub, sin depender de que la PC esté encendida. El vault local en PC se sincroniza automáticamente con GitHub mediante Obsidian Git y con Mega para distribución entre dispositivos.

> ⚠️ **Migración completada (2026-06-13):** Se migró de Google Drive File Stream a **Mega** como sistema principal de sincronización del vault entre dispositivos. Drive se mantiene ÚNICAMENTE para TAB_nexus (PDFs tablet ↔ PC). La cuenta Mega usada es exclusiva para el vault. La migración se realizó sin problemas — las carpetas deseadas se sincronizaron correctamente desde el inicio.

---

## Flujo actual

```
Claude (lee y edita archivos)
        ⇕
GitHub → https://github.com/Ruelas2022ETNumsa/University_vault_2026
        ⇕
Obsidian Git (auto-sync cada 5 min)
        ⇕
PC Escritorio Local → E:\University_vault_2026  [UNICO que sincroniza con Mega Y con Git]
        ⇕
Mega (sincronización vault entre dispositivos)
        ⇕
┌──────────────────────────┐
│ Tablet (FolderSync bidirec.)  │  Celular (FolderSync solo lectura)
│ /University_vault_2026       │  /University_vault_2026
└──────────────────────────┘
        ⇕
Google Drive (intocable — solo TAB_nexus)
        ⇕
Symlink: E:\University_vault_2026\_pdf\TAB_nexus
        ⇕
C:\Users\USUARIO\Mi unidad (kraaajooo123@gmail.com)\TAB_nexus
        ⇕
Autosync (tablet) — bidireccional, cada 1h, solo WiFi
        ⇕
Tablet Samsung S6 Lite → /storage/emulated/0/Documentos/Pdf/
```

### Flujo de apuntes desde tablet

```
Samsung Notes (apunte a mano)
        ↓
Exportar como PDF → /Documentos/Pdf/ en tablet
        ↓
Autosync detecta archivo nuevo → sube a Mi unidad/TAB_nexus en Drive
        ↓
File Stream replica → C:\Users\USUARIO\Mi unidad\TAB_nexus\
        ↓
Symlink → E:\University_vault_2026\_pdf\TAB_nexus\ (vault)
        ↓
PDF++ anota/mejora el PDF en Obsidian
        ↓
Autosync bidireccional → versión anotada baja a tablet también
        ↓
IA transcribe PDF → .md
        ↓
GitHub (via Obsidian Git)
```

---

## Lo que ya está hecho ✅

- [x] Vault renombrado a `University_vault_2026`
- [x] Repositorio GitHub creado: `University_vault_2026` (rama `main`)
- [x] Git instalado en la PC
- [x] Repositorio local vinculado a GitHub (`git remote` configurado)
- [x] Primer push realizado — archivos visibles en GitHub
- [x] Plugin **Obsidian Git** instalado, activado y configurado en PC
  - Auto-commit, auto-push y auto-pull cada **5 minutos** de forma automática
  - Pull adicional al arrancar Obsidian
  - El usuario no necesita ejecutar git manualmente — todo es automático
- [x] Conector **Filesystem** de Claude apuntando a `E:\University_vault_2026`
- [x] Conector **GitHub** conectado en Claude.ai — `https://api.githubcopilot.com/mcp`
- [x] Carpeta `_pdf/TAB_nexus/` creada en el vault como symlink ✅
- [x] Google Drive File Stream configurado en modo **replicar archivos** ✅
- [x] Symlink creado: `E:\University_vault_2026\_pdf\TAB_nexus` → `C:\Users\USUARIO\Mi unidad\TAB_nexus` ✅
- [x] Autosync instalado y configurado en tablet (bidireccional, cada 1h, solo WiFi) ✅
- [x] Par sincronizado: `/Documentos/Pdf/` ↔ `Mi unidad/TAB_nexus` ✅
- [x] Flujo completo verificado: PDF de tablet llega al vault en PC ✅
- [x] Flujo bidireccional verificado: anotaciones de PDF++ llegan a la tablet ✅

> Tareas y pendientes: [[_ToDo-system]]

---

## Sincronización tablet — Google Drive + Autosync

La tablet **no usa Obsidian**. Sincroniza PDFs via Autosync + Google Drive File Stream.

### Componentes

| Componente | Ubicación | Función |
|---|---|---|
| Autosync for Google Drive | Tablet | Sincroniza `/Documentos/Pdf/` ↔ `Mi unidad/TAB_nexus` bidireccional |
| Google Drive File Stream | PC | Replica `Mi unidad` a `C:\Users\USUARIO\Mi unidad\` |
| Symlink Windows | PC | Conecta `E:\University_vault_2026\_pdf\TAB_nexus` con la carpeta de Drive |

### Configuración Autosync (tablet)

- Par: `TAB_PDF>TAB_nexus`
- Carpeta izquierda: `/storage/emulated/0/Documentos/Pdf/`
- Carpeta derecha: `Mi unidad/TAB_nexus` en Google Drive
- Dirección: **bidireccional**
- Intervalo: cada **1 hora**
- Conexión: **solo WiFi**

### Configuración File Stream (PC)

- Modo Mi unidad: **Replicar archivos**
- Ruta local: `C:\Users\USUARIO\Mi unidad (kraaajooo123@gmail.com)\`

### Symlink (PC)

Creado con:
```
mklink /D "E:\University_vault_2026\_pdf\TAB_nexus" "C:\Users\USUARIO\Mi unidad (kraaajooo123@gmail.com)\TAB_nexus"
```

### Flujo de trabajo

**Tablet → vault:** Samsung Notes exporta PDF a `/Documentos/Pdf/` → Autosync lo sube a Drive → File Stream lo replica en PC → symlink lo hace visible en el vault.

**Vault → tablet:** PDF++ anota el PDF en el vault → File Stream lo sube a Drive → Autosync bidireccional lo baja a la tablet.

> Remotely Save fue descartado. La tablet no sincroniza el vault completo — solo la carpeta de PDFs.

---

## Sincronización móvil alterna — Git en Android

> Pendiente por falta de tiempo. Documentado para implementar cuando se disponga.
> Ventaja principal: el móvil quedaría en el mismo canal que PC y Claude (GitHub), una sola fuente de verdad sin servicios paralelos.

### Opción recomendada: MGit + Obsidian Git

**Requisitos:** Android, MGit (gratuito en F-Droid o APK), Obsidian instalado.

**Pasos:**

1. Instalar **MGit** desde F-Droid o desde el APK oficial
2. En GitHub → Settings → Developer Settings → Personal Access Tokens → generar token con permisos `repo`
3. En MGit → **Clone** → ingresar la URL del repositorio:
   `https://github.com/Ruelas2022ETNumsa/University_vault_2026`
4. Elegir carpeta local de destino en el Android (p.ej. `/storage/emulated/0/University_vault_2026`)
5. Ingresar usuario y token cuando MGit los pida
6. Esperar a que clone el vault completo
7. Abrir **Obsidian** en Android → abrir vault desde esa carpeta
8. Instalar plugin **Obsidian Git** en Obsidian Android
9. Configurar Obsidian Git con el mismo intervalo de auto-sync que la PC (5 min)
10. Verificar que pull y push funcionan desde Obsidian Git en Android

> MGit se usa para el clone inicial y para pull/push manuales si Obsidian Git no los resuelve solo. Una vez clonado, Obsidian Git maneja el sync diario.

---
## Acceso de Claude al Vault de Obsidian

### Métodos de Acceso

Claude puede interactuar con tu vault de dos formas distintas, cada una con capacidades y limitaciones propias.

---

### 1. Conector de GitHub (Integración nativa de Claude.ai)

**Estado:** Disponible directamente en Claude.ai, sin configuración extra.

#### ¿Qué puede hacer?

|Capacidad|¿Disponible?|Detalle|
|---|:-:|---|
|Leer archivos sin copiarlos al chat|✅|Claude accede al contenido del repo directamente|
|Copiar/pegar archivos al chat|✅|Puedes adjuntar archivos desde el repo para trabajar con ellos|
|Editar archivos existentes|❌|Solo lectura — no puede modificar ni hacer commits|
|Crear archivos nuevos|❌|No tiene permisos de escritura|
|Navegar la estructura del repo|✅|Puede listar carpetas y archivos|
|Funciona sin PC encendida|✅|Opera directamente sobre el repo remoto en GitHub|

#### ¿Cómo actúa?

El conector de GitHub de Claude.ai es esencialmente una integración de **solo lectura**. Cuando lo usas, Claude puede explorar y leer el contenido de tu repositorio sin que tengas que copiar y pegar nada manualmente. Sin embargo, **no puede escribir ni modificar** nada en el repo — es una ventana de lectura, no de edición.

Útil para: buscar notas, leer contenido, responder preguntas sobre tus archivos, resumir documentos.

---

### 2. MCP — Filesystem (Conector local)

**Estado:** Requiere PC encendida y el servidor MCP corriendo localmente. **Ruta local:** `E:\University_vault_2026`

#### ¿Qué puede hacer?

|Capacidad|¿Disponible?|Detalle|
|---|:-:|---|
|Leer archivos sin copiarlos al chat|✅|Accede directamente al sistema de archivos|
|Editar archivos existentes|✅|Modifica el archivo en disco en tiempo real|
|Crear archivos nuevos|✅|Escribe nuevos `.md` u otros archivos|
|Mover / renombrar archivos|✅|Operaciones completas de sistema de archivos|
|Funciona sin PC encendida|❌|Requiere que la PC esté activa y el servidor MCP corriendo|
|Hacer git push/pull|❌|Solo opera sobre archivos — no ejecuta comandos de terminal|

#### ¿Cómo actúa?

El MCP de Filesystem le da a Claude acceso **completo de lectura y escritura** sobre los archivos locales de tu vault. Los cambios se aplican directamente en disco, sin intermediarios. El ciclo de sincronización con GitHub depende del **auto-commit de Obsidian Git** (configurado hasta cada 5 minutos).

```
Claude edita archivo → cambio en E:\University_vault_2026 → 
Obsidian Git detecta cambio → auto-commit + push → GitHub actualizado
```

---

### 3. MCP — GitHub (Conector remoto)

**Estado:** Activo — `https://api.githubcopilot.com/mcp` **No requiere PC encendida.**

#### ¿Qué puede hacer?

|Capacidad|¿Disponible?|Detalle|
|---|:-:|---|
|Leer archivos sin copiarlos al chat|✅|Lee directamente desde el repo remoto|
|Editar archivos existentes|✅|Crea commits directamente en GitHub|
|Crear archivos nuevos|✅|Sube nuevos archivos al repo|
|Mover / renombrar archivos|⚠️|Posible, pero requiere operaciones combinadas|
|Funciona sin PC encendida|✅|Opera 100% en la nube|
|Hacer git push/pull|❌|No ejecuta comandos git — opera via API de GitHub|

#### ¿Cómo actúa?

El MCP de GitHub opera directamente sobre la **API de GitHub**, permitiendo leer y escribir en el repositorio remoto sin tocar tu PC. Los cambios llegan al vault local en el próximo **auto-pull de Obsidian Git**.

```
Claude edita via API de GitHub → commit en repo remoto → 
Obsidian Git detecta cambio → auto-pull → vault local actualizado
```

---

### Comparativa General

||Conector GitHub (nativo)|MCP Filesystem|MCP GitHub|
|---|:-:|:-:|:-:|
|**Leer sin copiar al chat**|✅|✅|✅|
|**Editar archivos**|❌|✅|✅|
|**Crear archivos**|❌|✅|✅|
|**Requiere PC encendida**|❌|✅|❌|
|**Opera en tiempo real**|Solo lectura|✅ directo en disco|Via commit en GitHub|
|**Latencia hasta vault local**|N/A|Inmediata|Hasta próximo auto-pull|

---

### Notas Importantes

- Claude **no puede ejecutar comandos de terminal** (git push, git pull, etc.) por ninguno de los métodos.
- Con MCP Filesystem, si la PC se apaga a mitad de una edición, los cambios quedan en disco pero **no sincronizados** hasta que Obsidian Git corra de nuevo.
- El Conector nativo de GitHub es el más limitado pero el más sencillo de usar para consultas rápidas.

---

## Notas adicionales

- OneDrive descartado: la página de autorización fallaba al conectar con Remotely Save. Migrado a Dropbox definitivamente.
- Microsoft 365 descartado como conector de Claude: servicio de pago.
- Google Drive descartado como sistema de sync del vault: reemplazado por Mega (ver sección abajo). Drive se mantiene exclusivamente para TAB_nexus.
- Remotely Save descartado: la sincronización completa del vault con servicios externos generó más problemas que ventajas. Mega client + FolderSync es el sistema definitivo.

---

## Sincronización Mega — Sistema Principal (desde 2026-06-13)

> Mega reemplaza a Google Drive File Stream para la sincronización del vault completo entre PC, laptop, tablet y celular. La cuenta Mega usada es **exclusiva para el vault**. La migración se realizó subiendo el vault manualmente a Mega primero, luego configurando la sincronización — los archivos fueron reconocidos automáticamente sin resubirse.

### Carpetas sincronizadas en Mega

| Carpeta local PC | Carpeta Mega |
|---|---|
| `E:\University_vault_2026\MOC` | `/University_vault_2026/MOC` |
| `E:\University_vault_2026\Semesters` | `/University_vault_2026/Semesters` |
| `E:\University_vault_2026\Semestres` | `/University_vault_2026/Semestres` |
| `E:\University_vault_2026\_PDF` | `/University_vault_2026/_PDF` |

> Pendiente: cuando el sistema esté estable, eliminar copia de TAB_nexus de `_PDF` en Mega.

### .megaignore (PC)

Archivo en raíz del vault `E:\University_vault_2026\.megaignore` generado por el cliente Mega PC con los siguientes patrones:

```
-:Thumbs.db
-:desktop.ini
-:~*
-:.*
-:*~.*
-:*.crdownload
-:*.sb-????????-??????
-:*.tmp
-f:.cache
-f:.git

# Obsidian conflictivos
-:workspace.json
-:workspace-mobile.json
-:graph.json
-f:.trash
```

> Nota: `-:.*` ya cubre `.gitignore`, `.gitattributes` y `.DS_Store` por ser archivos que empiezan con punto.

### Rol de cada dispositivo

| Dispositivo | Rol | Puede editar |
|---|---|---|
| PC Escritorio | Principal | ✅ sí, sincroniza con Mega Y con Git |
| Laptop | Secundario | ✅ sí, sincroniza con Mega |
| Tablet Samsung S6 Lite | Edición móvil | ✅ sí, bidireccional vía FolderSync |
| Celular | Solo lectura | ❌ no, unidireccional Mega → Celular |

> **Regla de oro:** No editar el mismo archivo en dos dispositivos simultáneamente. Cerrar Obsidian en un dispositivo y esperar sincronización (icono verde en Mega) antes de abrir en otro.

---

## Configuración FolderSync — TABLET (bidireccional)

App: **FolderSync** | Cuenta: Mega exclusiva del vault

### Pares configurados

| Par | Izquierda (tablet) | Derecha (Mega) |
|---|---|---|
| MOC | `/storage/emulated/0/University_vault_2026/MOC` | `/University_vault_2026/MOC` |
| Semesters | `/storage/emulated/0/University_vault_2026/Semesters` | `/University_vault_2026/Semesters` |
| Semestres | `/storage/emulated/0/University_vault_2026/Semestres` | `/University_vault_2026/Semestres` |
| _PDF | `/storage/emulated/0/University_vault_2026/_PDF` | `/University_vault_2026/_PDF` |

### Opciones de sync (aplicar a todos los pares)

**Encendido ✅**
- sync eliminaciones
- realizar eliminaciones después de las transferencias de archivos

**Apagado ☐**
- excluir de la sync total
- no crear carpetas vacías
- desactivar el cálculo de la suma de comprobación
- desactivar la comprobación del espacio libre en disco
- usar esquemas de archivos temporales

- **Sobrescribir archivos antiguos:** siempre
- **Conflictos:** más reciente
- **Conexión:** solo WiFi

### Exclusiones (aplicar a todos los pares)

| Tipo | Condición | Valor |
|---|---|---|
| Archivo | iguales a | `workspace.json` |
| Archivo | iguales a | `workspace-mobile.json` |
| Archivo | iguales a | `graph.json` |
| Archivo | iguales a | `Thumbs.db` |
| Archivo | termina con | `.tmp` |
| Carpeta | iguales a | `.trash` |
| Carpeta | iguales a | `.obsidian` |
| Carpeta | iguales a | `cache` |

---

## Configuración FolderSync — CELULAR (solo lectura)

App: **FolderSync** | Cuenta: Mega exclusiva del vault | Obsidian instalado en el celular.

### Par configurado

| Par | Izquierda (celular) | Derecha (Mega) | Dirección |
|---|---|---|---|
| Vault | `/storage/emulated/0/University_vault_2026` | `/University_vault_2026` | Solo a la izquierda (Mega → Celular) |

### Opciones de sync

**Encendido ✅**
- sync eliminaciones
- no crear carpetas vacías

**Apagado ☐**
- excluir de la sync total
- desactivar el cálculo de la suma de comprobación
- desactivar la comprobación del espacio libre en disco
- realizar eliminaciones después de las transferencias de archivos
- usar esquemas de archivos temporales

- **Sobrescribir archivos antiguos:** siempre
- **Conflictos:** usar archivo de derecha
- **Conexión:** solo WiFi

### Exclusiones

Iguales a las de la tablet (misma tabla de arriba).

%%
galaxy-links
[[_galaxy-system]]
[[_ToDo-system]]
%%
