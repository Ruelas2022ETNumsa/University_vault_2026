---
title: "ETN607 — Contexto sesión P2"
scope: vault
tags: [ETN607, sesión, P2, notebooklm]
date_updated: 2026-09-21
hora_inicio: 22:41
worker: alx-rul
---

# ETN607 — Contexto sesión P2

---

## Estado al cierre de sesión (21-09-2026 · sesión 3)

### Completado hoy

- `E1_F.md` → `E5_F.md` → todos generados y completos ✅
- Ejercicios complementarios (variantes) en curso — generados con NBLM
- `E11.md` generado → figura v4 corregida, formato de pasos corregido ✅
- Prompt `ETN607-comp_indice_BCv4ii.md` → mejorado y renombrado como `ETN607-comp_indice_BCv5ii.md` ✅
  - Eliminados: Mensajes 1 y 2 (complementos B/C), callout `ad-note`, niveles B/C
  - Conservados: Mensaje 3 (ejemplos similares, gatillo independiente), Mensaje 4 (uso principal)
  - Regla de pasos actualizada: paso = secuencia con resultado esperado que el siguiente usa como input
- `E12.md` generado — variante de E11 con $m_4$ en ramal izquierdo de $m_1$ ✅

### Pendiente

- Continuar generando ejercicios complementarios (variantes) con NBLM usando `ETN607-comp_indice_BCv5ii.md`
- Verificar figuras en Obsidian (E2 v4, E3, E4 péndulo invertido)
- Decidir si se agrega sección de linealización en E4 (el docente mencionó anular $\sin\theta$ para el informe)

---

## Archivos EX_F — estado final

| Archivo | Ubicación | Estado |
|---|---|---|
| `E1_F.md` | `E:\University_vault_2026\` | ✅ completo |
| `E2_F.md` | `E:\University_vault_2026\` | ✅ completo — figura v4, $B$ pared a pared |
| `E3_F.md` | `E:\University_vault_2026\` | ✅ completo — $m_3$ puntual, GDL $(y_3, a)$ |
| `E4_F.md` | `E:\University_vault_2026\` | ✅ completo — péndulo invertido, términos $\dot{x}\sin\theta\dot{\theta}$ explícitos |
| `E5_F.md` | `E:\University_vault_2026\` | ✅ completo |

## Ejercicios complementarios generados

| Archivo | Ubicación | Estado |
|---|---|---|
| `E11.md` | `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_2\ejercicios P2\` | ✅ completo — figura corregida, pasos corregidos |
| `E12.md` | `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_2\ejercicios P2\` | ✅ enunciado + tikz — variante E11 con $m_4$ en ramal izq. de $m_1$ → 2 GDL, sistema acoplado |

---

## Prompt activo

### ETN607-comp_indice_BCv5ii.md
`E:\University_vault_2026\_app\notebooklm\prompts\ETN607\ETN607-comp_indice_BCv5ii.md`

Mensajes disponibles:
- **Mensaje 3** — `"[Tema] · [Subtítulo] · ejercicio"` → NBLM busca ejemplos similares en libros y los resuelve (gatillo independiente)
- **Mensaje 4** — `"Resolver: [enunciado]"` → uso principal, resuelve enunciado propio consultando E1_F–E5_F como referencia de estilo

Regla de pasos activa: paso = secuencia de acciones con un resultado concreto que el paso siguiente usa como input.

---

## Archivos fuente

| Archivo | Ubicación | Rol |
|---|---|---|
| `P2-E1-607.md` … `P2-E5-607.md` | `E:\University_vault_2026\` | Transcripciones docente — fuente de verdad |
| `E1_NBLM.md` … `E5_NBLM.md` | `E:\University_vault_2026\` | Entregas de NBLM por ejercicio |
| `ETN607-comp_indice_BCv5ii.md` | `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\` | Prompt ejercicios complementarios — activo ✅ |
| `ETN607-transcription_Av7.md` | `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\` | Prompt transcripción ejercicios ✅ |

---

## Notas del método EX_F

- Fuentes: `PX-EX-607.md` (docente) + `EX_NBLM.md` → combinar lo mejor
- Figura: preferir NBLM si es correcta; corregir encima sin borrar versiones anteriores
- Notación: $x_1, y_2$… consistente, $C_0$ para constantes de integración
- EDOs: factorizar cuando corresponda, pero **mantener términos de corrección explícitos** (caso E4: $-\dot{x}\sin\theta\dot{\theta} + \dot{x}\dot{\theta}\sin\theta$)
- No simplificar pasos intermedios que el docente dejó explícitos

---

## Notas del método — ejercicios complementarios (variantes)

- Claude genera: **enunciado + tikz + descripción de figura** únicamente
- La resolución la hace **NBLM** — Claude NO resuelve estos ejercicios
- Flujo: Claude genera enunciado → usuario lo pasa a NBLM con Mensaje 4

---

## Próximo paso

1. Continuar generando ejercicios complementarios con `ETN607-comp_indice_BCv5ii.md`
2. Verificar figuras en Obsidian (E2 v4, E3, E4)
3. Decidir linealización en E4
