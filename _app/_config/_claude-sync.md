---
title: "Configuración Claude — Sync y Acceso al Vault"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[_galaxy-system]]"
tags: [beacon, sync, github, infraestructura]
date_created: 2026-05-28
date_updated: 2026-05-29
status: activo
---

# Configuración Claude — Sync y Acceso al Vault

> Sistema Galaxy: [[_galaxy-system]]

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
- [x] Plugin **Obsidian Git** instalado, activado y configurado en PC (auto-commit, auto-push, auto-pull cada 5 min + pull al arrancar)
- [x] Conector **Filesystem** de Claude apuntando a `E:\University_vault_2026`
- [x] Conector **GitHub** conectado en Claude.ai — `https://api.githubcopilot.com/mcp`
- [x] Plugin **Remotely Save** instalado en PC y conectado a **Dropbox** ✅
- [x] Vault sincronizándose correctamente con Dropbox desde PC

> **Nota:** OneDrive fue descartado — la página de autorización fallaba al intentar la integración con Remotely Save. Se migró a Dropbox sin problemas.

---

## Lo que falta ⏳

- [ ] **Remotely Save en móvil Android** — instalar el plugin y conectar al mismo Dropbox (sincronización oficial)
- [ ] **Git en Android** — sincronización alterna (ver sección abajo)
- [ ] ~~**Microsoft 365**~~ — descartado, servicio de pago

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

## Acceso de Claude al vault

| Conector | Estado | Función | Requiere PC encendida |
|----------|--------|---------|----------------------|
| Filesystem | ✅ Activo | Lee y escribe archivos en `E:\University_vault_2026` | Sí |
| GitHub | ✅ Activo — `https://api.githubcopilot.com/mcp` | Lee y escribe en el repositorio remoto | No |

- Con **Filesystem**: Claude edita en tiempo real; los cambios llegan al repo en el próximo auto-commit de Obsidian Git (hasta 5 min)
- Con **GitHub**: Claude edita directo en la nube; los cambios llegan al vault local en el próximo auto-pull de Obsidian Git
- Claude **no puede** ejecutar comandos de terminal (git push/pull) — solo leer y escribir archivos

---

## Notas adicionales

- OneDrive descartado: la página de autorización fallaba al conectar con Remotely Save. Migrado a Dropbox definitivamente.
- Microsoft 365 descartado como conector de Claude: servicio de pago.

%%
galaxy-links
[[_galaxy-system]]
%%
