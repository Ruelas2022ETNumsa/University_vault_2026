Déjame ver exactamente qué hay suelto en `_app`.Perfecto, ya tengo todo el panorama. Ahora te doy la propuesta concreta.

---

## Análisis de lo que hay suelto en `_app`

Revisando los archivos, hay tres categorías claras:

**Archivos que necesitan YAML** (son notas `.md` que aparecen en el grafo):

- `_appnotes/desmos_guide.md`
- `_appnotes/tags_notes.md`
- `_appnotes/desmoslm.md` ← redirige a desmos_guide
- `_appnotes/desmos_intro.md` ← redirige a desmos_guide
- `solve/git_solve.md`
- `TagsRoutes/logMessage.md` ← caso especial, es un log autogenerado

**Archivos que NO necesitan YAML** (no son notas, el grafo no los toca):

- `TagsRoutes/patch-log.txt` — texto plano
- `scripts/tag_routs_scripts/patch-obsidian.bat` y `.ps1` — scripts
- `Excalidraw/Drawing 2026-05-11 16.56.55.excalidraw.md` — caso especial

---

## Propuesta: nuevo tipo de cuerpo `guide`

Los archivos de `_appnotes/` y `solve/` no son notas académicas — son documentación de infraestructura. No encajan limpiamente en ningún tipo Galaxy existente. Propongo agregar un décimo tipo:

|`galaxy_body`|Símbolo|Rol|
|---|---|---|
|`guide`|📖|Guía de herramienta o proceso del vault. Vive en `_app/`.|

Así el grafo los muestra conectados pero visualmente distinguibles del contenido académico.

---

## YAML propuesto para cada archivo

**`desmos_guide.md`**

```yaml
---
title: "Desmos — Guía unificada para Obsidian"
galaxy_body: guide
scope: vault
tool: desmos-plugin
audience: [usuario, notebooklm, claude]
tags: [guide, desmos, infraestructura]
date_created: 2026-01-01
status: activo
---
```

Bloque `%%` al final:

```
%%
galaxy-links
[[_galaxy-system]]
[[convencion-notas]]
%%
```

**`tags_notes.md`**

```yaml
---
title: "Tags Routes — Guía de mantenimiento del plugin"
galaxy_body: guide
scope: vault
tool: tags-routes
audience: [claude]
tags: [guide, tags-routes, infraestructura]
date_created: 2026-01-01
status: activo
---
```

**`desmoslm.md`** y **`desmos_intro.md`** (archivos obsoletos que redirigen)

```yaml
---
title: "Desmos LM — deprecado"
galaxy_body: guide
scope: vault
status: deprecado
tags: [guide, desmos, deprecado]
---
```

**`git_solve.md`**

```yaml
---
title: "Git — Resolución de conflictos en Obsidian"
galaxy_body: guide
scope: vault
tool: obsidian-git
tags: [guide, git, infraestructura, solve]
date_created: 2026-01-01
status: activo
---
```

**`logMessage.md`** — este es autogenerado por el plugin TagsRoutes cada vez que corre. No vale la pena ponerle YAML porque se sobreescribe. Lo mejor es **excluirlo del grafo** desde `Settings → Graph → Filters → Files to exclude` con la ruta `_app/TagsRoutes/logMessage.md`.

---

## Excalidraw

`Drawing 2026-05-11 16.56.55.excalidraw.md` — este archivo lo maneja el plugin Excalidraw, no conviene tocarle el YAML. En cambio, si quieres que aparezca conectado en el grafo, la forma correcta es crear una nota `photon` en `Semesters/` que lo referencie con `[[Drawing 2026-05-11...]]`.

---

¿Procedo a agregar el YAML a los 5 archivos (`desmos_guide`, `tags_notes`, `desmoslm`, `desmos_intro`, `git_solve`) y también a actualizar `_galaxy-system.md` para registrar el tipo `guide`?