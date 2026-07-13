import sys
import os
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

file_path  = sys.argv[1]
vault_path = sys.argv[2]
heading    = sys.argv[3]  # ej: "## Metodología"
source_path = sys.argv[4]  # ruta absoluta del archivo fuente

# --- Rutas fijas ---
section_md   = os.path.join(vault_path, "Rubbish", "section.md")
section_json = os.path.join(vault_path, ".obsidian", "scripts", "python", "section_tool", "section.json")

# --- Detectar modo (A: vacío → edición+reintegración / B: con contenido → acumulación) ---
mode_b = os.path.exists(section_md) and os.path.getsize(section_md) > 0

# --- Validar archivo fuente ---
if not os.path.exists(source_path):
    print(f"Archivo no encontrado: {source_path}")
    sys.exit(0)

# --- Leer archivo fuente ---
with open(source_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# --- Detectar nivel del heading ---
match = re.match(r'^(#+)\s', heading)
if not match:
    print("Heading inválido. Ejemplo válido: ## Título")
    sys.exit(0)

level = len(match.group(1))
pattern = re.compile(r'^#{1,' + str(level) + r'}\s')

# --- Buscar inicio de la sección ---
start = None
in_code_block = False
for i, line in enumerate(lines):
    if line.startswith('```'):
        in_code_block = not in_code_block
    if not in_code_block and line.rstrip('\n') == heading:
        start = i
        break

if start is None:
    print(f"No se encontró: {heading}")
    sys.exit(0)

# --- Buscar fin de la sección (siguiente heading de mismo nivel o superior) ---
in_code_block = False
end = len(lines)
for i in range(start + 1, len(lines)):
    if lines[i].startswith('```'):
        in_code_block = not in_code_block
    if not in_code_block and pattern.match(lines[i]):
        end = i
        break

# --- Construir separador de ruta relativa al vault ---
rel_path = os.path.relpath(source_path, vault_path)
separator = f"--- {rel_path} ---\n"

# --- Extraer contenido ---
section_content = ''.join(lines[start:end])

if not mode_b:
    # --- Modo A: sobrescribir section.md y guardar section.json ---
    with open(section_md, 'w', encoding='utf-8') as f:
        f.write(separator)
        f.write(section_content)
    meta = {
        "heading": heading,
        "source_path": source_path
    }
    with open(section_json, 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    print(f"Sección extraída (Modo A): {heading}")
else:
    # --- Modo B: acumular en section.md, no tocar section.json ---
    with open(section_md, 'a', encoding='utf-8') as f:
        f.write("\n")
        f.write(separator)
        f.write(section_content)
    print(f"Sección acumulada (Modo B): {heading}")
