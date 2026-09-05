import sys
import shutil
import os

# Argumentos
file_path = sys.argv[1]
destino = sys.argv[2].strip().upper() if len(sys.argv) > 2 else "V"

# Rutas destino
RUTAS = {
    "V": r"C:\Users\USUARIO\Documents\HP Prime\Calculators\Prime",
    "F": r"C:\Users\USUARIO\Documents\HP Connectivity Kit\Calculadoras\TARS",
}

# Validar destino
if destino not in RUTAS:
    print(f"Destino '{destino}' no reconocido. Usá V (CASE) o F (TARS).")
    sys.exit(1)

# Validar que el archivo existe
if not os.path.isfile(file_path):
    print(f"Archivo no encontrado: {file_path}")
    sys.exit(1)

# Copiar
carpeta_destino = RUTAS[destino]
nombre_archivo = os.path.basename(file_path)
destino_final = os.path.join(carpeta_destino, nombre_archivo)

shutil.copy2(file_path, destino_final)

nombre_calc = "CASE" if destino == "V" else "TARS"
print(f"Copiado a {nombre_calc}: {nombre_archivo}")
