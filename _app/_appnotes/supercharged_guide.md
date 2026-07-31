---
title: "Supercharged Links Guide — Iconos en el explorador del vault"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
related_notes:
  - "[[plugin_guide]]"
  - "[[_galaxy-system]]"
tags: [beacon, obsidian, plugins, infraestructura, supercharged-links]
date_created: 2026-07-19
date_updated: 2026-07-31
status: activo
---

# Supercharged Links Guide — Iconos en el explorador del vault

> Plugin: **Supercharged Links**
> Repositorio: https://github.com/mdelobelle/obsidian_supercharged_links
> CSS snippet: `E:\University_vault_2026\.obsidian\snippets\supercharged-links.css`
> CSS generado por el plugin (no editar): `E:\University_vault_2026\.obsidian\snippets\supercharged-links-gen.css`

Muestra iconos/prefijos en el explorador lateral del vault según valores de campos YAML. Tres sistemas activos: **status lunar** (para archivos `tsk_`), **galaxy body** (para notas del vault) y **proyectos** (ship, carrier, operator, blueprint, dropship — con soporte de dos íconos simultáneos).

---

## Índice

- [[#1. Configuración del plugin]]
- [[#2. Sistema de status lunar — archivos tsk_]]
- [[#3. Sistema galaxy body — notas del vault]]
- [[#4. Sistema de proyectos — hangar]]
- [[#5. Archivos involucrados]]

---

## 1. Configuración del plugin

**Settings → Supercharged Links → Target Attributes for Styling:**

```
status, galaxy_body
```

El plugin lee ambos campos del YAML de cada nota y los expone como atributos HTML en el explorador:

| Campo YAML | Atributo HTML generado |
|---|---|
| `status` | `data-link-status="valor"` |
| `galaxy_body` | `data-link-galaxy_body="valor"` |

El CSS apunta a esos atributos con el selector `::before` para inyectar el icono.

> `supercharged-links-gen.css` es generado automáticamente por el plugin — no editar. El CSS real vive en `supercharged-links.css`.

---

## 2. Sistema de status lunar — archivos `tsk_`

Aplica al campo `status` en el frontmatter. Solo usado en archivos tipo `tsk_` en `_projects/`.

| `status` | Icono | Significado |
|---|---|---|
| `nueva` | 🌑 | Slot disponible — sin proyecto asignado |
| `creciente` | 🌒 | Proyecto en curso |
| `llena` | 🌕 | Proyecto terminado, pendiente de documentar y archivar |

**CSS:**
```css
/* =============================
   STATUS LUNAR — archivos tsk_
   ============================= */

.nav-file-title-content[data-link-status="nueva"]::before { content: "🌑 "; }
.nav-file-title-content[data-link-status="creciente"]::before { content: "🌒 "; }
.nav-file-title-content[data-link-status="llena"]::before { content: "🌕 "; }
```

---

## 3. Sistema galaxy body — notas del vault

Aplica al campo `galaxy_body` en el frontmatter. Cubre los 15 tipos del Sistema Galaxy.

| `galaxy_body` | Icono | Rol |
|---|---|---|
| `star` | ☀️ | MOC de un tema |
| `planet` | 🪐 | Nota de teoría central |
| `moon` | 🌙 | Propiedad, fórmula o resultado clave |
| `comet` | ☄️ | Ejercicio resuelto |
| `nebula` | 🌫️ | Agrupador de sesión |
| `dwarf` | ⬛ | Resumen condensado |
| `asteroid` | 🪨 | Referencia externa / extracto de PDF |
| `photon` | 💡 | Imagen estática pura |
| `neutrino` | ⚛️ | Código que genera imagen (Desmos / TikZJax) |
| `constellation` | 🌌 | Mapa mental galaxy (Excalidraw + Mindmap Builder) |
| `observatory` | 🔭 | Dibujo técnico libre en Excalidraw |
| `bridge` | 🌉 | Conexión entre materias |
| `beacon` | 📡 | Guía de infraestructura del vault |
| `supernova` | ✨ | Transcripción bruta de clase (NotebookLM) |
| `workshop` | 🔧 | Tarea académica por materia |

**CSS:**
```css
/* =============================
   GALAXY BODY
   ============================= */

.nav-file-title-content[data-link-galaxy_body="star"]::before { content: "☀️ "; }
.nav-file-title-content[data-link-galaxy_body="planet"]::before { content: "🪐 "; }
.nav-file-title-content[data-link-galaxy_body="moon"]::before { content: "🌙 "; }
.nav-file-title-content[data-link-galaxy_body="comet"]::before { content: "☄️ "; }
.nav-file-title-content[data-link-galaxy_body="nebula"]::before { content: "🌫️ "; }
.nav-file-title-content[data-link-galaxy_body="dwarf"]::before { content: "⬛ "; }
.nav-file-title-content[data-link-galaxy_body="asteroid"]::before { content: "🪨 "; }
.nav-file-title-content[data-link-galaxy_body="photon"]::before { content: "💡 "; }
.nav-file-title-content[data-link-galaxy_body="neutrino"]::before { content: "⚛️ "; }
.nav-file-title-content[data-link-galaxy_body="constellation"]::before { content: "🌌 "; }
.nav-file-title-content[data-link-galaxy_body="observatory"]::before { content: "🔭 "; }
.nav-file-title-content[data-link-galaxy_body="bridge"]::before { content: "🌉 "; }
.nav-file-title-content[data-link-galaxy_body="beacon"]::before { content: "📡 "; }
.nav-file-title-content[data-link-galaxy_body="supernova"]::before { content: "✨ "; }
.nav-file-title-content[data-link-galaxy_body="workshop"]::before { content: "🔧 "; }
```

---

## 4. Sistema de proyectos — hangar

Aplica a archivos en `_hangar/`. Combina dos campos YAML (`galaxy_body` + `status`) para mostrar dos íconos simultáneos en `::before`.

**Principio de cascada CSS:** los selectores combinados (`[data-link-galaxy_body][data-link-status]`) tienen mayor especificidad que los simples y los sobreescriben. Los selectores simples de status funcionan como fallback para archivos que solo tienen `status` sin `galaxy_body`.

---

### Operator

Solo tiene `status` — un ícono simple.

| `status` | Ícono | Significado |
|---|---|---|
| `free` | ✔ | Disponible |
| `busy` | ❌ | Cargado con un ship activo |

---

### Blueprint

Solo tiene `status` — un ícono simple.

| `status` | Ícono | Significado |
|---|---|---|
| `idea` | 💡 | Anotado, sin evaluar |
| `evaluando` | 🔍 | En análisis |
| `aprobado` | 📐 | Aprobado para convertirse en ship o carrier |

---

### Ship y Carrier — selector combinado

Cuando un archivo tiene ambos campos (`galaxy_body` + `status`), el CSS muestra **dos íconos en `::before`**: primero el body, luego el status.

**Formato visual:** `[body] [status] nombre-del-archivo`

| `galaxy_body` | `status` | Resultado |
|---|---|---|
| `ship` | `docked` | 🚀 🛸 |
| `ship` | `in-orbit` | 🚀 💫 |
| `ship` | `delayed` | 🚀 ⏸️ |
| `ship` | `docking` | 🚀 ⚙️ |
| `ship` | `aborted` | 🚀 💀 |
| `ship` | `delivered` | 🚀 ✅ |
| `carrier` | `docked` | 🛸 🛸 |
| `carrier` | `in-orbit` | 🛸 💫 |
| `carrier` | `delayed` | 🛸 ⏸️ |
| `carrier` | `docking` | 🛸 ⚙️ |
| `carrier` | `aborted` | 🛸 💀 |
| `carrier` | `delivered` | 🛸 ✅ |

> Nota: `carrier` + `docked` muestra 🛸 🛸 porque ambos comparten ícono. Es una colisión semántica del sistema, no del CSS.

**CSS — selectores combinados:**
```css
/* SHIP */
.nav-file-title-content[data-link-galaxy_body="ship"][data-link-status="docked"]::before    { content: "🚀 🛸 "; }
.nav-file-title-content[data-link-galaxy_body="ship"][data-link-status="in-orbit"]::before  { content: "🚀 💫 "; }
.nav-file-title-content[data-link-galaxy_body="ship"][data-link-status="delayed"]::before   { content: "🚀 ⏸️ "; }
.nav-file-title-content[data-link-galaxy_body="ship"][data-link-status="docking"]::before   { content: "🚀 ⚙️ "; }
.nav-file-title-content[data-link-galaxy_body="ship"][data-link-status="aborted"]::before   { content: "🚀 💀 "; }
.nav-file-title-content[data-link-galaxy_body="ship"][data-link-status="delivered"]::before { content: "🚀 ✅ "; }

/* CARRIER */
.nav-file-title-content[data-link-galaxy_body="carrier"][data-link-status="docked"]::before    { content: "🛸 🛸 "; }
.nav-file-title-content[data-link-galaxy_body="carrier"][data-link-status="in-orbit"]::before  { content: "🛸 💫 "; }
.nav-file-title-content[data-link-galaxy_body="carrier"][data-link-status="delayed"]::before   { content: "🛸 ⏸️ "; }
.nav-file-title-content[data-link-galaxy_body="carrier"][data-link-status="docking"]::before   { content: "🛸 ⚙️ "; }
.nav-file-title-content[data-link-galaxy_body="carrier"][data-link-status="aborted"]::before   { content: "🛸 💀 "; }
.nav-file-title-content[data-link-galaxy_body="carrier"][data-link-status="delivered"]::before { content: "🛸 ✅ "; }
```

**CSS — fallback (status sin galaxy_body):**
```css
.nav-file-title-content[data-link-status="docked"]::before    { content: "🛸 "; }
.nav-file-title-content[data-link-status="in-orbit"]::before  { content: "💫 "; }
.nav-file-title-content[data-link-status="delayed"]::before   { content: "⏸️ "; }
.nav-file-title-content[data-link-status="docking"]::before   { content: "⚙️ "; }
.nav-file-title-content[data-link-status="aborted"]::before   { content: "💀 "; }
.nav-file-title-content[data-link-status="delivered"]::before { content: "✅ "; }
```

> Si en el futuro se agrega un nuevo `galaxy_body` de proyecto con status, se agregan 6 reglas combinadas siguiendo el mismo patrón.

---

## 5. Archivos involucrados

| Archivo | Rol |
|---|---|
| `.obsidian\snippets\supercharged-links.css` | CSS principal — editable — contiene los tres sistemas |
| `.obsidian\snippets\supercharged-links-gen.css` | Generado automáticamente por el plugin — no editar |
| `.obsidian\snippets\legacy\supercharged-links.css.bk` | Backup v1 — CSS original sin selectores combinados |
| `.obsidian\snippets\legacy\supercharged-linksv2.css.bk` | Backup v2 — CSS con selectores combinados usando `::after` para status |

---

%%
# galaxy-links
[[_app/_appnotes/plugin_guide.md]]
[[_app/_config/_galaxy-system.md]]
%%
