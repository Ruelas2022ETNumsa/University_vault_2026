---
title: "Google_drive — Errores conocidos y soluciones"
galaxy_body: beacon
scope: vault
audience: [claude, usuario]
related_notes:
  - "[[]]"
tags: [beacon, solve]
date_created: 2026-06-03
status: inactivo
---

## Google Drive File Stream — error "ubicación de streaming no vacía"

**Error:** Drive no inicia y muestra:
> "Drive no ha podido cargar tu cuenta debido a un problema con tu ubicación de streaming."
> "La ubicación de streaming actual, E:\University_vault_2026\_PDF\TAB_nexus, no está vacía."

**Causa:** En algún momento anterior (durante los intentos fallidos de configurar
"Mi PC" en File Stream) quedó registrada `E:\University_vault_2026\_PDF` como
ubicación de streaming de Mi unidad. Drive detectó `TAB_nexus` (symlink con
contenido) dentro de esa ruta y se negó a iniciar para no sobreescribir archivos.

**Solución:**
1. Abrir Preferencias de Drive (aunque no cargue la cuenta — el ícono sigue
   accesible en la barra de tareas)
2. En la sección de ubicación de streaming, hacer clic en **Cambiar**
3. Crear una carpeta nueva y vacía, por ejemplo: `C:\Users\USUARIO\GoogleDrive_Stream`
4. Seleccionarla como nueva ubicación
5. Guardar → Drive pedirá reiniciar → reiniciar
6. Drive carga normalmente y retoma la sincronización

**Verificación post-solución:** confirmar que el symlink
`E:\University_vault_2026\_pdf\TAB_nexus` sigue mostrando los archivos
correctamente (el symlink no se ve afectado por el cambio de ubicación de Drive).

**Nota:** el cambio de ubicación de streaming no borra ni mueve los archivos
replicados anteriormente — Drive los retoma desde la nube en la nueva ruta.

**Fecha:** 2026-06-10

%%
galaxy-links

%%