============================================================
  SISTEMA DE MONITOREO DE ENLACES TCP/IP
  ETN921 - Teoria de Sistemas Operativos
  Plataforma: Windows 10 + IIS + MySQL 8.0.46 + PHP 7.1.11
============================================================


PRIMER ARRANQUE (HACER UNA SOLA VEZ POR SESION DE TRABAJO)
============================================================

Antes de tocar el menu.bat, asegurate de que los dos servicios
necesarios estan corriendo: MySQL e IIS.


PASO 1 - Arrancar MySQL 8.0
------------------------------------------------------------
   Abri cmd como Administrador y ejecuta:

       net start MySQL80

   Salidas posibles:

       "El servicio de MySQL80 se ha iniciado correctamente."
            -> Listo, MySQL esta funcionando.

       "El servicio solicitado ya se ha iniciado."
            -> Tambien esta OK. Ya estaba corriendo de antes.

       "Error del sistema 5..."
            -> No abriste cmd como Administrador. Cerrate y
               abri cmd con click derecho > Ejecutar como admin.

   Para verificar:

       sc query MySQL80 | findstr STATE

       Debe decir:  STATE : 4  RUNNING


PASO 2 - Arrancar IIS
------------------------------------------------------------
   Abri cmd como Administrador y ejecuta:

       iisreset /start

   Salida esperada:

       "Intento de inicio efectuado correctamente."

   Para verificar:

       sc query W3SVC | findstr STATE

       Debe decir:  STATE : 4  RUNNING

   Tambien podes abrir el navegador en http://localhost/
   y deberia mostrar la pagina por defecto de IIS.


PASO 3 - Verificar versiones de MySQL y PHP
------------------------------------------------------------
   En cmd, ejecuta:

       mysql --version
            Debe decir: mysql ... Ver 8.0.46 ...

       php --version
            Debe decir: PHP 7.1.11 ...

   Si alguno no se reconoce como comando, hay un problema
   con la variable PATH del sistema. Asegurate de tener en
   el PATH:

       C:\Program Files\MySQL\MySQL Server 8.0\bin
       C:\php

   (estos paths los configuraste cuando seguiste el PDF
    "IIS PHP y MySQL" del docente)


PASO 4 - Ejecutar el menu del proyecto
------------------------------------------------------------
   Click derecho sobre menu.bat -> Ejecutar como administrador

   Es OBLIGATORIO ejecutarlo como administrador para que pueda:
     - Crear tareas en el Task Scheduler
     - Copiar archivos a C:\inetpub\wwwroot\
     - Asignar permisos con icacls


============================================================
PRIMERA INSTALACION (HACER UNA SOLA VEZ EN TOTAL)
============================================================

Si es la PRIMERA VEZ que corres el proyecto en esta maquina,
seguir el menu en este orden:


PASO A - Fix de autenticacion de MySQL  (Opcion 3 -> 4)
------------------------------------------------------------
   IMPORTANTISIMO. Sin esto, PHP 7.1 no puede conectar a
   MySQL 8 y todo lo demas va a fallar.

   Cambia el usuario root para que use mysql_native_password
   en vez de caching_sha2_password (que PHP 7.1 no entiende).

   Se hace una sola vez y queda configurado para siempre.


PASO B - Crear la base de datos  (Opcion 3 -> 1)
------------------------------------------------------------
   Ejecuta sql\crear_bd.sql, que crea:
     - Base de datos: monitoreo_red
     - Tabla:         muestras


PASO C - Instalar la interfaz web en IIS  (Opcion 4 -> 1)
------------------------------------------------------------
   Copia los archivos de la carpeta web\ a:
       C:\inetpub\wwwroot\monitoreo\

   Crea la subcarpeta reportWEB y aplica permisos para que
   IIS (usuario IIS_IUSRS) pueda leer y ejecutar.

   Despues abri el navegador en:
       http://localhost/monitoreo/


PASO D - Cargar datos de prueba  (Opcion 7)
------------------------------------------------------------
   Inserta el contenido de sql\prueba.txt en la BD para
   que las graficas tengan datos sin esperar al cron.


PASO E - Activar monitoreo automatico  (Opcion 2 -> 1)
------------------------------------------------------------
   Crea dos tareas en el Task Scheduler:
     - MonitoreoRed_Muestra: cada 5 minutos
     - MonitoreoRed_Carga  : cada 1 hora

   IMPORTANTE: las tareas solo corren con la laptop ENCHUFADA
   a corriente alterna (por una opcion de Windows que viene
   activada por default). Si queres que corran con bateria:
   abri Task Scheduler (taskschd.msc), buscar las dos tareas,
   click derecho > Properties > Conditions, y desmarcar la
   opcion "Start the task only if the computer is on AC power".


============================================================
ARRANQUE NORMAL (LAS PROXIMAS VECES)
============================================================

Una vez que la primera instalacion esta lista, solo necesitas:

  1. net start MySQL80
  2. iisreset /start
  3. Abrir el navegador en http://localhost/monitoreo/

Si queres administrar el sistema (ver reportes, agregar
enlaces, resetear datos, etc), ejecuta menu.bat como admin.


============================================================
PARA AGREGAR O QUITAR ENLACES MONITOREADOS
============================================================

Tenes dos formas de hacerlo, ambas trabajan sobre el mismo
archivo (enlaces.txt):

OPCION A - Desde el navegador (mas comodo)
------------------------------------------------------------
   Abri en el navegador:

       http://localhost/monitoreo/gestionar_enlaces.php

   O desde la pagina principal hace click en
   "Agregar o quitar enlaces de la lista".

   Desde ahi podes:
     - Agregar nuevos enlaces (ej: www.umsa.bo)
     - Quitar los existentes con el boton rojo

OPCION B - Desde el menu de consola (menu.bat -> Opcion 8)
------------------------------------------------------------
   Ofrece las mismas operaciones:
     - 1) Agregar un enlace
     - 2) Quitar un enlace
     - 3) Editar manualmente con Notepad
     - 4) Restaurar la lista original de 10 enlaces

EFECTOS DE LOS CAMBIOS
------------------------------------------------------------
   - El monitoreo automatico (cada 5 minutos) leera la nueva
     lista en su proxima ejecucion. No hace falta reiniciar
     nada.
   - La pagina web se actualiza al refrescar.
   - Los reportes historicos siguen teniendo todos los datos
     de los enlaces viejos: si quitas un enlace, sus datos
     pasados siguen en la BD y se pueden consultar.


============================================================
PROBLEMAS COMUNES
============================================================

> "The server requested authentication method unknown..."
    Falta el Fix de auth de MySQL. Ejecuta menu.bat opcion 3 -> 4.

> Las tareas programadas no se ejecutan
    Tu laptop esta a bateria. Enchufala a corriente alterna o
    desmarca la opcion de "AC power" en Task Scheduler.

> http://localhost/monitoreo/ da error 500
    PHP no esta procesando los archivos. Verifica que el
    Handler Mapping de *.php en IIS este configurado para
    FastCGI -> C:\php\php-cgi.exe (paso 8 del PDF del docente).

> http://localhost/monitoreo/ da 403 Forbidden
    Falta agregar index.php como Default Document en IIS
    (paso 9 del PDF del docente). O ejecuta menu.bat opcion 4 -> 1
    de nuevo para reasignar permisos.

> El ping desde la web devuelve "Sin respuesta" siempre
    El usuario IIS_IUSRS no puede ejecutar ping_web.bat.
    Reinstala la web con menu.bat opcion 4 -> 1, que aplica
    los permisos correctos.


============================================================
ESTRUCTURA DEL PROYECTO
============================================================

proyecto_monitoreo_windows\
  menu.bat                       Menu principal (admin)
  README.txt                     Este archivo
  INSTRUCCIONES_WINDOWS.md       Documentacion detallada
  scripts\
    tomar_muestra.bat            Ping a los enlaces (cada 5 min)
    cargar_bd.bat                Carga muestras a BD (cada hora)
  sql\
    crear_bd.sql                 Crea BD y tabla muestras
    fix_auth_php71.sql           Fix MySQL8 + PHP 7.1
    prueba.txt                   Datos de ejemplo
  web\                           Se copia a inetpub\wwwroot\monitoreo\
    index.php                    Pagina principal
    ping_online.php              Componente 2 (GET, ?Equipo=N)
    ping_manual.php              Ping a direccion custom
    ping_web.bat                 .bat invocado por PHP (spec)
    ping_helper.php              PHP -> .bat, parsea es/en
    estado_enlaces.php           Tabla de estado actual
    reporte.php                  Componente 3 (POST, graficas)
    comparar.php                 Comparacion entre enlaces
    gestionar_enlaces.php        Pantalla web para editar lista
    enlaces.php                  Helper PHP que lee enlaces.txt
    enlaces.txt                  Lista de enlaces (unica fuente)
    estilos.css                  Estilos CSS

============================================================
