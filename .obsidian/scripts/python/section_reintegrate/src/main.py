import sys
import os
import json
import shutil
import re

sys.stdout.reconfigure(encoding='utf-8')

file_path   = sys.argv[1]
vault_path  = sys.argv[2]
source_path = sys.argv[3]

# --- Rutas fijas ---
section_md   = os.path.join(vault_path, "Rubbish", "section.md")
section_json = os.path.join(vault_path, ".obsidian", "scripts", "python", "section_tool", "section.json")

# --- Validar que section.md tiene contenido ---
if not os.path.exists(section_md) or os.path.getsize(section_md) == 0:
    print("section.md está vacío. Corré section_extract primero.")
    sys.exit(0)

# --- Validar section.json ---
if not os.path.exists(section_json):
    print("section.json no encontrado. Corré section_extract primero.")
    sys.exit(0)

with open(section_json, 'r', encoding='utf-8') as f:
    meta_list = json.load(f)

# --- Buscar entrada en section.json por source_path ---
entry = next((e for e in meta_list if e["source_path"] == source_path), None)
if entry is None:
    print(f"No se encontró en section.json: {source_path}")
    sys.exit(0)

heading = entry["heading"]

# --- Validar archivo fuente ---
if not os.path.exists(source_path):
    print(f"Archivo original no encontrado: {source_path}")
    sys.exit(0)

# --- Construir separador buscado ---
rel_path  = os.path.relpath(source_path, vault_path)
separator = f"--- {rel_path} ---" #separator = f"--- ```{rel_path}``` ---"

# --- Leer section.md y extraer el bloque correspondiente ---
with open(section_md, 'r', encoding='utf-8') as f:
    sec_lines = f.readlines()

block_start = None
for i, line in enumerate(sec_lines):
    if line.rstrip('\n') == separator:
        block_start = i
        break

if block_start is None:
    print(f"Separador no encontrado en section.md: {separator}")
    sys.exit(0)

# --- Buscar fin del bloque (siguiente separador o fin de archivo) ---
block_end = len(sec_lines)
for i in range(block_start + 1, len(sec_lines)):
    if re.match(r'^--- .+ ---$', sec_lines[i].rstrip('\n')):
        block_end = i
        break

# --- Contenido del bloque (sin la línea del separador) ---
new_section = sec_lines[block_start + 1:block_end]

# --- Crear backup del archivo fuente ---
base, ext = os.path.splitext(source_path)
n = 1
while True:
    backup_path = f"{base} {n}{ext}"
    if not os.path.exists(backup_path):
        break
    n += 1
shutil.copy2(source_path, backup_path)

# --- Leer archivo fuente ---
with open(source_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# --- Detectar nivel del heading ---
match = re.match(r'^(#+)\s', heading)
level = len(match.group(1))
pattern = re.compile(r'^#{1,' + str(level) + r'}\s')

# --- Buscar inicio de la sección en el archivo fuente ---
start = None
for i, line in enumerate(lines):
    if line.rstrip('\n') == heading:
        start = i
        break

if start is None:
    print(f"No se encontró en el original: {heading}")
    sys.exit(0)

# --- Buscar fin de la sección con fence_stack ---
fence_stack = []
end = len(lines)
for i in range(start + 1, len(lines)):
    m = re.match(r'^(`{3,})', lines[i])
    if m:
        ticks = m.group(1)
        if fence_stack and fence_stack[-1] == ticks:
            fence_stack.pop()
        elif not fence_stack:
            fence_stack.append(ticks)
    if not fence_stack and pattern.match(lines[i]):
        end = i
        break

# --- Reemplazar sección en el archivo fuente ---
new_lines = lines[:start] + new_section + lines[end:]

with open(source_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# --- Eliminar bloque de section.md ---
remaining = sec_lines[:block_start] + sec_lines[block_end:]
if remaining and remaining[0].strip() == '':
    remaining = remaining[1:]
with open(section_md, 'w', encoding='utf-8') as f:
    f.writelines(remaining)

# --- Eliminar entrada de section.json ---
meta_list = [e for e in meta_list if e["source_path"] != source_path]
if meta_list:
    with open(section_json, 'w', encoding='utf-8') as f:
        json.dump(meta_list, f, ensure_ascii=False, indent=2)
else:
    os.remove(section_json)

print(f"Sección reintegrada: {heading} | Backup: {os.path.basename(backup_path)}")
