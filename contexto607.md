---
title: "ETN607 — Contexto sesión P2"
scope: vault
tags: [ETN607, sesión, P2, notebooklm]
date_updated: 2026-09-21
hora_inicio: 12:20
worker: alx_gml
---

# ETN607 — Contexto sesión P2

---

## Estado al cierre de sesión (21-09-2026)

### Completado hoy

- Prompt de resolución `ETN607-study-P2v1.md` → revisado, corregido, listo
- Prompt de transcripción `ETN607-transcription_Av7.md` → reescrito desde cero, simplificado para ejercicios únicamente
- Enunciados P2 generados desde PDF → `enunp2.md`
- E1 transcripto por docente → `P2-E1-607.md` (fuente de verdad)
- E1 entregado por NBLM (M1 sin enunciado) → `E1_NBLM.md` — tenía errores
- E1 corregido manualmente → `E1_NBLM_CORREC.md`

### Pendiente

- Probar V7 con PDF de un solo ejercicio (E2–E5)
- Armar E1_FINAL = transcripción + NBLM corregido + NBLM desde PDF
- Decidir si se usan enunciados de `enunp2.md` como complemento en el prompt

---

## Archivos clave

| Archivo | Ubicación | Rol |
|---|---|---|
| `P2-E1-607.md` | `E:\University_vault_2026\` | Transcripción docente E1 — fuente de verdad |
| `P2-E2-607.md` … `P2-E5-607.md` | `E:\University_vault_2026\` | Transcripciones docente E2–E5 |
| `enunp2.md` | `E:\University_vault_2026\` | Enunciados formales E1–E5 generados hoy |
| `E1_NBLM.md` | `E:\University_vault_2026\` | Respuesta de NBLM con M1 — tiene errores de simplificación geométrica |
| `E1_NBLM_CORREC.md` | `E:\University_vault_2026\` | E1_NBLM corregido manualmente — paso intermedio |
| `ETN607-study-P2v1.md` | `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\` | Prompt resolución T3–T4 — listo ✅ |
| `ETN607-transcription_Av7.md` | `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\` | Prompt transcripción ejercicios — listo ✅ |

---

## Prompts activos

### ETN607-study-P2v1.md
Prompt de resolución. NBLM recibe un enunciado y devuelve figura TikZJax + Paso 0→5 + EDOs con `\boxed{}`.

Regla clave agregada hoy: `PROHIBIDO generar archivos en el Studio`.

Mensaje a usar:
```
Resolver: [enunciado desde enunp2.md]
```

### ETN607-transcription_Av7.md
Prompt simplificado — solo ejercicios, sin Cornell, sin IMA, sin marginalia.

NBLM recibe el PDF (un ejercicio por PDF), genera enunciado, TikZJax, transcribe con pasos comentados y corrige si hay errores.

Mensaje a usar:
```
De E1P2.pdf, muéstrame el ejercicio con la figura del bloque m1 con resorte K y dos masas colgantes m2 y m3
```

Nombres de PDF definidos: `E1P2.pdf`, `E2P2.pdf`, … `E5P2.pdf`

---

## Errores que cometió NBLM (registrar para mejorar prompt)

### E1 — M1 (resolución directa)
- **Omitió términos geométricos** en V: no incluyó $b_1/2$, $b_2/2$, $b_3/2$ ni $C_\rho$
- **Agrupó incorrectamente** T en $(m_1+m_2)\dot{x}_1^2$ en lugar de mantener separados $m_1\dot{x}_1^2 + m_2\dot{x}_1^2$
- **No expandió** la EDO de $y_3$ como hace el docente
- **Generó archivo en Studio** — ya corregido con regla PROHIBIDO en el prompt

---

## Flujo E_FINAL (pendiente ejecutar)

```
P2-EX.pdf
    ↓ (Av7 — M transcripción)
NBLM transcribe + TikZJax + pasos
    ↓
EX_NBLM_TRANSC.md
    +
PX-EX-607.md (transcripción docente)
    +
EX_NBLM_CORREC.md (corrección manual si aplica)
    ↓
EX_FINAL.md — ni tan explicativo ni tan crudo
```

---

## PDFs disponibles

- `E1P2.pdf` — E1: bloque horizontal + 2 masas colgantes + 2 resortes ← ya probado con study-P2v1 (M1), falta probar con Av7
- `e2_607xxx_260920_190447.pdf` — contiene E2, E3, E4, E5 juntos en un solo PDF → hay que separar por ejercicio antes de usar Av7

---

## Próximo paso

1. Separar `e2_607xxx_260920_190447.pdf` en PDFs individuales: `E2P2.pdf`, `E3P2.pdf`, `E4P2.pdf`, `E5P2.pdf`
2. Probar `ETN607-transcription_Av7.md` con `E1P2.pdf` primero
3. Si funciona → repetir E2–E5
4. Armar `E1_FINAL.md` como plantilla del formato final
