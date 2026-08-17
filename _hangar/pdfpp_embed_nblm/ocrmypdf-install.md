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
| Idioma `spa` | — | ❌ falta instalar |

**Ruta de Tesseract:** `C:\Program Files\Tesseract-OCR\tesseract.exe`

---

### Problemas encontrados

**1. Tesseract no está en el PATH**
WinError 2 al correr OCRmyPDF — no encuentra el ejecutable.
Solución: agregar `C:\Program Files\Tesseract-OCR` al PATH del sistema.
Inicio → "variables de entorno" → Variables del sistema → Path → Editar → Nuevo → pegar la ruta → Aceptar todo → reiniciar PowerShell.

**2. Idioma español falta**
Error: `OCR engine does not have language data for spa`
Solución: descargar `spa.traineddata` y copiarlo a `C:\Program Files\Tesseract-OCR\tessdata\`
Descarga: https://github.com/tesseract-ocr/tessdata/raw/main/spa.traineddata

---

### Próximos pasos

- [ ] Agregar `C:\Program Files\Tesseract-OCR` al PATH del sistema
- [ ] Descargar `spa.traineddata` y copiarlo a `tessdata\`
- [ ] Verificar con `tesseract --version` en PowerShell nuevo
- [ ] Probar: `py -m ocrmypdf -l spa+eng "Alonso & Finn-Mecánica_Vol 1-1970-.pdf" "Alonso & Finn-OCR.pdf"` desde `E:\University_vault_2026\_PDF\ETN-607`
- [ ] Evaluar calidad del OCR en el resultado
- [ ] Documentar resultado en `chronicle.md`

---

### Comando de prueba

```
cd "E:\University_vault_2026\_PDF\ETN-607"
py -m ocrmypdf -l spa+eng "Alonso & Finn-Mecánica_Vol 1-1970-.pdf" "Alonso & Finn-OCR.pdf"
```
