---
skill: "_start_movil607P1"
tipo: "documentación de caso especial"
fecha: "2026-09-04"
estado: "funcional — pendiente de pruebas"
autor: "krajo"
---

# Documentación — `_start_movil607P1`

## ¿Qué es este skill?

Variante del skill de inicio `_start` diseñada para uso **móvil** (claude.ai en celular), aplicada al caso específico de **ETN607 Mecánica Aplicada — Parcial 1**.

Opera en **modo solo lectura**: no edita, mueve ni crea archivos en el vault. Todo acceso al vault se hace vía **MCP de Google Drive** (conector nativo de claude.ai), lo que lo hace viable desde móvil donde no hay MCP Filesystem disponible.

---

## Diferencias respecto a `_start.md` estándar

| Aspecto | `_start.md` | `_start_movil607P1.md` |
|---|---|---|
| Acceso al vault | MCP Filesystem (local) | MCP Google Drive (remoto) |
| Escritura | Sí | No (solo lectura) |
| Contexto | General | Específico ETN607 P1 |
| Plataforma | Desktop | Móvil |
| Verificación MCP | write + edit | No aplica |

---

## Propósito del skill

Asistir en la **detección y adaptación de enunciados** de ejercicios para ETN607.

**Flujo esperado:**
1. El usuario entrega un enunciado (texto o foto desde el celular)
2. Claude lee `ENU607.md` en Drive para encontrar el ejercicio más similar
3. Adapta el enunciado al formato ENU
4. Devuelve un snippet listo para copiar a NotebookLM

---

## Cobertura temática (ETN607 — Temas 1 y 2)

- **T1:** Movimiento de cuerpos, métodos clásicos (Newton, Lagrange, Euler, D'Alembert, Hamilton)
- **T2:** Coordenadas rectangulares, cilíndricas y esféricas; coordenadas generalizadas; GDL; energía cinética

**Ejercicios mapeados:** E1–E23, clasificados por tipo de problema (GDE con restricción, polares, cilíndricas 3D, transformación de coordenadas, etc.)

---

## Estado actual

**Funcionó como se esperaba** en el caso de uso real durante P1.

**Pendiente de pruebas formales:**
- [ ] Verificar que el matching con ENU607.md sea correcto para todos los tipos de ejercicio
- [ ] Probar con fotos de enunciados (OCR + detección)
- [ ] Validar discriminadores clave (casos ambiguos: E8 vs E16 vs E22 vs E23)
- [ ] Confirmar que Drive MCP no requiere autenticación adicional en cada sesión móvil
- [ ] Evaluar si el snippet generado es directamente usable en NotebookLM sin ajuste manual

---

## Archivos relacionados

| Archivo | Rol |
|---|---|
| `E:\University_vault_2026\_skills\_start_movil607P1.md` | Skill original (este caso) |
| `E:\University_vault_2026\ENU607.md` | Base de ejercicios de referencia |
| `E:\University_vault_2026\Semesters\Sem_04\ETN607\Partial_1\ejercicios P1\` | Ejercicios resueltos P1 (P1-EX-607.md) |

---

## Notas de diseño

- Se definieron **discriminadores clave** en el skill para resolver ambigüedad entre ejercicios similares (ej: resorte + barra lineal → revisar anclaje y convención de ejes)
- El skill prohíbe explícitamente editar Drive, crear notas `.md` o usar GitHub MCP durante la sesión — pensado para mantener el vault limpio en sesiones de consulta rápida desde celular

---

## Para reutilizar este patrón

Si se necesita un skill similar para otro parcial o materia:
1. Copiar `_start_movil607P1.md` como base
2. Actualizar contexto temático y tabla de ejercicios
3. Ajustar rutas de `ENU___.md` y carpeta de ejercicios resueltos
4. Mantener el modo solo lectura si la sesión es móvil
