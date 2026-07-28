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
- ~~**AnkiDroid:** Configuración → Apariencia → Tema → Oscuro — pendiente~~✅

### FSRS — algoritmo moderno de repetición espaciada

~~FSRS viene integrado desde Anki v23.10+. Reemplaza SM-2 (algoritmo de los años 80) y reduce un 20-30% las revisiones diarias manteniendo la misma retención.~~ ✅

**Activar:**

1. ~~Seleccionar un deck → Options (engranaje) → Advanced~~ ✅
2. ~~Activar "FSRS" → Save~~ ✅
3. Hacer click en "Optimize" después de acumular ~30 días de revisiones para que el algoritmo se calibre con tu historial.

> ✅ Activar FSRS en todos los decks antes de empezar a estudiar.

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

Cada materia = deck principal. Los subtemas = subdecks. Los plugins de Obsidian que sincronizan por carpeta respetarán esta jerarquía automáticamente.

---

## 3. Addons recomendados

~~Instalar desde Tools → Add-ons → Get Add-ons. Pegar el código y reiniciar.~~ ✅

| Addon | Código | Estado |
|---|---|---|
| **Image Occlusion Enhanced** | `1374772155` | ✅ instalado |
| **Review Heatmap** | `1771074083` | ✅ instalado |
| **True Retention** | `613684242` | ✅ instalado |
| **Hierarchical Tags** | `1089921461` | ❌ incompatible con versión actual |
| **Math Delimiters Replacer** | `401047458` | ✅ instalado |

> [!warning] Hierarchical Tags obsoleto
> El código `1089921461` es incompatible con Anki moderno. No es necesario — las versiones actuales ya tienen jerarquía nativa con `::` (ej: `ETN901::Laplace`). Si se quiere color en los tags, existe **Colorful Tags** como alternativa futura.

> [!note] Math Delimiters Replacer
> Convierte `$...$` y `$$...$$` a formato MathJax con `Alt+M`. Solución temporal hasta tener el script automático. Ver pendiente urgente en sección 9.

### Image Occlusion — flujo básico

1. Crear nueva tarjeta → seleccionar tipo "Image Occlusion Enhanced"
2. Subir imagen (diagrama, circuito, esquema)
3. Dibujar rectángulos sobre las zonas a ocultar (valores, etiquetas, partes)
4. Cada rectángulo = una tarjeta separada
5. Add Cards → las tarjetas se generan automáticamente

> 💡 Alternativa desde Obsidian: el script "Image Occlusion" del plugin Excalidraw hace lo mismo sin salir de Obsidian. Evaluar cuál flujo es más cómodo en la sesión de prueba.

---

## 4. AnkiWeb — Sync en la nube

~~AnkiWeb es el servidor de sincronización oficial, completamente gratuito.~~ ✅

**Configurar sync:**

1. ~~Anki Desktop → Sync (icono nube arriba a la derecha)~~ ✅
2. ~~Ingresar cuenta de ankiweb.net~~ ✅
3. ~~Primera vez: elegir "Upload to AnkiWeb"~~ ✅ (sube los decks locales a la nube)
4. En sesiones posteriores: sync automático al abrir y cerrar Anki

**Frecuencia recomendada:** sync manual antes de cerrar Anki en PC, para que AnkiDroid tenga las tarjetas actualizadas.

> ⚠️ El sync solo funciona si Anki Desktop se sincronizó primero. AnkiDroid no puede recibir tarjetas directamente desde Obsidian — el flujo siempre es: Obsidian → Anki Desktop → AnkiWeb → AnkiDroid.

---

## 5. Móvil — AnkiDroid (Android)

**Instalación:**

1. ~~Play Store → buscar "AnkiDroid Flashcards" → Instalar (gratuito, sin publicidad)~~ ✅
2. ~~Abrir AnkiDroid → Settings → AnkiWeb account~~ ✅
3. ~~Ingresar la misma cuenta de ankiweb.net~~ ✅
4. ~~Sync → los decks del desktop aparecen en el móvil~~ ✅

> [!note] Búsqueda en Play Store
> Buscar exactamente **"AnkiDroid Flashcards"**. Confirmar desarrollador: **AnkiDroid Open Source Team** (aparece en azul debajo del nombre). Versión actual: 2.24.0.

> [!note] Primera sync en AnkiDroid
> Al aparecer mensaje de conflicto → elegir **"AnkiWeb"**. El desktop ya subió los datos, el móvil debe descargar.

**Modo oscuro en AnkiDroid:** Settings → Apariencia → Tema → Dark / Night Mode

**Uso en móvil:** solo para repasar. La creación de tarjetas se hace desde Obsidian o Anki Desktop — no desde el móvil.

---

## 6. Integración con Obsidian

### Addon nativo de Marginalia — Anki Advanced Sync

~~El addon de Marginalia tiene sync nativo con Anki.~~ ✅ Probado — ver Opción A en sección 7.

**Activar:**

1. ~~Marginalia Settings → Addons → Anki Advanced Sync → ON~~ ✅
2. ~~Anki debe estar abierto con AnkiConnect activo~~ ✅

**Sintaxis real (corregida tras prueba):**

```
RESPUESTA %%> PREGUNTA ;; %%
```

> [!warning] Orden invertido
> Lo que va **antes** de `%%>` es el reverso (respuesta). Lo que va entre `%%>` y `;;` es el frente (pregunta). No es lo que indica la documentación original del plugin.

**Pendiente de prueba:**
- [ ] ¿El addon respeta los tag-class (`!`, `?`, `F-`) como tags en Anki?
- [ ] ¿Las imágenes (`img:[[...]]`) llegan correctamente a Anki?
- [ ] ¿Los crops de PDF++ se exportan como imagen en la tarjeta?
- [ ] ¿El sync es bidireccional (cambios en Anki reflejados en Obsidian)?

---

## 7. Plugins de Obsidian a probar

Probar en orden. Quedarse con el que mejor se integre al flujo Galaxy.

### Opción A — Anki Advanced Sync (addon de Marginalia) ✅ PROBADA

**Pros:** integración nativa con `;;`, conoce la sintaxis de Marginalia, soporta crops de PDF++.
**Contras:** sintaxis de frente/reverso invertida respecto a lo esperado. LaTeX `$...$` no renderiza sin conversión manual.

> [!note] Resultado de prueba
> Sync funciona correctamente en ambas direcciones (Desktop ↔ AnkiDroid). Tag mapping funciona tanto por frontmatter como inline. LaTeX requiere conversión manual o script. **Fuerte candidato por integración con marginalia.**

> [!tip] Tag inline descubierto en prueba
> El tag después del ID no se muestra en la tarjeta pero sí determina el deck:
> `Respuesta %%> Pregunta ;; ^anki-ID #tag %%`
> Más limpio que frontmatter para notas mixtas.

> [!note] "Felicitaciones — mazo finalizado"
> FSRS no muestra tarjetas hasta que toca revisarlas. Para ver tarjetas en pruebas: **Estudio personalizado → Repasar tarjetas adelantadas → 9999**.

Ver documentación completa: [[Untitled 1]]

---

### Opción B — AnkiSync+ (plugin de Obsidian)

**Pros:** integración con Excalidraw, soporte de imágenes, organización por tags como decks, limpieza automática de tarjetas eliminadas.
**Contras:** sintaxis de tarjetas puede chocar con la sintaxis de Marginalia.
**Instalación:** Community Plugins → buscar "AnkiSync+" → Instalar → Activar.

**Configuración básica:**

1. Settings → AnkiSync+ → Anki URL: `http://127.0.0.1:8765`
2. Definir carpeta del vault a escanear
3. Definir formato de tarjeta (Basic, Cloze)

---

### Opción C — Yanki (plugin de Obsidian)

**Pros:** pure Markdown sin sintaxis especial, una nota = una tarjeta, carpetas como decks, no interfiere con Marginalia.
**Contras:** requiere notas dedicadas a flashcards (no inline en notas de clase).
**Instalación:** Community Plugins → buscar "Yanki" → Instalar → Activar.

**Configuración básica:**

1. Settings → Yanki → seleccionar carpetas del vault a sincronizar
2. Formato de tarjeta en la nota:

```markdown
---
# Frente de la tarjeta
¿Cuál es la condición de convergencia de Laplace?

## Reverso
Re(s) > σ₀ donde σ₀ es la abscisa de convergencia.
```

3. Command Palette → "Yanki: Sync flashcard notes to Anki"

---

### Opción D — Obsidian-Anki-Sync (debanjandhar12)

**Pros:** el más potente para LaTeX — permite cloze dentro de bloques matemáticos. Esencial si se quieren tarjetas tipo:

```
$$\mathcal{L}\{f(t)\} = \int_0^\infty <!-- replace id="1" text="e^{-st} f(t)" --> dt$$
```

**Contras:** sintaxis más compleja, puede chocar con LaTeX del vault.
**Instalación:** Community Plugins → buscar "Anki Sync" (debanjandhar12) → Instalar.

---

## 8. Flujo Galaxy propuesto (a validar)

```
Clase / Estudio
     ↓
Nota .md en supernova con marginalia %%> pregunta ;; %%
     ↓
Anki Advanced Sync (addon Marginalia) o plugin Obsidian
     ↓
Anki Desktop (con AnkiConnect activo)
     ↓
Sync → AnkiWeb
     ↓
AnkiDroid (Android) — repasar en cualquier lugar
```

**Para Image Occlusion (circuitos, diagramas):**

```
Diagrama en Excalidraw
     ↓
Script "Image Occlusion" de Excalidraw → genera tarjetas con zonas ocultas
     ↓ (o directamente desde Anki con Image Occlusion Enhanced)
Anki Desktop
     ↓
AnkiWeb → AnkiDroid
```

---

## 9. Pendientes de prueba

### Instalación y configuración base

- [x] Instalar Anki Desktop desde ankiweb.net
- [x] Crear cuenta en ankiweb.net
- [x] Instalar AnkiConnect (código `2055492159`) y configurar CORS para Obsidian
- [x] Activar modo oscuro en Anki Desktop
- [x] Activar FSRS en opciones del deck
- [x] Instalar AnkiDroid en Android y vincular cuenta
- [x] Verificar sync Desktop → AnkiWeb → AnkiDroid con una tarjeta de prueba

### Addons de Anki Desktop

- [x] Instalar Image Occlusion Enhanced (`1374772155`)
- [x] Instalar Review Heatmap (`1771074083`)
- [x] Instalar True Retention (`613684242`)
- [x] ~~Instalar Hierarchical Tags (`1089921461`)~~ — incompatible, no necesario
- [x] Instalar Math Delimiters Replacer (`401047458`) — solución temporal para LaTeX

### Integración con Obsidian — plugins a comparar

- [x] **Opción A** — Anki Advanced Sync (addon Marginalia): ✅ probado. Funciona. Ver [[Untitled 1]].
- [ ] **Opción B** — AnkiSync+: instalar y probar con una nota simple. Verificar integración con Excalidraw.
- [ ] **Opción C** — Yanki: instalar y probar con carpeta `_anki/` dedicada.
- [ ] **Opción D** — Obsidian-Anki-Sync: probar solo si se necesita cloze dentro de LaTeX.
- [ ] Decidir qué plugin integrar a Galaxy y documentar en `_marginalia_system.md` o nota dedicada.

### Image Occlusion

- [ ] Probar script Image Occlusion desde Excalidraw con un diagrama de circuito real
- [ ] Comparar con Image Occlusion Enhanced desde Anki Desktop
- [ ] Decidir cuál flujo es más cómodo para ingeniería

### 🔴 Pendiente urgente — Script conversor `$` → MathJax

**Problema:** las marginalia con fórmulas usan `$...$` (sintaxis Obsidian) pero Anki necesita `\(...\)`. La conversión manual con `Alt+M` es inviable para uso real.

**Solución propuesta:** script que antes del sync:
1. Lee la nota `.md`
2. Convierte `$$...$$` → `\[...\]` y `$...$` → `\(...\)`
3. Solo dentro de bloques `%%> ... %%` para no afectar el resto de la nota
4. Exporta a Anki normalmente
5. Revierte los cambios en el `.md` automáticamente

---

%%
# galaxy-links
[[_app/_config/_marginalia_system.md]]
[[_app/_appnotes/Marginalia_guide.md]]
[[_app/_projects/tsk_alx-rul.md]]
%%
