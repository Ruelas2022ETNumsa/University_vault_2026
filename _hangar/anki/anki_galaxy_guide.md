---
title: "Anki — Guía de instalación e integración Galaxy"
scope: vault
status: activo
date_created: 2026-07-26
date_updated: 2026-08-02
tags: [anki, obsidian, galaxy, spaced-repetition]
---

# Anki — Guía de instalación e integración Galaxy

> Documento maestro del sistema Anki Galaxy. Las opciones A, B y C están probadas y documentadas en sus respectivos archivos.

---

## Índice

- [[#1. Instalación base]]
- [[#2. Configuración inicial]]
- [[#3. Addons de Anki]]
- [[#4. AnkiWeb y AnkiDroid]]
- [[#5. Opciones de integración con Obsidian]]
- [[#6. Flujo Galaxy definitivo]]
- [[#7. Scripts pendientes]]

---

## 1. Instalación base

### Anki Desktop (Windows)
✅ Instalado en `E:\Programas\anki\` — versión 26.05

### AnkiConnect — addon obligatorio
✅ Código: `2055492159` — instalado y configurado con CORS para Obsidian.

```json
{
  "apiKey": null,
  "apiLogPath": null,
  "webBindAddress": "127.0.0.1",
  "webBindPort": 8765,
  "webCorsOrigin": "http://localhost",
  "webCorsOriginList": [
    "http://localhost",
    "app://obsidian.md"
  ]
}
```

> ⚠️ Anki Desktop debe estar abierto para que cualquier plugin de Obsidian sincronice.

---

## 2. Configuración inicial

### Modo oscuro
✅ Preferencias → Apariencia → Night Mode (Desktop) | Configuración → Apariencia → Oscuro (AnkiDroid)

### FSRS
✅ Activado. Engranaje del deck → Options → Advanced → FSRS → Save.
Hacer "Optimize" después de ~30 días de revisiones — no tocar parámetros hasta entonces.

### Estructura de decks Galaxy

```
Galaxy
├── General          ← deck por defecto para notas sin deck específico
├── ETN901
├── ETN806
└── ImageOcclusion  ← cartas de Excalidraw (Image Occlusion Enhanced)
```

---

## 3. Addons de Anki

| Addon | Código | Estado | Uso |
|---|---|---|---|
| AnkiConnect | `2055492159` | ✅ activo | Obligatorio — puente con Obsidian |
| Image Occlusion Enhanced | `1374772155` | ✅ activo | Tipo de nota para flujo Excalidraw → Opción C |
| Review Heatmap | `1771074083` | ✅ activo | Visualización de racha de estudio |
| True Retention | `613684242` | ✅ activo | Estadísticas de retención real |
| Math Delimiters Replacer | `401047458` | ✅ activo | Solo relevante para Opción A |
| Hierarchical Tags | `1089921461` | ❌ descartado | Incompatible con Anki moderno — jerarquía nativa con `::` |

---

## 4. AnkiWeb y AnkiDroid

✅ Cuenta creada y vinculada. Flujo establecido:

```
Obsidian → Anki Desktop → AnkiWeb → AnkiDroid
```

- Primera sync Desktop: "Upload to AnkiWeb"
- Primera sync AnkiDroid: "AnkiWeb" (descargar lo que subió el desktop)
- AnkiDroid: solo para repasar — creación siempre desde Obsidian o Desktop

---

## 5. Opciones de integración con Obsidian

### Opción A — Anki Advanced Sync (addon Marginalia) ✅ PROBADA

> Documentación completa: [[anki-opcionA-marginalia]]

**Sintaxis:**
```
RESPUESTA %%> PREGUNTA ;; %%
```

**Resultado:** sync funciona, tag mapping funciona. LaTeX `$...$` no renderiza sin conversión manual — requiere Script 2 (pendiente).

| | |
|---|---|
| **Mejor para** | Notas con marginalia existentes — reutiliza el flujo de estudio activo |
| **Limitación clave** | LaTeX requiere conversión `$` → `\(...\)` antes del sync |
| **Mantenimiento** | Activo (parte de Cornell Marginalia) |

---

### Opción B — Flashcards (reuseman) ✅ PROBADA

> Documentación completa: [[anki-opcionB-flashcards]]

**Sintaxis:**
```markdown
¿Pregunta? #card
Respuesta con $LaTeX$ directo.

¿Inline? :: Respuesta inline

La fórmula es ==$E=mc^2$== en contexto. (cloze)
```

**Resultado:** todas las pruebas pasaron. LaTeX `$...$` renderiza directo sin conversión. Deck automático por carpeta.

| | |
|---|---|
| **Mejor para** | Notas dedicadas a flashcards, fórmulas LaTeX, diagramas Excalidraw simples (SVG) |
| **Limitación clave** | Sin mantenimiento desde Oct 2022. No soporta Image Occlusion Enhanced |
| **Mantenimiento** | Inactivo desde Oct 2022 — funcional pero sin updates |

---

### Opcion C — Obsidian_to_Anki (Pseudonium) ✅ PROBADA

> Documentacion completa: [[anki-opcionC-obsidian-to-anki]]
> Scripts y gestion de carpetas: [[shellcmd_occlusion_actions]]

**Instalacion:** manual desde https://github.com/ObsidianToAnki/Obsidian_to_Anki/releases
(no esta en Community Plugins)

**Sintaxis:**
```markdown
TARGET DECK: Galaxy::General

START
Basico
¿Pregunta?
Reverso: Respuesta con $LaTeX$ directo.
END
```

**Resultado:** funciona. Es el unico plugin que soporta el flujo completo Image Occlusion Enhanced desde Excalidraw.

| | |
|---|---|
| **Mejor para** | Image Occlusion desde Excalidraw — flujo visual de diagramas |
| **Limitacion clave** | `<!--ID-->` problematico si se borran cartas en Anki manualmente. Instalacion manual |
| **Mantenimiento** | Inactivo — repo transferido, desarrollo pausado |

**Script de gestion — `occlusion_actions/main.py` ✅ COMPLETO:**
Gestiona las carpetas `nombre__timestamp` generadas por el script Image Occlusion. Tres acciones:
- **B** — Borra carpetas, notas Anki, decks vacios y tags huerfanos (requiere Anki abierto)
- **S** — Archiva carpetas exportadas a `_legacy/nombre/` junto al archivo fuente
- **Z** — Restaura desde legacy a `Image-Occlusions/`

Configurado en Shell Commands con prompt `Occlusion Actions` y boton ribbon via Commander.

**Flujo Image Occlusion (exclusivo de Opcion C):**
```
Excalidraw → script "Image Occlusion" (zsviczian) → genera q-/a-.png + .md
     ↓
Opcion C (Scan Vault) → Anki Desktop (Image Occlusion Enhanced)
     ↓
AnkiWeb → AnkiDroid
```

Template activo: `_templates/tpl-excalidraw_occlusion.md`
Template de creacion: `_templates/tpl-Anki_excalidraw.md`

> [!warning] Excalidraws de occlusion se crean como `.md`
> El template `tpl-Anki_excalidraw.md` crea archivos `.md` (no `.excalidraw`) para que `{{title}}` devuelva el nombre limpio sin extension. Son completamente funcionales como excalidraw.

---

### ❌ Descartadas

| Plugin | Razón |
|---|---|
| AnkiSync+ (RochaG07) | Creaba decks pero no tarjetas — sin fix, sin mantenimiento |
| Opción D — Obsidian-Anki-Sync (debanjandhar12) | No probada — descartada por complejidad. Opción B resuelve LaTeX |

---

## 6. Flujo Galaxy definitivo

### Decisión

| Caso de uso | Plugin | Razón |
|---|---|---|
| Flashcards de texto, fórmulas, teoría | **Opción B** (Flashcards reuseman) | LaTeX directo, sintaxis limpia, deck por carpeta |
| Image Occlusion — diagramas Excalidraw | **Opción C** (Obsidian_to_Anki) | Único flujo funcional para Image Occlusion Enhanced |
| Marginalia existentes | **Opción A** (Marginalia) | Reutiliza el flujo Marginalia sin duplicar trabajo — con Script 2 pendiente |

> Las 3 opciones coexisten. No son excluyentes.

### Flujo B — texto y fórmulas (principal)

```
Nota galaxy (planet, moon, comet)
  └── ¿Pregunta? #card
      Respuesta con $LaTeX$
           ↓
  Flashcards (reuseman) → ribbon → sync
           ↓
  Anki Desktop → AnkiWeb → AnkiDroid
```

### Flujo C — Image Occlusion (visual)

```
Observatory / Constellation (.excalidraw.md)
           ↓
  Excalidraw → Ctrl+P → "Image Occlusion" (script zsviczian)
  → seleccionar _templates/proex.md
  → genera Excalidraw-Image-Occlusions/nombre__FECHA/
           ↓
  Obsidian_to_Anki → ribbon → Scan Vault
           ↓
  Anki Desktop (Image Occlusion Enhanced) → AnkiWeb → AnkiDroid
```

### Flujo A — marginalia (complementario)

```
Nota con marginalia activa
  └── RESPUESTA %%> PREGUNTA ;; #tag %%
           ↓
  Marginalia → Ctrl+P → "Sync ALL Vault Flashcards (Tag-Mapped)"
           ↓
  Anki Desktop → AnkiWeb → AnkiDroid
```

> ⚠️ LaTeX en Opción A requiere Script 2 (pendiente) para renderizar en AnkiDroid.

---

## 7. Scripts — estado actual

### Script 1 — Conversor Marginalia -> Flashcards
Convierte `RESPUESTA %%> PREGUNTA ;; %%` a formato `PREGUNTA #card \n RESPUESTA` para usar Opcion B con notas que ya tienen marginalia.
**Estado:** pendiente — idea valida, no implementada.

### Script 2 — Conversor `$` -> MathJax (Opcion A)
Convierte `$...$` -> `\(...\)` y `$$...$$` -> `\[...\]` antes del sync con Marginalia. Revierte despues.
**Estado:** implementado y documentado en `shellcmd_latex_mathjax.md` ✅

### Script 3 — `occlusion_actions/main.py` (Opcion C)
Gestiona carpetas Image Occlusion: borrar, archivar en legacy, restaurar desde legacy.
**Estado:** completo y probado (B/S/Z) ✅ | Documentado en `shellcmd_occlusion_actions.md`

### Script 4 — Limpiar `<!--ID-->` de Image-Occlusions (pendiente)
Borra todas las lineas `<!--ID: ...-->` de los `.md` en `Image-Occlusions/`. Necesario si se borran mazos en Anki manualmente y se quiere re-exportar.
**Estado:** pendiente — cubierto parcialmente por accion B del Script 3.

---

%%
# galaxy-links
[[_app/_config/_marginalia_system.md]]
[[_app/_appnotes/Marginalia_guide.md]]
[[anki-opcionA-marginalia]]
[[anki-opcionB-flashcards]]
[[anki-opcionC-obsidian-to-anki]]
%%
