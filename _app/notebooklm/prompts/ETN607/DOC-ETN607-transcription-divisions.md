---
title: "DOC — ETN607 Transcription Divisions Prompt"
galaxy_body: beacon
scope: vault
audience: [usuario, claude]
tags: [beacon, notebooklm, ETN607, infraestructura, prompts, transcripción, divisiones]
date_created: 2026-09-20
date_updated: 2026-09-20
reviewed: 2026-09-20
status: archivado — no probado
---

# DOC — ETN607 Transcription Divisions Prompt

Documentación del prompt de transcripción para hojas con plantillas de divisiones (Cornell / Áurea) en ETN607.

> [!warning] Estado
> Este prompt **nunca fue probado en NotebookLM**. Las plantillas TABnote con divisiones fueron creadas, pero el flujo completo no fue validado. Movido a `legacy/` como referencia para una implementación futura.

---

## Archivo

| Archivo | Rol | Estado |
|---|---|---|
| `legacy/ETN607-transcription-divisions.md` | Transcripción para hojas con divisiones (Cornell / Áurea) | archivado — no probado |

---

## Diferencia con `ETN607-transcription_Av6`

`Av6` asume plantillas simples (sin líneas divisorias). Este prompt fue diseñado para el caso en que el apunte usa plantillas con 4 zonas delimitadas por líneas gruesas:

```
┌─────────────────────────────┐
│         TÍTULO              │  ← franja superior
├──────────────┬──────────────┤
│   zona       │   zona       │  ← zona corta + zona desarrollo
│   corta      │   desarrollo │
├──────────────┴──────────────┤
│         RESUMEN             │  ← franja inferior
└─────────────────────────────┘
```

La zona corta puede estar a izquierda (Cornell) o derecha (Áurea):

| Plantilla | Zona corta | Zona desarrollo | Diferencia |
|---|---|---|---|
| Cornell | izquierda (angosta) | derecha (amplia) | ::cue ← izq · ::note ← der |
| Áurea | derecha (angosta) | izquierda (amplia) | ::note ← izq · ::cue ← der |

En ambas, el alumno ya llenó ::cue y ::note durante la clase. NLM transcribe ambas zonas literalmente, sin reformular ni inventar contenido.

---

## Qué hace este prompt

### Detección de plantilla
Antes de transcribir, NLM inspecciona la estructura visual de la página:
- Líneas divisorias gruesas → plantilla con divisiones → aplica este flujo
- Sin líneas divisorias → plantilla simple → usar Av6
- Ambigüedad → pregunta al usuario antes de continuar

### Orden de lectura
Independiente de la plantilla:
1. Zona título (franja superior)
2. Zona desarrollo (::note) — arriba hacia abajo
3. Zona corta (::cue) — arriba hacia abajo
4. Zona resumen (franja inferior)

Excepción: si un desarrollo continúa visualmente entre zonas (fórmula partida, tabla) → leerlo como unidad.

### Mensajes disponibles

| Mensaje | Trigger | Acción |
|---|---|---|
| M1 | "De apuntesTX, muéstrame subtítulo Y [HASTA Z] con complemento nivel B/C" | Transcripción + complemento del rango indicado |
| M2 | "De apuntesTX, subtítulo Y, muéstrame ejercicios resueltos" | Ejercicios de libros fuente para ese subtítulo |
| M3 | "De apuntesTX, muéstrame el ejercicio [ec inicial] hasta [ec final]" | Transcripción de ejercicios del cuaderno por enunciado/ecuación |

### Output por subtítulo

El bloque Cornell viene del apunte — transcripción literal de ambas zonas. Diferencia clave respecto a Av6: el ::cue lo llenó el alumno, no NLM. El Complemento NLM compensa esto aportando resumen, palabras clave y preguntas desde los libros fuente, y siempre está presente.

---

## Lo que estaba implementado

- Detección de plantilla Cornell vs Áurea por posición de zona corta
- Orden de lectura por zonas
- Transcripción literal de ::cue y ::note
- Detección y transcripción de IMA, marginalia, callouts, figuras
- Complemento NLM automático (resumen + palabras clave + preguntas)
- Complemento B/C desde libros fuente
- Niveles B/C con misma lógica que Av6
- TikZJax y formato array LaTeX
- Fuentes cargadas: mismas que Av6 (Taylor, Goldstein, Wells, Nelson, Lim, Alonso & Finn)

## Lo que falta validar

- Comportamiento real de NLM al detectar líneas divisorias en el PDF
- Precisión en la distinción Cornell vs Áurea
- Si NLM respeta el orden de lectura (::note antes que ::cue) en hojas con divisiones
- El bug del identificador cornell en línea separada (heredado de Av6, sin confirmar en este contexto)
- Compatibilidad con plantillas TABnote reales — las plantillas fueron creadas pero no usadas con este prompt

---

## Base para una implementación futura

**Punto de partida:** este archivo en legacy/.

**Qué revisar antes de activar:**
1. Confirmar que las plantillas TABnote con divisiones están en uso activo
2. Probar detección de plantilla con un PDF real de 1–2 páginas
3. Validar orden de lectura (::note → ::cue)
4. Comparar output con Av6 en la misma página para detectar diferencias

**Relación con Av6:** podrían unificarse en un solo prompt con detección automática de plantilla al inicio, en lugar de mantener dos prompts separados.

---

%%
# galaxy-links
[[ETN607-transcription-divisions]]
[[ETN607-transcription_Av6]]
[[DOC-ETN607-transcription]]
%%
