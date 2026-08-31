### **Ejemplo 1: Destino condicionado (control en la izquierda)**

En este caso, la condición se ubica a la izquierda de la asignación para controlar de forma directa la entrada de habilitación de reloj (*clock enable*) de los registros de destino:

```ahpl
A * ~a <- B ; D * a <- C
```

* **Interpretación:** Si \( a = 0 \) (es decir, el término negado \( \sim a \) es verdadero), se habilita el reloj del registro \( A \) para capturar el valor de \( B \) (\( A \leftarrow B \)). Si \( a = 1 \), se habilita el reloj del registro \( D \) para capturar el valor de \( C \) (\( D \leftarrow C \)). Ambas operaciones ocurren de manera simultánea en el mismo paso y bajo el mismo ciclo de reloj. Si una condición de control es \( 0 \), el registro destino correspondiente no se modifica y retiene su estado previo.

---

### **Ejemplo 2: Origen seleccionado (control en la derecha)**

Aquí, la condición se coloca a la derecha del operador de asignación para detallar un circuito combinacional de selección de bus o multiplexor:

```ahpl
D <- (A ! B ! C) * (f, g, h)
```

* **Interpretación:** El registro \( D \) recibirá el contenido de uno de los tres registros de origen según cuál de las señales de control de un solo bit (\( f, g, h \)) valga \( 1 \). Si \( f = 1 \), se transfiere \( A \) (\( D \leftarrow A \)); si \( g = 1 \), se transfiere \( B \) (\( D \leftarrow B \)); y si \( h = 1 \), se transfiere \( C \) (\( D \leftarrow C \)). Se asume que las variables de control en el vector de la derecha son mutuamente excluyentes. Si todas son \( 0 \), se transfiere un vector de ceros hacia el registro destino.

---

### **¿Qué hace el operador `*` (Asterisco)?**

El operador **`*`** representa una **condición aplicada a una transferencia o conexión de datos** en AHPL. Su comportamiento lógico y físico varía según su posición con respecto a la asignación:

1. **A la izquierda de la asignación (`<-`):** Controla las líneas de habilitación de reloj (*clock*) de los registros. Físicamente, el pulso de reloj solo se propaga e impacta en los flip-flops del registro destino si la condición booleana asociada es verdadera (\( 1 \)).
2. **A la derecha de la asignación (`<-` o `=`):** Especifica compuertas lógicas de enrutamiento y circuitos de bus. Físicamente, actúa como un multiplexor que selecciona combinacionalmente cuál vector de datos de origen se propagará hacia el bus o registro receptor basándose en el estado del vector de control.

---

### **¿Qué hace el operador `!` (Admiración) en el Ejemplo 2?**

El operador **`!`** representa la operación de **concatenación de filas** (*row catenation*). 

* **No debe confundirse con un complemento lógico (NOT)**. 
* En este contexto, su función es agrupar físicamente los registros vectoriales independientes \( A \), \( B \) y \( C \) para formar una estructura matricial compuesta (un arreglo de filas). Esto permite que el operador de selección condicional `*` interactúe con el vector de señales \( (f, g, h) \) y decida combinacionalmente cuál fila de esa matriz es enviada como origen al registro \( D \).

---

💡 ¿Te gustaría que diseñemos un módulo AHPL completo donde usemos este patrón de origen seleccionado para implementar un decodificador o un multiplexor de bus de datos?