# =============================================================================
# main.py
# Proyecto : tars-hpprgm-conversion
# Fecha    : 2026-09-05
# Version  : 2 — N funciones EXPORT dinamico (backward compatible v1)
# Estado   : activo
# Notas    : detecta automaticamente todas las funciones EXPORT en el fuente
#            y construye la tabla de exportados con N entradas.
#            Compatible con pruebas 1, 2, 3, 4 y 5.
# =============================================================================
import sys
import os
import re
import struct


def detectar_exports(codigo_utf8):
    """
    Busca todas las funciones EXPORT en el fuente PPL.
    Retorna lista de nombres en el orden en que aparecen.
    Soporta: EXPORT NOMBRE() y EXPORT NOMBRE(args)
    """
    patron = re.compile(r'^\s*EXPORT\s+([A-Za-z][A-Za-z0-9_]*)\s*\(', re.MULTILINE)
    return patron.findall(codigo_utf8)


def build_hpprgm(exports, codigo_utf8):
    """
    Construye el binario .hpprgm para N funciones exportadas.
    exports: lista de nombres de funciones EXPORT (orden del fuente)
    """
    codigo_utf16 = codigo_utf8.encode('utf-16-le')

    # --- Tabla de exportados ---
    # Por cada funcion: 31 00 + nombre UTF-16 LE + 00 00 00 00
    tabla = b''
    for nombre in exports:
        nombre_utf16 = nombre.encode('utf-16-le')
        tabla += bytes([0x31, 0x00]) + nombre_utf16 + bytes([0x00, 0x00, 0x00, 0x00])

    # --- Header blob ---
    header_data = (
        struct.pack('<H', 0)              # 0 variables exportadas
        + struct.pack('<H', 0)            # 0 views
        + struct.pack('<H', len(exports)) # N funciones exportadas
        + bytes(6)                        # 6 bytes opcionales (ceros)
        + tabla
    )
    header_blob = struct.pack('<I', len(header_data)) + header_data

    # --- Source blob ---
    source_data = codigo_utf16 + bytes([0x00, 0x00])
    source_blob = struct.pack('<I', len(source_data)) + source_data

    return header_blob + source_blob


def main():
    if len(sys.argv) < 2:
        print("ERROR: se requiere la ruta del archivo como argumento.")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"ERROR: archivo no encontrado: {file_path}")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        codigo = f.read()

    nombre_archivo = os.path.splitext(os.path.basename(file_path))[0]

    # Detectar funciones EXPORT
    exports = detectar_exports(codigo)

    if not exports:
        print(f"ERROR: no se encontro ninguna funcion EXPORT en {nombre_archivo}")
        sys.exit(1)

    print(f"INFO: {len(exports)} EXPORT(s) detectado(s): {', '.join(exports)}")

    binario = build_hpprgm(exports, codigo)

    # Ruta destino: carpeta HP Prime del usuario actual
    user_documents = os.path.expanduser("~\\Documents")
    destino_dir = os.path.join(user_documents, "HP Prime", "Calculators", "Prime")

    if not os.path.isdir(destino_dir):
        print(f"ERROR: carpeta destino no encontrada: {destino_dir}")
        sys.exit(1)

    destino = os.path.join(destino_dir, nombre_archivo + ".hpprgm")

    with open(destino, 'wb') as f:
        f.write(binario)

    print(f"OK: {nombre_archivo}.hpprgm copiado a CASE ({len(exports)} EXPORT(s))")


if __name__ == "__main__":
    main()
