---
title: "ETN607 — Contexto sesión P2"
scope: vault
tags: [ETN607, sesión, P2, notebooklm]
date_updated: 2026-09-21
hora_inicio: 16:40
worker: krajo
---

# ETN607 — Contexto sesión P2

---

## Estado al cierre de sesión (21-09-2026 · sesión 2)

### Completado hoy

- `E1_F.md` → generado, revisado, EDOs factorizadas, enunciado colocado por usuario ✅
- `E2_F.md` → generado, figura v4 corregida (2 cuñas trapecio, $B_2 \to B$), desarrollo completo ✅
- `E3_F.md` → generado, figura corregida ($m_3$ como masa puntual, ramal izq de $m_2$ al piso), nota auxiliar de expansión de $y_1$ ✅
- `E4_F.md` → generado, péndulo invertido (hacia arriba), términos de corrección en EDO de $\theta$ mantenidos explícitos ✅
- `E5_F.md` → **pendiente**

### Pendiente

- Generar `E5_F.md` (falta fuente: `P2-E5-607.md` + `E5_NBLM.md`)
- Revisar si los enunciados en cada `EX_F.md` son suficientes o hay que ajustarlos
- Verificar figuras en Obsidian (E2 v4, E3, E4 péndulo invertido)

---

## Archivos EX_F generados esta sesión

| Archivo | Ubicación | Estado |
|---|---|---|
| `E1_F.md` | `E:\University_vault_2026\` | ✅ completo |
| `E2_F.md` | `E:\University_vault_2026\` | ✅ completo — figura v4, $B$ pared a pared |
| `E3_F.md` | `E:\University_vault_2026\` | ✅ completo — $m_3$ puntual, GDL $(y_3, a)$ |
| `E4_F.md` | `E:\University_vault_2026\` | ✅ completo — péndulo invertido, términos $\dot{x}\sin\theta\dot{\theta}$ explícitos |
| `E5_F.md` | `E:\University_vault_2026\` | ⏳ pendiente |

## Archivos fuente

| Archivo | Ubicación | Rol |
|---|---|---|
| `P2-E1-607.md` … `P2-E5-607.md` | `E:\University_vault_2026\` | Transcripciones docente — fuente de verdad |
| `E1_NBLM.md` … `E4_NBLM.md` | `E:\University_vault_2026\` | Entregas de NBLM por ejercicio |
| `ETN607-study-P2v1.md` | `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\` | Prompt resolución T3–T4 ✅ |
| `ETN607-transcription_Av7.md` | `E:\University_vault_2026\_app\notebooklm\prompts\ETN607\` | Prompt transcripción ejercicios ✅ |

---

## Prompts activos

### ETN607-transcription_Av7.md
NBLM recibe PDF (un ejercicio por PDF) → genera enunciado + TikZJax + transcripción con pasos comentados.

Mensaje a usar:
```
De [EXP2.pdf], muéstrame el ejercicio con [descripción breve del sistema]
```

### ETN607-study-P2v1.md
NBLM recibe enunciado → devuelve figura TikZJax + Paso 0→5 + EDOs con `\boxed{}`.
Regla activa: `PROHIBIDO generar archivos en el Studio`.

Mensaje a usar:
```
Resolver: [enunciado]
```

---

## Notas del método EX_F

- Fuentes: `PX-EX-607.md` (docente) + `EX_NBLM.md` → combinar lo mejor
- Figura: preferir NBLM si es correcta; corregir encima sin borrar versiones anteriores
- Notación: $x_1, y_2$… consistente, $C_0$ para constantes de integración
- EDOs: factorizar cuando corresponda, pero **mantener términos de corrección explícitos** (caso E4: $-\dot{x}\sin\theta\dot{\theta} + \dot{x}\dot{\theta}\sin\theta$)
- No simplificar pasos intermedios que el docente dejó explícitos

---

## Próximo paso

1. Generar `E5_F.md` — leer `P2-E5-607.md` + `E5_NBLM.md` y combinar
2. Revisión final de figuras en Obsidian (E2 v4, E3, E4)
3. Decidir si se agrega sección de linealización en E4 (el docente mencionó anular $\sin\theta$ para el informe)
