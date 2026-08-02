---
title: "Anki — Opcion C: Obsidian_to_Anki (Pseudonium / ObsidianToAnki)"
scope: vault
status: activo
date: 2026-08-02
tags: [anki, obsidian-to-anki, pseudonium, image-occlusion, excalidraw, setup, galaxy]
---

# Anki — Opción C: Obsidian_to_Anki (Pseudonium)

> Plugin: **Obsidian_to_Anki**
> Repo original: https://github.com/Pseudonium/Obsidian_to_Anki
> Repo activo (transferido): https://github.com/ObsidianToAnki/Obsidian_to_Anki
> Instalación: manual desde releases (no está en Community Plugins)
> Carpeta: `.obsidian/plugins/obsidian-to-anki-plugin/`

---

## 1. Instalación

1. Ir a https://github.com/ObsidianToAnki/Obsidian_to_Anki/releases
2. Descargar el `.zip` del último release
3. Extraer en `.obsidian/plugins/obsidian-to-anki-plugin/` — deben quedar `main.js`, `manifest.json`, `styles.css`
4. Obsidian → Configuración → Plugins de la comunidad → activar **Obsidian_to_Anki**
5. Con Anki Desktop abierto, hacer scan inicial: ribbon → botón Anki (o `Ctrl+P` → "Obsidian_to_Anki: Scan Vault")
6. En Settings del plugin → **Regenerate Note Type Table** → carga todos los tipos de nota desde Anki

> ⚠️ AnkiConnect debe estar instalado y configurado previamente (código `2055492159`).
> ⚠️ No está en Community Plugins — instalación siempre manual desde GitHub releases.

---

## 2. Configuración aplicada para Galaxy

### Defaults

| Setting | Valor | Razón |
|---|---|---|
| Scan Directory | *(vacío)* | Escanea todo el vault — controlado por globs |
| Tag | `Galaxy` | Todas las cartas llevan el tag Galaxy en Anki automáticamente |
| Deck | `Galaxy::General` | Deck por defecto si no se especifica TARGET DECK |
| Scheduling Interval | `0` | Sin scan automático — manual siempre |
| Add File Link | `true` | Cada carta tiene link de vuelta al archivo Obsidian |
| Add Context | `false` | No arrastra headers al contexto |
| CurlyCloze | `false` | No usar `{cloze}` — usar sintaxis estándar |
| ID Comments | `true` | El plugin escribe `<!--ID: ...-->` en el archivo para tracking |
| Add Obsidian Tags | `false` | No importar tags de Obsidian a Anki |

### Ignored File Globs

```
**/*.excalidraw.md
Excalidraw/template/**
_app/**
_assets/**
_PDF/**
_projects/**
_skills/**
_templates/**
_inbox/**
_blueprint/**
borrar/**
Borrar/**
Zettelkasten/**
MOC/**
Rubbish/**
Semestres/**
```

> `Semestres/**` excluye el vault legacy ETN302/ETN806.
> `Semesters/**` se escanea — es el vault Galaxy activo.

---

## 3. Sintaxis soportada

### Básica (Básico en español)
```markdown
TARGET DECK: Galaxy::General

START
Básico
¿Cuál es la Transformada de Laplace de $e^{at}$?
Reverso: $\mathcal{L}\{e^{at}\} = \dfrac{1}{s-a}$
END
```

> ⚠️ Anki en español → el tipo se llama `Básico` y el campo `Reverso:`, no `Basic`/`Back:`.
> ⚠️ `TARGET DECK` va en el cuerpo del archivo, no en el frontmatter YAML.

### Cloze
```markdown
START
Básico
La ROC de $e^{at}u(t)$ es {{c1::$\text{Re}(s) > a$}}.
END
```

### Inline (STARTI/ENDI)
```markdown
¿Qué es BIBO? STARTI[Básico] Bounded Input Bounded Output. ENDI
```

### Con FILE TAGS
```markdown
FILE TAGS: ETN901 parcial1

START
Básico
¿Qué es la densidad conjunta?
Reverso: Función $f_{XY}(x,y)$ tal que $P(A) = \iint_A f_{XY}\,dx\,dy$
END
```

---

## 4. Flujo Image Occlusion — Excalidraw → Anki

Este es el caso de uso principal y diferenciador de Opción C.

### Dependencias

| Componente | Descripción |
|---|---|
| Plugin Excalidraw (zsviczian) | Plugin base de dibujo |
| Script "Image Occlusion" (zsviczian) | Script dentro de Excalidraw que genera los archivos de oclusión |
| Obsidian_to_Anki (Opción C) | Exporta los `.card.md` generados a Anki |
| Template `proex.md` | Define el formato de las cartas generadas |
| AnkiConnect | Puente entre Obsidian y Anki Desktop |

### Template — `_templates/proex.md`

```markdown
TARGET DECK: Galaxy::General
START
Image Occlusion Enhanced
ID (hidden): {{card_number}}
Header: 
Image: ![[{{answer}}]]
Question Mask: ![[{{question}}]]
Footer: 
Remarks: [[{{editSource}}|✏️ Editar fuente]]
Sources: [[{{batchMarker}}|📋 Batch]]
Extra 1: 
Extra 2: 
Answer Mask: 
Original Mask: 
END
```

> Los placeholders `{{card_number}}`, `{{question}}`, `{{answer}}`, `{{editSource}}`, `{{batchMarker}}` son reemplazados automáticamente por el script de zsviczian.

### Flujo paso a paso

1. Abrir o crear un dibujo en `Excalidraw/Observatory/` o `Constellations/`
2. En Excalidraw → `Ctrl+P` → buscar **"Image Occlusion"** → ejecutar script
3. El script pregunta el template → seleccionar `_templates/proex.md`
4. El script genera una subcarpeta en `Excalidraw-Image-Occlusions/` con:
   - `q-TIMESTAMP.png` — imagen con área tapada (pregunta)
   - `a-TIMESTAMP.png` — imagen completa (respuesta)
   - `TIMESTAMP.md` — archivo con la carta en formato START/END
   - `batch-marker.md` — índice de las cartas generadas
5. Con Anki abierto → Obsidian ribbon → **Scan Vault**
6. Las cartas aparecen en Anki con tipo `Image Occlusion Enhanced`

### Estructura de archivos generados

```
Excalidraw-Image-Occlusions/
  nombre.excalidraw__FECHA/
    q-20260728200757904.png     ← imagen pregunta (con tapado)
    a-20260728200757904.png     ← imagen respuesta (revelada)
    20260728200757904.md        ← carta — escaneada por Opción C
    batch-marker.md             ← índice — no contiene flashcards
```

---

## 5. Comportamiento del plugin — botones de Settings

| Botón | Qué hace | Cuándo usarlo |
|---|---|---|
| **Regenerate Note Type Table** | Reconecta con Anki y actualiza los tipos de nota y sus campos en `data.json` | Al instalar un tipo de nota nuevo en Anki, o si los campos no aparecen |
| **Clear Media Cache** | Borra `Added Media` en `data.json` — fuerza re-subida de imágenes PNG | Si actualizaste una imagen con el mismo nombre y no se refleja en Anki |
| **Clear File Hash Cache** | Borra `File Hashes` en `data.json` — fuerza re-escaneo de todos los archivos | Si el plugin saltea archivos que no cambiaron pero necesitás re-exportar |

---

## 6. Problemas conocidos y soluciones

### ❌ No crea cartas — solo crea el mazo
**Causa:** el tipo de nota en el `START` no coincide con el nombre en Anki. Anki en español usa `Básico`, no `Basic`.
**Solución:** usar el nombre exacto en español. Ver sección 3.

### ❌ El plugin saltea archivos ya escaneados
**Causa:** `File Hashes` en `data.json` — si el archivo no cambió, el plugin lo ignora.
**Solución:** Settings → **Clear File Hash Cache** → scan de nuevo.

### ❌ Borraste el mazo en Anki pero el plugin no re-exporta las cartas
**Causa:** el plugin escribió `<!--ID: 1785283725903-->` en el `.md` al sincronizar. Ese ID apunta a una nota que ya no existe en Anki. El plugin intenta actualizar en vez de crear.
**Solución:** borrar manualmente la línea `<!--ID: ...-->` de los archivos afectados y hacer scan.
**Mejora pendiente:** script Shell Commands que borre todos los `<!--ID-->` de `Excalidraw-Image-Occlusions/` con un click.

### ❌ Las imágenes de Image Occlusion no llegan a Anki
**Causa:** `Added Media` en caché — el plugin ya registró esas imágenes y las saltea.
**Solución:** Settings → **Clear Media Cache** → scan.

---

## 7. Resultados de prueba

| Aspecto | Estado | Nota |
|---|---|---|
| Tarjeta `Básico` | ✅ funciona | Usar `Básico`/`Reverso:` en español |
| LaTeX `$...$` | ✅ renderiza directo | Sin conversión manual |
| TARGET DECK en cuerpo | ✅ funciona | No en frontmatter YAML |
| Image Occlusion Enhanced | ✅ funciona | Con template `proex.md` y script zsviczian |
| Imágenes q-/a- en Anki | ✅ funciona | Se ven correctamente en Desktop y AnkiDroid |
| Link de vuelta a Obsidian | ✅ funciona | `Add File Link: true` |
| Tag automático `Galaxy` | ✅ funciona | `Tag: "Galaxy"` en Defaults |
| Sync → AnkiDroid | ✅ funciona | Flujo normal Desktop → AnkiWeb → Android |
| Excalidraw → Anki (full flow) | ✅ funciona | Script zsviczian + template proex.md + Opción C |

---

## 8. Veredicto Opción C

**Pros:**
- Único flujo funcional para Image Occlusion desde Excalidraw ✅
- Soporte para `Image Occlusion Enhanced` (tipo de nota con q-/a- PNG)
- Sintaxis START/END clara y explícita
- LaTeX renderiza directo
- Add File Link — trazabilidad hacia Obsidian
- Tag automático configurable

**Contras:**
- No está en Community Plugins — instalación y actualizaciones manuales
- Tipo de nota y campos deben coincidir exactamente con el idioma de Anki
- `<!--ID-->` problemático si se borran cartas en Anki manualmente
- Sync inconsistente si no se hace Clear Hash Cache tras ciertos cambios
- Sin mantenimiento activo (repo transferido, desarrollo pausado)

**Candidato para:** Image Occlusion desde Excalidraw. Complemento de Opción B para el flujo visual.

---

%%
# galaxy-links
[[anki_galaxy_guide]]
[[anki-opcionB-flashcards]]
[[Obsidian_to_anki]]
[[shellcmd_occlusion_actions]]
[[tsk_obsidian_to_anki]]
%%
