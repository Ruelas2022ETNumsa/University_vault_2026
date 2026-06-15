Sistema de computación, ETN 903
Examen final, semestre I/2026

La propuesta de solución debe ser elaborada a mano y presentada en formato PDF
El Código de las soluciones debe ser presentado en formato TXT
El examen debe ser presentado en un archivo ZIP hasta las 9:30 del 12 de junio de 2026
al e-mail: javisanabria@gmail.com

solución (arquitectura)

1. En la cabecera IPv4 se incluyen las direcciones de red de origen y destino, pero no las mascaras
   de red. Como sabemos un IP, por ejemplo 192.168.1.10/24 y 192.168.1.10/27 son iguales
   porque en la cabecera solo aparece 192.168.1.10 y no las mascaras: /24 o /27. Desarrollar un
   sistema de computación que permita saber si un IP pertenece a una red clase: A, B o C o es
   un IP de una sub-red

2. Desarrollar un sistema de computación que permita convertir de números a texto. El sistema
   debe leer desde teclado un numero de hasta 4 dígitos y desplegar en pantalla 80x25 el equivalente.
   Este problema debe ser implementado usando Assembler en línea extendido.
   Por ejemplo.

   entrada = 1973                               entrada = 28            entrada = 9
   salida = mil novecientos setenta y tres      salida = veintiocho     salida = nueve

3. Sin utilizar interrupciones, desarrollar un sistema de computación que lea una cadena de caracteres
   desde teclado e imprima en pantalla 80x25 solo los caracteres de las posiciones impares de la misma.
   Por ejemplo

   entrada = la libertad es hacer lo que tienes que hacer, no lo que quieres hacer ¿Que opinas?
             0123456789012345678901234567890123456789012345678901234567890123456789012345678901
 
   salida =   a l b r a   s h c r l   u   i n s q e h c r,  o l   u   u e e   a e   Q e o i a ?