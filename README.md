```
                                     00898008    899999                  
                                    088999000008899888999999808          
                                   0008086680099988086699988980000       
                                  808868888808898000000899980880088      
                                088008988800888898889888999998998000     
                                880089698000000088999889666980088000     
                               256669008000000000089999664446980896      
                              3125446800000008000899999699989888866      
                             31154446680000094989669988888888888998      
                            21154444669000008699669889800008898899       
                           433114444669800000889698000000089966669       
                           225233566669800000089998000000089666698       
                           2445313544668000000088998800000899669         
                           2544555522256988800000899989696988            
                           635444555555555552356680088999988989          
                           0555555555555555555455555566996899989524      
                           955555555544444444444455555556649      66     
                          4444666455552555544544555555555446             
                         446644445555555555522255555555445896            
                         444444554444445552222555555555454  66           
                           6964455555555555555555555555558   64          
                           2445554552132222231322255555446    44         
                        31113125555551111111111111125555559   94         
                      31111111125555531111111111111325555556   44        
                     5111111111125555211111111111113255555225445         
                     111111111111225522111111111111113255555552322       
                    1711111331111113222211111111111111325555555522325    
                   51111546600821111132521111111111111132555555522222311 
                   255446666000041111355553111111111111132255522225555235
                  964666666600000921112544531111111111111132222222255525 
                   944444466000000095335444531111133225521133233332554   
                   8254454660000000000099999525444455231111133331135     
                   5332544668000000000000000000944442111111111131114     
                   233326666800000000000000000084554411333323333311113   
                  843335996600000000000000000008455552133332222223333    
                  942334999600000000000000000009460089955549             
                  45433466690000000000000000000690888888                 
                 655445466680000000000000000008888888888                 
                 233446666000000000000000000008888888888                 
                53333446690000000000000000008888868888888                
               4232212466000000000000000000008889 68888888               
              6233252566998000000000000000000888   98888898              
             8232332568899690000000000000000008    888888999             
             53323356600096669000000889008000008    88888999             
            42333233460000896669999990 8896800088    8888999             
            6325545259000000899000000   8646988899    88888996           
             94222549000000000000000     944698999     888889966         
00000        000000000000000000080        966988999     888864222222252  
00888       000000000000000000080         8646988899      89652222255554 
 0800800000000000000000000000000           84469888998      8655452264559
  00000000000000000000000000000             94444444446       8889469    
    000000000000008000000000000              89452222222225              
           00000000000000000088                94222222222224            
           80000000000000000888                 94222222244524           
           80000000000800008888                  8642222224645           
           80000000808600000888                    864526554965          
           80000000006600000888                     096989449            
           80000000009600000888                         8969             
           4000000086490000088                                           
           400000009448000888                                            
           9000000094600088                                              
           00000000946000                                                
          4000000008680                                                  
          800000000880                                                   
         800000000880                                                    
        800000008800                                                     
       800000008000                                                      
      000000880000                                                       
      000008880000                                                       
       00099800000                                                       
       0008800000000                                                     
       08969 0000000                                                     
       08669  0000                                                       
       894669                                                            
       964444                                                            
       94455556                                                          
        65554548                                                         
        86444649

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




