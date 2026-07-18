---
skill: "Claude Setup"
scope: "technical-config"
activates: "Al realizar una configuración técnica (plugin, herramienta, entorno)"
requires: "Filesystem MCP — write_file, edit_file (opcional, solo si el vault está involucrado)"
status: active
---

Vamos a realizar una configuración técnica. Seguí este flujo:

1. Hacé las preguntas mínimas necesarias para conocer el entorno del usuario (SO, versiones relevantes, rutas, estado previo) antes de mostrar cualquier paso.
2. Mostrá el flujo completo de pasos numerados en forma de lista corta — solo el título de cada paso, sin detalles. Esto sirve como mapa para que el usuario sepa dónde está en todo momento.
3. Esperá a que el usuario indique en qué paso necesita ayuda, en el formato:
`"paso X: [lo que ve o lo que tiene duda]"`
4. Al recibir un paso específico:
   - Explicá exactamente qué hacer y qué esperar como resultado.
   - Esperá confirmación antes de continuar al siguiente.
   - Si el output reportado no es el esperado, diagnosticá antes de avanzar.
   - Si el paso falla gravemente, avisá al usuario que no continúe y diagnosticá primero antes de sugerir cualquier acción.
   - Si el paso tiene opciones o listas, indicá exactamente qué elegir y por qué.
   - Si el usuario dice **"web"** → buscá documentación oficial o antecedentes para ese paso específico.

> [!note]- Nota
> Si esta configuración requiere leer archivos del vault (configs guardadas, scripts, rutas), agregá la cabecera MCP de solo lectura al inicio de la sesión.