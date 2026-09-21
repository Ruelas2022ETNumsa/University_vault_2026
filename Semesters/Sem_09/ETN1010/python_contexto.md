============================================================
ENTORNO PYTHON — ETN1010
============================================================

SISTEMA
-------
Sistema operativo: Windows 10

CARPETA DEL PROYECTO
--------------------
E:\University_vault_2026\Semesters\Sem_09\ETN1010

Para entrar desde CMD:
cd /d E:\University_vault_2026\Semesters\Sem_09\ETN1010


============================================================
PYTHON
============================================================

Versión instalada:
Python 3.13.13

Ruta de Python:
C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe

Comprobar versión:
python --version

También se puede usar:
py --version

Ubicación del lanzador:
C:\Windows\py.exe


============================================================
PIP
============================================================

Versión:
pip 26.0.1

Ruta:
C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\Lib\site-packages\pip

Comprobar:
py -m pip --version


IMPORTANTE:
-----------
El comando "pip" directamente está apuntando a una instalación
antigua de Python 3.11 que ya no existe.

NO usar como primera opción:
pip install paquete

Usar preferentemente:
python -m pip install paquete

o:
py -m pip install paquete


============================================================
PAQUETES INSTALADOS
============================================================

1. scikit-learn
----------------
Versión: 1.9.1

Descripción:
Biblioteca de Python para aprendizaje automático (Machine Learning),
análisis de datos y minería de datos.

Dependencias principales:
- joblib
- narwhals
- numpy
- scipy
- threadpoolctl

Ubicación:
C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\Lib\site-packages


2. pandas
----------
Versión: 3.0.5

Descripción:
Biblioteca para manipulación, análisis y procesamiento de datos.
Utiliza principalmente estructuras como DataFrame y Series.

Ubicación:
C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\Lib\site-packages


============================================================
COMANDOS ÚTILES
============================================================

Ver versión de Python:
python --version

Ver versión de pip:
python -m pip --version

Ver información de scikit-learn:
python -m pip show scikit-learn

Ver información de pandas:
python -m pip show pandas

Comprobar que ambos funcionan:
python -c "import sklearn, pandas; print('scikit-learn:', sklearn.__version__); print('pandas:', pandas.__version__)"

Instalar nuevos paquetes:
python -m pip install NOMBRE_DEL_PAQUETE

Actualizar un paquete:
python -m pip install --upgrade NOMBRE_DEL_PAQUETE


============================================================
VERIFICACIÓN ACTUAL
============================================================

Python:
3.13.13

pip:
26.0.1

scikit-learn:
1.9.1

pandas:
3.0.5

Resultado:
Todos los paquetes comprobados funcionan correctamente.


============================================================
NOTA SOBRE EL ANTIGUO PIP
============================================================

El antiguo pip.exe intenta utilizar:

C:\Users\USUARIO\AppData\Local\Programs\Python\Python311\python.exe

Esa instalación de Python 3.11 ya no está disponible.

La instalación actual utiliza:

C:\Users\USUARIO\AppData\Local\Programs\Python\Python313\python.exe

Por eso se recomienda utilizar:

python -m pip

en lugar de:

pip

============================================================