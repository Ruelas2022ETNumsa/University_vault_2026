```ahpl
MODULE: RECEPTOR_SIMPLE
MEMORY: REG; listo
INPUTS: entrada; start
OUTPUTS: salida; listo

1. -> (!start)/(1)
2. REG <- entrada
3. listo <- 1
   -> (1)
END SEQUENCE
salida = REG
END
```


---

otra pregunta 

---

## Módulo de Transmisión de Datos Simple

### 1. Definición formal
Un módulo AHPL es una descripción procedimental que divide un sistema digital en una sección de datos y una sección de control. La sección de control ejecuta una secuencia paso a paso sincronizada por un reloj común, gobernando la carga de registros internos mediante transferencias y controlando líneas externas mediante conexiones.

### 2. Idea clave
El handshake o sincronización asíncrona permite comunicar dos módulos independientes mediante líneas de petición (\( ready \)) y reconocimiento (\( accept \)), asegurando que la información sea leída correctamente antes de continuar con la secuencia.

### 3. Caja negra del módulo
```tikz
\usetikzlibrary{shapes.geometric, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\sffamily, >=Stealth, thick]
  % Caja del módulo
  \draw[fill=teal!10, draw=teal, rounded corners] (0,0) rectangle (4.5,3.5);
  \node at (2.25,1.75) [align=center] {\textbf{TRANSMISOR} \\ \textbf{SIMPLE}};
  
  % Entradas (izquierda)
  \draw[<-] (0,2.8) -- (-1.5,2.8) node[left] {\( X \)};
  \draw[<-] (0,1.75) -- (-1.5,1.75) node[left] {\( start \)};
  \draw[<-] (0,0.7) -- (-1.5,0.7) node[left] {\( accept \)};
  
  % Salidas (derecha)
  \draw[->] (4.5,2.2) -- (6,2.2) node[right] {\( Z \)};
  \draw[->] (4.5,1.1) -- (6,1.1) node[right] {\( ready \)};
\end{tikzpicture}
\end{document}
```

### 4. Código AHPL

```ahpl
MODULE: TRANSMISOR_SIMPLE
MEMORY: R; ready
INPUTS: X; start; accept
OUTPUTS: Z; ready

1. -> (!start)/(1)
2. R <- X; ready <- 1
3. -> (!accept)/(3)
4. ready <- 0
   -> (1)
END SEQUENCE
Z = R
END
```

### 5. Tabla de lectura paso a paso

| Paso | Operación | Condición | Estado resultante |
|---|---|---|---|
| `1.` | \( \rightarrow (\overline{start})/(1) \) | \( \overline{start} \) | **Espera activa (Polling):** El control permanece en el paso 1 si la señal \( start \) es \( 0 \). |
| `2.` | \( R \leftarrow X \); \( ready \leftarrow 1 \) | — | **Carga y petición:** Se transfiere el dato de entrada \( X \) al registro de almacenamiento \( R \) y se levanta la bandera de datos listos (\( ready = 1 \)). |
| `3.` | \( \rightarrow (\overline{accept})/(3) \) | \( \overline{accept} \) | **Handshake de espera:** Permanece en el paso 3 hasta que el receptor acuse recibo activando la señal \( accept \). |
| `4.` | \( ready \leftarrow 0 \) | — | **Liberación y ciclo:** Se baja la bandera de datos listos y se retorna de forma incondicional al paso 1 para esperar una nueva transmisión. |
| `—` | \( Z = R \) | En todo momento | **Salida combinacional permanente:** La salida física \( Z \) siempre refleja en paralelo el valor actual almacenado en el registro \( R \). |

