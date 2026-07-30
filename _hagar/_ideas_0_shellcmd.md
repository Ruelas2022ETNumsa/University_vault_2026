# Ideas Shell Commands — Vault ETN901

> Lista de ideas para implementar con Shell Commands en Obsidian. Pendiente de depuración — algunas ya pueden estar cubiertas.

---

## 📄 Procesamiento de archivos externos

- [ ] Extraer texto de un PDF y guardarlo como nota `.md` en el vault
- [ ] Convertir Word (`.docx`) a Markdown
- [ ] Convertir PowerPoint (`.pptx`) a Markdown
- [ ] Descargar una página web y guardarla como nota limpia

---

## 🔗 Integración con herramientas externas

- [ ] Sincronizar tareas del vault con Google Tasks o Todoist
- [ ] Enviar una nota por email directamente desde Obsidian
- [ ] Subir una nota a GitHub como issue

---

## 🛠️ Mantenimiento del vault

- [ ] Backup selectivo — copiar solo notas modificadas hoy a una carpeta de respaldo
- [ ] Detectar archivos huérfanos — notas que nadie enlaza
- [ ] Generar estadísticas del vault — notas por `galaxy_body`, por materia, por `status`
- [ ] Detectar imágenes en `_assets/` no referenciadas por ninguna nota y moverlas a `borrar/`
- [ ] Detectar notas sin YAML o con YAML incompleto (campos obligatorios ausentes)
- [ ] Listar notas con `status: borrador` más antiguas de N días

---

## 🤖 Automatización del sistema operativo

- [ ] Abrir el archivo activo en VS Code
- [ ] Imprimir la nota activa desde Obsidian
- [ ] Mover archivos entre carpetas del vault con lógica condicional basada en YAML

---

## 🐍 Python + vault

- [ ] File watcher — detectar cuando se guarda una nota nueva y ejecutar procesamiento automático (ej. `notebooklm_fix` al pegar una supernova)
- [ ] Publicar notas seleccionadas a GitHub Pages como sitio web
- [ ] Script que valide convención de nombres (`ETNXXX-TNN-nombre.md`) y reporte violaciones

---

## 🌐 Integración con APIs

- [ ] Consultar Wolfram Alpha con una expresión matemática y traer resultado como nota
- [ ] Buscar en arXiv o Google Scholar y guardar resultados como `asteroid`
- [ ] Traducir contenido de una nota con DeepL o Google Translate

---

## ⚙️ Ideas propias — basadas en el vault

- [ ] Auto-actualizar `date_updated` en el YAML al guardar cualquier beacon (trigger: archivo modificado)
- [ ] Generar índice Dataview por `galaxy_body` — lista todas las notas de un tipo con un comando
- [ ] Script que verifique que toda nota tenga el bloque `%% galaxy-links %%` al final
- [ ] Al crear una nota nueva, preguntar al usuario el tipo (`galaxy_body`) y la materia, y generar el YAML base automáticamente (con Prompt de Shell Commands)
- [ ] Mover automáticamente archivos de `borrar/` a la papelera del sistema después de N días
- [ ] Script que detecte notas `supernova` sin notas `planet` derivadas (transcripciones sin diseccionar)
- [ ] Reporte semanal: notas creadas esta semana, por materia y tipo, guardado como nota `dwarf` de resumen
- [ ] Sincronización forzada de Obsidian Git con un hotkey (git pull + push manual sin esperar el auto-sync)
- [ ] Abrir la carpeta del archivo activo en el Explorador de Windows

---

## ❓ A depurar (pueden estar ya cubiertas)

- Watcher de archivos — ¿ya existe algo similar con los eventos del plugin Shell Commands?
- Git commit manual — ¿ya está configurado en `_sync-system`?
- Estadísticas del vault — ¿Dataview ya lo cubre parcialmente?

---

# otros agregados a revisar

**Scripts Python pendientes — sistema galaxy**

**Correcciones / limpieza**
- [ ] `notebooklm_fix` — ✅ hecho
- [ ] Listar notas con `status: pendiente` → genera nota con la lista
- [ ] Detectar planets/comets con bloque `%%` vacío
- [ ] Normalizar `date_updated` al día actual en archivo activo

**Validación de YAML**
- [ ] Verificar campos obligatorios según `galaxy_body` — alertar si faltan
- [ ] Detectar `galaxy_body` con valores inválidos (typos)
- [ ] Detectar wikilinks en `%%` que apunten a archivos inexistentes

**Reportes**
- [ ] Generar nota `dwarf` automáticamente con comets de un tema agrupados por `source`
- [ ] Listar todas las notas de una materia con su `status`

**Automatización estructural**
- [ ] Renombrar archivo según convención galaxy + actualizar wikilinks que apuntan a él
- [ ] Sincronizar bloque `%%` con wikilinks declarados en YAML (`orbiting`, `concepts_used`, etc.)

---

# ideas

un script que detecte lo nuevo respecto a lo antiguo, mas que todo para notas de transcripcion se buscaria que el script haga una historial de transcripcion tipo.
fecha-> se transcribio x y esto se lleva a las nevas notas task

