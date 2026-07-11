import sys
import os
import json
import re

file_path  = sys.argv[1]
vault_path = sys.argv[2]
heading    = sys.argv[3]  # ej: "## Metodología"
source_path = sys.argv[4]  # ruta absoluta del archivo fuente

# --- Rutas fijas ---
section_md   = os.path.join(vault_path, "Rubbish", "section.md")
section_json = os.path.join(vault_path, ".obsidian", "scripts", "python", "section_tool", "section.json")

# --- Validar que section.md está vacío ---
if os.path.exists(section_md) and os.path.getsize(section_md) > 0:
    print("section.md ya tiene contenido. Corré section_reintegrate primero.")
    sys.exit(0)

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
for i, line in enumerate(lines):
    if line.rstrip('\n') == heading:
        start = i
        break

if start is None:
    print(f"No se encontró: {heading}")
    sys.exit(0)

# --- Buscar fin de la sección (siguiente heading de mismo nivel o superior) ---
end = len(lines)
for i in range(start + 1, len(lines)):
    if pattern.match(lines[i]):
        end = i
        break

# --- Extraer y escribir en section.md ---
section_content = ''.join(lines[start:end])

with open(section_md, 'w', encoding='utf-8') as f:
    f.write(section_content)

# --- Guardar metadata en section.json ---
meta = {
    "heading": heading,
    "source_path": source_path
}
with open(section_json, 'w', encoding='utf-8') as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)

print(f"Sección extraída: {heading}")
