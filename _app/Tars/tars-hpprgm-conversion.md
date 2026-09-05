---
galaxy_body: ship
project: "tars-hpprgm-conversion"
date: 2026-09-04
status: docked
fleet:
blocked_by:
---

## Handoff

**Última sesión:** 2026-09-04
**Retomar desde:** Sección Planificación — elegir opción a probar e implementar
**Completado esta sesión:** investigación del formato .hpprgm, relevamiento de antecedentes, documentación de opciones
**Próximo paso:** elegir opción (A, B o C) y arrancar implementación
**Preguntas de cierre:** ¿se prueba primero con Xprime como referencia de formato o se va directo a construir el binario desde Python?

---

## Resumen y objetivo

Automatizar el envío de archivos `.hpprgm` desde Obsidian a CASE (HP Prime virtual) sin drag and drop manual. El script debe generar un archivo que CASE reconozca y cargue correctamente.

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
| 2026-09-04 | Script en Python dentro de Shell Commands | Consistente con el resto de scripts del vault |
| 2026-09-04 | Destino principal: CASE vía `HP Prime\Calculators\Prime` | Ruta confirmada — CASE la detecta al abrir |
| 2026-09-04 | TARS (física) se trabaja por drag and drop manual desde el Kit | No hay ruta de carpeta para la calc física — requiere USB conectado |
| 2026-09-04 | Opción A seleccionada como camino a explorar | Formato documentado, antecedentes concretos en PrimeComm y Xprime |

> [!note]- Descartadas
> - **xcopy directo a `Calculadoras\CASE`** — CASE al abrir reemplaza el archivo con su versión binaria compilada y el programa queda inutilizable.
> - **Copia simple a `HP Prime\Calculators\Prime`** — el archivo llega pero CASE lo trata como binario inválido porque el fuente UTF-8 no tiene el header `.hpprgm` correcto.
> - **Script sin Python (xcopy puro)** — descartado porque se necesita lógica condicional (V/F) y construcción de binario.

---

## Planificación

El archivo `.hpprgm` es un formato binario con header de 16 bytes seguido del contenido en UTF-16 LE. Un fuente guardado en Obsidian como texto plano UTF-8 no tiene ese header — CASE lo rechaza o lo corrompe al abrirlo.

La solución es que Python construya el `.hpprgm` correcto: leer el fuente UTF-8, armar el header binario, codificar el contenido en UTF-16 LE y escribir el archivo resultante en la carpeta de CASE.

Restricciones:
- Sin dependencias externas (solo stdlib de Python)
- El archivo resultante debe ser reconocido por CASE sin pasos manuales adicionales
- El nombre del programa en el header debe coincidir con el nombre del archivo

---

## Sugerencias

| Fuente | Resumen | Aprovechable |
| ------ | ------- | ------------ |
| [TI-Planet Wiki — HP Prime File Format](https://wiki.tiplanet.org/HP_Prime/File_Format) | Documenta la estructura binaria completa del `.hpprgm`: header de 16 bytes, flag de nombre en byte 8 (0x00 sin nombre / 0x01 con nombre), nombre en UTF-16 LE terminado en 0x00 0x00, luego el contenido | Estructura exacta del header para armar el binario |
| [PrimeComm — PrimeProgramFile.cs](https://github.com/eried/PrimeComm) | Librería C# que lee y construye `.hpprgm`. Tiene el algoritmo de parsing y construcción del binario ya resuelto | Portar la lógica de construcción a Python |
| [Xprime](https://github.com/Insoft-UK/Xprime) | Editor macOS que exporta `.hpprgm` en formato G1 (antiguo). Funciona pero requiere abrir el archivo en CASE y hacer "Check" una vez para que la calc lo resave al formato moderno | Opción de fallback si el formato moderno es difícil de replicar |
| [Gist fakuivan](https://gist.github.com/fakuivan/ee66d88e8b7f42fa4e148c4b9e92c1d8) | Script bash/Python que decodifica `.hpprgm` leyendo contenido como UTF-16 LE — confirma que la lógica inversa funciona en Python | Referencia para validar decodificación y entender el offset del contenido |

---

## Opciones

### Opción A — Python construye el `.hpprgm` moderno (formato named)
Python lee el fuente UTF-8, arma el header binario con nombre, codifica en UTF-16 LE y escribe el archivo. CASE lo carga sin pasos adicionales.
- **Pro:** flujo 100% automático, sin intervención manual
- **Contra:** requiere replicar el formato binario exacto — si hay bytes de metadata adicional no documentados puede fallar

### Opción B — Python genera formato G1 (Xprime approach)
Usar el formato antiguo G1 que Xprime ya tiene resuelto. CASE acepta el archivo pero requiere abrir el editor y hacer "Check" una vez para que lo resave al formato moderno.
- **Pro:** formato más simple, antecedente funcional en Xprime
- **Contra:** requiere un paso manual en CASE la primera vez que se carga cada archivo

### Opción C — Tomar un `.hpprgm` existente como plantilla
Leer un `.hpprgm` real generado por CASE (del drag and drop), extraer su header exacto y reemplazar solo el contenido con el fuente nuevo. Garantiza que el header es 100% válido.
- **Pro:** sin ingeniería inversa del formato — se usa un header real
- **Contra:** el header tiene el nombre del programa hardcodeado — hay que actualizar ese campo igual

---

## Flujo de pasos

1. Tomar un `.hpprgm` existente generado por CASE y analizarlo en hex para verificar la estructura contra la documentación de TI-Planet
2. Decidir entre Opción A, B o C
3. Implementar la conversión en `main.py`
4. Testear con `KMH_CONV.hpprgm` — copiar a `HP Prime\Calculators\Prime` y verificar que CASE lo carga sin errores
5. Testear con un archivo nuevo que no existía antes en CASE
6. Si pasa ambos tests → integrar al script `tars-sync`

---

## Tareas

- [x] Confirmar ruta de destino para CASE (`HP Prime\Calculators\Prime`)
- [x] Investigar formato `.hpprgm`
- [x] Relevar antecedentes y proyectos similares
- [x] Documentar opciones de conversión
- [ ] Analizar un `.hpprgm` real en hex
- [ ] Elegir opción (A, B o C)
- [ ] Implementar conversión en `main.py`
- [ ] Testear con archivo existente
- [ ] Testear con archivo nuevo
- [ ] Integrar al script `tars-sync`

---

## Preguntas abiertas

- ¿Hay bytes de metadata adicional en el header moderno que no están documentados en TI-Planet y que podrían hacer fallar la Opción A?
- ¿El nombre en el header del `.hpprgm` debe coincidir exactamente con el nombre del archivo o con el nombre del programa declarado en el fuente (`EXPORT KMH_CONV()`)?

---

## Recursos

- `E:\University_vault_2026\_app\Tars\tars-sync-shellcommands.md` — blueprint original del script
- `E:\University_vault_2026\.obsidian\scripts\python\tars-sync\main.py` — script actual (copia simple, sin conversión)
- [TI-Planet — HP Prime File Format](https://wiki.tiplanet.org/HP_Prime/File_Format)
- [PrimeComm — GitHub](https://github.com/eried/PrimeComm)
- [Xprime — GitHub](https://github.com/Insoft-UK/Xprime)
