---
title: HP Prime G2 — Guía de configuración y uso
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
tags:
  - beacon
  - hp-prime
  - calculadora
  - ingenieria-electronica
  - tars
date_created: 2026-09-02
date_updated: 2026-09-02
status: activo
---

# HP Prime G2 — Guía de configuración y uso (TARS)

Guía de configuración inicial, actualización de firmware y uso de la HP Prime G2,
nombrada TARS. Documentada en sesión del 2026-09-02 (16:40 — ~19:00).

---

## Identificación del dispositivo

| Campo | Valor |
|---|---|
| Modelo | HP Prime G2 |
| Revisión de hardware | D |
| Número de serie | 9CJ5... |
| Nombre asignado | TARS |
| Software | 2.4 |
| Build date | 2025-09-15 |
| Software revision | 15515 |
| Versión CAS | 1.5.0 |
| MicroPython | 1.9.4 |
| Sistema operativo | V2.060.650 |

> Revisión D = G2 confirmado. Tiene WiFi integrado y CPU ARM Cortex-A7 a 528 MHz.

---

## Acceso a configuración

```
Shift + Home → Settings (configuración general)
```

La configuración está dividida en 4 páginas.

---

## Página 1/4 — Configuración de inicio

| Opción | Valor elegido | Notas |
|---|---|---|
| Medida del ángulo | Grados | Cambiar a radianes con Shift+7 cuando se necesite |
| Formato de números | Ingeniería, 5 decimales | Exponentes múltiplos de 3 (kilo, mega, mili, micro) |
| Agrupación de dígitos | 123.456,789 | Formato latinoamericano |
| Entrada | Libro de texto (Textbook) | Muestra fórmulas como en papel |
| Enteros | HEX, 16 bits | Para electrónica digital y microcontroladores de 16 bits |
| Idioma | Español | |

### Nota sobre formato de números

Opciones disponibles: Estándar / Fijo / Científico / **Ingeniería** / Flotante / Redondeo.
Ingeniería es ideal para electrónica porque los exponentes son siempre múltiplos de 3,
alineados con los prefijos del SI (kilo=10³, mega=10⁶, mili=10⁻³, micro=10⁻⁶).

### Nota sobre el modo de entrada

- Libro de texto: fórmulas visualmente igual que en apuntes → menos errores
- Algebraico: entrada lineal clásica
- RPN: primero valores, luego operador (estilo HP clásico, curva de aprendizaje)

---

## Página 2/4 — Pantalla y sistema

| Opción | Valor elegido | Notas |
|---|---|---|
| Tamaño de fuente | Grande | Más cómodo para leer fórmulas |
| Nombre de calculadora | TARS | Referencia a la IA de Interstellar |
| Vis. libro de texto | Activado | |
| Pantalla del menú | Activado | |
| Tiempo (reloj en standby) | Activado | El ahorro al desactivarlo es insignificante |
| Fecha | 02/09/2026, DD/MM/AAAA, Lu | |
| Tema de color | Oscuro + Azul | La pantalla es LCD — el color no afecta el consumo |

> En pantallas LCD el color del tema no afecta el consumo de batería
> (la retroiluminación siempre está encendida al mismo nivel).

---

## Página 3/4 — Modo y ángulo predeterminado

| Opción | Valor elegido | Notas |
|---|---|---|
| Configuración | Custom Mode | Acceso completo a CAS, programación y todas las funciones |
| Ángulo predeterminado | Grados | Cambiar a radianes con Shift+7 según la necesidad |

### Opciones adicionales (aparecen al activar Custom Mode)

| Opción | Valor elegido | Notas |
|---|---|---|
| Tiempo de espera | 30 minutos | Balance entre comodidad y ahorro de batería |
| Contraseña | Pendiente | Configurar cuando se domine el funcionamiento |
| Memoria | Conservar y restaurar | Guarda estado completo al apagar, restaura al encender |
| Parpadeo de LED | A gusto del usuario | Solo activo en modo examen — sin efecto en uso normal |

---

## Página 4/4 — Red inalámbrica

WiFi integrado (G2). Al momento de la configuración no se encontró ninguna red.
Pendiente configurar cuando haya red disponible.

### Modo examen (referencia, no usar en configuración normal)

La HP Prime tiene modo examen para deshabilitar funciones durante evaluaciones.
El LED en el borde superior parpadea para que el supervisor lo vea a distancia.

| Perfil | Uso |
|---|---|
| Básico | Examen genérico simple |
| Custom Mode | Configurable por el profesor |
| CSE Nederland | Solo para exámenes nacionales de Países Bajos — no aplica |

> No activar el modo examen accidentalmente. Para salir: conectar por USB a la PC.

---

## Software instalado en PC

| Programa | Versión / Fecha | Uso |
|---|---|---|
| HP Prime Connectivity Kit | 2025-09-15 (x64) | Sincronizar, transferir apps, actualizar firmware |
| HP Prime Virtual Calculator | 2025-09-15 (x64) | Emulador completo de TARS en PC |

### Documentación descargada (español)

- `Emulator_Help_ESP_2015_06_17_1.pdf` — ayuda del emulador
- `User_Guide_ESP_2018_01_12_1.pdf` — manual completo ← el más útil
- `Quick_Start_Guide_ESP_2017_11_20_1.pdf` — guía rápida
- `Datastreamer_ESP_2014_12_03_1.pdf` — manual del datastreamer

---

## Actualización de firmware

### Versión antes / después

| | Antes | Después |
|---|---|---|
| Software | anterior a 2.4 | **2.4** |
| Build date | 2020 | **2025-09-15** |
| Método | — | USB + Connectivity Kit |

### Procedimiento de actualización

1. Instalar HP Prime Connectivity Kit
2. Abrir el programa → aceptar descarga de actualizaciones
3. Conectar TARS por USB
4. El programa detecta TARS y ofrece actualizar → aceptar
5. No desconectar USB ni apagar durante el proceso

### Problema ocurrido y solución

Durante la actualización, TARS se apagó al finalizar porque la batería estaba agotada.
La pantalla mostraba un pequeño destello al encender/apagar el switch de corriente
pero no arrancaba completamente.

**Causa:** la batería se agotó justo cuando el firmware intentó reiniciarse para completar
la instalación. El firmware quedó instalado correctamente pero sin energía para arrancar.

**Solución aplicada:**
1. Desconectar el cable USB
2. Abrir la tapa trasera con destornillador
3. Retirar la batería
4. Conectar USB a la PC **sin batería**
5. La calculadora arrancó con la energía del USB y completó la instalación
6. Con el USB aún conectado, colocar la batería de vuelta
7. Cerrar la tapa y dejar cargando 20-30 minutos

> Este problema es documentado y frecuente en foros de HP. No representa daño permanente.
> El LED en el borde superior y el destello de pantalla son señales de que la calc no está muerta.

---

## Pendiente

- Configurar WiFi de TARS
- Aprender funciones CAS básicas para ingeniería electrónica:
  - Simplificación de expresiones
  - Derivadas e integrales
  - Números complejos y fasores
  - Manejo de fracciones y ecuaciones
- Configurar contraseña de TARS (cuando se domine el funcionamiento)
- Explorar la calculadora virtual en PC

---

%%
# galaxy-links
[[_app/Tars/HP_Prime_guide.md]]
%%
