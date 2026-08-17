"""
pdf_figure_search/main.py  v2  —  2026-08-17
==============================================
Busca una etiqueta de figura en los PDFs de una materia y devuelve
una lista de links PDF++ ordenados por proximidad al numero de pagina
indicado por NotebookLM. El resultado se copia al portapapeles listo
para pegar en Obsidian.

Contexto
--------
NotebookLM entrega referencias de figuras en formato:
    [[nombre.pdf#page=N]]
    *Fig. 2-1*
El page=N es el numero impreso en el libro, que puede tener desfase
respecto al numero real del visor PDF++ (portada, indice, etc.).
El script resuelve ese desfase devolviendo los 3 candidatos mas
cercanos ordenados por error minimo.

Uso
---
  py main.py <sigla> <nblm_ref> [etiqueta]

  sigla     — carpeta en _PDF (ej: ETN607 o ETN-607)  [obligatorio]
  nblm_ref  — bloque pegado desde NotebookLM (multiline) [obligatorio]
              Formato esperado:
                [[Dare A. Wells.pdf#page=11]]
                *Fig. 2-1*
  etiqueta  — fallback si nblm_ref no trae etiqueta (ej: "Fig. 2-4") [opcional]

Logica
------
  1. Parsea nblm_ref: extrae nombre del PDF, etiqueta (ignora asteriscos
     de italics) y hint_page (numero de pagina del link).
  2. Localiza la carpeta del PDF en _PDF/ segun la sigla.
  3. Agrupa PDFs partidos (-1to9, -10to16) bajo su nombre base.
  4. Genera 6 variantes de busqueda: Fig./fig./Figure/Figura con y sin punto.
  5. Busca en cada pagina del PDF con PyMuPDF.
  6. Calcula error = |pagina_visor - hint_page| y toma top 3.
  7. Copia resultado al portapapeles via PowerShell Here-String.
  Si el PDF no tiene capa de texto: reporta el PDF e incluye el
  comando ocrmypdf listo para correr en shell.

Dependencias
------------
  PyMuPDF   — pip install pymupdf      (busqueda de texto en PDF)
  ocrmypdf  — pip install ocrmypdf     (solo si hay PDFs sin OCR)
  Tesseract — winget + tessdata spa    (motor OCR, requerido por ocrmypdf)

Configuracion
-------------
  VAULT_PATH    — ruta absoluta del vault (modificar si cambia)
  PDF_ROOT      — _PDF/ dentro del vault
  SPLIT_PATTERN — regex para detectar sufijos de PDFs partidos

Doc: E:/University_vault_2026/_app/shellcommands/shellcmd_pdf_figure_search.md
"""

import os
import re
import sys
import subprocess

try:
    import pymupdf as fitz
except ImportError:
    print("PyMuPDF no instalado. Ejecuta: py -m pip install pymupdf")
    sys.exit(1)

# ── Configuracion ─────────────────────────────────────────────────────────────

VAULT_PATH    = r"E:\University_vault_2026"
PDF_ROOT      = os.path.join(VAULT_PATH, "_PDF")
SPLIT_PATTERN = r"-\d+to\d+"


# ── Parseo de referencia NotebookLM ──────────────────────────────────────────

def parse_nblm_ref(ref: str):
    """
    Extrae (pdf_name, label, hint_page) desde el bloque pegado de NotebookLM.

    Formato soportado (v2):
      [[Dare A. Wells.pdf#page=11]]
      *Fig. 2-1*

    Los asteriscos de italics son ignorados al extraer la etiqueta.
    Retorna (pdf_name, label, hint_page) — hint_page puede ser None.
    """
    ref = ref.strip()
    if not ref:
        return None, None, None

    pdf_name  = None
    label     = None
    hint_page = None

    # Extraer nombre de PDF y page hint desde [[ ]] con #page=N
    pdf_match = re.search(r'\[\[([^\]]+\.pdf)(?:#page=(\d+))?\]\]', ref)
    if pdf_match:
        pdf_name = pdf_match.group(1).strip()
        if pdf_match.group(2):
            hint_page = int(pdf_match.group(2))

    # Extraer etiqueta — ignora asteriscos de italics Markdown
    label_match = re.search(
        r'\*{0,2}(Fig\.?\s*\d[\d\-\.]*|fig\.?\s*\d[\d\-\.]*|Figure\s*\d[\d\-\.]*|Figura\s*\d[\d\-\.]*)\*{0,2}',
        ref
    )
    if label_match:
        label = label_match.group(1).strip()

    return pdf_name, label, hint_page


# ── Funciones generales ───────────────────────────────────────────────────────

def build_variants(label: str):
    """Genera todas las variantes de busqueda a partir de la etiqueta."""
    num = re.sub(r'^(figura|figure|fig\.?)\s*', '', label.strip(), flags=re.IGNORECASE).strip()
    variants = [
        f"Fig. {num}",
        f"Fig {num}",
        f"fig. {num}",
        f"fig {num}",
        f"Figure {num}",
        f"Figura {num}",
    ]
    return variants, num


def get_pdf_folder(sigla: str):
    """Busca la carpeta en _PDF que coincida con la sigla."""
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
    """Agrupa PDFs partidos (1to9, 10to16) bajo su nombre base."""
    groups = {}
    for pdf in sorted(pdf_list):
        base = re.sub(SPLIT_PATTERN, "", pdf, flags=re.IGNORECASE)
        base = re.sub(r"-+\.", ".", base)
        base = re.sub(r"-+", "-", base).strip("-")
        if base not in groups:
            groups[base] = []
        groups[base].append(pdf)
    return groups


def find_parts_for_pdf(pdf_name: str, groups: dict):
    """
    Dado un nombre de PDF (que puede o no tener sufijo -1to9 etc.),
    devuelve la lista de archivos reales donde buscar.
    Busqueda case-insensitive y tolerante al sufijo de particion.
    """
    name_lower = pdf_name.lower()

    # Coincidencia exacta primero
    for base, parts in groups.items():
        for part in parts:
            if part.lower() == name_lower:
                return parts

    # Coincidencia por nombre base (sin sufijo)
    name_stripped = re.sub(SPLIT_PATTERN, "", name_lower, flags=re.IGNORECASE)
    name_stripped = re.sub(r"-+\.", ".", name_stripped)
    name_stripped = re.sub(r"-+", "-", name_stripped).strip("-")

    for base, parts in groups.items():
        base_lower = base.lower()
        if base_lower == name_stripped or name_stripped in base_lower:
            return parts

    return None


def search_in_pdf(pdf_path: str, variants: list):
    """Busca variantes en el PDF. Retorna lista de paginas (1-indexed)."""
    found_pages = []
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            text = doc[page_num].get_text("text")
            for v in variants:
                if v in text:
                    found_pages.append(page_num + 1)
                    break
        doc.close()
    except Exception:
        pass
    return found_pages


def rank_by_proximity(pages: list, hint: int, top: int = 3):
    """
    Ordena las paginas por proximidad al hint (numero impreso de NotebookLM).
    Retorna los `top` candidatos con su error:
    [(page, error), ...]
    """
    scored = sorted(set(pages), key=lambda p: abs(p - hint))
    return [(p, abs(p - hint)) for p in scored[:top]]


def ocr_command(pdf_path: str) -> str:
    name   = os.path.basename(pdf_path)
    stem, ext = os.path.splitext(name)
    out_path  = os.path.join(os.path.dirname(pdf_path), f"{stem}_OCR{ext}")
    return f'py -m ocrmypdf -l spa+eng --force-ocr "{pdf_path}" "{out_path}"'


def format_link(pdf_name: str, page: int) -> str:
    return f"[[{pdf_name}#page={page}]]"


def copy_to_clipboard(text: str):
    try:
        ps = f"@'\r\n{text}\r\n'@ | Set-Clipboard"
        subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps],
            check=True, capture_output=True
        )
        return True
    except Exception:
        return False


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 3:
        print("[pdf_figure_search] Uso: py main.py <sigla> <nblm_ref> [etiqueta]", file=sys.stderr)
        sys.exit(1)

    sigla    = sys.argv[1].strip()
    nblm_ref = sys.argv[2].strip()
    label    = sys.argv[3].strip() if len(sys.argv) > 3 else ""

    # ── Parseo del bloque NLM ─────────────────────────────────────────────────
    target_pdf = None
    hint_page  = None

    parsed_pdf, parsed_label, parsed_page = parse_nblm_ref(nblm_ref)

    if parsed_pdf:
        target_pdf = parsed_pdf
    if parsed_page:
        hint_page = parsed_page
    if parsed_label:
        label = parsed_label  # etiqueta extraida del bloque tiene prioridad

    if not nblm_ref:
        print("[pdf_figure_search] Falta la referencia NotebookLM (D3).", file=sys.stderr)
        sys.exit(1)

    if not label:
        print("[pdf_figure_search] No se pudo extraer la etiqueta del bloque NLM. Verificar formato.", file=sys.stderr)
        sys.exit(1)

    if not target_pdf:
        print("[pdf_figure_search] No se pudo extraer el nombre del PDF del bloque NLM. Verificar formato.", file=sys.stderr)
        sys.exit(1)

    # ── Carpeta de PDFs ───────────────────────────────────────────────────────
    folder = get_pdf_folder(sigla)
    if not folder:
        disponibles = ', '.join(os.listdir(PDF_ROOT))
        print(f"[pdf_figure_search] Carpeta '{sigla}' no encontrada. Disponibles: {disponibles}", file=sys.stderr)
        sys.exit(1)

    # ── Variantes ─────────────────────────────────────────────────────────────
    variants, num = build_variants(label)

    # ── PDFs a buscar ─────────────────────────────────────────────────────────
    pdf_list = list_pdfs(folder)
    if not pdf_list:
        print(f"[pdf_figure_search] No hay PDFs en {folder}", file=sys.stderr)
        sys.exit(1)

    groups = group_split_pdfs(pdf_list)

    # Modo selectivo — solo el PDF indicado por NotebookLM
    parts = find_parts_for_pdf(target_pdf, groups)
    if not parts:
        print(f"[pdf_figure_search] PDF '{target_pdf}' no encontrado en {folder}.", file=sys.stderr)
        sys.exit(1)
    search_groups = {target_pdf: parts}

    # ── Buscar ────────────────────────────────────────────────────────────────
    results = []   # (pdf_file, page, error)
    no_text = []   # (base_name, [parts])

    for base_name, parts in search_groups.items():
        group_found = []
        for part in parts:
            pdf_path = os.path.join(folder, part)
            pages = search_in_pdf(pdf_path, variants)
            if pages:
                if hint_page is not None:
                    ranked = rank_by_proximity(pages, hint_page, top=3)
                    for p, err in ranked:
                        group_found.append((part, p, err))
                else:
                    for p in pages:
                        group_found.append((part, p, None))
        if not group_found:
            no_text.append((base_name, parts))
        else:
            results.extend(group_found)

    # ── Construir salida ──────────────────────────────────────────────────────
    lines = []

    if hint_page:
        lines.append(f"> Figura {num} en {target_pdf} — top 3 por proximidad a page={hint_page} (NLM)")
    else:
        lines.append(f"> Figura {num} en {target_pdf}")
    lines.append("")

    if results:
        for pdf_file, page, err in results:
            err_str = f"  ← error {err}" if err is not None else ""
            lines.append(f"{format_link(pdf_file, page)}{err_str}")
        lines.append("")

    if no_text:
        lines.append("> No encontrado (posiblemente sin capa de texto):")
        lines.append("")
        for base_name, parts in no_text:
            for part in parts:
                pdf_path = os.path.join(folder, part)
                lines.append(f"[[{part}]]")
                lines.append("```sh")
                lines.append(ocr_command(pdf_path))
                lines.append("```")
                lines.append("")
        lines.append("> Corre el comando en shell, luego vuelve a ejecutar el script.")

    output = "\n".join(lines)

    # ── Portapapeles ──────────────────────────────────────────────────────────
    ok = copy_to_clipboard(output)

    if ok:
        n = len(results)
        hint_str = f" (hint page={hint_page})" if hint_page else ""
        print(f"OK: Figura {num} en {target_pdf}{hint_str} - {n} candidato(s) copiados al portapapeles.")
    else:
        print(output)


if __name__ == "__main__":
    main()
