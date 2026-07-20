---
status: creciente
---

**Contexto — Gemini Helper en University Vault**

**Estado:** plugin no instalado, nada configurado. Primera vez.

**Decisión tomada:** Shell Commands descartado para el caso Gemini/NotebookLM. Gemini Helper es la ruta elegida.

**NotebookLM se mantiene intacto** para sus dos usos (transcripción de supernovas y estudio activo con libros). Gemini Helper no lo reemplaza.

**Rol de Gemini Helper en el ecosistema:**

- Automatizador interno del vault via Workflow Builder
- Búsqueda semántica (RAG) sobre notas galaxy ya creadas
- Chat con contexto del vault para tareas de escritura dentro de Obsidian
- Potencial integración con los MCP ya existentes (Filesystem, GitHub, Basic Memory)

**Caso de uso prioritario a explorar en sesión:** Workflow Builder para disección de supernovas — leer una nota `supernova` (transcripción de NotebookLM) y crear automáticamente las notas galaxy hijas (`planet`, `moon`, `comet`) con YAML correcto, convención de nombres `ETNXXX-TNN-nombre.md`, y las dos capas de links, en las rutas correctas del vault.

**Entorno:**

- Windows 10 (PC) / Windows 11 (laptop)
- Python 3.13 en `C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe`
- Vault en `E:\University_vault_2026`
- API key de Gemini: pendiente verificar si ya existe en Google Cloud

**Archivos de referencia del vault para la sesión:**

- `_app/_config/_claude-boot.md` — arquitectura completa del vault
- `_app/_config/_notebooklm-system.md` — sistema NotebookLM
- `_app/_config/_TABnote-system.md` — flujo supernova → galaxy
- `_app/shellcommands/shellcmd_scripting_guide.md` — referencia de variables (útil para entender el vault aunque Shell Commands esté descartado)