"""
latex_to_mathjax — Script 2 (toggle con bandera YAML + contador exports + limpieza IDs)

Flujo según estado de `latex_converted` en YAML:

    CASO A — bandera ausente o false:
        1. Convierte L→M en el body ($→\(...\), $$→\[...\])
        2. Crea/actualiza latex_converted: true
        (anki_exports no se toca)

    CASO B — bandera true:
        1. Borra IDs Anki (^anki-XXXXXXXXXXXXX ) del body
        2. Convierte M→L en el body (\(...\)→$, \[...\]→$$)
        3. Setea latex_converted: false
        4. Incrementa anki_exports (export_1, export_2, ...)

Uso desde Shell Commands:
    python main.py "<file_path_absolute>"

Restricciones:
    - No toca bloques de código (`...` ni ```...```)
    - Solo modifica latex_converted y anki_exports en el YAML
    - El patrón de ID asumido: ^anki-XXXXXXXXXXXXX<espacio>
      (13 dígitos numéricos, delimitado por espacio en ambos lados)
"""

import sys
import re


# ---------------------------------------------------------------------------
# Protección / restauración de bloques de código
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
# Conversiones
# ---------------------------------------------------------------------------

def latex_to_mathjax(body: str) -> str:
    """L→M: $...$ → \(...\)  y  $$...$$ → \[...\]"""
    text, placeholders = protect_code(body)
    text = re.sub(r'\$\$([\s\S]+?)\$\$', lambda m: r'\[' + m.group(1) + r'\]', text)
    text = re.sub(r'(?<!\$)\$(?!\$)([^\$\n]+?)\$', lambda m: r'\(' + m.group(1) + r'\)', text)
    return restore_code(text, placeholders)


def mathjax_to_latex(body: str) -> str:
    """M→L: \[...\] → $$...$$  y  \(...\) → $...$"""
    text, placeholders = protect_code(body)
    text = re.sub(r'\\\[([\s\S]+?)\\\]', lambda m: '$$' + m.group(1) + '$$', text)
    text = re.sub(r'\\\(([\s\S]+?)\\\)', lambda m: '$' + m.group(1) + '$', text)
    return restore_code(text, placeholders)


def remove_anki_ids(body: str) -> str:
    """
    Borra IDs de Anki del body.
    Patrón: ^anki- seguido de exactamente 13 dígitos y un espacio.
    El espacio delimitador derecho se conserva.
    Ejemplo: ';; ^anki-1785295229260 #tag %%' → ';; #tag %%'
    """
    return re.sub(r'\^anki-\d{13} ', '', body)


# ---------------------------------------------------------------------------
# YAML: parseo, lectura de banderas, actualización
# ---------------------------------------------------------------------------

def parse_frontmatter(content: str) -> tuple[str, str]:
    """Separa YAML frontmatter del body. Devuelve (frontmatter, body)."""
    match = re.match(r'^(---\n[\s\S]*?\n---\n?)', content)
    if match:
        return match.group(1), content[len(match.group(1)):]
    return '', content


def get_flag(frontmatter: str, key: str) -> str | None:
    """Lee el valor de una clave YAML simple. Devuelve None si no existe."""
    match = re.search(rf'^{re.escape(key)}:\s*(.+?)\s*$', frontmatter, re.MULTILINE)
    return match.group(1) if match else None


def set_flag(frontmatter: str, key: str, value: str) -> str:
    """Actualiza o inserta una clave YAML antes del cierre ---."""
    line = f'{key}: {value}'
    if re.search(rf'^{re.escape(key)}:', frontmatter, re.MULTILINE):
        return re.sub(rf'^{re.escape(key)}:.*$', line, frontmatter, flags=re.MULTILINE)
    else:
        return re.sub(r'(\n---\n?)$', f'\n{line}\\1', frontmatter)


def next_export_value(current: str | None) -> str:
    """
    Dado el valor actual de anki_exports (ej. 'export_3'),
    devuelve el siguiente (ej. 'export_4').
    Si no existe o no parsea, devuelve 'export_1'.
    """
    if current:
        match = re.match(r'export_(\d+)', current.strip())
        if match:
            return f'export_{int(match.group(1)) + 1}'
    return 'export_1'


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
    except Exception as e:
        print(f"ERROR al leer el archivo: {e}", file=sys.stderr)
        sys.exit(1)

    frontmatter, body = parse_frontmatter(content)

    latex_converted = get_flag(frontmatter, 'latex_converted')
    already_converted = (latex_converted == 'true')

    if not already_converted:
        # CASO A — L→M
        new_body = latex_to_mathjax(body)
        frontmatter = set_flag(frontmatter, 'latex_converted', 'true')
        msg = "✓ L→M: LaTeX convertido a MathJax. Listo para sync con Anki."

    else:
        # CASO B — M→L
        new_body = remove_anki_ids(body)
        new_body = mathjax_to_latex(new_body)
        frontmatter = set_flag(frontmatter, 'latex_converted', 'false')
        current_exports = get_flag(frontmatter, 'anki_exports')
        next_exports = next_export_value(current_exports)
        frontmatter = set_flag(frontmatter, 'anki_exports', next_exports)
        msg = f"✓ M→L: MathJax revertido a LaTeX. IDs Anki eliminados. Exports: {next_exports}."

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + new_body)
    except Exception as e:
        print(f"ERROR al escribir el archivo: {e}", file=sys.stderr)
        sys.exit(1)

    print(msg)


if __name__ == "__main__":
    main()
