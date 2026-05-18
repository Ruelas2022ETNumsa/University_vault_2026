# Resolver Conflictos de Git en Obsidian

## ¿Qué es un conflicto de Git?

Ocurre cuando **dos máquinas modificaron el mismo archivo** y Git no sabe con cuál versión quedarse. Verás algo así en el archivo conflictivo:

```
<<<<<<< HEAD
    Contenido en tu máquina local
=======
    Contenido en GitHub (otra máquina)
>>>>>>> origin/main
```

---

## Pasos para resolver el conflicto

### 1. Activar Source Mode en Obsidian
Abre el archivo conflictivo y cambia a **Source mode** (ícono en la esquina superior derecha). Esto te permite ver los marcadores de conflicto en texto plano.

### 2. Ubicar los marcadores de conflicto
Busca los tres marcadores dentro del archivo:
- `<<<<<<< HEAD` → inicio del conflicto (versión local)
- `=======` → separador entre versiones
- `>>>>>>> origin/main` → fin del conflicto (versión remota)

### 3. Elegir qué conservar

**Opción A — Quedarte con la versión local:**
Borra desde `<<<<<<< HEAD` hasta `=======` (incluyendo esa línea), y también borra `>>>>>>> origin/main`.

**Opción B — Quedarte con la versión remota:**
Borra desde `<<<<<<< HEAD` hasta `=======` (incluyendo el contenido local y el separador), y también borra `>>>>>>> origin/main`.

**Opción C — Combinar ambas versiones:**
Edita el texto a tu gusto mezclando ambas partes, y borra los tres marcadores (`<<<<<<<`, `=======`, `>>>>>>>`).

> ⚠️ El archivo resuelto **no debe contener ningún marcador** `<<<<<<<`, `=======` ni `>>>>>>>`.

### 4. Guardar el archivo
Guarda con `Ctrl + S` después de resolver.

### 5. Confirmar y subir los cambios
Ejecuta en orden desde Obsidian:
1. `Git: Commit all changes`
2. `Git: Push`

---

## Prevenir conflictos en el futuro

En la configuración del plugin **Obsidian Git**, activa:

| Ajuste | Valor recomendado |
|---|---|
| Pull before push | ✅ Activado |
| Auto pull interval | Cada 5–10 minutos |
| Sync method | Rebase |

### Regla de oro
> Antes de empezar a editar en una segunda máquina, siempre ejecuta **`Git: Pull`** para traer los últimos cambios desde GitHub.

---

## Flujo de trabajo recomendado

```
Abrir Obsidian → Git: Pull → Editar notas → Git: Commit all changes → Git: Push
```

Siguiendo este orden en **ambas máquinas** se evitan la mayoría de los conflictos.
