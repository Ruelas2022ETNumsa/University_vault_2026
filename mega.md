# Contexto: Segundo Cerebro Obsidian — Sincronización Mega + FolderSync (continuación)

## Referencia al vault
- Vault PC: `E:\University_vault_2026\`
- Vault Tablet: `/storage/emulated/0/University_vault_2026/`

## Decisión de migración
Se migra de Google Drive File Stream a Mega para sincronización del vault.
Drive se mantiene ÚNICAMENTE para TAB_nexus (PDFs tablet ↔ PC) — intocable.
Mega reemplaza Drive para todas las carpetas de notas.

## Estado actual del sistema completo

### Google Drive (intocable)
| Componente | Función |
|---|---|
| Autosync (tablet) | `/Documentos/Pdf/` ↔ `Mi unidad/TAB_nexus` bidireccional |
| File Stream (PC) | Replica Mi unidad a `C:\Users\USUARIO\Mi unidad (kraaajooo123@gmail.com)\` |
| Symlink (PC) | `E:\University_vault_2026\_pdf\TAB_nexus` → `C:\Users\USUARIO\Mi unidad\TAB_nexus` |
| FolderSync (celular) | Drive/TAB_nexus → CELL_PDF solo lectura |

### Mega (nuevo sistema principal)
Carpetas sincronizadas entre PC y Mega:
- `MOC`
- `Semesters`
- `Semestres`
- `_PDF` (contiene copia física de PDFs — TAB_nexus será eliminado de aquí cuando todo esté estable)

## Configuración FolderSync — TABLET (bidireccional)
4 pares configurados con Mega como cuenta:

| Par | Izquierda (tablet) | Derecha (Mega) |
|---|---|---|
| MOC | `/storage/emulated/0/University_vault_2026/MOC` | `MOC` |
| Semesters | `/storage/emulated/0/University_vault_2026/Semesters` | `Semesters` |
| Semestres | `/storage/emulated/0/University_vault_2026/Semestres` | `Semestres` |
| _PDF | `/storage/emulated/0/University_vault_2026/_PDF` | `_PDF` |

### Opciones de sync (tablet — bidireccional):
- sync eliminaciones ✅
- excluir de la sync total ☐
- no crear carpetas vacías ☐
- desactivar el cálculo de la suma de comprobación ☐
- desactivar la comprobación del espacio libre en disco ☐
- realizar eliminaciones después de las transferencias de archivos ✅
- usar esquemas de archivos temporales ☐

Opciones unidireccionales: no aplica

- Sobrescribir archivos antiguos: **siempre**
- Conflictos: **sobrescribir el más reciente**
- Conexión: **solo WiFi**

## Configuración FolderSync — CELULAR (solo lectura)
| Par | Izquierda (celular) | Derecha | Tipo |
|---|---|---|---|
| TAB_nexus | `/storage/emulated/0/Documentos/CELL_PDF` | Drive/TAB_nexus | A la izquierda |

### Opciones de sync (celular — solo lectura):
- sync eliminaciones ✅
- excluir de la sync total ☐
- no crear carpetas vacías ✅
- desactivar el cálculo de la suma de comprobación ☐
- desactivar la comprobación del espacio libre en disco ☐
- realizar eliminaciones después de las transferencias de archivos ☐
- usar esquemas de archivos temporales ☐

- Sobrescribir archivos antiguos: **siempre**
- Conflictos: **usar archivo de derecha**
- Conexión: **solo WiFi**

## Pendiente en el nuevo chat
1. Configurar `.megaignore` en PC para excluir archivos innecesarios
   (`.obsidian/workspace.json`, cache, archivos temporales)
2. Configurar sincronización Mega en la laptop
3. Verificar bidireccional tablet ↔ Mega ↔ PC con archivo de prueba
4. Cuando todo estable: eliminar copia de TAB_nexus de `_PDF` en Mega
5. Migración progresiva completa a Mega — eliminar dependencia de Drive

## Nota .megaignore
Mega soporta archivo `.megaignore` en la raíz de la carpeta sincronizada
para excluir archivos/carpetas específicas de la sincronización.
Pendiente configurar en el nuevo chat.