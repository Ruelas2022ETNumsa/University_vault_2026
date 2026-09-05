---
galaxy_body: dropship
carrier: "[[_app/Tars/work/tars_conversion/tsk_carrier.md]]"
scope: opcion-C
status: activo
date: 2026-09-04
---

## Proposito

Documentar y probar la Opción C del carrier `tars-hpprgm-conversion` — usar un `.hpprgm` real generado por CASE (vía drag and drop) como plantilla binaria, localizar el source blob al final del archivo, y reemplazarlo con el fuente nuevo codificado en UTF-16 LE.

---

## Contenido

### Concepto

En lugar de construir el header desde cero (Opción A), se toma un `.hpprgm` válido generado por CASE como plantilla. Python lee el archivo en binario, localiza donde termina el header y empieza el source (último blob), lo reemplaza con el nuevo fuente en UTF-16 LE, y escribe el archivo resultante.

Garantiza que el header es 100% compatible porque viene de CASE mismo — sin ingeniería inversa adicional.

---

### Análisis de viabilidad

**Lo que ya sabemos (de la investigación de Opciones A y B):**

- El source blob es **siempre el último blob** del archivo (confirmado por cyrille, ingeniero HP)
- Cada blob sigue el patrón: `[tamaño 4 bytes LE][datos]`
- El source blob contiene el código en UTF-16 LE terminado en `00 00`
- El nombre del programa está en el header (formato named) en UTF-16 LE terminado en `00 00 00 00`

**Estrategia de localización del source blob:**

El source blob es el último bloque del archivo. Para encontrarlo sin parsear todo el header:
1. Leer los últimos 4 bytes antes del contenido final no es directo — mejor buscar desde el final
2. Alternativa más robusta: buscar el source leyendo el archivo blob a blob desde el inicio hasta el último

**Estrategia más simple:** buscar el último bloque leyendo el tamaño del source desde atrás. Como el source es UTF-16 LE y sabemos que el contenido del programa empieza con `E` (`45 00` en UTF-16 LE para `EXPORT`), se puede validar.

---

### Lógica de implementación

```python
import sys
import os
import struct


def find_source_offset(data):
    # Recorre los blobs secuencialmente desde el inicio
    # Cada blob: [4 bytes tamaño LE][datos de ese tamaño]
    # El source es el último blob
    offset = 0
    last_blob_offset = None

    while offset < len(data):
        if offset + 4 > len(data):
            break
        size = struct.unpack_from('<I', data, offset)[0]
        if size == 0 or offset + 4 + size > len(data):
            break
        last_blob_offset = offset
        offset += 4 + size

    return last_blob_offset


def reemplazar_source(plantilla_path, nuevo_codigo_utf8, destino_path):
    with open(plantilla_path, 'rb') as f:
        data = bytearray(f.read())

    # Localizar el source blob (ultimo blob)
    source_offset = find_source_offset(data)
    if source_offset is None:
        print("No se pudo localizar el source blob")
        sys.exit(1)

    # Nuevo source en UTF-16 LE + terminador 00 00
    nuevo_source = nuevo_codigo_utf8.encode('utf-16-le') + bytes([0x00, 0x00])
    nuevo_size = struct.pack('<I', len(nuevo_source))

    # Reemplazar desde source_offset hasta el fin del archivo
    nuevo_data = bytes(data[:source_offset]) + nuevo_size + nuevo_source

    with open(destino_path, 'wb') as f:
        f.write(nuevo_data)

    print("Source reemplazado correctamente")
    print("Bytes originales: " + str(len(data)))
    print("Bytes nuevo: " + str(len(nuevo_data)))


def main():
    if len(sys.argv) < 2:
        print("Uso: python test_conversion_c.py <ruta_archivo_fuente.hpprgm>")
        sys.exit(1)

    fuente_path = sys.argv[1]

    if not os.path.isfile(fuente_path):
        print("Archivo no encontrado: " + fuente_path)
        sys.exit(1)

    # Plantilla: un .hpprgm real generado por CASE del mismo programa
    nombre = os.path.splitext(os.path.basename(fuente_path))[0]
    carpeta_destino = r"C:\Users\USUARIO\Documents\HP Prime\Calculators\Prime"
    plantilla_path = os.path.join(carpeta_destino, nombre + ".hpprgm")

    if not os.path.isfile(plantilla_path):
        print("Plantilla no encontrada en CASE: " + plantilla_path)
        print("Primero carga el programa via drag and drop para tener la plantilla.")
        sys.exit(1)

    with open(fuente_path, 'r', encoding='utf-8') as f:
        nuevo_codigo = f.read()

    destino_path = plantilla_path  # sobreescribe la plantilla con el nuevo source

    print("Reemplazando source en: " + nombre + ".hpprgm")
    reemplazar_source(plantilla_path, nuevo_codigo, destino_path)
    print("Abri CASE y verifica que el programa actualizado carga correctamente.")


if __name__ == "__main__":
    main()
```

---

### Ventaja vs Opción A

| Aspecto | Opción A | Opción C |
| ------- | -------- | -------- |
| Header | Construido por Python | Tomado de CASE (100% válido) |
| Requiere plantilla previa | No | Sí (drag and drop una vez) |
| Funciona con nombre distinto al de la plantilla | Sí | No (el nombre en el header es el de la plantilla) |
| Robustez ante cambios de formato | Media | Alta |

### Limitación clave

El nombre en el header binario de la plantilla está hardcodeado. Si se quiere crear un programa con un nombre distinto al de la plantilla, hay que actualizar también el campo del nombre en el header — lo que requiere parsear el header igual que en la Opción A.

Para el caso de uso actual (actualizar un programa ya existente con el mismo nombre), la Opción C es más robusta que la A.

---

### Referencias

| Fuente | URL | Qué aporta |
| ------ | --- | ---------- |
| Omnimaga — cyrille (HP) | https://www.omnimaga.org/hp-prime/the-hpprgm-format/ | Confirma que el source es siempre el último blob |
| TI-Planet Wiki | https://wiki.tiplanet.org/HP_Prime/File_Format | Estructura de blobs: `[tamaño 4 bytes LE][datos]` |
| Python binary replace | https://python-list.python.narkive.com/XcZdeesn/finding-replacing-a-long-binary-pattern-in-a-bin-file | Técnica de lectura/reemplazo de binarios en Python |

---

### Prerequisito para la prueba

Tener `KMH_CONV.hpprgm` generado por CASE (via drag and drop) en `HP Prime\Calculators\Prime`. Ese archivo actúa como plantilla — el script reemplaza su source con el fuente actualizado.

---

### Preguntas abiertas

- ¿La función `find_source_offset` localiza correctamente el último blob en un `.hpprgm` real con variables exportadas?
- ¿El tamaño en el source blob incluye o excluye el terminador `00 00`?

---

### Resultados de prueba

- [ ] Prueba 1 — reemplazar source de `KMH_CONV.hpprgm` con código modificado (mismo nombre): pendiente
- [ ] Prueba 2 — verificar que CASE carga el source nuevo sin requerir pasos adicionales: pendiente

### Veredicto

Pendiente. Menor prioridad que Opción A — útil como fallback para actualizar programas ya existentes con nombre conocido.
