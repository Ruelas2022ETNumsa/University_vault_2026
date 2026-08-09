

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

Cerebro digital para ingeniería. Sistema de notas académicas construido en Obsidian, organizado como un universo de galaxias donde cada materia es una galaxia y cada nota tiene un rol preciso dentro de ella.

---

## Idea central — Sistema Galaxy

El conocimiento se estructura en capas orbitales. Cada nota tiene un tipo (`galaxy_body`) definido en su YAML que determina su rol: teoría central, fórmula, ejercicio resuelto, resumen, referencia externa, mapa mental, etc. Los `[[wikilinks]]` en bloques `%%comentados%%` construyen el grafo de Obsidian sin ensuciar el modo de lectura.

Trece tipos de cuerpo galaxy: `star` `planet` `moon` `comet` `nebula` `dwarf` `asteroid` `photon` `neutrino` `constellation` `observatory` `bridge` `beacon`

---

## Estructura de carpetas

```

University_vault_2026/ 
├── Semesters/ ← contenido académico — Sem_NN / ETNXXX / Partial_N / Topic_NN 
├── MOC/ ← índices por materia, enlazan todas sus stars 
├── _PDF/ ← PDFs físicos (apuntes, libros, papers) 
├── _app/ ← infraestructura del vault (config, scripts, Excalidraw) 
├── _assets/ ← imágenes exportadas (.png, .svg, .jpg) 
├── _templates/ ← plantillas Templater por tipo galaxy 
└── borrar/ ← carpeta de espera antes de eliminar permanentemente

```

---

## Convención de nombres

```

ETNXXX-TNN-nombre-descriptivo.md

```

Semestre y parcial no van en el nombre — están en la ruta de carpeta y en el YAML.

---

## Sincronización

| Dispositivo | Sistema | Rol |
|---|---|---|
| PC Escritorio | Mega + Obsidian Git | Principal — sincroniza con Mega y con GitHub |
| Laptop | Mega | Secundario — bidireccional |
| Tablet Samsung S6 Lite | FolderSync + Mega | Edición móvil — bidireccional |
| Celular | FolderSync + Mega | Solo lectura |

GitHub actúa como backup de las notas `.md`. Los PDFs viven en Mega únicamente (`_PDF/`).

---

## Archivos de configuración

Toda la documentación del sistema vive en `_app/_config/`:

- `_galaxy-system.md` — sistema completo de tipos, convenciones y plantillas YAML
- `_sync-system.md` — configuración de sincronización entre dispositivos
- `_pdf-system.md` — flujo de integración de PDFs con el vault
- `_template-system.md` — sistema de plantillas Templater
- `_mindmap-system.md` — sistema Excalidraw + Mindmap Builder
- `_graph-system.md` — Desmos y TikZJax (neutrinos)
- `_ToDo-system.md` — pendientes activos del vault
