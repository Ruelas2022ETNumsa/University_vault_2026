# fecha: 13-july-2026
# v2 — consulta Wolfram Alpha Full API con una expresión seleccionada.
# Extrae todos los pods disponibles en texto y descarga PNG del pod Plot.
# Guarda imagen en _assets/ima-N.png (sin sobreescritura).
# Inserta en stdout el bloque markdown para Shell Commands → nota activa.
# Pods omitidos si no existen o no tienen plaintext.
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

# Pods a extraer en orden — (id, etiqueta en nota)
PODS_ORDER = [
    ("GeometricFigure",                              "Figura geométrica"),
    ("RealAlternateForm",                             "Forma alternativa (real)"),
    ("AlternateForm",                                 "Forma alternativa"),
    ("Root",                                          "Raíces"),
    ("PropertiesAsARealFunction",                     "Propiedades"),
    ("Derivative",                                    "Derivada"),
    ("IndefiniteIntegralAssumingAllVariablesAreReal", "Integral indefinida"),
    ("GlobalMinimum",                                 "Mínimo global"),
    ("GlobalMaximum",                                 "Máximo global"),
    ("Result",                                        "Resultado"),
]

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
pods_by_id = {p["id"]: p for p in pods}

# --- Buscar URL de gráfica ---
plot_url = None
plot_pod = pods_by_id.get("Plot")
if plot_pod:
    subpods = plot_pod.get("subpods", [])
    if subpods and subpods[0].get("img", {}).get("src"):
        plot_url = subpods[0]["img"]["src"]

# --- Descargar y guardar imagen ---
image_block = ""

if plot_url:
    assets_path = os.path.join(vault_path, ASSETS_DIR)
    os.makedirs(assets_path, exist_ok=True)

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
        image_block = f"**Gráfica:**\n![[{img_name}]]"
    except Exception as e:
        image_block = f"**Gráfica:** *(error al descargar: {e})*"

# --- Extraer pods de texto ---
lines = []

if image_block:
    lines.append(image_block)

for pod_id, label in PODS_ORDER:
    pod = pods_by_id.get(pod_id)
    if not pod:
        continue
    subpods = pod.get("subpods", [])
    texts = [s["plaintext"] for s in subpods if s.get("plaintext", "").strip()]
    if not texts:
        continue
    content = " | ".join(texts)
    lines.append(f"**{label}:**\n${content}$")

# --- Construir output para la nota ---
body = "\n\n".join(lines)

output = f"""
**WolframAlpha:** ${expression}$

{body}

```
Resolvé paso a paso sin ejercicio adicional (MODO 3):
{expression}
Si aplica, graficá usando Desmos o TikZJax.
```
"""

print(output)
