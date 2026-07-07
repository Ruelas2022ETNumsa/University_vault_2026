import sys
import re
import os

file_path  = sys.argv[1]
vault_path = sys.argv[2]

if not file_path:
    print("No hay archivo activo.")
    sys.exit(0)

abs_path = os.path.join(vault_path, file_path)

with open(abs_path, 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# --- 0. Bloques cornell mal formados ---
# Apertura: 5 backticks + newline + cornell  →  5 backticks + cornell (en la misma linea)
content = re.sub(r'`````\ncornell\n', '`````cornell\n', content)
# Apertura: 3 o 4 backticks + newline + cornell  →  5 backticks + cornell
content = re.sub(r'(?m)^````?\ncornell\n', '`````cornell\n', content)
# Cierre: menos de 5 backticks seguidos de linea en blanco + > [!summary]  →  5 backticks
content = re.sub(r'(?<!`)````?(?!`)(\n\n> \[!summary\])', r'`````\1', content)

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
    r'\$\$\\begin\{array\}.*?\\end\{array\}\$\$',
    fix_arrays,
    content,
    flags=re.DOTALL
)

# --- 4. Insertar bloques marginalia dentro de bloques cornell ---
def fix_cornell(match):
    block = match.group(0)
    # Solo insertar si aun no tiene bloques marginalia (idempotente)
    if '```marginalia' in block:
        return block
    block = re.sub(
        r'(::cue\n)',
        '::cue\n````marginalia\n%%> %%\n',
        block
    )
    block = re.sub(
        r'(::note\n)',
        '````\n::note\n````marginalia\n%%< %%\n',
        block
    )
    return block

content = re.sub(
    r'`````cornell\n.*?`````',
    fix_cornell,
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