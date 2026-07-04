# Ejemplos: obsidian-cornell-notes

---

## 1. Fila simple (cue + note)

````cornell
::cue
¿Qué es una función?
::note
Una relación entre dos conjuntos donde cada elemento del dominio
tiene **exactamente una** imagen en el codominio.
````

---

## 2. Múltiples filas en un solo bloque

````cornell
::cue
¿Qué es la derivada?
::note
La tasa de cambio instantánea de una función:
$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$

::cue
¿Qué es la integral?
::note
El área bajo la curva. Operación inversa a la derivada:
$\int_a^b f(x)\,dx = F(b) - F(a)$

::cue
Regla de la cadena
::note
Si $y = f(g(x))$, entonces:
$\frac{dy}{dx} = f'(g(x)) \cdot g'(x)$
````

---

## 3. Cue-only (sin ::note)

````cornell
::cue
Tema pendiente: repasar límites al infinito

::cue
Ejercicio para resolver: $\lim_{x \to 0} \frac{\sin x}{x}$
````

---

## 4. Contenido rico: callouts, código, tabla

````cornell
::cue
> [!tip] Regla mnemónica
> **CCANNID** para axiomas de cuerpo
::note
> [!warning] No confundir
> El neutro aditivo ($0$) ≠ neutro multiplicativo ($1$)

| Operación | Neutro |
|-----------|--------|
| Suma      | $0$    |
| Producto  | $1$    |

::cue
Ejemplo en Python
::note
```python
def derivada_numerica(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h
```
````

---

## 5. Tu estructura actual (::note primero)

> El plugin acepta empezar con `::note` en lugar de `::cue`.
> Útil para mantener tu formato actual: Desarrollo izquierda, Claves derecha.
> **Pero el layout lo invierte**: ::note va al 72% (derecha por defecto).
> Probá si tu vault lo renderiza bien con ::note primero.

````cornell
::note
📝 **Desarrollo**

Si $a, b \in \mathbb{R}$:
- $a + b = b + a$ (conmutatividad)
- $(a+b)+c = a+(b+c)$ (asociatividad)

::cue
🔑 **Claves**

Conmutatividad · Asociatividad

¿Qué axiomas rigen la suma?
````
