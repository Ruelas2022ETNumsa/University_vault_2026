# Prueba: pegar imagen en Claude y guardar al vault

**Estado:** pendiente de ejecución — prueba aislada  
**Proyecto relacionado:** IMA-SRC

---

## Intención

Probar si Claude puede tomar una imagen pegada directamente en el chat y guardarla en la carpeta `assets` del vault de Obsidian.

## Lo que se quiere validar

1. Claude puede recibir una imagen pegada y escribirla al vault via MCP Filesystem
2. Si al guardar la imagen se renombra automáticamente o conserva el nombre original
3. El formato de referencia `![[nombre_imagen.png]]` funciona correctamente en Obsidian después

## Cómo hacer la prueba

1. Abrir una nueva sesión con Claude
2. Pegar cualquier imagen en el chat
3. Pedirle a Claude que la guarde en `E:\University_vault_2026\assets\`
4. Verificar en el vault si el archivo llegó y con qué nombre
5. Intentar referenciarla con `![[nombre.png]]` en algún `.md`

## Notas previas

- Se desconoce si Claude renombrará el archivo al guardarlo — eso hay que observarlo
- La imagen puede ser cualquiera, no tiene que ser del proyecto IMA-SRC
- Si el nombre se pierde o cambia, evaluar si Claude puede aceptar un nombre específico como parámetro

---

## Tarea 2: agregar etiqueta "Figura X" a imágenes en apuntes de tablet

**Estado:** pendiente de evaluar  
**Contexto:** al tomar apuntes físicos en la tablet, las imágenes no tienen etiqueta. NBLM usa la etiqueta del libro (ej: "Figura 4.4") como referencia principal — si los apuntes propios la tuvieran, NBLM podría referenciarlas igual.

**Lo que se quiere:** definir un formato de etiqueta para imágenes propias en los apuntes de tablet, equivalente al que usan los libros.
