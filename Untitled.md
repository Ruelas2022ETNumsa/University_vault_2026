# University_Vault_2026

```text
University_Vault_2026/
│
├── Semesters/                  
│   └── Sem_NN/                 
│       └── ETNXXX/             
│           ├── Partial_1/      
│           │   └── Topic_NN_nombre-descriptivo/
│           │       └── [notas]
│           ├── Partial_2/
│           └── Partial_3/
│
├── MOC/                        
│
├── _app/                       
│   ├── _config/                
│   │   ├── _galaxy-system.md
│   │   ├── _pdf-system.md
│   │   ├── _mindmap-system.md
│   │   ├── _template-system.md
│   │   ├── convencion-notas.md
│   │   ├── TagsRoute.md
│   │   ├── _claude-sync.md
│   │   └── tagroute_parche/
│   │
│   ├── _appnotes/              
│   │   ├── desmos_guide.md
│   │   ├── tags_notes.md
│   │   └── ...
│   │
│   ├── Excalidraw/             
│   │   ├── Constellations/
│   │   └── Observatory/
│   │
│   ├── scripts/                
│   │   └── tag_routs_scripts/
│   │
│   ├── solve/                  
│   │   └── git_solve.md
│   │
│   └── TagsRoutes/
│
├── _assets/                    
│
├── _pdf/                       
│   ├── ETN806/
│   ├── ETN302/
│   └── ETNXXX/
│
├── _templates/                 
│   ├── tpl-star.md
│   ├── tpl-planet.md
│   ├── tpl-moon.md
│   ├── tpl-comet.md
│   ├── tpl-nebula.md
│   ├── tpl-dwarf.md
│   ├── tpl-asteroid.md
│   ├── tpl-photon.md
│   ├── tpl-bridge.md
│   ├── tpl-constellation.md
│   ├── tpl-observatory.md
│   ├── contextogen.md
│   └── alt-B/
│       └── plantillas-A-respaldo.md
│
└── borrar/
```

---

# Descripción de la estructura

## `Semesters/`

Contiene todo el contenido académico organizado por semestre, materia, parcial y tema.

### Ejemplo

```text
Semesters/
└── Sem_03/
    └── ETN302/
        ├── Partial_1/
        │   └── Topic_01_limites/
        └── Partial_2/
```

---

## `MOC/`

Notas índice generales por materia.

Cada MOC enlaza:

- Stars
    
- Planets
    
- Moons
    
- Constellations
    
- PDFs relacionados
    

---

## `_app/`

Infraestructura interna del sistema Obsidian.

No contiene contenido académico directo.

### `_config/`

Configuraciones y documentación del sistema.

### `_appnotes/`

Guías internas de herramientas y workflows.

### `Excalidraw/`

Archivos fuente `.excalidraw`.

#### `Constellations/`

Mapas mentales integrados con Mindmap Builder.

#### `Observatory/`

Dibujos libres técnicos.

### `scripts/`

Automatizaciones y mantenimiento.

### `solve/`

Problemas conocidos y soluciones documentadas.

### `TagsRoutes/`

Sistema de rutas automáticas mediante tags.

---

## `_assets/`

Archivos visuales exportados:

- PNG
    
- SVG
    
- JPEG
    
- imágenes insertadas
    

Regla:

- mismo nombre que la nota fuente.
    

---

## `_pdf/`

Repositorio físico de PDFs.

La organización conceptual ocurre mediante:

- nombres de archivos
    
- notas asteroid
    
- enlaces internos
    

---

## `_templates/`

Plantillas Templater del sistema galaxy.

Cada tipo de cuerpo tiene su plantilla:

- star
    
- planet
    
- moon
    
- comet
    
- nebula
    
- dwarf
    
- asteroid
    
- photon
    
- bridge
    
- constellation
    
- observatory
    

---

## `borrar/`

Zona temporal antes de eliminación permanente.

Útil para:

- recuperación rápida
    
- evitar borrar accidentalmente
    
- limpiar después de sincronizar git
    

---

# Convención rápida

## Semestres

```text
Sem_01
Sem_02
Sem_08
```

---

## Materias

```text
ETN302
ETN806
INF101
```

---

## Topics

```text
Topic_01_limites
Topic_02_derivadas
Topic_03_integrales
```

---

# Ejemplo de nota

```md
# Límites laterales

## Definición
...

## Ejemplo
...

## Relación
[[Topic_02_derivadas]]

#calculo #limites
```




# TILU
- AS
## ASDSAD
- ASDSAD

# OTRO
- AS 
- SA
- ASD