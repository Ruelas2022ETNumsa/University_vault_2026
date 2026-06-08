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
date_updated: 2026-05-30
status: activo
---

# Sistema Sync — Vault y Acceso Claude

> Sistema Galaxy: [[_galaxy-system]]
> Pendientes: [[_ToDo-system]]

## Objetivo

Que Claude pueda leer, crear y editar notas `.md` del vault de Obsidian directamente desde GitHub, sin depender de que la PC esté encendida. El vault local en PC se sincroniza automáticamente con GitHub mediante Obsidian Git. El móvil accede al vault mediante Remotely Save + Dropbox.

---

## Flujo actual

```
Claude (lee y edita archivos)
        ⇕
GitHub → https://github.com/Ruelas2022ETNumsa/University_vault_2026
        ⇕
Obsidian Git (auto-sync cada 5 min)
        ⇕
PC Local → E:\University_vault_2026
        ⇕
Remotely Save (sync con Dropbox) ← OFICIAL
        ⇕
Móvil Android (Obsidian + Remotely Save + Dropbox) ← pendiente configurar
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
- [x] Plugin **Remotely Save** instalado en PC y conectado a **Dropbox** ✅
- [x] Vault sincronizándose correctamente con Dropbox desde PC

> Tareas y pendientes: [[_ToDo-system]]

> **Nota:** OneDrive fue descartado — la página de autorización fallaba al intentar la integración con Remotely Save. Se migró a Dropbox sin problemas.

---

## Sincronización móvil oficial — Remotely Save + Dropbox

Pasos para completar la configuración en Android:

1. Instalar **Obsidian** en Android si no está instalado
2. Abrir el vault o crear uno con el mismo nombre (`University_vault_2026`)
3. Ir a **Settings → Community Plugins → Browse** → buscar **Remotely Save** → instalar y activar
4. En Remotely Save Settings → **Remote Service** → seleccionar **Dropbox**
5. Hacer click en **Auth** → autorizar la misma cuenta Dropbox que usa la PC
6. Verificar que la carpeta de destino coincide con la configuración de PC
7. Hacer **Run Once** para forzar el primer sync y verificar que los archivos llegan
8. Configurar sync automático según preferencia (al abrir, al cerrar, cada N minutos)

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

%%
galaxy-links
[[_galaxy-system]]
[[_ToDo-system]]
%%
