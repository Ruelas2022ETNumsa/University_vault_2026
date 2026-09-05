---
galaxy_body: dropship
carrier: "[[_app/Tars/work/tars_conversion/tsk_carrier.md]]"
scope: opcion-A
status: activo
date: 2026-09-04
---

## Proposito

Documentar y probar la Opción A del carrier `tars-hpprgm-conversion` — construir el archivo `.hpprgm` en formato moderno directamente desde Python, sin depender de un archivo existente como plantilla.

---

## Contenido

### Concepto

Python lee el fuente `.hpprgm` guardado en Obsidian como texto plano UTF-8, arma el header binario con nombre (formato "named"), codifica el contenido en UTF-16 LE y escribe el archivo resultante en `HP Prime\Calculators\Prime`. CASE lo detecta y carga sin pasos adicionales.

---

### Hallazgo clave — Cyrille (ingeniero de HP, Omnimaga 2014)

Fuente: https://www.omnimaga.org/hp-prime/the-hpprgm-format/

Cyrille (del equipo HP) confirmó que:
> "a lot of the data in the header is optional, you can send a program without its variables or any of the exported data info, put the source nevertheless and, once on the calculator, open, add a space and exit to compile"

Y la estructura general es:
```
[header blob] [variable value blobs x N] [source blob — siempre el último]
```

El source siempre es el último blob. Los blobs de variables son opcionales. Para nuestro caso (solo fuente sin variables exportadas), el archivo puede ser mínimo.

---

### Estructura del blob (formato general)

Cada blob sigue el patrón:
```
[tamaño del blob — 4 bytes LE, excluye a sí mismo] [datos del blob]
```

### Estructura detallada del header blob (Hasse, Omnimaga 2014)

```
0x0000-0x0003  tamaño del header (excluye estos 4 bytes)
0x0004-0x0005  cantidad de variables exportadas
0x0006-0x0007  cantidad de algo (¿views?)
0x0008-0x0009  cantidad de funciones exportadas
0x000A-0x000F  bytes opcionales — Connectivity Kit genera: 7F 01 00 00 00 00
               pero todo ceros también funciona
0x0010-...     tabla de ítems exportados:
               - 30 00 = variable
               - 31 00 = función exportada
               seguido del nombre en UTF-16 LE terminado en 00 00 00 00
```

### Estructura del source blob

```
[tamaño — 4 bytes LE] [código fuente en UTF-16 LE hasta 00 00]
```

### Estructura mínima viable para un programa simple (sin variables)

Para un programa como `KMH_CONV` sin variables exportadas (solo `EXPORT KMH_CONV()`):

```
HEADER BLOB:
  4 bytes: tamaño del header (sin contar estos 4 bytes)
  2 bytes: 00 00  (0 variables)
  2 bytes: 00 00  (0 views)
  2 bytes: 01 00  (1 función exportada)
  6 bytes: 00 00 00 00 00 00  (opcionales, todo ceros)
  --- tabla exportados ---
  2 bytes: 31 00  (función exportada)
  N bytes: nombre en UTF-16 LE  (ej. "KMH_CONV")
  4 bytes: 00 00 00 00  (fin de nombre)

SOURCE BLOB:
  4 bytes: tamaño del source (sin contar estos 4 bytes)
  N bytes: código fuente en UTF-16 LE
  2 bytes: 00 00  (fin)
```

### Referencias

| Fuente | URL | Qué aporta |
| ------ | --- | ---------- |
| Omnimaga — The .hpprgm format | https://www.omnimaga.org/hp-prime/the-hpprgm-format/ | Estructura completa del header + confirmación de cyrille (HP) de que los blobs de variables son opcionales |
| TI-Planet Wiki | https://wiki.tiplanet.org/HP_Prime/File_Format | Estructura del formato named (bytes 0-15 + flag) |
| PrimeComm — PrimeUsbFile.cs | https://github.com/eried/PrimeLib/PrimeUsbFile.cs | Implementación C# de referencia |
| Gist fakuivan | https://gist.github.com/fakuivan/ee66d88e8b7f42fa4e148c4b9e92c1d8 | Script Python que decodifica el source blob leyendo UTF-16 LE |

### Implementación propuesta (Python puro, sin dependencias)

```python
import sys
import os
import struct

def build_hpprgm(nombre_programa, codigo_utf8):
    # Codificar nombre y código en UTF-16 LE
    nombre_utf16 = nombre_programa.encode('utf-16-le')
    codigo_utf16 = codigo_utf8.encode('utf-16-le')

    # --- Tabla de exportados ---
    # 31 00 = función exportada + nombre + 00 00 00 00
    tabla = bytes([0x31, 0x00]) + nombre_utf16 + bytes([0x00, 0x00, 0x00, 0x00])

    # --- Header blob ---
    # 2 bytes variables + 2 bytes views + 2 bytes funciones exportadas + 6 bytes opcionales + tabla
    header_data = (
        struct.pack('<H', 0)      # 0 variables
        + struct.pack('<H', 0)    # 0 views
        + struct.pack('<H', 1)    # 1 función exportada
        + bytes(6)                # 6 bytes opcionales (ceros)
        + tabla
    )
    header_blob = struct.pack('<I', len(header_data)) + header_data

    # --- Source blob ---
    source_data = codigo_utf16 + bytes([0x00, 0x00])
    source_blob = struct.pack('<I', len(source_data)) + source_data

    return header_blob + source_blob


def main():
    file_path = sys.argv[1]

    # Leer fuente
    with open(file_path, 'r', encoding='utf-8') as f:
        codigo = f.read()

    # Nombre del programa = nombre del archivo sin extensión
    nombre = os.path.splitext(os.path.basename(file_path))[0]

    # Construir binario
    binario = build_hpprgm(nombre, codigo)

    # Ruta destino
    destino = os.path.join(
        r"C:\Users\USUARIO\Documents\HP Prime\Calculators\Prime",
        nombre + ".hpprgm"
    )

    with open(destino, 'wb') as f:
        f.write(binario)

    print(f"Copiado a CASE: {nombre}.hpprgm")


if __name__ == "__main__":
    main()
```

### Preguntas abiertas resueltas

- ✅ ¿Los blobs de variables son obligatorios? **No** — cyrille (HP) lo confirmó
- ✅ ¿El source es siempre el último blob? **Sí**
- ⬜ ¿El nombre en la tabla de exportados debe coincidir con el del `EXPORT NombrePrograma()`? Por verificar con prueba real
- ⬜ ¿El fin de nombre es siempre `00 00 00 00` (4 bytes) o `00 00` (2 bytes)? La documentación de Hasse dice 4 bytes — verificar

### Resultados de prueba

- [x] Prueba 1 — `KMH_CONV.hpprgm` (programa existente con código real): **EXITOSO** — CASE lo reconoció y ejecutó correctamente. Output visible en terminal de CASE.
- [ ] Prueba 2 — archivo nuevo nunca cargado en CASE: pendiente

### Veredicto

**APROBADO (parcial)** — 2026-09-04. El binario generado por Python es reconocido y ejecutable por CASE sin pasos adicionales.

> [!note] Contexto de la prueba
> La prueba se realizó desde consola (PowerShell) pasando la ruta del archivo como argumento. El flujo final previsto es distinto: el script se activaría desde Obsidian vía Shell Commands + Commander, tomando el archivo activo con `{{file_path:absolute}}`. Esa integración es viable pero aún no probada.

**Candidato para integración futura con Shell Commands + Commander.**
Pendiente antes de cerrar:
- [ ] Prueba 2 — archivo nuevo nunca cargado en CASE
- [ ] Pruebas con otros tipos de contenido (variables exportadas, múltiples funciones)
- [ ] Prueba end-to-end desde Obsidian vía Shell Commands
