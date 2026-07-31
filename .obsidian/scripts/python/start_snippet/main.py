# ============================================================
# start_snippet — main.py
# Versión: v1
# ============================================================
# Descripción:
#   Copia al portapapeles el snippet de inicio de sesión de Claude
#   con la hora actual (HH:MM) al momento de ejecución.
#
# Uso:
#   Ejecutar desde Shell Commands (Obsidian) via Ctrl+P
#   → "Start — copiar snippet"
#   Luego pegar directamente en Claude.
#
# Output esperado al pegar:
#   Usá el MCP Filesystem y leé E:\University_vault_2026\_skills\_start.md
#   Hora de inicio: 14:35
#
# Dependencias: solo stdlib (subprocess, datetime)
# ============================================================

import subprocess
from datetime import datetime

hora = datetime.now().strftime("%H:%M")
texto = (
    "Usá el MCP Filesystem y leé E:\\University_vault_2026\\_skills\\_start.md\n"
    f"Hora de inicio: {hora}"
)

subprocess.run(
    ["powershell", "-command", f"Set-Clipboard -Value '{texto}'"],
    check=True
)
