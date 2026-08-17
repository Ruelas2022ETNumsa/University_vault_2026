"""
pdf_figure_search/main.py
Busca una etiqueta de figura en los PDFs de una materia y devuelve
una lista de links PDF++ lista para pegar en Obsidian.

Uso: py main.py <sigla> <etiqueta>
Ejemplo: py main.py ETN607 "4.3"
         py main.py ETN-607 "Fig. 2-4"
"""

import os
import sys
import subprocess

try:
    import pymupdf as fitz
except ImportError:
    print("PyMuPDF no instalado. Ejecuta: py -m pip install pymupdf")
    sys.exit(1)

# ── Configuración ────────────────────────────────────────────────────────────

VAULT_PATH = r"E:\University_vault_2026"
PDF_ROOT   = os.path.join(VAULT_PATH, "_PDF")
SPLIT_PATTERN = r"-\d+to\d+"


# ── Funciones ────────────────────────────────────────────────────────────────

def build_variants(label: str):
    import re
    num = re.sub(r"^(figura|figure|fig\.?)\s*", "", label.strip(), flags=re.IGNORECASE).strip()
    prefixes = [
        f"Fig. {num}",
        f"Fig {num}",
        f"fig. {num}",
        f"fig {num}",
        f"Figure {num}",
        f"Figura {num}",
    ]
    return prefixes, num


def get_pdf_folder(sigla: str):
    candidates = [
        sigla,
        sigla[:3] + "-" + sigla[3:],
        sigla.replace("-", ""),
    ]
    for name in os.listdir(PDF_ROOT):
        if name.upper() in [c.upper() for c in candidates]:
            return os.path.join(PDF_ROOT, name)
    return None


def list_pdfs(folder: str):
    return [f for f in os.listdir(folder) if f.lower().endswith(".pdf")]


def group_split_pdfs(pdf_list: list):
    import re
    groups = {}
    for pdf in sorted(pdf_list):
        base = re.sub(SPLIT_PATTERN, "", pdf, flags=re.IGNORECASE)
        base = re.sub(r"-+\.", ".", base)
        base = re.sub(r"-+", "-", base).strip("-")
        if base not in groups:
            groups[base] = []
        groups[base].append(pdf)
    return groups


def search_in_pdf(pdf_path: str, variants: list):
    found_pages = []
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text("text")
            for v in variants:
                if v in text:
                    found_pages.append(page_num + 1)
                    break
        doc.close()
    except Exception as e:
        pass  # PDF ilegible — se reporta como sin texto
    return found_pages


def ocr_command(pdf_path: str) -> str:
    name = os.path.basename(pdf_path)
    stem, ext = os.path.splitext(name)
    out_name = f"{stem}_OCR{ext}"
    folder = os.path.dirname(pdf_path)
    out_path = os.path.join(folder, out_name)
    return f'py -m ocrmypdf -l spa+eng --force-ocr "{pdf_path}" "{out_path}"'


def format_link(pdf_name: str, page: int) -> str:
    return f"[[{pdf_name}#page={page}]]"


def copy_to_clipboard(text: str):
    try:
        # Here-string de PowerShell con @' '@ — maneja apóstrofes y caracteres especiales
        ps = f"@'\r\n{text}\r\n'@ | Set-Clipboard"
        subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps],
            check=True,
            capture_output=True
        )
        return True
    except Exception:
        return False


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    # Argumentos desde Shell Commands
    if len(sys.argv) < 3:
        error = "[pdf_figure_search] Faltan argumentos: sigla y etiqueta."
        print(error, file=sys.stderr)
        sys.exit(1)

    sigla  = sys.argv[1].strip()
    label  = sys.argv[2].strip()

    # 1. Carpeta de PDFs
    folder = get_pdf_folder(sigla)
    if not folder:
        disponibles = ', '.join(os.listdir(PDF_ROOT))
        print(f"[pdf_figure_search] Carpeta '{sigla}' no encontrada. Disponibles: {disponibles}", file=sys.stderr)
        sys.exit(1)

    # 2. Variantes de búsqueda
    variants, num = build_variants(label)

    # 3. PDFs y grupos
    pdf_list = list_pdfs(folder)
    if not pdf_list:
        print(f"[pdf_figure_search] No hay PDFs en {folder}", file=sys.stderr)
        sys.exit(1)

    groups = group_split_pdfs(pdf_list)

    # 4. Buscar
    results  = []   # (pdf_file, page)
    no_text  = []   # (base_name, [parts])

    for base_name, parts in groups.items():
        group_found = []
        for part in parts:
            pdf_path = os.path.join(folder, part)
            pages = search_in_pdf(pdf_path, variants)
            for p in pages:
                group_found.append((part, p))
        if not group_found:
            no_text.append((base_name, parts))
        else:
            results.extend(group_found)

    # 5. Construir salida
    lines = []

    if results:
        lines.append(f"> Figura {num} — empezá por la última coincidencia de cada grupo.")
        lines.append("")
        for pdf_file, page in results:
            lines.append(format_link(pdf_file, page))
        lines.append("")

    if no_text:
        lines.append("> No encontrado en los siguientes PDFs (posiblemente sin capa de texto):")
        lines.append("")
        for base_name, parts in no_text:
            for part in parts:
                pdf_path = os.path.join(folder, part)
                lines.append(f"[[{part}]]")
                lines.append(f"```sh")
                lines.append(ocr_command(pdf_path))
                lines.append(f"```")
                lines.append("")
        lines.append("> Corré el comando en shell, luego volvé a ejecutar el script.")

    output = "\n".join(lines)

    # 6. Copiar al portapapeles
    ok = copy_to_clipboard(output)

    # 7. Notificación stdout (Shell Commands puede mostrarlo o ignorarlo)
    if ok:
        print(f"OK: Figura {num} - {len(results)} resultado(s) copiados al portapapeles.")
    else:
        print(output)


if __name__ == "__main__":
    main()
