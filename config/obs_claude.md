# Configuración: Acceso de Claude al Vault de Obsidian

## Objetivo
Que Claude (IA) pueda leer, crear y editar notas `.md` del vault de Obsidian
directamente desde GitHub, sin depender de que la PC esté encendida.
El vault local en PC se sincroniza automáticamente con GitHub mediante el plugin Obsidian Git.

---

## Flujo deseado

```
Claude (edita/crea notas)
        ↕
GitHub → https://github.com/Ruelas2022ETNumsa/University_vault_2026
        ↕
Obsidian Git (sincroniza automáticamente)
        ↕
PC Local → E:\University_vault_2026
```

---

## Lo que ya está hecho ✅

- [x] Vault de Obsidian renombrado a `University_vault_2026`
- [x] Repositorio GitHub creado: `University_vault_2026` (rama `main`)
- [x] Git instalado en la PC
- [x] Repositorio local vinculado a GitHub (`git remote` configurado)
- [x] Primer push realizado — archivos visibles en GitHub
- [x] Plugin **Obsidian Git** instalado en Obsidian
- [x] Conector Filesystem de Claude apuntando a `E:\University_vault_2026`

---

## Lo que falta ⏳

- [ ] **Activar Obsidian Git** en Obsidian
  - Ir a `Settings → Community Plugins → Obsidian Git → activar toggle`
  - Esto genera el archivo `data.json` con la configuración del plugin
- [ ] **Configurar Obsidian Git** (Claude lo hará editando `data.json`)
  - Auto-pull cada 5 minutos
  - Auto-push cada 5 minutos
  - Mensaje de commit automático
- [ ] **Conectar GitHub a Claude** (conector GitHub en Claude.ai)
  - Esto permitirá a Claude editar archivos directamente en la nube
  - Sin depender de que la PC esté encendida

---

## Pendiente inmediato

1. Abrir Obsidian con el vault `University_vault_2026`
2. Ir a `Settings → Community Plugins` y activar **Obsidian Git**
3. Cerrar Obsidian
4. Avisar a Claude para que configure el `data.json` automáticamente

---

## Notas
- El conector Filesystem de Claude solo funciona con la PC encendida
- Una vez conectado GitHub a Claude, la PC puede estar apagada y Claude seguirá teniendo acceso al vault
- Claude NO puede ejecutar comandos de terminal (git push/pull), solo leer y escribir archivos
