---
tags: [robotic-arm, compra, checklist, hub]
project: Robotic_Arm_AI
hardware: LEGO Robot Inventor 51515
created: 2026-10-09
related: "[[arm_todo]]"
---

# arm_hub-compra-checklist

Revisión simple al comprar un set 51515 (nuevo o usado). No confundir con [[robarm-compra]].

## Contenido a verificar
- [ ] Hub
- [ ] Batería recargable (propia del hub, no usa pilas AA)
- [ ] Cable micro USB
- [ ] 4 motores
- [ ] Sensor de color
- [ ] Sensor de distancia

## Caso 1: todo sellado de fábrica
- [ ] Todas las bolsas selladas (no solo algunas).
- [ ] Insertar batería y mantener el **botón central 1-2 s**.
- [ ] Botón central **verde** = encendido y batería ≥ 20% (según LEGO).
- Con esto alcanza; la prueba con app es un extra.

## Caso 2: algo abierto
- [ ] Intentar encender igual (la batería puede o no tener carga).
- [ ] Si no responde: conectar micro USB a cargador o power bank.
- [ ] Mirar la **luz junto al puerto USB** (no es un aro que se llene):
  - apagada = no carga
  - **roja = cargando**
  - **verde = carga completa**
  - **amarilla = problema con el cargador** (probar otro cargador o cable)
- [ ] Carga completa: 2-5 h. Basta unos minutos para confirmar que enciende.
- [ ] Si tras cargar un rato sigue sin responder: señal de alerta.
- [ ] Matriz de luces 5x5: ver que se encienda completa, sin píxeles muertos.

## Pruebas extra (opcionales)
- Programa de prueba preinstalado del SPIKE Prime: corazón al encender, tocar botón central, motor de un lado y sensor del lado opuesto. (?) No confirmado en el hub del Inventor.
- Si se usa la app SPIKE 3: probablemente pida actualizar el Hub OS (tarda e implica internet). No hacerlo en la tienda.
- Otros colores del botón central (blanco, naranja/rojo/violeta intermitente) son códigos de error. Anotar el color y buscarlo.

## Llevar
- [ ] Cable micro USB
- [ ] Cargador o power bank
- [ ] Celular con la app SPIKE instalada (opcional)

Ver también: [[arm_pybricks-notas]], [[arm_todo]]
