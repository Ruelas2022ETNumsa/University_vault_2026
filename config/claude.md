# Configuración: Acceso de Claude al Vault de Obsidian

## Objetivo
Que Claude (IA) pueda leer, crear y editar notas `.md` del vault de Obsidian
directamente desde GitHub, sin depender de que la PC esté encendida.
El vault local en PC se sincroniza automáticamente con GitHub mediante el plugin Obsidian Git.

---

## Flujo actual

```
Claude (edita/crea notas)
        ↕
GitHub → https://github.com/Ruelas2022ETNumsa/University_vault_2026
        ↕
Obsidian Git (auto-sync cada 5 min)
        ↕
PC Local → E:\University_vault_2026
        ↕
Remotely Save (sync con OneDrive)
        ↕
Móvil (Obsidian + Remotely Save)
```

---

## Lo que ya está hecho ✅

- [x] Vault de Obsidian renombrado a `University_vault_2026`
- [x] Repositorio GitHub creado: `University_vault_2026` (rama `main`)
- [x] Git instalado en la PC
- [x] Repositorio local vinculado a GitHub (`git remote` configurado)
- [x] Primer push realizado — archivos visibles en GitHub
- [x] Plugin **Obsidian Git** instalado y activado en Obsidian
- [x] **Obsidian Git configurado** (auto-commit, auto-push, auto-pull cada 5 min + pull al arrancar)
- [x] Conector Filesystem de Claude apuntando a `E:\University_vault_2026`
- [x] Plugin **Remotely Save** instalado en PC y conectado a **OneDrive**
- [x] Plugin **Remotely Save** instalado en **móvil** y conectado al mismo OneDrive
- [x] Vault sincronizado y accesible desde el móvil

---

## Lo que falta ⏳

- [ ] **Conectar GitHub a Claude** (conector GitHub en Claude.ai)
  - Permitirá a Claude editar archivos directamente en la nube
  - Sin depender de que la PC esté encendida
- [ ] **Conectar Microsoft 365 a Claude** (conector disponible en Claude.ai)
  - Permitirá a Claude leer/escribir notas directamente desde OneDrive
  - Complementa el acceso móvil

---

## Pendiente inmediato

1. Conectar conector **GitHub** en Claude.ai → Settings → Connectors
2. Opcionalmente conectar **Microsoft 365** para acceso vía OneDrive

---

## Notas
- El conector Filesystem de Claude solo funciona con la PC encendida
- Una vez conectado GitHub a Claude, la PC puede estar apagada y Claude seguirá teniendo acceso al vault
- Claude NO puede ejecutar comandos de terminal (git push/pull), solo leer y escribir archivos
