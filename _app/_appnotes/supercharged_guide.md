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
date_updated: 2026-07-19
status: activo
---

# Supercharged Links Guide — Iconos en el explorador del vault

> Plugin: **Supercharged Links**
> Repositorio: https://github.com/mdelobelle/obsidian_supercharged_links
> CSS snippet: `E:\University_vault_2026\.obsidian\snippets\supercharged-links.css`
> CSS generado por el plugin (no editar): `E:\University_vault_2026\.obsidian\snippets\supercharged-links-gen.css`

Muestra iconos/prefijos en el explorador lateral del vault según valores de campos YAML. Dos sistemas activos: **status lunar** (para archivos `tsk_`) y **galaxy body** (para notas del vault).

---

## Índice

- [[#1. Configuración del plugin]]
- [[#2. Sistema de status lunar — archivos tsk_]]
- [[#3. Sistema galaxy body — notas del vault]]
- [[#4. Archivos involucrados]]

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

## 4. Archivos involucrados

| Archivo | Rol |
|---|---|
| `.obsidian\snippets\supercharged-links.css` | CSS principal — editable — contiene ambos sistemas |
| `.obsidian\snippets\supercharged-links-gen.css` | Generado automáticamente por el plugin — no editar |

---

%%
# galaxy-links
[[_app/_appnotes/plugin_guide.md]]
[[_app/_config/_galaxy-system.md]]
%%
