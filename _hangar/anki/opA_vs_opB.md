Tengo todo lo que necesito. La tabla:

---

## Opción A (Marginalia) vs Opción B (Flashcards) — para ingeniería en Galaxy

| Criterio | Opción A — Marginalia | Opción B — Flashcards |
|---|---|---|
| **LaTeX** | ✅ con Script 2 (toggle automático) | ✅ nativo, sin scripts |
| **Sintaxis en nota activa** | ✅ invisible — la marginalia no interrumpe el flujo de la nota | 🟡 `#card` y `::` visibles en el body |
| **Integración con notas galaxy** | ✅ natural — planet/moon/comet siguen leyéndose normalmente | 🟡 los tags `#card` ensucian visualmente |
| **Cloze** | ❌ no nativo | ✅ con `==highlight==` — útil para definiciones parciales |
| **Reversed** | ❌ no nativo | ✅ con `#card-reverse` |
| **Inline cards** | 🟡 sintaxis `%%> ;; %%` | ✅ con `::` más limpio |
| **Deck por carpeta** | 🟡 por tag mapping (manual) | ✅ automático — la carpeta galaxy ya es el deck |
| **Blur / Active Recall en Obsidian** | ✅ modo estudio nativo con el ojo 👁️ | ❌ no existe |
| **Compatibilidad con estructura galaxy** | ✅ alta — marginalia vive al margen, no toca el contenido | 🟡 media — el contenido galaxy y las cards se mezclan |
| **Mantenimiento del plugin** | ✅ activo (v4.9.0, mayo 2026) | ⚠️ inactivo desde oct 2022 |
| **Riesgo de rotura** | bajo | medio-alto a largo plazo |
| **Excalidraw SVG embebido** | 🟡 no probado explícitamente | ✅ funciona con auto-export SVG |
| **Overhead de flujo** | 🟡 Script 2 + sync (2 clicks) | ✅ 1 click directo |
| **Fricción en notas con mucho LaTeX** | 🟡 el Script 2 resuelve pero agrega un paso | ✅ cero fricción |

---

## Veredicto

**Para el Sistema Galaxy, Opción A gana como plugin principal.** La razón central es arquitectónica: Galaxy está diseñado con notas de contenido puro (planet, moon, comet) donde el texto no debería tener ruido sintáctico. Marginalia respeta eso — la tarjeta vive al margen, la nota galaxy sigue siendo legible. Con el Script 2 el problema de LaTeX está resuelto.

**Opción B tiene un caso válido como complemento**, no como sustituto: notas dedicadas exclusivamente a flashcards (dwarf de repaso, formularios T00) donde cloze y reversed agregan valor real y no hay marginalia que proteger. La carpeta ya es el deck — eso encaja perfecto con Galaxy.

**Recomendación concreta:**

| Tipo de nota galaxy | Plugin |
|---|---|
| planet, moon, comet — teoría y ejercicios | **Opción A** — marginalia al margen |
| dwarf, formularios T00 — repaso puro | **Opción B** — cloze y reversed cuando sirvan |
| constellation/observatory — Image Occlusion | **Opción C** — exclusivo, ya decidido |

Coexisten sin conflicto porque operan sobre tipos de nota distintos y no comparten sintaxis.