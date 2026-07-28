---
title: "Anki — Prueba Opción B: Flashcards (reuseman)"
scope: vault
status: probado
date: 2026-07-27
tags: [anki, flashcards, reuseman, setup, galaxy]
---

# Anki — Opción B: Flashcards (reuseman)

> Plugin: **Flashcards** por reuseman
> Repo: https://github.com/reuseman/flashcards-obsidian
> Stars: 1.1k | Última release: Oct 2022 (mantenimiento mínimo pero funcional)

---

## 1. Instalación

1. Obsidian → Configuración → Plugins de la comunidad → Explorar
2. Buscar **"Flashcards"** (autor: reuseman) → Instalar → Activar
3. Con Anki Desktop abierto, ir a Settings del plugin → presionar **"Grant Permission"**
4. Presionar **"Test"** — ambos botones deben pasar ✅

> ⚠️ AnkiConnect debe estar instalado y configurado previamente (código `2055492159`).

---

## 2. Configuración recomendada para Galaxy

| Setting | Valor recomendado | Razón |
|---|---|---|
| Context-aware mode | `0` | Los headers `##` se arrastran al frente — evitar |
| Source support | `1` | Agrega link de vuelta a la nota original en Obsidian |
| Code highlight support | `1` | Necesario para ingeniería |
| Inline ID support | `1` | Tracking de tarjetas inline |
| Folder-based deck name | `1` | Carpeta = deck automático |
| Default deck name | `Galaxy::General` | En vez de `default` |
| Default Anki tag | `galaxy` o vacío | Cambiado desde `obsidian` |
| Flashcards tag | `card` | Default, no cambiar |
| Inline separator | `::` | Default, no cambiar |
| Inline reverse separator | `:::` | Default, no cambiar |

---

## 3. Sintaxis soportada

### Básica
```markdown
¿Cuál es la transformada de Laplace de $e^{at}$? #card
$\mathcal{L}\{e^{at}\} = \dfrac{1}{s-a}$
```

### Inline
```markdown
¿Qué es la ROC? :: Región donde $\sum |x[n]| \cdot r^{-n} < \infty$
```

### Cloze con highlight
```markdown
La energía almacenada es ==$E = \dfrac{1}{2}Li^2$== donde L es inductancia.
```

### Reversed
```markdown
¿Qué significa BIBO? #card-reverse
Bounded Input Bounded Output — toda entrada acotada produce una salida acotada.
```

### Con imagen
```markdown
¿Qué muestra este diagrama? #card
![[diagrama.svg]]
```

### Deck manual por frontmatter
```markdown
---
cards-deck: Galaxy::ETN901
---
```
> Si no se especifica, el deck se determina por la carpeta del archivo (con Folder-based deck name activado).

---

## 4. Comportamiento del plugin

- Al sincronizar, inserta automáticamente en el frontmatter: `cards-deck: NombreCarpeta`
- Agrega un ID de 13 dígitos al final de cada tarjeta: `^1785190534496`
- **No borrar el ID** — se usa para rastrear y actualizar tarjetas en syncs futuros
- El ribbon tiene un botón dedicado para sincronizar
- También disponible desde `Ctrl+P` → "Flashcards: Generate for the current file" o "Generate for all files"

---

## 5. Resultados de prueba

### Pruebas realizadas

| Aspecto | Estado | Nota |
|---|---|---|
| Tarjeta básica con `#card` | ✅ funciona | |
| Inline con `::` | ✅ funciona | |
| Cloze con `==highlight==` | ✅ funciona | |
| Reversed con `#card-reverse` | ✅ funciona | |
| LaTeX `$...$` | ✅ renderiza directo | Sin conversión manual — resuelve pendiente urgente de Opción A |
| Imagen embebida `![[img]]` | ✅ funciona | |
| Excalidraw `.svg` | ✅ funciona | Requiere "Export SVG to vault" manual antes del sync |
| Folder → deck automático | ✅ funciona | |
| Deck manual por frontmatter | ✅ funciona | |
| Sync → AnkiDroid | ✅ funciona | Flujo normal Desktop → AnkiWeb → Android |

### Observaciones

> [!note] Context-aware mode
> Con `context-aware: 1` los headers `##` se arrastran al frente de la tarjeta. Desactivar siempre.

> [!note] Tag automático
> El plugin agrega el tag `obsidian` (o el configurado) a todas las tarjetas en Anki. Cambiarlo a `galaxy` o dejarlo vacío en Settings.

> [!note] Excalidraw — paso manual requerido
> Antes de sincronizar con Flashcards, exportar el dibujo manualmente desde Excalidraw:
> Excalidraw → botón "Export SVG to vault" → genera `.svg` en la misma carpeta
> Luego embeber con `![[nombre.svg]]` en la nota.

> [!warning] Auto-export SVG
> Activar en Settings de Excalidraw: **Auto-export SVG → ON**
> Así el `.svg` se actualiza automáticamente cada vez que editás el dibujo.

---

## 6. Integración con Excalidraw — Image Occlusion

El script de Image Occlusion de TrillStones genera archivos `.card.md` con este formato:

```
TARGET DECK: Default
START
Basic
Front: ![[question.png]]
Back: ![[answer.png]]
[[editSource|Jump to edit source]]
[[batchMarker|Jump to batch file]]
Tags: Obsidian_to_Anki
END
```

> ⚠️ Este formato es de **Obsidian_to_Anki (Pseudonium)**, no de Flashcards (reuseman).
> Para usar Image Occlusion de Excalidraw se necesita instalar Obsidian_to_Anki → ver **Opción C**.

---

## 7. Idea pendiente — Script conversor Marginalia → Flashcards

**Problema:** Marginalia usa `RESPUESTA %%> PREGUNTA ;; %%` y Flashcards usa `PREGUNTA #card` + salto. Son incompatibles directamente.

**Experimento realizado:** usar `%%> Pregunta ;; #tag %%::Respuesta` — la `::` de Flashcards se activa pero arrastra todo el bloque `%%>...%%` como parte del frente.

**Solución propuesta:** script que convierta marginalia a formato Flashcards antes del sync:
```
RESPUESTA %%> PREGUNTA ;; %% → PREGUNTA #card \n RESPUESTA
```
Solo procesar líneas con `%%>` y `;;`. Revertir después del sync.

**Estado:** 🟡 pendiente — idea válida, no implementada.

---

## 8. Veredicto Opción B

**Pros:**
- LaTeX `$...$` renderiza directo sin conversión ✅
- Sintaxis más limpia y variada (inline, cloze, reversed)
- Imágenes y Excalidraw funcionan bien
- Deck automático por carpeta muy conveniente
- Botón de ribbon rápido

**Contras:**
- Sin mantenimiento activo desde Oct 2022
- No compatible con Image Occlusion de Excalidraw (necesita Opción C)
- Sintaxis no se mezcla con Marginalia sin script

**Candidato para:** notas dedicadas a flashcards, diagramas Excalidraw simples, fórmulas LaTeX.

---

%%
# galaxy-links
[[anki_galaxy_guide.md]]
[[anki-opcionA-marginalia.md]]
[[Untitled 1.md]]
%%
