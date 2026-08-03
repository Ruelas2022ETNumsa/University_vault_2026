# ============================================================
# start_snippet — main.py
# Versión: v2
# ============================================================
# Descripción:
#   Copia al portapapeles el snippet de inicio de sesión de Claude
#   con la hora actual (HH:MM) y el worker activo (título del archivo
#   abierto en Obsidian) al momento de ejecución.
#
# Uso:
#   Ejecutar desde Shell Commands (Obsidian) via Ctrl+P
#   → "Start — copiar snippet"
#   Luego pegar directamente en Claude.
#
# Output esperado al pegar:
#   Usá el MCP Filesystem y leé E:\University_vault_2026\_skills\_start.md
#   Hora de inicio: 14:35
#   trabajas como: nombre_worker
#
# Configuración Shell Commands:
#   python "{{vault_path}}\.obsidian\scripts\python\start_snippet\main.py" "{{title}}"
#
# Dependencias: solo stdlib (subprocess, datetime, sys)
# ============================================================

import subprocess
import sys
from datetime import datetime

hora = datetime.now().strftime("%H:%M")
worker = sys.argv[1] if len(sys.argv) > 1 else ""

texto = (
    "Usá el MCP Filesystem y leé E:\\University_vault_2026\\_skills\\_start.md\n"
    f"Hora de inicio: {hora}\n"
    f"worker: {worker}"
)

subprocess.run(
    ["powershell", "-command", f"Set-Clipboard -Value '{texto}'"],
    check=True
)
