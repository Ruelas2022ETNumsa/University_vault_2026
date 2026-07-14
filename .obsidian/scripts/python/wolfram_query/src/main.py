# fecha: 13-july-2026
# v1 — consulta Wolfram Alpha Full API con una expresión seleccionada.
# Extrae resultado en texto y descarga PNG del pod Plot si existe.
# Guarda imagen en _assets/ima-N.png (sin sobreescritura).
# Inserta en stdout el bloque markdown para Shell Commands → nota activa.
# Args: argv[1] expression · argv[2] vault_path

import sys
import os
import json
import re
import urllib.request
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

APP_ID     = "A3WL4X56LG"
ASSETS_DIR = "_assets"

expression = sys.argv[1]
vault_path = sys.argv[2]

# --- Llamada a WA Full API ---
encoded = urllib.parse.quote(expression)
url = f"https://api.wolframalpha.com/v2/query?input={encoded}&appid={APP_ID}&output=json"

try:
    with urllib.request.urlopen(url, timeout=10) as r:
        data = json.loads(r.read().decode('utf-8'))
except Exception as e:
    print(f"[ERROR] No se pudo conectar con Wolfram Alpha: {e}")
    sys.exit(1)

if not data.get("queryresult", {}).get("success"):
    print("[ERROR] Wolfram Alpha no pudo interpretar la expresión.")
    sys.exit(1)

pods = data["queryresult"].get("pods", [])

# --- Extraer resultado texto ---
result_text = "(sin resultado)"
for pod in pods:
    if pod.get("primary") or pod.get("id") == "Result":
        subpods = pod.get("subpods", [])
        if subpods and subpods[0].get("plaintext"):
            result_text = subpods[0]["plaintext"]
            break

# --- Buscar URL de gráfica ---
plot_url = None
for pod in pods:
    title = pod.get("title", "").lower()
    pid   = pod.get("id", "").lower()
    if "plot" in pid or "plot" in title:
        subpods = pod.get("subpods", [])
        if subpods and subpods[0].get("img", {}).get("src"):
            plot_url = subpods[0]["img"]["src"]
            break

# --- Descargar y guardar imagen ---
image_link = "*(sin gráfica disponible)*"

if plot_url:
    assets_path = os.path.join(vault_path, ASSETS_DIR)
    os.makedirs(assets_path, exist_ok=True)

    # Calcular siguiente N sin sobreescribir
    existing = [
        f for f in os.listdir(assets_path)
        if re.match(r'^ima-\d+\.png$', f)
    ]
    numbers = [int(re.search(r'\d+', f).group()) for f in existing]
    next_n  = max(numbers) + 1 if numbers else 1
    img_name = f"ima-{next_n}.png"
    img_path = os.path.join(assets_path, img_name)

    try:
        urllib.request.urlretrieve(plot_url, img_path)
        image_link = f"![[{img_name}]]"
    except Exception as e:
        image_link = f"*(error al descargar imagen: {e})*"

# --- Construir output para la nota ---
output = f"""
**WA:** {result_text}
{image_link}

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
{expression}
Si aplica, graficá usando Desmos o TikZJax.
```
"""

print(output)
