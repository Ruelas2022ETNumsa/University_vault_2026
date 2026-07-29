"""
latex_to_mathjax — Script 2 (toggle con bandera YAML)

Flujo:
    Lee `latex_converted` en el YAML frontmatter:
    - false / ausente → convierte L→M  ($→\(...\), $$→\[...\]) y setea bandera true
    - true            → revierte M→L  (\(...\)→$, \[...\]→$$) y setea bandera false

Uso desde Shell Commands:
    python main.py "<file_path_absolute>"

Restricciones:
    - No toca bloques de código (`...` ni ```...```)
    - No toca el YAML frontmatter (salvo la bandera latex_converted)
    - Los IDs de Anki (^anki-XXXX) no se ven afectados
"""

import sys
import re


# ---------------------------------------------------------------------------
# Protección de bloques de código
# ---------------------------------------------------------------------------

def protect_code(text: str) -> tuple[str, dict]:
    placeholders = {}
    counter = [0]

    def protect(match):
        key = f"\x00CODE{counter[0]}\x00"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key

    text = re.sub(r'```[\s\S]*?```', protect, text)
    text = re.sub(r'`[^`\n]+`', protect, text)
    return text, placeholders


def restore_code(text: str, placeholders: dict) -> str:
    for key, original in placeholders.items():
        text = text.replace(key, original)
    return text


# ---------------------------------------------------------------------------
# Conversión L → M  (Obsidian LaTeX → MathJax)
# ---------------------------------------------------------------------------

def latex_to_mathjax(body: str) -> str:
    text, placeholders = protect_code(body)
    # $$ primero para no confundir con $
    text = re.sub(r'\$\$([\s\S]+?)\$\$', lambda m: r'\[' + m.group(1) + r'\]', text)
    text = re.sub(r'(?<!\$)\$(?!\$)([^\$\n]+?)\$', lambda m: r'\(' + m.group(1) + r'\)', text)
    return restore_code(text, placeholders)


# ---------------------------------------------------------------------------
# Conversión M → L  (MathJax → Obsidian LaTeX)
# ---------------------------------------------------------------------------

def mathjax_to_latex(body: str) -> str:
    text, placeholders = protect_code(body)
    # \[...\] primero para no confundir con \(...\)
    text = re.sub(r'\\\[([\s\S]+?)\\\]', lambda m: '$$' + m.group(1) + '$$', text)
    text = re.sub(r'\\\(([\s\S]+?)\\\)', lambda m: '$' + m.group(1) + '$', text)
    return restore_code(text, placeholders)


# ---------------------------------------------------------------------------
# YAML: leer bandera y actualizar
# ---------------------------------------------------------------------------

def parse_frontmatter(content: str) -> tuple[str, str, bool]:
    """
    Separa YAML frontmatter del cuerpo.
    Devuelve (frontmatter_raw, body, latex_converted_bool).
    """
    match = re.match(r'^(---\n[\s\S]*?\n---\n?)', content)
    if not match:
        return '', content, False

    frontmatter = match.group(1)
    body = content[len(frontmatter):]

    flag_match = re.search(r'^latex_converted:\s*(true|false)\s*$', frontmatter, re.MULTILINE)
    converted = flag_match.group(1) == 'true' if flag_match else False

    return frontmatter, body, converted


def update_flag(frontmatter: str, new_value: bool) -> str:
    """
    Actualiza o inserta la bandera latex_converted en el YAML.
    """
    flag_line = f'latex_converted: {"true" if new_value else "false"}'
    if re.search(r'^latex_converted:', frontmatter, re.MULTILINE):
        return re.sub(r'^latex_converted:.*$', flag_line, frontmatter, flags=re.MULTILINE)
    else:
        # Insertar antes del cierre ---
        return re.sub(r'(\n---\n?)$', f'\n{flag_line}\\1', frontmatter)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("ERROR: Se requiere la ruta del archivo como argumento.", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: Archivo no encontrado: {file_path}", file=sys.stderr)
        sys.exit(1)

    frontmatter, body, already_converted = parse_frontmatter(content)

    if not already_converted:
        # L → M
        new_body = latex_to_mathjax(body)
        new_frontmatter = update_flag(frontmatter, True)
        msg = "✓ L→M: LaTeX convertido a MathJax. Listo para sync."
    else:
        # M → L
        new_body = mathjax_to_latex(body)
        new_frontmatter = update_flag(frontmatter, False)
        msg = "✓ M→L: MathJax revertido a LaTeX. Obsidian restaurado."

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_frontmatter + new_body)

    print(msg)


if __name__ == "__main__":
    main()
