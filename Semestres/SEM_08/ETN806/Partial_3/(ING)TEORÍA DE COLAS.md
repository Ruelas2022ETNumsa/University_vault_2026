# TEORÍA DE COLAS

### Una Cola es una línea de espera y la Teoría de Colas es una colección de modelos matemáticos que describen sistemas de líneas de espera particulares o de sistemas de colas.

Los modelos sirven para encontrar un buen compromiso entre los costos del sistema y los tiempos promedio de la línea de espera para un sistema dado. ‘‘El objetivo esencial es determinar que capacidad o tasa de servicio proporciona el balance correcto, para que el tiempo de espera no sea muy largo y el costo de servicio no sea muy alto’’.

Esto no es sencillo de determinar, ya que, un cliente no llega a un horario fijo, como también, el tiempo de servicio no tiene un horario fijo. Por lo tanto, se deduce de aquí, que los sistemas de líneas de espera son sistemas probabilísticos y aleatorios. El análisis cuantitativo con frecuencia es útil en estas situaciones.

El tener que esperar en una cola es una experiencia cotidiana que normalmente se considera desagradable. Esperar ser servido en un restaurante o en la cola de un banco, es una confrontación con la pérdida de tiempo por parte del cliente.


### Ejemplos típicos de teoría de cola

|SITUACION|LLEGADAS|COLA|MECANISMO DE SERVICIO|
|:--|:--|:--|:--|
|Aeropuerto|Pasajero|sala de espera|avión|
|Panadería|clientes|clientes con números|vendedor|
|Dpto. de bomberos|alarmas de incendio|incendio|dpto. de bomberos|
|Compañía telefónica|Números marcados|llamadas|conmutador|

# DEFINICION DE LA TEORIA DE COLAS

La Teoría de Colas es el estudio matemático del comportamiento de líneas de espera. Estas se presentan cuando ‘‘clientes’’ llegan a un ‘‘lugar’’ demandando un servicio a un ‘‘servidor’’, el cual, tiene una cierta capacidad de atención. Si el servicio no está disponible inmediatamente y el cliente decide esperar, entonces se forma en la cola o línea de espera.

**Esquema General del Sistema de Colas:** Llegadas -> Línea o Cola de Espera -> Servidor (Mecanismo de Servicio) -> Salidas.

# CONCEPTOS BASICOS DEL SISTEMA DE COLAS

**a) Clientes:** término usado en un sistema de colas para referirse por ejemplo a:
- Gente esperando líneas telefónicas desocupadas.
- Máquinas que esperan ser reparadas.
- Aviones esperando aterrizar.

**b) Instalaciones de Servicio:** este término se usa para referirse por ejemplo a:
- Líneas telefónicas.
- Talleres de reparación.
- Pistas de aeropuerto.

**c) Llegadas:** es el número de clientes que llegan a las instalaciones de servicio.

**d) Tasa de Servicio:** este término se usa para designar la capacidad de servicio, por ejemplo:
- Un sistema telefónico entre dos ciudades puede manejar 90 llamadas por minuto.
- Una instalación de reparación puede (de media), reparar máquinas a razón de una cada 8 horas.
- Una pista de aeropuerto en la que aterrizan dos aviones por minuto.

**e) Número de Servidores de Servicio:** es la cantidad de servidores de que disponemos, por ejemplo:
- Número de conmutadores telefónicos.
- Número de puestos de reparación.
- Número de pistas de aterrizaje de un aeropuerto.

El número de servidores no tiene porqué ser siempre en paralelo, es decir, puede que un sistema de colas tenga varias fases:

|Servidores|fases|ejemplos típicos|
|:--|:--|:--|
|Uno|una|kiosco de prensa con un empleado|
|varios|una|oficina bancaria con varios cajeros|
|Uno|varios|lavado / secado de automóviles|
|varios|varias|centro de servicio radiológico del hospital|

# COSTOS ASOCIADOS AL SISTEMA DE COLAS

**a) Los costos de espera.** Esperar significa desperdicio de algún recurso activo que bien se puede aprovechar en otra cosa. Lo normal es pensar que estos costos de espera decrecen conforme aumenta la capacidad de servicio del sistema.

**b) Los costos de servicio.** Contra la reducción anterior de los costos de espera, es también normal que el costo asociado a incrementar la capacidad de servicio, crezca con alguna proporcionalidad en relación a esta capacidad.

**c) Los costos totales del sistema de servicio.** La suma de los dos costos anteriores, da una función de costos totales del sistema en función de la capacidad. Aquí hay que tomar en cuenta que para tasas bajas de servicio, se experimentan largas colas y costos de espera muy altos. Conforme aumenta este servicio, disminuyen los costos de espera, pero aumenta el costo de servicio y el costo total disminuye.

# TIPOS DE SISTEMAS DE COLAS

Según el tipo de sistema de colas, tenemos varios tipos de éstas, las cuales son:

**a) Una línea, un servidor:** El primer sistema, es típico de una consulta médico - paciente, el lavado de carros automático o un muelle de descarga de un solo lugar. 
_(Esquema: llegadas —> cola —> servidor —> salida)_

**b) Una línea, múltiples servidores:** El segundo sistema, es típico de una peluquería o una panadería, en donde los clientes toman un número al entrar y se les sirve cuando les llega el turno. _(Esquema: llegada —> cola —> servidores)_

**c) Varias líneas, múltiples servidores:** El tercer sistema en que cada servidor tiene una línea separada, es característico de los bancos y las tiendas de autoservicio. Para este tipo de servicio pueden separarse los servidores y tratarlos como sistemas independientes de un servidor y una cola. _(Esquema: Llegada —> cola/servidor/salidas (repetido x3))_

**d) Una línea, múltiples servidores secuenciales:** En el cuarto sistema un cliente después de ser atendido por un servidor, pasa al siguiente, después al siguiente y así sucesivamente, hasta salir de la cola. Este sistema es útil para las líneas de producción, en donde hay varios pasos intermedios para el proceso de manufactura. _(Esquema: Llegada —> COLA —> SERVIDOR —> COLA —> SERVIDOR —> salida)_

# DISTRIBUCIONES

Puesto que, la Teoría de Colas se basa en la probabilidad, con el fin de estudiar las opciones más ventajosas para controlar situaciones o procesos en los que existen líneas de espera, ocupándose para aquello de factores como el patrón de llegada a la cola, las distintas necesidades de cada nueva llegada, así como de las probabilidades y patrones estadísticos de los tiempos de espera y de procesado. En razón, tenemos para aquello, dos tipos de distribuciones que nos proveen información para controlar mencionadas situaciones. Estas son:

**1. La Distribución de Poisson:** Esta distribución es muy frecuente en los problemas relacionados con la investigación operativa, sobre todo en el área de la gestión de colas. Suele describir por ejemplo, la llegada de pacientes a un ambulatorio, las llamadas a una central telefónica, la llegada de coches a un túnel de lavado, etc.. Todos estos casos pueden ser descritos por una variable aleatoria discreta que tiene valores no-negativos enteros.

**2. La Distribución Exponencial:** La distribución de Poisson describe las llegadas por unidad de tiempo y la distribución Exponencial estudia el tiempo entre cada una de estas llegadas. Si las llegadas son de Poisson, el tiempo entre ellas es Exponencial. La distribución de Poisson es discreta, mientras que la distribución Exponencial es continua, porque el tiempo entre llegadas no tiene por qué ser un número entero. Esta distribución se usa mucho para describir el tiempo entre eventos, específicamente, la variable aleatoria que representa el tiempo necesario para servir a la llegada. Un ejemplo típico puede ser el tiempo que un médico dedica a un paciente.