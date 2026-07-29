"""
latex_to_mathjax — Script 2
Convierte delimitadores LaTeX dentro de bloques Marginalia (%%> ... %%)
de sintaxis Obsidian ($...$ / $$...$$) a sintaxis MathJax (\(...\) / \[...\])

Uso desde Shell Commands:
    python main.py "<file_path_absolute>"

Flujo:
    1. Lee el archivo activo
    2. Localiza todos los bloques %%> ... %%
    3. Dentro de cada bloque convierte $$ → \[...\] y $ → \(...\)
    4. Escribe el archivo modificado en disco
    5. Obsidian detecta el cambio → Ctrl+Z restaura el original

Restricciones:
    - No toca bloques de código (`...` ni ```...```)
    - No toca wikilinks [[...]]
    - Solo opera dentro de bloques %%> ... %%
"""

import sys
import re


# ---------------------------------------------------------------------------
# Conversión LaTeX → MathJax dentro de un bloque de texto
# ---------------------------------------------------------------------------

def convert_latex_in_block(block_text: str) -> str:
    """
    Recibe el contenido interno de un bloque Marginalia (sin los delimitadores %%>/%%)
    y devuelve el texto con los delimitadores LaTeX convertidos a MathJax.

    Orden de operaciones:
        1. Proteger bloques de código inline y multilinea
        2. Convertir $$...$$ → \[...\]
        3. Convertir $...$ → \(...\)
        4. Restaurar los bloques de código protegidos
    """

    # --- Paso 1: proteger bloques de código ---
    placeholders = {}
    counter = [0]

    def protect(match):
        key = f"\x00CODE{counter[0]}\x00"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key

    # Multilinea primero (```...```)
    text = re.sub(r'```[\s\S]*?```', protect, block_text)
    # Inline (`...`)
    text = re.sub(r'`[^`\n]+`', protect, text)

    # --- Paso 2: $$ → \[...\] ---
    # No greedy, no captura $ sueltos
    text = re.sub(r'\$\$([\s\S]+?)\$\$', lambda m: r'\[' + m.group(1) + r'\]', text)

    # --- Paso 3: $ → \(...\) ---
    # Excluye: $$ (ya convertido), wikilinks [[...]], $ suelto sin cierre en la misma línea
    # Patrón: $ seguido de contenido no-vacío sin salto de línea, cerrado por $
    text = re.sub(r'(?<!\$)\$(?!\$)([^\$\n]+?)\$', lambda m: r'\(' + m.group(1) + r'\)', text)

    # --- Paso 4: restaurar bloques de código ---
    for key, original in placeholders.items():
        text = text.replace(key, original)

    return text


# ---------------------------------------------------------------------------
# Localización y conversión de bloques Marginalia
# ---------------------------------------------------------------------------

def convert_file(file_path: str) -> tuple[str, int]:
    """
    Lee el archivo, aplica la conversión dentro de cada bloque %%> ... %%
    y devuelve (contenido_modificado, cantidad_de_bloques_procesados).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks_found = 0

    def replace_block(match):
        nonlocal blocks_found
        opening = match.group(1)   # %%>  (con posible contenido inline)
        inner   = match.group(2)   # contenido del bloque
        closing = match.group(3)   # %%

        converted = convert_latex_in_block(inner)

        # Solo cuenta como "procesado" si hubo cambios reales
        if converted != inner:
            blocks_found += 1

        return opening + converted + closing

    # Patrón: bloque Marginalia %%> ... %%
    # Captura: (delimitador apertura)(contenido)(delimitador cierre)
    pattern = re.compile(
        r'(%%>[ \t]*\n?)'   # grupo 1: apertura  %%>
        r'([\s\S]*?)'       # grupo 2: contenido (no greedy)
        r'(%%)',            # grupo 3: cierre    %%
        re.MULTILINE
    )

    modified = pattern.sub(replace_block, content)

    return modified, blocks_found


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("ERROR: Se requiere la ruta del archivo como argumento.", file=sys.stderr)
        print("Uso: python main.py \"<ruta_absoluta_del_archivo>\"", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        modified_content, blocks_changed = convert_file(file_path)
    except FileNotFoundError:
        print(f"ERROR: Archivo no encontrado: {file_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR inesperado: {e}", file=sys.stderr)
        sys.exit(1)

    # Escribir el archivo modificado en disco
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)

    # stdout → Shell Commands puede mostrarlo como notificación
    if blocks_changed > 0:
        print(f"✓ LaTeX → MathJax: {blocks_changed} bloque(s) Marginalia convertido(s).")
    else:
        print("Sin cambios — no se encontraron fórmulas $...$ dentro de bloques %%> ... %%.")


if __name__ == "__main__":
    main()
