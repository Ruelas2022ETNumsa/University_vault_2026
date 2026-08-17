---
galaxy_body: dropship
carrier: "[[_hangar/pdfpp_embed_nblm/pdfpp_embed_nblm.md]]"
scope: prueba
status: activo
date: 2026-08-16
---

## Proposito

Registro de instalación y configuración de OCRmyPDF en Windows para el carrier `pdfpp_embed_nblm`. Fase de pruebas por línea de comandos — no integrado a Obsidian aún.

---

## Contenido

### Estado de instalación

| Componente | Versión | Estado |
| ---------- | ------- | ------ |
| Python | 3.13.13 | ✅ instalado |
| Tesseract | 5.4.0 | ✅ instalado vía winget |
| OCRmyPDF | 17.10.0 | ✅ instalado vía pip |
| pypdfium2 | 5.13.0 | ✅ instalado vía pip |
| Idioma `eng` | — | ✅ incluido por defecto |
| Idioma `spa` | — | ✅ instalado manualmente (tessdata) |
| pngquant | — | ❌ no instalado — necesario para --optimize 2 |
| JBIG2 | — | ❌ no instalado — opcional, reduce tamaño |

**Ruta de Tesseract:** `C:\Program Files\Tesseract-OCR\tesseract.exe`

---

### Pruebas realizadas — Alonso & Finn-Mecánica_Vol 1-1970-.pdf

**PDF original:** 19.025 KB

**Prueba 1 — sin flags extra**
Comando: `py -m ocrmypdf -l spa+eng "Alonso & Finn..." "Alonso & Finn-OCR.pdf"`
Resultado: falló — PDF tiene estructura Tagged, OCRmyPDF se niega sin flag explícito.

**Prueba 2 — force-ocr**
Comando: `py -m ocrmypdf -l spa+eng --force-ocr "Alonso & Finn..." "Alonso & Finn-OCR.pdf"`
Resultado: ✅ generó PDF con capa de texto — 41.087 KB (doble del original)
Búsqueda en Obsidian: ✅ Ctrl+F encuentra `figura` y `fig`
Problemas: OCR con errores en dígitos similares (ej: `3` reconocido como `8`) — esperado en texto antiguo. Warnings de diacríticos en páginas con mucho español.

**Prueba 3 — force-ocr + optimize 1**
Comando: `py -m ocrmypdf -l spa+eng --force-ocr --optimize 1 "Alonso & Finn..." "Alonso & Finn-OCR-opt.pdf"`
Resultado: ✅ completó — 41.087 KB — sin ahorro respecto a prueba 2 (optimize 1 no tiene efecto en este PDF)
Conclusión: necesario probar --optimize 2 con pngquant instalado.

**Prueba 4 — force-ocr + optimize 2 (con pngquant 2.17.0)**
Comando: `py -m ocrmypdf -l spa+eng --force-ocr --optimize 2 "Alonso & Finn..." "Alonso & Finn-OCR-opt2.pdf"`
Resultado: ✅ completó — 41.087 KB — sin ahorro respecto a prueba 3
Conclusión: pngquant instalado y funcionando pero sin efecto. El PDF es un escaneado en escala de grises — pngquant cuantiza paletas de color, no tiene qué reducir en grises. Ninguna de las optimizaciones (opt1, opt2) produjo cambio respecto a la prueba 2 base. Para PDFs escaneados en grises, el resultado óptimo es OCRmyPDF sin flags de optimización.

**Prueba 5 — Ctrl+F en Obsidian**
Archivo: `Alonso & Finn-OCR.pdf` (prueba 2, 41.087 KB)
Resultado: ✅ búsqueda funciona correctamente en Obsidian
Conclusión: flujo OCR cerrado para Alonso & Finn. Capa de texto funcional.

---

### Notas técnicas

- `--force-ocr` necesario para PDFs Tagged — rasteriza todas las páginas
- `--optimize 2` requiere `pngquant` — instalar con `winget install -e --id ImageOptim.pngquant`
- `--optimize 1` sin pérdida, no requiere dependencias extra
- Warnings `[WinError 2]` = componentes opcionales ausentes (JBIG2, pngquant) — no afectan el OCR
- `lots of diacritics` = warning esperado en texto en español
- `no best words` = páginas con figuras o contenido vectorial sin texto reconocible
- GPU: Tesseract usa solo CPU — sin aceleración por GPU

---

### Comandos de referencia

```
# Básico con force-ocr
py -m ocrmypdf -l spa+eng --force-ocr "input.pdf" "output-OCR.pdf"

# Con compresión sin pérdida (no requiere pngquant)
py -m ocrmypdf -l spa+eng --force-ocr --optimize 1 "input.pdf" "output-OCR-opt.pdf"

# Con compresión con pérdida (requiere pngquant)
py -m ocrmypdf -l spa+eng --force-ocr --optimize 2 "input.pdf" "output-OCR-opt2.pdf"

# Solo inglés
py -m ocrmypdf -l eng --force-ocr "input.pdf" "output-OCR.pdf"
```

---

### Próximos pasos

- [x] Instalar pngquant: descargado zip desde pngquant.org, exe en `C:\tools\pngquant\pngquant\`, agregado al PATH manualmente
- [x] Probar --optimize 2 con Alonso & Finn — sin ahorro (41.087 KB igual que opt1)
- [x] Probar búsqueda Ctrl+F en Obsidian — funciona correctamente
- [ ] Probar con otros PDFs de ETN-607 — verificar cuáles necesitan OCR
- [x] Documentar resultado en chronicle.md
- [x] Compresión descartada para PDFs en escala de grises — optimize 1 y 2 sin efecto
