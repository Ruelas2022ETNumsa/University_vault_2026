# Excluir `appearance.json` de la sincronización Mega

## Por qué excluirlo

`appearance.json` controla qué CSS snippets están **encendidos o apagados** en Obsidian. Cada dispositivo tiene sus propios snippets activos:

- **PC** tiene encendidos: `supercharged-links-gen`, `supercharged-links`
- **Tablet / Celular** tienen sus propios snippets (ej: `mobile-line-width`)

Si `appearance.json` se sincroniza, la configuración de snippets de la PC **pisa** la de los móviles o viceversa, rompiendo la apariencia en alguno de los dispositivos.

---

## Paso 1 — Agregar exclusión en `.megaignore` (PC)

Abrí el archivo `E:\University_vault_2026\.megaignore` y agregá esta línea dentro del bloque de Obsidian:

```
-:appearance.json
```

El bloque debería quedar así:

```
# Obsidian — solo estos generan conflicto entre dispositivos
-:workspace.json
-:workspace-mobile.json
-:graph.json
-:community-plugins.json
-:core-plugins.json
-:appearance.json
```

---

## Paso 2 — Agregar exclusión en FolderSync (Tablet)

En la app **FolderSync** de la tablet, entrá a cada par configurado (MOC, Semesters, Semestres, _PDF) y agregá esta exclusión:

> Como los pares de la tablet excluyen la carpeta `.obsidian` completa (`Carpeta | iguales a | .obsidian`), `appearance.json` ya queda excluido automáticamente en la tablet.

**No se necesita acción adicional en la tablet.**

---

## Paso 3 — Agregar exclusión en FolderSync (Celular)

El celular sincroniza el vault completo desde Mega (dirección: solo lectura). La carpeta `.obsidian` **no está excluida** en el par del celular, por lo que `appearance.json` sí llegaría.

Entrá al par del celular en FolderSync y agregá:

| Tipo | Condición | Valor |
|---|---|---|
| Archivo | iguales a | `appearance.json` |

---

## Paso 4 — Verificar que cada dispositivo mantiene su propio `appearance.json`

Después de aplicar las exclusiones, cada dispositivo conserva su propio archivo sin que Mega lo sobreescriba. Podés verificarlo encendiendo/apagando un snippet en la PC y confirmando que en el celular o tablet no cambia nada.

---

## Resumen de cambios

| Dispositivo | Acción necesaria |
|---|---|
| PC | Agregar `-:appearance.json` en `.megaignore` |
| Laptop | Misma línea en su `.megaignore` local (si tiene uno) |
| Tablet | Sin acción — `.obsidian` ya está excluida en FolderSync |
| Celular | Agregar exclusión de archivo `appearance.json` en FolderSync |

---

> **Nota:** Este cambio no afecta el tema visual general (modo claro/oscuro, fuente base) si esos ajustes los manejás igual en todos los dispositivos. Solo aísla la lista de snippets activos.
