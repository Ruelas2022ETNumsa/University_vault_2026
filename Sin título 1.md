##### Ej. Escribir el programa de software para imprimir, desde el computador SIC, la palabra: SALUDO. Se debe considerar la segunda versión de la Interface de la impresora (controlada por la CPU). La palabra a imprimirse se encuentra grabada en las siguientes direcciones de la memoria del computador: 300; 301; 302 (especificar en detalle, el contenido de estas 3 posiciones). Utilizar la notación octal para todos los números.

**Resolución**
Conversión ASCII a octal, empaquetado de 2 caracteres por palabra de 18 bits (1º carácter en $DR_{10:17}$, 2º carácter en $DR_{1:8}$) y bucle de E/S programada con polling de estatus (`IS2`) y salida de datos (`OD2`).

Conversión de caracteres ASCII a octal:

$$
\text{'S'} = 083_{10} = 01010011_2 = 123_8
$$


$$
\text{'A'} = 065_{10} = 01000001_2 = 101_8
$$


$$
\text{'L'} = 076_{10} = 01001100_2 = 114_8
$$


$$
\text{'U'} = 085_{10} = 01010101_2 = 125_8
$$


$$
\text{'D'} = 068_{10} = 01000100_2 = 104_8
$$


$$
\text{'O'} = 079_{10} = 01001111_2 = 117_8
$$


Empaquetado en memoria (2 caracteres por palabra de 18 bits):

$$
\text{Contenido}(00300) = \text{'A'}(DR_{1:8}) ! \text{'S'}(DR_{10:17}) = 101_8 \cdot 1000_8 + 123_8 = 101123_8
$$


$$
\text{Contenido}(00301) = \text{'U'}(DR_{1:8}) ! \text{'L'}(DR_{10:17}) = 125_8 \cdot 1000_8 + 114_8 = 125114_8
$$


$$
\text{Contenido}(00302) = \text{'O'}(DR_{1:8}) ! \text{'D'}(DR_{10:17}) = 117_8 \cdot 1000_8 + 104_8 = 117104_8
$$


Cálculo del contador negativo para 3 palabras:

$$
\text{Contador}_8 = 2^{18} - 3 = 777777_8 - 000003_8 + 1_8
$$


$$
\therefore\quad \color{orange}{\text{Contador}_8 = 777775_8}
$$


**Tabla de datos**

| Dirección | Contenido | Descripción |
| :-: | :-: | - |
| `00100` | `000300` | Puntero a la dirección inicial del bloque en memoria (`00300`) |
| `00101` | `777775` | Conteo negativo de palabras a transferir ($-3_{10} = 777775_8$) |
| `00300` | `101123` | Palabra 1: 'S' ($123_8$) en bits 10:17 + 'A' ($101_8$) en bits 1:8 |
| `00301` | `125114` | Palabra 2: 'L' ($114_8$) en bits 10:17 + 'U' ($125_8$) en bits 1:8 |
| `00302` | `117104` | Palabra 3: 'D' ($104_8$) en bits 10:17 + 'O' ($117_8$) en bits 1:8 |

**Tabla de instrucciones**

| Dirección | Instrucción | Explicación / Acción |
| :-: | :-: | - |
| `00000` | `IS2` | Consulta el estatus del dispositivo #2. Si $busy = 0$ (disponible), salta a `00002` |
| `00001` | `JMP 00000` | Bucle de espera activa (polling) mientras la impresora esté ocupada ($busy = 1$) |
| `00002` | `LAC I 00100` | Carga en `AC` la palabra apuntada indirectamente por la dirección `00100` |
| `00003` | `OD2` | Transfiere la palabra del `AC` a la impresora (#2) mediante salida de datos |
| `00004` | `ISZ 00100` | Incrementa el puntero de dirección de memoria para acceder a la siguiente palabra |
| `00005` | `ISZ 00101` | Incrementa el contador negativo; si alcanza cero (3 palabras enviadas), salta a `00007` |
| `00006` | `JMP 00000` | Salta al inicio del bucle para transferir la siguiente palabra |
| `00007` | `HLT` | Detiene la ejecución de la CPU tras completar la impresión de las 3 palabras |
