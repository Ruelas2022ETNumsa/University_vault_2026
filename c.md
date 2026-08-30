```text
5. → (~IR & ~IR, ~IR & IR, IR) / (10, 20, 30)
```

| Paso | Operación | Condición | Estado resultante |
|---|---|---|---|
| `5.` | \( \rightarrow (\overline{IR}_0 \land \overline{IR}_1, \overline{IR}_0 \land IR_1, IR_0)/(10, 20, 30) \) | — | **Bifurcación de tres vías mutuamente excluyente** según el valor de los bits \( IR_0 \) e \( IR_1 \). |

### **Activación de las ramas según la combinación de bits**

Las tres condiciones especificadas en la tupla son **mutuamente excluyentes** y su suma lógica es igual a **1**:

*   **Combinación `00` (\( IR_0 = 0 \) e \( IR_1 = 0 \)):** Satisface la primera condición, \( \overline{IR}_0 \land \overline{IR}_1 \). El flujo de control salta al primer destino, que corresponde al **paso 10**.
*   **Combinación `01` (\( IR_0 = 0 \) e \( IR_1 = 1 \)):** Satisface la segunda condición, \( \overline{IR}_0 \land IR_1 \). El flujo de control salta al segundo destino, que corresponde al **paso 20**.
*   **Combinaciones `10` y `11` (\( IR_0 = 1 \)):** Satisface la tercera condición, \( IR_0 \), de manera independiente al estado del bit \( IR_1 \). El flujo de control salta al tercer destino, correspondiente al **paso 30**.

💡 ¿Te gustaría ver cómo se realiza la síntesis física y la implementación de las ecuaciones de compuertas lógicas de control para este paso de bifurcación de tres vías?