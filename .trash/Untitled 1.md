Aquí tienes la traducción y adaptación de la siguiente tanda de variables (basada en las 8 imágenes provistas), aplicando el cambio solicitado en las opciones de los campos:

### 1. `{{yaml_content:with-dashes}}` o `{{yaml_content:no-dashes}}`

- **Descripción:** Da el frontmatter YAML de la nota actual. Los guiones `---` se pueden incluir o excluir. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo. Además, debe estar presente una sección de frontmatter YAML.
    
- **Default value for `{{yaml_content}}`**
    
    - **Descripción:** Si no está disponible, entonces:
        
    - **Campo:** [Cancel execution and show errors/Cancel execution silently/Execute whit value:]
        

### 2. `{{yaml_value:property}}`

- **Descripción:** Lee un único valor del frontmatter del archivo actual. Toma el nombre de una propiedad como argumento. Puedes acceder a propiedades anidadas con la notación de punto: `propiedad1.propiedad2`. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo. Además, la propiedad YAML dada debe existir en el frontmatter del archivo.
    
- **Default value for `{{yaml_value}}`**
    
    - **Descripción:** Si no está disponible, entonces:
        
    - **Campo:** [Cancel execution and show errors/Cancel execution silently/Execute whit value:]
        

### 3. `{{yaml_values:property:separator}}`

- **Descripción:** Lee una lista de valores del frontmatter del archivo actual. Toma el nombre de una propiedad y un separador como argumentos. Puedes acceder a propiedades anidadas con la notación de punto: `propiedad1.propiedad2`. Solo disponible cuando el panel activo contiene un archivo, no en la vista de gráfico u otra vista que no sea de archivo. Además, la propiedad YAML dada debe existir en el frontmatter del archivo.
    
- **Default value for `{{yaml_values}}`**
    
    - **Descripción:** Si no está disponible, entonces:
        
    - **Campo:** [Cancel execution and show errors/Cancel execution silently/Execute whit value:]
        

### 4. `{{event_file_content}}`

- **Descripción:** Da el contenido del archivo relacionado con el evento, incluyendo el frontmatter YAML. Si necesitas excluir el YAML, usa `{{event_note_content}}` en su lugar. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
    
- **Default value for `{{event_file_content}}`**
    
    - **Descripción:** Si no está disponible, entonces:
        
    - **Campo:** [Cancel execution and show errors/Cancel execution silently/Execute whit value:]
        

### 5. `{{event_file_extension:with-dot}}` o `{{event_file_extension:no-dot}}`

- **Descripción:** Da la terminación del nombre del archivo relacionado con el evento. Usa `{{event_file_extension:with-dot}}` para incluir un punto precedente. Si la extensión está vacía, no se añade ningún punto. `{{event_file_extension:no-dot}}` nunca incluye un punto. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
    
- **Default value for `{{event_file_extension}}`**
    
    - **Descripción:** Si no está disponible, entonces:
        
    - **Campo:** [Cancel execution and show errors/Cancel execution silently/Execute whit value:]
        

### 6. `{{event_file_name}}`

- **Descripción:** Da el nombre del archivo relacionado con el evento con una extensión de archivo. Si lo necesitas sin la extensión, usa `{{event_title}}` en su lugar. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
    
- **Default value for `{{event_file_name}}`**
    
    - **Descripción:** Si no está disponible, entonces:
        
    - **Campo:** [Cancel execution and show errors/Cancel execution silently/Execute whit value:]
        

### 7. `{{event_file_path:relative}}` o `{{event_file_path:absolute}}`

- **Descripción:** Da la ruta al archivo relacionado con el evento, ya sea como absoluta desde la raíz del sistema de archivos, o como relativa desde la raíz de la bóveda de Obsidian. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
    
- **Default value for `{{event_file_path}}`**
    
    - **Descripción:** Si no está disponible, entonces:
        
    - **Campo:** [Cancel execution and show errors/Cancel execution silently/Execute whit value:]
        

### 8. `{{event_file_uri}}`

- **Descripción:** Da un URI de Obsidian que abre el archivo relacionado con el evento. Solo disponible en los eventos: Menú de archivo, Archivo creado, Contenido de archivo modificado, Archivo eliminado, Archivo movido, Archivo renombrado.
    
- **Default value for `{{event_file_uri}}`**
    
    - **Descripción:** Si no está disponible, entonces:
        
    - **Campo:** [Cancel execution and show errors/Cancel execution silently/Execute whit value:]