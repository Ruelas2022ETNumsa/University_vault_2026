import sys
import os
import re
import json
import shutil
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# Argumentos
# ---------------------------------------------------------------------------
# Uso: main.py <nombre_excalidraw> <vault_path>
# Ejemplo: main.py "Prueba_anki.excalidraw" "E:\University_vault_2026"

if len(sys.argv) < 3:
    print("Error: se necesitan 2 argumentos — nombre_excalidraw y vault_path", file=sys.stderr)
    sys.exit(1)

excalidraw_name = sys.argv[1].strip()
vault_path = sys.argv[2].strip()

occlusions_dir = os.path.join(vault_path, "Excalidraw", "Image-Occlusions")

# ---------------------------------------------------------------------------
# Buscar carpetas con ese nombre base
# ---------------------------------------------------------------------------
if not os.path.isdir(occlusions_dir):
    print(f"Error: no se encontró la carpeta {occlusions_dir}", file=sys.stderr)
    sys.exit(1)

prefix = excalidraw_name + "__"
carpetas = [
    d for d in os.listdir(occlusions_dir)
    if d.startswith(prefix) and os.path.isdir(os.path.join(occlusions_dir, d))
]

if len(carpetas) == 0:
    print(f"No se encontraron carpetas para '{excalidraw_name}'.", file=sys.stderr)
    sys.exit(1)

if len(carpetas) == 1:
    print(f"Solo hay una carpeta para '{excalidraw_name}' — nada que borrar.")
    sys.exit(0)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
ID_PATTERN = re.compile(r'<!--ID:\s*(\d+)\s*-->')

def get_ids_from_folder(folder_path):
    """Extrae todos los <!--ID: N--> de los .md de una carpeta (excluye batch-marker)."""
    ids = []
    for fname in os.listdir(folder_path):
        if fname.endswith(".md") and fname != "batch-marker.md":
            fpath = os.path.join(folder_path, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            found = ID_PATTERN.findall(content)
            ids.extend([int(i) for i in found])
    return ids

def folder_has_unsynced_md(folder_path):
    """True si algún .md (excepto batch-marker) NO tiene <!--ID:-->."""
    for fname in os.listdir(folder_path):
        if fname.endswith(".md") and fname != "batch-marker.md":
            fpath = os.path.join(folder_path, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            if not ID_PATTERN.search(content):
                return True
    return False

def get_folder_timestamp(folder_name):
    """Extrae el timestamp del nombre de carpeta para ordenar. Formato: nombre__YYYY-MM-DD HH.MM.SS"""
    parts = folder_name.split("__")
    if len(parts) >= 2:
        return parts[-1]
    return folder_name

def anki_delete_notes(note_ids):
    """Llama a AnkiConnect deleteNotes. Devuelve (ok, mensaje)."""
    payload = json.dumps({
        "action": "deleteNotes",
        "version": 6,
        "params": {"notes": note_ids}
    }).encode("utf-8")
    req = urllib.request.Request(
        "http://127.0.0.1:8765",
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("error"):
                return False, f"AnkiConnect error: {result['error']}"
            return True, None
    except urllib.error.URLError:
        return False, "Anki no esta abierto o AnkiConnect no responde en localhost:8765"

# ---------------------------------------------------------------------------
# Determinar qué conservar y qué borrar
# ---------------------------------------------------------------------------
carpetas_full = {c: os.path.join(occlusions_dir, c) for c in carpetas}
carpetas_sorted = sorted(carpetas, key=get_folder_timestamp)  # ascendente — última es la más reciente

# Caso A: alguna carpeta tiene .md sin ID → esa es la nueva, conservarla
carpeta_conservar = None
for c in carpetas_sorted:
    if folder_has_unsynced_md(carpetas_full[c]):
        carpeta_conservar = c
        break

# Caso B: todas tienen ID → conservar la más reciente
if carpeta_conservar is None:
    carpeta_conservar = carpetas_sorted[-1]

carpetas_borrar = [c for c in carpetas if c != carpeta_conservar]

# ---------------------------------------------------------------------------
# Borrar de Anki y del vault
# ---------------------------------------------------------------------------
total_ids_borrados = 0
errores = []

for c in carpetas_borrar:
    fpath = carpetas_full[c]
    ids = get_ids_from_folder(fpath)

    if ids:
        ok, msg = anki_delete_notes(ids)
        if ok:
            total_ids_borrados += len(ids)
        else:
            errores.append(f"{c}: {msg}")
            # Si Anki no responde, detenemos todo — no borrar carpeta sin confirmar borrado en Anki
            print(f"Error al borrar notas de Anki: {msg}", file=sys.stderr)
            sys.exit(1)

    shutil.rmtree(fpath)

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
if errores:
    print(f"Completado con errores: {'; '.join(errores)}", file=sys.stderr)
else:
    msg_parts = [
        f"OK Image Occlusion Reset",
        f"Conservada: {carpeta_conservar}",
        f"Carpetas borradas: {len(carpetas_borrar)}",
        f"Notas eliminadas de Anki: {total_ids_borrados}",
    ]
    sys.stdout.buffer.write((" | ".join(msg_parts) + "\n").encode("utf-8"))
