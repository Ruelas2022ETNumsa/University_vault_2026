# Ejercicio 1 2022
Explicar de forma sencilla el concepto de sincronización. (10 puntos).

---

En las redes de telefonía digital, la **sincronización** es el proceso fundamental de coordinar el tiempo (temporización) tanto para la transmisión de **bits** como para la organización de las **tramas** de datos. Su objetivo principal es evitar desajustes de tiempo conocidos como **deslizamientos** durante la comunicación.

Para lograr que toda la red trabaje de manera coordinada, el proceso se realiza mediante la siguiente estructura:

* **Jerarquía de Relojes (Master y Esclavos)**: Cada central telefónica cuenta con un reloj que establece su base de tiempo. Dentro de la red, la **central madre** posee el **reloj master (maestro)**, mientras que las demás centrales actúan como **esclavas** y deben sincronizarse obligatoriamente con el reloj master. Esta jerarquía permite monitorear y controlar la **tasa de deslizamiento** del sistema.
* **Funciones de la Base de Tiempo**: Una vez coordinada la base de tiempo, cumple dos funciones operativas clave en la central:
  1. **Recepción**: Permite recibir correctamente los trenes de bits que provienen de otras centrales digitales.
  2. **Envío y Conmutación**: Controla los equipos de la central para conmutar y enviar los trenes de bits de forma ordenada hacia otras centrales o hacia los abonados (usuarios finales).