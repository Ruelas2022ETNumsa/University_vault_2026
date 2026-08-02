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
# Uso: main.py <nombre_excalidraw> <vault_path> <accion>
# Ejemplo: main.py "Prueba_anki.excalidraw" "E:\University_vault_2026" "B"

if len(sys.argv) < 4:
    print("Error: se necesitan 3 argumentos — nombre_excalidraw, vault_path, accion", file=sys.stderr)
    sys.exit(1)

excalidraw_name = sys.argv[1].strip()
vault_path      = sys.argv[2].strip()
accion          = sys.argv[3].strip().upper()

occlusions_dir = os.path.join(vault_path, "Excalidraw", "Image-Occlusions")
legacy_dir     = os.path.join(occlusions_dir, "_legacy")

# ---------------------------------------------------------------------------
# Cancelar
# ---------------------------------------------------------------------------
if accion not in ("B", "S", "Z"):
    print("Operación cancelada")
    sys.exit(0)

# ---------------------------------------------------------------------------
# Validar directorio base
# ---------------------------------------------------------------------------
if not os.path.isdir(occlusions_dir):
    print(f"Error: no se encontró la carpeta {occlusions_dir}", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
ID_PATTERN = re.compile(r'<!--ID:\s*(\d+)\s*-->')

def get_carpetas(nombre):
    """Devuelve todas las carpetas de Image-Occlusions que empiecen con nombre__"""
    prefix = nombre + "__"
    return [
        d for d in os.listdir(occlusions_dir)
        if d.startswith(prefix) and os.path.isdir(os.path.join(occlusions_dir, d))
        and not d.startswith(os.path.join(occlusions_dir, "_legacy"))
    ]

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
        return False, "Anki no está abierto o AnkiConnect no responde en localhost:8765"

def find_excalidraw_file(nombre):
    """
    Busca el .excalidraw.md del nombre dado.
    Primero en Excalidraw/Image-Occlusions/, fallback en Excalidraw/.
    Devuelve la ruta completa o None.
    """
    candidato = nombre + ".excalidraw.md"

    ruta1 = os.path.join(occlusions_dir, candidato)
    if os.path.isfile(ruta1):
        return ruta1

    ruta2 = os.path.join(vault_path, "Excalidraw", candidato)
    if os.path.isfile(ruta2):
        return ruta2

    return None

# ---------------------------------------------------------------------------
# Accion B — Borrar todo
# ---------------------------------------------------------------------------
if accion == "B":
    carpetas = get_carpetas(excalidraw_name)

    if not carpetas:
        print(f"No se encontraron carpetas para '{excalidraw_name}'.", file=sys.stderr)
        sys.exit(1)

    # Recolectar todos los IDs primero
    todos_ids = []
    for c in carpetas:
        todos_ids.extend(get_ids_from_folder(os.path.join(occlusions_dir, c)))

    # Si hay IDs, Anki debe estar abierto
    if todos_ids:
        ok, msg = anki_delete_notes(todos_ids)
        if not ok:
            print(f"Error: {msg} — operación detenida, no se borró nada.", file=sys.stderr)
            sys.exit(1)

    # Borrar carpetas del vault
    for c in carpetas:
        shutil.rmtree(os.path.join(occlusions_dir, c))

    sys.stdout.buffer.write(
        f"Tarjetas de '{excalidraw_name}' eliminadas de Anki y vault | "
        f"Carpetas: {len(carpetas)} | Notas Anki: {len(todos_ids)}\n".encode("utf-8")
    )

# ---------------------------------------------------------------------------
# Accion S — Legacy (archivar)
# ---------------------------------------------------------------------------
elif accion == "S":
    carpetas = get_carpetas(excalidraw_name)

    if not carpetas:
        print(f"No se encontraron carpetas para '{excalidraw_name}'.", file=sys.stderr)
        sys.exit(1)

    destino_base = os.path.join(legacy_dir, excalidraw_name)
    os.makedirs(destino_base, exist_ok=True)

    # Mover carpetas de oclusión
    for c in carpetas:
        src = os.path.join(occlusions_dir, c)
        dst = os.path.join(destino_base, c)
        shutil.move(src, dst)

    # Mover .excalidraw.md si existe
    excalidraw_file = find_excalidraw_file(excalidraw_name)
    if excalidraw_file:
        dst_file = os.path.join(destino_base, os.path.basename(excalidraw_file))
        shutil.move(excalidraw_file, dst_file)

    sys.stdout.buffer.write(
        f"'{excalidraw_name}' archivado en legacy\n".encode("utf-8")
    )

# ---------------------------------------------------------------------------
# Accion Z — Revisar (restaurar desde legacy)
# ---------------------------------------------------------------------------
elif accion == "Z":
    origen_base  = os.path.join(legacy_dir, excalidraw_name)

    if not os.path.isdir(origen_base):
        print(f"Archivo no encontrado en legacy: '{excalidraw_name}'", file=sys.stderr)
        sys.exit(1)

    # Mover todo el contenido de _legacy/nombre/ → Image-Occlusions/
    for item in os.listdir(origen_base):
        src = os.path.join(origen_base, item)
        dst = os.path.join(occlusions_dir, item)
        shutil.move(src, dst)

    # Limpiar carpeta legacy vacía
    try:
        os.rmdir(origen_base)
    except OSError:
        pass  # no vacía — no pasa nada

    sys.stdout.buffer.write(
        f"'{excalidraw_name}' restaurado para revisión\n".encode("utf-8")
    )
