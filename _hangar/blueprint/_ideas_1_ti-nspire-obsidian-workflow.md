---
galaxy_body: blueprint
status: evaluando
priority: media
date: 2026-08-31
---

# Ideas TI-Nspire × Obsidian workflow

> **Relación:** Integración de la calculadora TI-Nspire CX II CAS con Obsidian como entorno intermedio para editar archivos .tns con ayuda de IA

---

## Herramientas consideradas

- [ ] **TnsTools** (MaksimirKurtov) — convierte .tns ↔ XML en Python puro, maneja el cifrado 3DES sin depender de software de TI. Es el núcleo del flujo de edición de programas.
- [ ] **to_tns converter** (Kiritiop) — skill para Claude Code que convierte documentos (PDF, DOCX, MD, CSV, XLSX) directamente a .tns tipo Notes. Usa Luna internamente para el binario final.
- [ ] **Ti-Nspire-CX-CAS-programs** (sononicola) — colección de .tns reales para ingeniería (FEM, fluidos, estructuras). Útil como referencia de qué estructura tienen los archivos y qué tipo de contenido soportan.
- [ ] **Shell Commands** (Taitava) — plugin de Obsidian que ejecuta comandos de terminal desde la paleta o con hotkeys, pasando variables como `{{file_path}}`. Permite disparar los scripts Python de conversión desde dentro de Obsidian.
- [ ] **Commander** (jsmorabito) — plugin de Obsidian que agrega comandos a cualquier parte de la UI (barra lateral, header de nota, menú contextual). Sirve para crear botones visuales que llamen a los Shell Commands definidos.

---

## Flujo central

- [ ] Definir la carpeta intermedia en el vault (ej. `_calculadora/`) donde viven los archivos convertidos como .md o .xml
- [ ] Script Python `tns_to_md.py`: toma un .tns, lo convierte a XML con TnsTools, lo transforma a Markdown legible y lo guarda en la carpeta intermedia
- [ ] Script Python `md_to_tns.py`: toma el .md editado, reconstruye el XML y genera el .tns listo para cargar
- [ ] Configurar dos Shell Commands en Obsidian: uno para cada dirección del flujo (`{{file_path}}` como argumento)
- [ ] Agregar botones en la UI con Commander que disparen esos dos comandos

---

## Modelo de calculadora

- [ ] **TI-Nspire CX II CAS** — objetivo del flujo. Requiere OS 3.0.2 o superior (cumple). Soporta archivos .tns con Notes, programas TI-Basic, hojas de cálculo y gráficos. Límite ~12 KB por página de Notes.

---

## A depurar

- ¿Luna (dependencia de to_tns) compila bien en Windows sin WSL?
- ¿TnsTools cubre todos los tipos de .tns o solo los de tipo Notes/programa?
- Commander vs Shell Commands: definir cuál hace qué (Commander = botón visual, Shell Commands = lógica del comando)

---

## Referencias

**Calculadora**
- TnsTools (conversión .tns ↔ XML): https://github.com/MaksimirKurtov/TnsTools
- to_tns converter (documentos → .tns): https://github.com/Kiritiop/ti-nspire-tns-converter-python-claude-skill
- Ejemplos .tns reales (ingeniería): https://github.com/sononicola/Ti-Nspire-CX-CAS-programs
- Luna (compilador binario .tns, dependencia de to_tns): https://github.com/ndless-nspire/Luna
- Hackspire — formato TNS documentado: https://hackspire.org/index.php/TNS_File_Format

**Obsidian**
- Shell Commands (ejecutar scripts Python desde Obsidian): https://github.com/taitava/obsidian-shellcommands
- Commander (botones en la UI de Obsidian): https://github.com/jsmorabito/obsidian-commander
