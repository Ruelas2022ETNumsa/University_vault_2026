```
                &$$$&$$$$X$$&    
               $&$$$$$$$$$$$&&$  
              $$$X&&&$$$$XX$$$&  
             :;xX&&&$$$X$$$$$$X  
            ::+xXX&&$X$$&&$XXX$  
            ++:+xX&&&$$$&&$XXX   
            ;+++;++++x$$$X$$X    
            +++++++++++++xx      
           Xxx+++++++++++xxX     
            xx+++;++;;++++ ++    
          :..:;++.....:;+++Xxx   
         :.::::;;;:....:;++;;;   
        +:;x$&;::+;::...:;;+;;;;:
        Xxxx$&&X;;++:::::::;;;;+ 
        +;+x$&&&&&&$$Xx+:::::::  
        x;+X$&&&&&&&&$Xx;;;+;;:: 
        +++X$&&&&&&&&$$$$        
       +;+XX&&&&&&&&$$$$$$       
      +;;;X$&&&&&&&&&$$$$$$      
     +;;;X&$X$$$$&&&&& $$$XX     
     ;;;;x&&&$$$& XX$$$ $$$XX    
&$$  &&&&&&&&&&&   XX$$$ $$X;;++x
&&&&&&&&&&&&&&&    XXXXXX  XXxx++
   &&&&&&&&&&&&     $x+;;;;+     
    $&&&&&$&$$$       X+;;+x+    
     &&&&$$&&$$         X$XX     
     &&&&x$&$$                   
    $&&&&X&&                     
    &&&&&$                       
   &&&&&&                        
  &&&$&&                         
  &&$$&&&                        
   $XX&&&                        
   Xx++                          
   xx+xx
```

# University_vault_2026

> [!tip] Consideraciones Claude
>
> **Hora pico: 9 am – 3 pm** (lunes a viernes, no aplica fines de semana)
>
> En este horario el consumo de tokens es significativamente mayor.
>
> **Conversación simple** → consumo bajo; la hora pico no duele mucho. El problema surge si la conversación se extiende, porque el historial acumulado se reenvía completo en cada turno.
>
> **Sesiones de vault** → el gasto se multiplica desde varios frentes a la vez: cada lectura de archivo carga contexto, cada escritura es una operación de herramienta, y el historial crece con cada turno. El costo elevado no viene del archivo en sí, sino de todo ese contexto combinado que viaja en cada mensaje.
>
> **Regla práctica:** en hora pico, conversación corta y puntual está bien. Para sesiones de vault largas, mejor después de las 3 pm Bolivia.

---

## Checklist de seguridad — verificación de virus (cuando haya tiempo)

> [!tip] No urgente — todo lo revisado hasta ahora salió limpio
> Investigación realizada el 2026-08-18. SFC encontró y reparó archivos dañados del sistema. Malwarebytes y Defender no detectaron amenazas. Proceso `\` confirmado como Claude Desktop.

- [ ] Reiniciar la PC y verificar que Configuración > Aplicaciones > Inicio abre normalmente (pendiente tras reparación del SFC)
- [ ] Correr DISM hasta completar: `DISM /Online /Cleanup-Image /RestoreHealth`
- [ ] Correr TDSSKiller de Kaspersky (descargar desde bleepingcomputer.com/download/tdsskiller)
- [ ] Hacer escaneo offline de Windows Defender: Seguridad de Windows → Protección antivirus → Opciones de examen → Examen sin conexión
- [ ] Revisar `C:\ProgramData` por carpetas con nombres aleatorios raros
- [ ] Correr `ipconfig /displaydns` en CMD y revisar si hay dominios desconocidos
- [ ] Verificar registro manualmente:
  - `reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
  - `reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run`
- [ ] Subir cualquier ejecutable sospechoso a virustotal.com

> Ver análisis completo en: [[_app/_config/_basic-memory-system]]

---

## Reemplazar Office pirata (cuando haya tiempo)

> [!tip] Pendiente — investigado el 2026-08-18
> Opciones gratuitas probadas y recomendadas para reemplazar Word, Excel y PowerPoint.

### Online (sin instalar nada)
- **Google Docs / Sheets / Slides** — con cuenta Gmail ya está disponible. Guarda automáticamente, permite edición colaborativa. Compatible con .docx, .xlsx, .pptx.
  - Docs → reemplaza Word
  - Sheets → reemplaza Excel
  - Slides → reemplaza PowerPoint

### Offline (instalar en laptop)
- **OnlyOffice** — interfaz casi idéntica a Office moderno, compatibilidad ~99% con archivos .docx/.xlsx/.pptx. Mejor opción para archivos con formato complejo.
  - Descargar: onlyoffice.com
- **LibreOffice** — 100% gratuito, sin publicidad, open source. Muy sólido para documentos de texto y hojas de cálculo. A veces tiene problemas con .pptx complejos.
  - Descargar: libreoffice.org
- **FreeOffice** (SoftMaker) — muy liviano, buena opción si la laptop tiene recursos limitados.
  - Descargar: freeoffice.com

### Recomendación práctica
Combinar **Google Docs/Sheets/Slides** para el día a día + **OnlyOffice** instalado para cuando no haya internet o lleguen archivos con formato complejo de PowerPoint.
