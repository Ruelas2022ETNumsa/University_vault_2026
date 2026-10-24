Dir     Instrucción    Comentario
-----   ------------   ------------------------------------------
00000   IS2            ¿Impresora lista? (busy = 0 → salta a 00002)
00001   JMP 00000      Si está ocupada, vuelve a preguntar (espera)
00002   LAC I 00100    AC ← contenido de la dirección apuntada por [00100]
00003   OD2            Envía AC a la impresora (imprime 2 caracteres)
00004   ISZ 00100      Puntero + 1 (apunta a la siguiente palabra)
00005   ISZ 00101      Contador + 1; si llega a 0 → salta a 00007
00006   JMP 00000      Si no es 0, repite para la siguiente palabra
00007   HLT            Fin del programa