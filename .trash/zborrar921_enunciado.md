# Proyecto de Investigación

**Materia:** Teoría de Sistemas Operativos (ETN921)

## Objetivo

Desarrollar un sistema de computación utilizando el protocolo **SNMP** para gestionar una computadora con sistema operativo **Windows** desde un servidor SNMP con sistema operativo **GNU/Linux**.

---

# Componentes del sistema

El sistema tiene tres componentes:

1. Un servidor SNMP instalado en GNU/Linux.
2. Una computadora con Windows con el agente SNMP habilitado.
3. Un firewall en Windows que permita tráfico por los puertos UDP **161** y **162**.

---

# Descripción

## 1. Servidor SNMP en GNU/Linux

Investigar cómo instalar y configurar un servidor SNMP en GNU/Linux.

Para instalar paquetes en GNU/Linux Mint se utiliza:

```bash
sudo apt-get install nombre-de-paquete
```

Se recomienda utilizar herramientas de IA para aprender a instalar y configurar SNMP en:

- GNU/Linux Mint 21.2
- Windows (habilitación del agente SNMP)

---

## 2. Agente SNMP en Windows

Investigar cómo habilitar y configurar el agente SNMP en una computadora con sistema operativo Windows.

---

## 3. Firewall y VirtualBox

Investigar cómo configurar:

- El firewall de Windows.
- La máquina virtual VirtualBox.

El objetivo es permitir que el servidor SNMP pueda gestionar variables de la computadora Windows.

### Ejemplo

```text
interfaces.ifTable.ifEntry.ifInOctets.1 : Counter: 21296438
```

Esta variable permite medir el tráfico de entrada de la tarjeta de red de la computadora.

---

# Desarrollo de la aplicación

La aplicación debe desarrollarse en:

- PHP (lógica de la aplicación)
- HTML (interfaz de usuario)

Siguiendo la metodología utilizada en los sistemas desarrollados anteriormente en GNU/Linux y Windows.

---

# Sugerencias

Tomando como base la presentación realizada en clases:

- SNMP_Seminario_01

Además, se recomienda investigar los documentos RFC relacionados con SNMP para profundizar en el protocolo.

---

# Recomendación Final

Es suficiente que el estudiante logre ejecutar un comando SNMP en el servidor GNU/Linux y obtener una medida de alguna variable de la computadora Windows mediante el agente SNMP previamente habilitado y configurado.

### Ejemplo

```bash
snmpget -c RedPrueba 192.168.5.130 interfaces.ifTable.ifEntry.ifInOctets.1
```

Resultado esperado:

```text
interfaces.ifTable.ifEntry.ifInOctets.1 : Counter: 33922904
```

---

# Fecha de entrega

**Hasta el miércoles 17 de junio de 2026**

**Correo:** javisanabria@gmail.com