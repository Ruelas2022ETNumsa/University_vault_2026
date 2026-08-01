---
galaxy_body: ship
project: "Color Folders and Files — instalación y configuración"
date: 2026-07-31
status: delivered
fleet:
blocked_by:
---

## Handoff

**Última sesión:** 2026-07-31
**Retomar desde:** —
**Completado esta sesión:** instalación del plugin, generación de paleta Galaxy, exportación de presets JSON, documentación del flujo de aplicación.
**Próximo paso:** —
**Preguntas de cierre:** —

---

## Resumen y objetivo

Instalar y configurar el plugin **Color Folders and Files** (Mithadon) para colorear las carpetas del vault Galaxy. Objetivo: distinguir visualmente las carpetas raíz del File Explorer de Obsidian usando la paleta Galaxy con fondo sólido y texto en tono claro del mismo color.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-07-31 | Plugin elegido: Color Folders and Files (Mithadon) | 33k descargas, paleta completamente customizable, compatible con Windows |
| 2026-07-31 | Estilo opción B — fondo sólido + texto claro | Texto coloreado (opción A) no era suficientemente visible en el Explorer |
| 2026-07-31 | BG = color sólido Galaxy, Text = relleno claro del mismo color | Coherencia visual: misma familia cromática en BG y texto |
| 2026-07-31 | Presets creados via Import JSON, aplicación carpeta por carpeta | El JSON importado crea los presets en Settings — no los aplica automáticamente a las carpetas |
| 2026-07-31 | JSON guardado en `.obsidian/plugins/color-folders-files/` | Copia de respaldo de la configuración de presets |

> [!note]- Descartadas
> Opción A (solo text color, fondo transparente) — descartada porque el nombre de la carpeta no se distinguía bien con el Explorer de Obsidian en tema oscuro.
> Explorer Colors (VaguelyElectric) — descartado, 13 estrellas, mantenimiento pasivo, bug de layout switch.
> File Color (ecustic) — descartado, abandonado desde dic 2023, cascada rota.

---

## Paleta aplicada

| Carpeta | BG (sólido) | Text (claro) |
| ------- | ----------- | ------------ |
| `_app` | `#005F73` azul petróleo | `#BFD7DC` |
| `_hangar` | `#0A9396` verde azulado | `#C2E4E5` |
| `_inbox` | `#EE9B00` ámbar | `#FBE6BF` |
| `_PDF` | `#BB3E03` naranja quemado | `#EECFC0` |
| `_skills` | `#474448` gris antracita | `#D1D0D1` |
| `_templates` | `#474448` gris antracita | `#D1D0D1` |
| `_void` | `#629900` verde oliva | `#D8E6BF` |
| `Semesters` | `#5A189A` morado | `#D6C5E6` |
| `Semestres` | `#5A189A` morado | `#D6C5E6` |
| `MOC` | `#DA627D` rosa | `#F6D8DF` |
| `Canvas` | `#C1121F` rojo | `#F0C4C7` |
| `Excalidraw` | `#BB3E03` naranja quemado | `#EECFC0` |
| `Marginalia` | `#629900` verde oliva | `#D8E6BF` |
| `Rubbish` | `#474448` gris antracita | `#D1D0D1` |

---

## Flujo de aplicación

### Importar presets (hecho)
1. Settings → Color Folders and Files → **Import**
2. Seleccionar `Color folders files settings v1 4 1.json`
3. Los presets quedan disponibles en "Existing presets" — **no se aplican solos**

### Aplicar preset a cada carpeta
1. Clic derecho sobre la carpeta en el File Explorer
2. Seleccionar **Customize appearance**
3. En el dropdown "Apply preset" → elegir el preset del nombre correspondiente
4. Click **Apply changes**
5. Repetir para cada carpeta raíz

### Alternativa via data.json (no probada)
El plugin guarda los estilos aplicados en su `data.json` interno (`.obsidian/plugins/color-folders-files/data.json`). Teóricamente se podría editar ese archivo directamente para asignar colores a carpetas por ruta, evitando el clic derecho uno por uno. **No probado — requiere sesión dedicada si se quiere explorar.**

---

## Recursos

- Plugin: [Color Folders and Files — Mithadon](https://github.com/mithadon/obsidian-color-folders-files)
- JSON de presets: `E:\University_vault_2026\.obsidian\plugins\color-folders-files\Color folders files settings v1 4 1.json`
- Paleta Galaxy completa: `E:\University_vault_2026\_app\_config\_galaxy-system.md`
