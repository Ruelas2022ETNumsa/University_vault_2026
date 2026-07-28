---
title: "Anki — Instalación, Configuración y Prueba Opción A"
scope: vault
status: probado parcialmente
date: 2026-07-27
tags: [anki, marginalia, setup, galaxy]
---

# Anki — Instalación, Configuración y Prueba Opción A

> Documento de sesión. Registra lo probado, lo que funcionó, lo que no, y los pendientes.

---

## 1. Instalación

### Anki Desktop (Windows)
- Descargado desde la página oficial: https://apps.ankiweb.net/
- Versión: estable para Windows x64
- Instalado en: `E:\Programas\anki\`
- Modo oscuro activado al abrir por primera vez: Preferencias → Apariencia → Night Mode

### AnkiDroid (Android)
- Descargado desde Play Store
- Buscar exactamente: **"AnkiDroid Flashcards"**
- Confirmar desarrollador: **AnkiDroid Open Source Team** (aparece en azul debajo del nombre)
- Versión actual al momento de instalación: 2.24.0
- Gratuito, sin publicidad

---

## 2. Cuenta AnkiWeb y Sincronización

### Crear cuenta
- Ir a: https://ankiweb.net → registrarse con Gmail u otro correo
- La cuenta es gratuita y necesaria para sync entre dispositivos

### Primera sincronización — Anki Desktop
1. Abrir Anki Desktop → click en ícono de nube (sync)
2. Ingresar credenciales de ankiweb.net
3. Al aparecer mensaje de conflicto → elegir **"Subir a AnkiWeb"**
   - Razón: cuenta nueva, vacía en ambos lados — el PC es la fuente

### Primera sincronización — AnkiDroid
1. Abrir AnkiDroid → Configuración → AnkiWeb account
2. Ingresar mismas credenciales
3. Al aparecer mensaje de conflicto → elegir **"AnkiWeb"**
   - Razón: el desktop ya subió los datos, el móvil debe descargar

### Flujo de sync establecido
```
Obsidian → Anki Desktop → AnkiWeb → AnkiDroid
```
> ⚠️ Anki Desktop debe estar abierto y corriendo para que cualquier sync desde Obsidian funcione. Sin Anki abierto aparece el error: `could not connect to anki`.

---

## 3. Configuración de Anki Desktop

### AnkiConnect — addon obligatorio
- Código: `2055492159`
- Instalar: Herramientas → Complementos → Obtener complementos → pegar código → OK → reiniciar Anki
- Después de instalar, configurar CORS para Obsidian:
  - Herramientas → Complementos → seleccionar AnkiConnect → Config
  - Reemplazar contenido con:

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
- OK → reiniciar Anki

### FSRS — algoritmo moderno
- Activar: engranaje ⚙️ del deck → Opciones → Advanced → activar FSRS → Guardar
- No modificar parámetros — se calibran solos después de ~30 días de revisiones
- Activar en todos los decks antes de empezar a estudiar

### Addons instalados

| Addon | Código | Estado |
|---|---|---|
| AnkiConnect | `2055492159` | ✅ instalado y configurado |
| Image Occlusion Enhanced | `1374772155` | ✅ instalado |
| Review Heatmap | `1771074083` | ✅ instalado |
| True Retention | `613684242` | ✅ instalado |
| Hierarchical Tags | `1089921461` | ❌ incompatible con versión actual |
| Math Delimiters Replacer | `401047458` | ✅ instalado (ver sección LaTeX) |

> ℹ️ **Hierarchical Tags** está obsoleto para Anki moderno. Las versiones actuales ya tienen jerarquía de tags nativa con `::` — ejemplo: `ETN901::Laplace`. No requiere addon.

---

## 4. Opción A — Anki Advanced Sync (addon de Marginalia)

### Activación
- Ya incluido en el plugin Cornell Marginalia
- Settings de Obsidian → Marginalia → Addons → **Anki Advanced Sync → ON**
- Requiere Anki Desktop abierto con AnkiConnect activo

### Comandos disponibles
Accesibles desde Command Palette (`Ctrl+P`):
- `Cornell Marginalia: Sync Flashcards to Anki (Current Note)` — sincroniza solo la nota activa, pide nombre del deck
- `Cornell Marginalia: Sync ALL Vault Flashcards to Anki (Tag-Mapped)` — sincroniza todo el vault según tag mappings configurados

### Sintaxis real de la marginalia para Anki

```
RESPUESTA %%> PREGUNTA ;; %%
```

> ⚠️ El orden es **RESPUESTA primero, PREGUNTA después del `%%>`**. Lo que va antes del `%%>` es el reverso de la tarjeta. Lo que va entre `%%>` y `;;` es el frente.

Después de la primera sincronización, el plugin inserta un ID automático:

```
RESPUESTA %%> PREGUNTA ;; ^anki-1785189199235 %%
```

### Tag Mapping — asignar notas a decks automáticamente

**Configuración:**
Settings → Marginalia → Anki Auto-Sync (Tag Mappings) → `+ Add Route`

Ejemplo configurado:
- `#pepe` → `Deck:New1`
- `#tilin` → `Deck2:New2`

**Método 1 — tag en frontmatter:**
```markdown
---
tags: [pepe]
---

Respuesta %%> Pregunta ;; %%
```

**Método 2 — tag inline después del `;;` (descubierto en prueba):**
```
Respuesta %%> Pregunta ;;  #pepe %%
```
> ✅ Funciona. El tag después del `;;` el ide ID  se coloca de forma automatica al exportar, no se muestra en la tarjeta pero sí determina el deck. Más limpio que frontmatter para notas mixtas.

Luego ejecutar: `Sync ALL Vault Flashcards to Anki (Tag-Mapped)`

### LaTeX — estado actual

Anki usa MathJax con delimitadores `\(...\)` y `\[...\]`, no `$...$` de Obsidian.

**Problema:** las marginalia con `$formula$` se exportan sin renderizar en AnkiDroid.

**Solución actual (manual):**
- Addon `Math Delimiters Replacer` (código `401047458`)
- Seleccionar texto en Anki → `Alt+M` → convierte `$` a `\(...\)`
- Tedioso para uso regular

**Formato que sí renderiza en móvil:**
```
\(\mathcal{L}\{e^{at}\} = \dfrac{1}{s-a}\) %%> ¿Transformada de Laplace de \(e^{at}\)? ;; %%
```

### Observación sobre "Felicitaciones — mazo finalizado"
- FSRS no muestra tarjetas hasta que toca revisarlas según el algoritmo
- Para ver tarjetas en modo prueba: **Estudio personalizado → Repasar tarjetas adelantadas → 9999**
- No afecta el algoritmo de forma permanente

### Resultado general de la prueba

| Aspecto | Estado |
|---|---|
| Sync Obsidian → Anki Desktop | ✅ funciona |
| Sync Anki Desktop → AnkiDroid | ✅ funciona |
| Tag mapping a decks | ✅ funciona (frontmatter e inline) |
| Texto simple | ✅ funciona |
| LaTeX `\(...\)` manual | ✅ renderiza en móvil |
| LaTeX `$...$` de Obsidian | ❌ no renderiza sin conversión |

---

## 5. Pendientes

### 🔴 Urgente — Script conversor `$` → MathJax

**Problema:** las marginalia con fórmulas usan `$...$` (sintaxis Obsidian) pero Anki necesita `\(...\)`. La conversión manual con `Alt+M` en Anki es inviable para uso real.

**Solución propuesta:** script que antes del sync:
1. Lee la nota `.md`
2. Convierte `$$...$$` → `\[...\]` y `$...$` → `\(...\)`
3. Solo dentro del contenido de marginalia (`%%> ... %%`)
4. Exporta a Anki normalmente
5. Revierte los cambios en el `.md` (`Ctrl+Z` o automático)

**Alcance:** aplicar solo dentro de bloques `%%> ... %%` para no afectar el resto de la nota.

---

%%
# galaxy-links
[[anki_galaxy_guide.md]]
[[_skills/_start.md]]
%%
