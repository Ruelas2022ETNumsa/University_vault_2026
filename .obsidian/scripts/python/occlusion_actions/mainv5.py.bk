# ===========================================================================
# occlusion_actions — main.py
# ---------------------------------------------------------------------------
# PROPOSITO:
#   Gestiona las carpetas de Image Occlusion de un excalidraw dado.
#   Tres acciones disponibles via argumento:
#
#   B — Borrar: elimina todas las carpetas nombre__timestamp del vault,
#       borra las notas en Anki via AnkiConnect, elimina decks si quedaron
#       vacios y limpia tags huerfanos.
#
#   S — Legacy: archiva todas las carpetas y el .excalidraw.md en
#       Excalidraw/Image-Occlusions/_legacy/nombre/. No toca Anki.
#
#   Z — Revisar: restaura el contenido de _legacy/nombre/ de vuelta a
#       Excalidraw/Image-Occlusions/. No toca Anki.
#
#   otro — Cancelar: sale sin modificar nada.
#
# USO:
#   main.py <nombre_excalidraw> <vault_path> <accion>
#   Ejemplo: main.py "Prueba_anki" "E:\University_vault_2026" "B"
#
# DEPENDENCIAS (solo accion B):
#   - AnkiConnect activo en localhost:8765
#   - Anki abierto al momento de ejecutar
#
# CONFIGURADO EN:
#   Obsidian Shell Commands — prompt Occlusion Actions
#   Variables: {{_excalidraw_name}}, {{vault_path}}, {{_occlusion_action}}
# ===========================================================================

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
    print("Operacion cancelada")
    sys.exit(0)

# ---------------------------------------------------------------------------
# Validar directorio base
# ---------------------------------------------------------------------------
if not os.path.isdir(occlusions_dir):
    print(f"Error: no se encontro la carpeta {occlusions_dir}", file=sys.stderr)
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

DECK_PATTERN = re.compile(r'^TARGET DECK:\s*(.+)$', re.MULTILINE)
TAG_PATTERN  = re.compile(r'^FILE TAGS:\s*(.+)$',   re.MULTILINE)

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

def get_deck_tag_from_folder(folder_path):
    """Lee el primer .md (excluye batch-marker) y extrae TARGET DECK y FILE TAGS."""
    for fname in sorted(os.listdir(folder_path)):
        if fname.endswith(".md") and fname != "batch-marker.md":
            fpath = os.path.join(folder_path, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            deck = DECK_PATTERN.search(content)
            tag  = TAG_PATTERN.search(content)
            return (
                deck.group(1).strip() if deck else None,
                tag.group(1).strip()  if tag  else None
            )
    return None, None

def anki_request(action, **params):
    """Llamada genérica a AnkiConnect. Devuelve result o None si hay error."""
    payload = json.dumps({
        "action": action,
        "version": 6,
        "params": params
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
                return None
            return result.get("result")
    except urllib.error.URLError:
        return None

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

    # Recorrer carpetas — acumular IDs, decks y tags únicos
    registro = {"ids": [], "decks": set(), "tags": set()}
    for c in carpetas:
        fpath = os.path.join(occlusions_dir, c)
        registro["ids"].extend(get_ids_from_folder(fpath))
        deck, tag = get_deck_tag_from_folder(fpath)
        if deck:
            registro["decks"].add(deck)
        if tag:
            registro["tags"].add(tag)

    # Si hay IDs, Anki debe estar abierto — borrar notas
    if registro["ids"]:
        ok, msg = anki_delete_notes(registro["ids"])
        if not ok:
            print(f"Error: {msg} — operacion detenida, no se borro nada.", file=sys.stderr)
            sys.exit(1)

    # Borrar carpetas del vault
    for c in carpetas:
        shutil.rmtree(os.path.join(occlusions_dir, c))

    # Verificar decks — borrar solo si quedaron vacíos
    decks_borrados = []
    for deck in registro["decks"]:
        cards = anki_request("findCards", query=f'deck:"{deck}"')
        if cards is not None and len(cards) == 0:
            anki_request("deleteDecks", decks=[deck], cardsToo=True)
            decks_borrados.append(deck)

    # Verificar tags — cuales quedaron vacios
    tags_borrados = []
    for tag in registro["tags"]:
        notes = anki_request("findNotes", query=f'tag:{tag}')
        if notes is not None and len(notes) == 0:
            tags_borrados.append(tag)

    # Limpiar tags huerfanos
    anki_request("clearUnusedTags")

    sys.stdout.buffer.write((
        f"'{excalidraw_name}' eliminado \n"
        f"Carpetas: {len(carpetas)} \n"
        f"cartas Anki: {len(registro['ids'])} \n"
        f"Decks borrados: {decks_borrados if decks_borrados else 'ninguno'} \n"
        f"Tags borrados: {tags_borrados if tags_borrados else 'ninguno'}"
        f"\n"
    ).encode("utf-8"))

# ---------------------------------------------------------------------------
# Accion S — Legacy (archivar)
# ---------------------------------------------------------------------------
elif accion == "S":
    carpetas = get_carpetas(excalidraw_name)

    if not carpetas:
        print(f"No se encontraron carpetas para '{excalidraw_name}'.", file=sys.stderr)
        sys.exit(1)

    # Clasificar carpetas: con IDs (exportadas) y sin IDs (no exportadas)
    con_ids = []
    sin_ids = []
    for c in carpetas:
        fpath = os.path.join(occlusions_dir, c)
        ids = get_ids_from_folder(fpath)
        if ids:
            con_ids.append(c)
        else:
            sin_ids.append(c)

    # Si ninguna fue exportada a Anki — bloquear
    if not con_ids:
        print(f"'{excalidraw_name}' aun no fue exportado a Anki — legacy cancelado.", file=sys.stderr)
        sys.exit(1)

    destino_base = os.path.join(legacy_dir, excalidraw_name)
    os.makedirs(destino_base, exist_ok=True)

    # Mover solo carpetas con IDs — sobreescribir si ya existe en legacy
    for c in con_ids:
        src = os.path.join(occlusions_dir, c)
        dst = os.path.join(destino_base, c)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.move(src, dst)

    # Mover .excalidraw.md si existe
    excalidraw_file = find_excalidraw_file(excalidraw_name)
    if excalidraw_file:
        dst_file = os.path.join(destino_base, os.path.basename(excalidraw_file))
        shutil.move(excalidraw_file, dst_file)

    # Armar mensaje
    msg = f"'{excalidraw_name}' archivado en legacy | Carpetas: {len(con_ids)}"
    if sin_ids:
        msg += f" | Sin exportar (no archivadas): {sin_ids}"
    sys.stdout.buffer.write((msg + "\n").encode("utf-8"))

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
