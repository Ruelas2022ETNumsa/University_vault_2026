---
title: "Anki — Guía de instalación e integración Galaxy"
scope: vault
status: en progreso
date_created: 2026-07-26
date_updated: 2026-07-27
tags: [anki, obsidian, galaxy, spaced-repetition]
---

# Anki — Guía de instalación e integración Galaxy

> Documento de prueba. Todo lo marcado como `[ ]` debe probarse antes de considerarse parte del sistema Galaxy.

---

## Índice

- [[#1. Instalación — Anki Desktop (Windows)]]
- [[#2. Configuración inicial]]
- [[#3. Addons recomendados]]
- [[#4. AnkiWeb — Sync en la nube]]
- [[#5. Móvil — AnkiDroid (Android)]]
- [[#6. Integración con Obsidian]]
- [[#7. Plugins de Obsidian a probar]]
- [[#8. Flujo Galaxy propuesto]]
- [[#9. Pendientes de prueba]]

---

## 1. Instalación — Anki Desktop (Windows)

1. ~~Descargar desde [ankiweb.net](https://apps.ankiweb.net/) — versión estable para Windows.~~ ✅
2. ~~Instalar normalmente. No requiere cuenta para funcionar en local.~~ ✅ instalado en `E:\Programas\anki\`
3. ~~Crear cuenta gratuita en [ankiweb.net](https://ankiweb.net) — necesaria para sync con móvil.~~ ✅

### AnkiConnect — addon obligatorio para integración con Obsidian

AnkiConnect es el puente que permite a Obsidian (y otros programas) comunicarse con Anki. Sin esto ningún plugin de Obsidian puede enviar tarjetas a Anki.

**Instalación:**

1. ~~Abrir Anki → Tools → Add-ons → Get Add-ons~~ ✅
2. ~~Pegar código: `2055492159` → OK~~ ✅
3. ~~Reiniciar Anki~~ ✅

**Configuración de CORS** (necesaria para que Obsidian pueda conectarse):

1. ~~Abrir Anki → Tools → Add-ons → seleccionar AnkiConnect → Config~~ ✅
2. ~~Reemplazar el contenido con:~~ ✅

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

3. ~~OK → reiniciar Anki~~ ✅

> ⚠️ Anki debe estar abierto y corriendo para que cualquier plugin de Obsidian pueda sincronizar tarjetas.

---

## 2. Configuración inicial

### Modo oscuro

~~Anki moderno tiene modo oscuro nativo — no requiere addon.~~ ✅

- ~~**Desktop:** Preferencias (`Ctrl+P`) → Apariencia → Tema → Night Mode / Dark~~ ✅
- ~~**AnkiDroid:** Configuración → Apariencia → Tema → Oscuro~~ ✅

### FSRS — algoritmo moderno de repetición espaciada

~~FSRS viene integrado desde Anki v23.10+. Reemplaza SM-2 y reduce un 20-30% las revisiones diarias manteniendo la misma retención.~~ ✅

**Activar:**

1. ~~Seleccionar un deck → Options (engranaje) → Advanced~~ ✅
2. ~~Activar "FSRS" → Save~~ ✅
3. Hacer click en "Optimize" después de acumular ~30 días de revisiones.

> [!note] Observación
> Al activar FSRS se despliegan varias opciones adicionales — no tocar nada por ahora. Los parámetros se optimizan solos con el uso.

### Estructura de decks recomendada para Galaxy

```
Galaxy
├── ETN901 — Señales y Sistemas
│   ├── Laplace
│   ├── Fourier
│   └── Z
├── ETN806 — Circuitos
│   ├── RC
│   └── RLC
└── General
    └── Fórmulas clave
```

---

## 3. Addons recomendados

~~Instalar desde Tools → Add-ons → Get Add-ons. Pegar el código y reiniciar.~~ ✅

| Addon | Código | Estado |
|---|---|---|
| **Image Occlusion Enhanced** | `1374772155` | ✅ instalado |
| **Review Heatmap** | `1771074083` | ✅ instalado |
| **True Retention** | `613684242` | ✅ instalado |
| **Hierarchical Tags** | `1089921461` | ❌ incompatible — no necesario |
| **Math Delimiters Replacer** | `401047458` | ✅ instalado (solo para Opción A) |

> [!warning] Hierarchical Tags obsoleto
> Incompatible con Anki moderno. No necesario — jerarquía nativa con `::` (ej: `ETN901::Laplace`).

> [!note] Math Delimiters Replacer
> Solo relevante para Opción A (Marginalia). Opción B (Flashcards) renderiza `$...$` directamente.

---

## 4. AnkiWeb — Sync en la nube

~~AnkiWeb es el servidor de sincronización oficial, completamente gratuito.~~ ✅

1. ~~Anki Desktop → Sync → ingresar cuenta~~ ✅
2. ~~Primera vez: "Upload to AnkiWeb"~~ ✅
3. En sesiones posteriores: sync automático al abrir y cerrar Anki

> ⚠️ Flujo siempre: Obsidian → Anki Desktop → AnkiWeb → AnkiDroid

---

## 5. Móvil — AnkiDroid (Android)

~~Play Store → "AnkiDroid Flashcards" (AnkiDroid Open Source Team) → Instalar → vincular cuenta~~ ✅

> [!note] Primera sync en AnkiDroid
> Al aparecer mensaje de conflicto → elegir **"AnkiWeb"**.

**Uso en móvil:** solo para repasar. Creación desde Obsidian o Anki Desktop únicamente.

---

## 6. Integración con Obsidian

### Addon nativo de Marginalia — Anki Advanced Sync

~~Marginalia Settings → Addons → Anki Advanced Sync → ON~~ ✅ Probado — ver Opción A.

**Sintaxis real (corregida tras prueba):**

```
RESPUESTA %%> PREGUNTA ;; %%
```

> [!warning] Orden invertido
> Lo que va **antes** de `%%>` es el reverso. Lo que va entre `%%>` y `;;` es el frente.

---

## 7. Plugins de Obsidian a probar

### Opción A — Anki Advanced Sync (addon Marginalia) ✅ PROBADA

**Pros:** integración nativa con `;;`, tag mapping inline y por frontmatter.
**Contras:** LaTeX `$...$` no renderiza sin conversión. Orden frente/reverso invertido.

> [!note] Resultado
> Sync funciona. Tag mapping funciona. LaTeX requiere conversión manual. **Fuerte candidato por integración con Marginalia.**

> [!tip] Tag inline descubierto
> `Respuesta %%> Pregunta ;; ^anki-ID #tag %%` — el tag determina el deck sin mostrarse en la tarjeta.

Ver documentación completa: [[Untitled 1]]

---

### Opción B — Flashcards (reuseman) ✅ PROBADA

**Pros:** LaTeX `$...$` renderiza directo, sintaxis variada (inline `::`, cloze `==`, reversed), imágenes y Excalidraw funcionan, deck automático por carpeta.
**Contras:** sin mantenimiento desde Oct 2022. No compatible con Image Occlusion de Excalidraw (necesita Opción C). No se mezcla con Marginalia sin script.

> [!note] Resultado
> Todas las pruebas pasaron. LaTeX renderiza en AnkiDroid sin conversión — resuelve pendiente de Opción A. Excalidraw requiere "Export SVG to vault" antes del sync. **Candidato para notas dedicadas y diagramas.**

> [!warning] AnkiSync+ (RochaG07) — descartado
> Probado antes de Flashcards. Creaba decks pero no tarjetas. Sin fix, sin mantenimiento activo. Descartado.

**Configuración básica:**
1. Community Plugins → "Flashcards" (reuseman) → Instalar → Activar
2. Settings → Grant Permission + Test (con Anki abierto)
3. Context-aware: `0` | Folder-based deck: `1` | Default deck: `Galaxy::General`

Ver documentación completa: [[anki-opcionB-flashcards]]

---

### Opción C — Obsidian_to_Anki (Pseudonium) — PENDIENTE

**Por qué es necesaria:** el script Image Occlusion de TrillStones genera archivos `.card.md` en formato Obsidian_to_Anki. Sin este plugin no se puede completar el flujo Excalidraw → Image Occlusion → Anki.
**Instalación:** Community Plugins → buscar "Export to Anki" o "Obsidian_to_Anki" (Pseudonium).

---

### Opción D — Obsidian-Anki-Sync (debanjandhar12) — PENDIENTE

**Para qué sirve:** cloze dentro de bloques LaTeX. Sintaxis más compleja.
```
<!-- replaceblock-start -->
<!-- replace id="1" text="valor" -->
$$formula$$
<!-- replaceblock-end -->
```

---

## 8. Flujo Galaxy propuesto

**Flujo principal (texto y fórmulas):**
```
Nota .md con marginalia %%> pregunta ;; %%
     ↓
Opción A (Marginalia) o Opción B (Flashcards)
     ↓
Anki Desktop → AnkiWeb → AnkiDroid
```

**Flujo Image Occlusion (circuitos, diagramas):**
```
Diagrama en Excalidraw
     ↓
Script Image Occlusion (TrillStones) → genera .card.md
     ↓
Opción C (Obsidian_to_Anki) exporta a Anki
     ↓
AnkiWeb → AnkiDroid
```

---

## 9. Pendientes de prueba

### Completado ✅

- [x] Instalar Anki Desktop, AnkiConnect, FSRS, modo oscuro
- [x] Instalar AnkiDroid y vincular cuenta
- [x] Sync Desktop → AnkiWeb → AnkiDroid verificado
- [x] Addons: Image Occlusion, Review Heatmap, True Retention, Math Delimiters Replacer
- [x] **Opción A** — Marginalia Anki Sync: ✅ funciona. Ver [[Untitled 1]]
- [x] **Opción B** — Flashcards (reuseman): ✅ funciona. Ver [[anki-opcionB-flashcards]]
- [x] ~~AnkiSync+ (RochaG07)~~ — descartado

### Pendiente 🔲

- [ ] **Opción C** — Obsidian_to_Anki (Pseudonium): instalar y probar. Necesario para Image Occlusion de Excalidraw.
- [ ] **Opción D** — Obsidian-Anki-Sync (debanjandhar12): probar si se necesita cloze en LaTeX.
- [ ] Image Occlusion completo: Excalidraw → TrillStones script → Opción C → Anki
- [ ] Decidir flujo definitivo Galaxy y documentar en `_marginalia_system.md`

### 🟡 Ideas pendientes — Scripts

**Script 1 — Conversor Marginalia → Flashcards**
Convertir `RESPUESTA %%> PREGUNTA ;; %%` a `PREGUNTA #card \n RESPUESTA` antes del sync, revertir después.

**Script 2 — Conversor `$` → MathJax (solo para Opción A)**
Convertir `$...$` → `\(...\)` dentro de bloques `%%> ... %%` antes del sync con Marginalia. No necesario para Opción B.

---

%%
# galaxy-links
[[_app/_config/_marginalia_system.md]]
[[_app/_appnotes/Marginalia_guide.md]]
[[_app/_projects/tsk_alx-rul.md]]
[[Untitled 1]]
[[anki-opcionB-flashcards]]
%%
