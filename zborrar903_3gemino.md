
## Enunciado y Plataforma

El objetivo del proyecto es desarrollar un sistema de computación que lea una cadena de caracteres ingresada por el usuario desde el teclado, procese dicha cadena para extraer solo los caracteres ubicados en posiciones impares, y muestre el resultado en una pantalla de texto.

- El entorno de desarrollo utilizará el ensamblador MASM 5.0.
    
- La arquitectura objetivo es Intel 8086 operando en Modo Real.
    
- El programa se ejecutará y probará utilizando el emulador DOSBox.
    
- Todo el código fuente deberá estar contenido en un único archivo con extensión ASM.
    
- La salida visual se mostrará en una pantalla de texto configurada en resolución de 80 columnas por 25 filas.
    

## Restricciones del Sistema

La restricción principal y fundamental del proyecto es la prohibición estricta de utilizar interrupciones del sistema operativo o del BIOS para las operaciones de entrada, salida o manejo de video.

- Queda totalmente prohibido el uso de la interrupción 10h, habitualmente usada para el manejo de video.
    
- Queda totalmente prohibido el uso de la interrupción 16h, habitualmente usada para la lectura del teclado.
    
- Queda totalmente prohibido el uso de la interrupción 21h para tareas de lectura y escritura convencionales del DOS.
    
- La única excepción permitida para el uso de interrupciones será el bloque de código final para devolver el control al sistema operativo: `mov ax,4C00h` seguido de `int 21h`.
    

## Manejo de Entrada por Teclado

Dado que está prohibido usar interrupciones, se requiere una implementación a bajo nivel para capturar las teclas pulsadas por el usuario.

- El usuario recibirá un mensaje en pantalla solicitando que ingrese el texto y presione ENTER para confirmar.
    
- La lectura se realizará directamente leyendo el buffer de teclado del BIOS, ubicado en la dirección de memoria 0040:001E.
    
- Para procesar las teclas desde este buffer, será necesario gestionar de manera cuidadosa los punteros de cabeza y cola correspondientes a dicha área de memoria.
    
- La captura de datos finalizará exclusivamente cuando el sistema detecte la tecla ENTER.
    
- El carácter ENTER actúa como señal de finalización, por lo que no se guardará en memoria ni formará parte de la longitud de la cadena capturada.
    

## Estructuras de Almacenamiento

El programa requerirá espacios en memoria predefinidos para alojar tanto los datos entrantes como los procesados.

- Se establece un tamaño máximo de cadena de 255 caracteres para permitir entradas largas y simplificar la reserva de memoria.
    
- La cadena original ingresada por el usuario se guardará en un arreglo definido como `cadena_entrada db 255 dup(?)`.
    
- La longitud real de los caracteres capturados se almacenará en la variable `tam_in dw ?`.
    
- La cadena resultante del procesamiento se guardará en un segundo arreglo definido como `cadena_salida db 255 dup(?)` para garantizar que siempre exista espacio suficiente.
    
- La cantidad de caracteres impares extraídos se registrará en la variable `tam_out dw ?`.
    
- No se utilizarán terminadores especiales para indicar el fin de las cadenas, por lo que marcadores como 0, el signo de dólar, CR o LF están descartados.
    
- Todas las operaciones de bucle e iteración sobre las cadenas dependerán estrictamente de las longitudes numéricas almacenadas en las variables `tam_in` y `tam_out`.
    

## Lógica de Procesamiento

El objetivo de la extracción es obtener los caracteres basados en un índice de posición.

- La numeración de las posiciones de la cadena inicia desde el índice 0.
    
- La posición 0 se considera par y su carácter correspondiente debe ser ignorado.
    
- La posición 1 se considera impar y su carácter correspondiente debe ser copiado a la cadena de salida.
    
- Los espacios en blanco ingresados por el usuario se consideran caracteres válidos y normales, por lo que participan en el conteo de paridad exactamente igual que las letras y los números.
    
- Para detectar matemáticamente la paridad, se verificará el bit menos significativo del registro contador de posición.
    
- Si el bit menos significativo es igual a 0, la posición es par.
    
- Si el bit menos significativo es igual a 1, la posición es impar y el carácter se extrae.
    

## Manejo de Video e Impresión

La visualización de los datos se realizará escribiendo directamente en la memoria encargada del video.

- El acceso a la pantalla se hará escribiendo en el segmento directo de memoria de video, ubicado en B800h.
    
- Cada celda visual en el modo texto ocupará exactamente dos bytes: un byte para el código del carácter y un byte para su atributo visual.
    
- El atributo de color establecido para todo el programa será 07h, lo que genera un texto en color gris claro sobre un fondo de color negro.
    
- La limpieza total de la pantalla se realizará escribiendo de forma directa el carácter de espacio junto con su atributo de color.
    
- Este borrado de pantalla utilizará una instrucción de repetición conceptualmente basada en mover el valor 0720h repetidas veces, llenando las 2000 celdas de la pantalla.
    
- Si la longitud de la cadena impresa llega a superar el ancho de la columna 79, el texto continuará su impresión de forma automática en la fila inferior.
    
- Este salto de línea al llegar al borde derecho de la pantalla es un comportamiento exclusivo de la visualización y no requiere insertar caracteres adicionales en la memoria de la cadena.
    

## Arquitectura del Programa

El desarrollo prioriza un código didáctico, legible y clásico de la época del ensamblador.

- Para simplificar la escritura del código y procesar los arreglos, se considerará válido y deseable el uso de las instrucciones de cadena nativas del procesador, tales como LODSB, STOSB, MOVSB y REP.
    
- El programa seguirá un diseño modular mediante procedimientos para facilitar su lectura y mantenimiento, sin necesidad de recurrir a archivos externos.
    
- La rutina `LimpiarPantalla` se encargará de preparar el lienzo visual vaciando la memoria B800h.
    
- La rutina `LeerCadena` gestionará exclusivamente la interacción del usuario a través del buffer del BIOS, determinando la longitud y controlando el fin de lectura mediante la tecla ENTER.
    
- La rutina `ProcesarCadena` aplicará la lógica matemática de paridad para leer la cadena de entrada y generar la cadena resultante de posiciones impares.
    
- La rutina `ImprimirCadena` se diseñará como un bloque genérico que reciba la dirección y la longitud de cualquier cadena, utilizándose sin duplicar código para imprimir tanto las instrucciones en pantalla, como el texto original y su resultado final.
    
- La ejecución culminará con una llamada a la rutina `Finalizar`, la cual terminará el proceso de forma segura.