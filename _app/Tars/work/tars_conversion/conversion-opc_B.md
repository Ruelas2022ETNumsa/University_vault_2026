---
galaxy_body: dropship
carrier: "[[_app/Tars/work/tars_conversion/tsk_carrier.md]]"
scope: opcion-B
status: activo
date: 2026-09-04
---

## Proposito

Documentar y probar la Opción B del carrier `tars-hpprgm-conversion` — generar el `.hpprgm` en formato G1 (antiguo / "unnamed"), el mismo que usa Xprime. CASE acepta el archivo pero requiere abrir el editor y hacer "Check" una vez para que lo resave al formato moderno.

---

## Contenido

### Concepto

El formato G1 es el formato original del HP Prime, más simple que el moderno. No incluye nombre en el header — solo el tamaño del contenido y el contenido mismo en UTF-16 LE. Xprime (editor macOS para HP Prime) lo usa como formato de exportación.

La calc acepta el archivo, pero al abrirlo en el editor y hacer "Check" (o simplemente abrirlo y salir), la calc lo resave automáticamente al formato moderno. Después corre normalmente.

---

### Estado de la investigación

**Xprime no es open source** — el código fuente no está disponible públicamente. El repo de GitHub (https://github.com/Insoft-UK/Xprime) contiene solo assets, ejemplos y el binario compilado para macOS. No hay acceso a la implementación interna del formato G1.

Lo que sí está documentado es el formato "unnamed" de TI-Planet Wiki, que corresponde al formato G1:

---

### Estructura del formato G1 / "unnamed" (TI-Planet Wiki)

```
Byte 0–7:   0C 00 00 00 00 00 00 00   → type header fijo
Byte 8–15:  00 00 00 00 00 00 00 00   → name flag = 0x00 (unnamed / sin nombre)
Byte 16–19: [tamaño del contenido — 4 bytes LE]
Byte 20+:   [contenido en UTF-16 LE]
```

El flag en byte 8 = `0x00` indica formato unnamed (G1).
El flag en byte 8 = `0x01` indica formato named (moderno — Opción A).

Diferencia clave con la Opción A: no hay tabla de exportados ni nombre en el header. Solo tamaño + contenido.

---

### Implementación propuesta (Python puro)

```python
import sys
import os
import struct


def build_hpprgm_g1(codigo_utf8):
    codigo_utf16 = codigo_utf8.encode('utf-16-le')

    # Header fijo (type)
    header_type = bytes([0x0C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    # Name flag = 0x00 (unnamed)
    header_flag = bytes([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    # Tamaño del contenido (4 bytes LE)
    size = struct.pack('<I', len(codigo_utf16))

    return header_type + header_flag + size + codigo_utf16


def main():
    if len(sys.argv) < 2:
        print("Uso: python test_conversion_b.py <ruta_archivo.hpprgm>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print("Archivo no encontrado: " + file_path)
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        codigo = f.read()

    nombre = os.path.splitext(os.path.basename(file_path))[0]

    print("Convirtiendo (formato G1): " + nombre + ".hpprgm")
    print("Fuente: " + str(len(codigo)) + " caracteres")

    binario = build_hpprgm_g1(codigo)
    print("Binario generado: " + str(len(binario)) + " bytes")

    carpeta_destino = r"C:\Users\USUARIO\Documents\HP Prime\Calculators\Prime"
    destino = os.path.join(carpeta_destino, nombre + ".hpprgm")

    if not os.path.isdir(carpeta_destino):
        print("Carpeta destino no encontrada: " + carpeta_destino)
        sys.exit(1)

    with open(destino, 'wb') as f:
        f.write(binario)

    print("Escrito en: " + destino)
    print("Abri CASE, abre el programa en el editor y hace Check.")
    print("Luego de ese paso deberia correr normalmente.")


if __name__ == "__main__":
    main()
```

---

### Comparación con Opción A

| Aspecto | Opción A (named/moderno) | Opción B (unnamed/G1) |
| ------- | ------------------------ | --------------------- |
| Nombre en header | Sí | No |
| Tabla de exportados | Sí | No |
| Paso manual en CASE | No | Sí (Check una vez) |
| Complejidad del script | Media | Baja |
| Estado | **APROBADO** | Pendiente de prueba |

---

### Referencias

| Fuente | URL | Qué aporta |
| ------ | --- | ---------- |
| Xprime — GitHub | https://github.com/Insoft-UK/Xprime | Confirma que el formato G1 funciona con paso "Check"; código no disponible |
| TI-Planet Wiki — unnamed format | https://wiki.tiplanet.org/HP_Prime/File_Format | Estructura del formato unnamed (G1) — byte 8 = 0x00, size en bytes 16-19 |

---

### Preguntas abiertas

- ¿El header type (`0C 00 00 00 00 00 00 00`) es el mismo que en el formato named? TI-Planet lo indica igual para ambos — verificar con prueba
- ¿El "Check" en CASE es suficiente o hay que ejecutar el programa para que resave al formato moderno?
- ¿Vale la pena probar esta opción dado que la Opción A ya fue aprobada?

---

### Resultados de prueba

- [ ] Prueba 1 — `KMH_CONV.hpprgm` con formato G1: pendiente
- [ ] Prueba 2 — verificar que el paso "Check" en CASE resave al formato moderno: pendiente

### Veredicto

Pendiente. Opción A ya aprobada — esta opción es de menor prioridad salvo que A falle con casos más complejos.
