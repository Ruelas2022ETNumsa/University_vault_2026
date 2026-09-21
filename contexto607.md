---
title: "ETN607 — Continuación sesión P2"
scope: vault
audience: [usuario, claude]
tags: [ETN607, sesión, continuación, P2, notebooklm]
date_created: 2026-09-21
status: activo
---

# ETN607 — Continuación sesión P2

Archivo de continuación de sesión. Leer este archivo al inicio de una nueva sesión para retomar el trabajo del Parcial 2 sin perder contexto.

---

## Estado actual (21-09-2026)

El flujo de resolución de ejercicios para P2 está **listo para usar en NLM**. Los prompts están creados y documentados. Los ejercicios del docente están digitalizados.

Lo que **no se hizo todavía**: usar NLM con los prompts. Todo lo de abajo está preparado pero no probado en sesión real.

---

## Archivos creados en esta sesión

### Ejercicios resueltos del docente — digitalizados

Ubicación: `E:\University_vault_2026\`

| Archivo | Sistema | N | Coord. |
|---|---|---|---|
| `P2-E1-607.md` | Bloque horizontal + 2 masas colgantes + 2 resortes (cable) | 2 | x₁, y₃ |
| `P2-E2-607.md` | Bloque en plano 60° + masa colgante (cable) | 1 | x₁ |
| `P2-E3-607.md` | 3 masas + polea + 2 resortes | 2 | y₃, a |
| `P2-E4-607.md` | Carro M + péndulo simple m | 2 | x, θ |
| `P2-E5-607.md` | Péndulo doble (igual longitud ℓ) | 2 | θ, φ |

> **Nota E3:** es el ejercicio con más correcciones intermedias en el apunte del docente. Las EDOs finales deben verificarse contra Wells Cap.4 cuando se use en NLM.

Estos archivos son las **fuentes de referencia** que se cargan en el notebook de NLM junto con los libros.

### Enunciados para NLM

Ubicación: `E:\University_vault_2026\Untitled 1.md`

Contiene los 5 enunciados formales (E1–E5) con descripción detallada del sistema físico, coordenadas, restricciones y lo que se pide. Listos para pasar a NLM.

### Prompts creados

Ubicación: `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\`

| Archivo | Tipo | Para | Estado |
|---|---|---|---|
| `ETN607-study-P2v1.md` | Prompt NLM | Resolución de ejercicios T3–T4 + TikZJax | activo ✅ |
| `ETN607-ejercicio-detector_P2.md` | Prompt Claude | Generar enunciados desde foto/descripción | activo ✅ |
| `ETN607-ejercicio-detector_P1.md` | Prompt Claude | Igual pero T1–T2 | legacy |

---

## Cómo usar los prompts

### Para resolver un ejercicio en NLM

**Notebook necesario:** el que tiene cargados Taylor, Goldstein, Wells, Lim + los P2-EX-607.md

**Prompt a cargar:** `ETN607-study-P2v1.md`

Tres formas de enviar un ejercicio:

```
M1 — enunciado directo:
Resolver: [enunciado completo del sistema]

M2 — enunciado desde el detector:
Enunciado: [texto que generó el detector P2]

M3 — variante de ejercicio base:
Variante de P2-E4: [descripción del cambio, ej: agregar fricción al carro]
```

NLM responde con: figura TikZJax → resolución Paso 0 al Paso 5 → EDOs encuadradas con \boxed{}.

### Para generar un enunciado desde una foto (pre-NLM)

**Prompt a usar en Claude:** `ETN607-ejercicio-detector_P2.md`

```
Caso A — descripción:
[describir el sistema en texto]

Caso B — foto:
[subir imagen del ejercicio]
```

Claude devuelve el enunciado formal + snippet listo para pegar en NLM como M2.

---

## Flujo completo recomendado

```
foto del ejercicio
      ↓
Claude + detector_P2
      ↓
snippet "Enunciado: ..."
      ↓
NLM + study-P2v1  →  figura TikZJax + resolución completa
      ↓
comparar EDOs con el apunte del docente (P2-EX-607.md)
```

Para variantes o ejercicios propios → saltar directo a NLM con M1 o M3.

---

## Decisión pendiente — estrategia de estudio

Se discutió pero no se cerró:

- **Opción A** (solo ejercicios): usar los P2-EX-607 como base, generar variantes, resolver con NLM. Sin transcripción de apuntes teóricos.
- **Opción B** (transcripción + ejercicios): transcribir los apuntes de T3–T4 primero con `ETN607-transcription_Av6`, luego resolver ejercicios.

**Conclusión de la sesión:** el parcial evalúa solo resolución de ejercicios → **Opción A es suficiente**. La transcripción queda disponible si surge una duda teórica puntual.

---

## Prompt de transcripción (si se necesita)

**Prompt a cargar en NLM:** `ETN607-transcription_Av6.md`

Ubicación: `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\ETN607-transcription_Av6.md`

```
M1 — transcribir subtítulo:
De apuntesTX, muéstrame [subtítulo Y] [HASTA subtítulo Z]

M2 — transcribir ejercicios del cuaderno:
De apuntesTX, muéstrame el ejercicio [ec inicial] hasta [ec final]

M3 — corregir contra libros fuente:
Corrige [subtítulo Y] [HASTA Z] · fuente apuntesTX
```

> El M3 de Av6 corrige contra T1–T2 solamente. Para T3–T4 no tiene libros de corrección configurados — si se necesita corrección habría que agregar Taylor Cap.7 y Goldstein Cap.1–2 al prompt.

---

## Documentación de referencia

| DOC | Cubre |
|---|---|
| `DOC-ETN607-study.md` | Prompts de resolución (study-P2v1, detector P2) |
| `DOC-ETN607-transcription.md` | Prompts de transcripción (Av6, comp_apuntes, comp_indice) |
| `DOC-ETN607-transcription-divisions.md` | Prompt de divisiones Cornell/Áurea — archivado, no probado |

Todos en: `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\`

---

## Próximo paso sugerido

Probar el flujo completo con **E4 (carro + péndulo)** — es el ejercicio más limpio del lote:

1. Cargar `ETN607-study-P2v1.md` en NLM como prompt del sistema
2. Cargar `P2-E4-607.md` como fuente junto con Taylor y Wells
3. Enviar: `Enunciado: [texto de E4 desde Untitled 1.md]`
4. Comparar figura TikZJax y EDOs con el apunte del docente
5. Si el output cierra → repetir con E1, E2, E3, E5 en ese orden
