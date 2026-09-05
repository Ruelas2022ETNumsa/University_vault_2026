import sys
import os
import struct


def build_hpprgm(nombre_programa, codigo_utf8):
    nombre_utf16 = nombre_programa.encode('utf-16-le')
    codigo_utf16 = codigo_utf8.encode('utf-16-le')

    tabla = bytes([0x31, 0x00]) + nombre_utf16 + bytes([0x00, 0x00, 0x00, 0x00])

    header_data = (
        struct.pack('<H', 0)
        + struct.pack('<H', 0)
        + struct.pack('<H', 1)
        + bytes(6)
        + tabla
    )
    header_blob = struct.pack('<I', len(header_data)) + header_data

    source_data = codigo_utf16 + bytes([0x00, 0x00])
    source_blob = struct.pack('<I', len(source_data)) + source_data

    return header_blob + source_blob


def main():
    if len(sys.argv) < 2:
        print("Uso: python test_conversion.py <ruta_archivo.hpprgm>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print("Archivo no encontrado: " + file_path)
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        codigo = f.read()

    nombre = os.path.splitext(os.path.basename(file_path))[0]

    print("Convirtiendo: " + nombre + ".hpprgm")
    print("Fuente: " + str(len(codigo)) + " caracteres")

    binario = build_hpprgm(nombre, codigo)
    print("Binario generado: " + str(len(binario)) + " bytes")

    carpeta_destino = r"C:\Users\USUARIO\Documents\HP Prime\Calculators\Prime"
    destino = os.path.join(carpeta_destino, nombre + ".hpprgm")

    if not os.path.isdir(carpeta_destino):
        print("Carpeta destino no encontrada: " + carpeta_destino)
        sys.exit(1)

    with open(destino, 'wb') as f:
        f.write(binario)

    print("Escrito en: " + destino)
    print("Abri CASE y verifica si KMH_CONV aparece y carga correctamente.")


if __name__ == "__main__":
    main()
