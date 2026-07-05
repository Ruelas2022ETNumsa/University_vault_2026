import sys
import re
import os

vault_path = sys.argv[1]
file_path  = sys.argv[2]

if not file_path:
    print("No hay archivo activo.")
    sys.exit(0)

abs_path = os.path.join(vault_path, file_path)

with open(abs_path, 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# --- 1. \frac -> \dfrac ---
content = re.sub(r'(?<!d)(?<!t)\\frac', r'\\dfrac', content)

# --- 2. Bloques desmos sin etiqueta ---
content = re.sub(r'```\nleft=', '```desmos-graph\nleft=', content)

# --- 3. Arrays en una linea: espacio+\+espacio -> \\+salto de linea ---
def fix_arrays(match):
    block = match.group(0)
    block = re.sub(r' \\ ', r'\\\\\n', block)
    return block

content = re.sub(
    r'\$\$\\begin\{array\}.*?\\end\{array\}\$\,
    fix_arrays,
    content,
    flags=re.DOTALL
)

# --- Guardar si hubo cambios ---
if content != original:
    with open(abs_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Correcciones realizadas.")
else:
    print("Sin cambios.")