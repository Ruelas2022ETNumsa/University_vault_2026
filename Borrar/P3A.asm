; ============================================================
; P3A.asm  |  MASM 5.0  |  8086 modo real  |  DOSBox
;
; Lee una cadena por teclado SIN interrupciones.
; Teclado: BIOS Data Area seg. 0040h, buffer circular
;          [0040:001Ah] HEAD  ultimo char leido
;          [0040:001Ch] TAIL  ultimo char escrito por BIOS
;          [0040:001Eh..003Dh] 16 words (scancode|ASCII)
; Video  : acceso directo a B800h, cada celda = char + atrib
; Unica INT permitida: 21h/4C00h para terminar el programa
; ============================================================

pila    SEGMENT PARA STACK 'STACK'
        DW  64 DUP(0)
pila    ENDS

; ------------------------------------------------------------
datos   SEGMENT PARA 'DATA'

MAX_CADENA  EQU  80         ; limite de caracteres a leer
COLS        EQU  80         ; columnas de pantalla
ATRI        EQU  07h        ; atributo: gris sobre negro

; Posicion de cada fila en B800h: fila * 80cols * 2bytes
POS_LBL1    EQU  0 * COLS * 2
POS_IN      EQU  1 * COLS * 2
POS_LBL2    EQU  3 * COLS * 2
POS_OUT     EQU  4 * COLS * 2

cadena_entrada  DB  MAX_CADENA DUP(0)
cadena_salida   DB  MAX_CADENA DUP(0)
tam_in          DW  0       ; chars leidos del teclado
tam_out         DW  0       ; chars copiados a cadena_salida

label1      DB  'Cadena original:'
LEN_LBL1    EQU  $ - label1
label2      DB  'Resultado:'
LEN_LBL2    EQU  $ - label2

datos   ENDS

; ------------------------------------------------------------
codigo  SEGMENT PUBLIC 'code'
program PROC FAR
        ASSUME SS:pila, DS:datos, CS:codigo

        ;inicializar DS
        PUSH DS
        SUB  AX, AX
        PUSH AX
        MOV  AX, datos
        MOV  DS, AX

        ; ES -> segmento de video
        MOV  AX, 0B800h
        MOV  ES, AX

        CALL LimpiarPantalla
; imprimir "Cadena original:" fila 0
        MOV  SI, OFFSET label1          
        MOV  CX, LEN_LBL1
        MOV  DI, POS_LBL1
        CALL ImprimirTexto
; leer teclado con eco en fila 1
        MOV  DI, POS_IN                 
        CALL LeerCadena
; extraer chars de posiciones impares
        CALL ProcesarCadena             
; imprimir "Resultado:" fila 3
        MOV  SI, OFFSET label2          
        MOV  CX, LEN_LBL2
        MOV  DI, POS_LBL2
        CALL ImprimirTexto
; imprimir resultado en fila 4
        MOV  SI, OFFSET cadena_salida   
        MOV  CX, WORD PTR [tam_out]
        MOV  DI, POS_OUT
        CALL ImprimirTexto

	espera:
        JMP  espera

program ENDP

; ============================================================
; LimpiarPantalla: escribe espacio+atributo en las 2000 celdas
; ============================================================
LimpiarPantalla PROC NEAR
        MOV  DI, 0
        MOV  AX, (ATRI SHL 8) OR ' '   ; AH=atrib AL=espacio
        MOV  CX, 2000
        REP  STOSW
        RET
LimpiarPantalla ENDP

; ============================================================
; ImprimirTexto: vuelca DS:SI (CX chars) en ES:DI (B800h)
; Cada caracter se escribe como word: AL=char AH=atributo
; ============================================================
ImprimirTexto PROC NEAR
        JCXZ fin_impr
bucle1:
        LODSB
        MOV  AH, ATRI
        STOSW
        LOOP bucle1
fin_impr:
        RET
ImprimirTexto ENDP

; ============================================================
; LeerCadena: captura teclado leyendo el buffer del BDA
;
; El BIOS mantiene un buffer circular en 0040h. Cuando HEAD
; != TAIL hay un caracter disponible en [0040h:HEAD].
; Se lee el word (AL=ASCII AH=scancode), se avanza HEAD con
; wrap, y se restaura ES a video para escribir el eco.
; BX recorre cadena_entrada, BP guarda la posicion de eco.
; ============================================================
LeerCadena PROC NEAR
        MOV  BX, OFFSET cadena_entrada
        MOV  CX, 0
        MOV  BP, DI                     ; posicion eco en video

leer_char:
        ; Apuntar ES al BDA y verificar si hay tecla pendiente
        ; HEAD (001Ah) != TAIL (001Ch) => hay dato en el buffer
        MOV  AX, 0040h
        MOV  ES, AX
        MOV  DI, 001Ah                  ; DI = offset de HEAD
        MOV  AX, ES:[DI]                ; AX = HEAD
        MOV  DI, 001Ch                  ; DI = offset de TAIL
        CMP  AX, ES:[DI]
        JE   leer_char                  ; HEAD==TAIL: buffer vacio

        ; Leer el word en [0040h:HEAD]: AL=ASCII AH=scancode
        ; Avanzar HEAD += 2, volver a 001Eh si supera 003Eh
        MOV  DI, 001Ah
        MOV  SI, ES:[DI]                ; SI = HEAD actual
        MOV  AX, ES:[SI]                ; AX = char leido
        ADD  SI, 2
        CMP  SI, 003Eh
        JB   sin_wrap
        MOV  SI, 001Eh
sin_wrap:
        MOV  DI, 001Ah
        MOV  ES:[DI], SI                ; HEAD actualizado

        ; Restaurar ES a video para poder escribir eco
        PUSH AX
        MOV  AX, 0B800h
        MOV  ES, AX
        POP  AX

        ; Filtrar: ignorar teclas sin ASCII (AL=0) y validar ENTER
        CMP  AL, 0
        JE   leer_char
        CMP  AL, 0Dh                    ; ENTER = fin de lectura
        JE   fin_leer
        CMP  CX, MAX_CADENA             ; buffer lleno = ignorar
        JAE  leer_char

        ; Guardar char en cadena_entrada y mostrar eco en video
        MOV  [BX], AL
        INC  BX
        INC  CX
        MOV  DI, BP
        MOV  AH, ATRI
        STOSW                           ; eco: char+atrib en B800h
        MOV  BP, DI

        JMP  leer_char

fin_leer:
        MOV  tam_in, CX
        RET
LeerCadena ENDP

; ============================================================
; ProcesarCadena: copia chars de indices impares (1,3,5...)
;
; Arranca SI en cadena_entrada+1 (indice 1) y avanza de 2
; en 2: LODSB carga el impar (SI++) e INC SI salta el par.
; SHR CX,1 calcula cuantos impares hay; ADC ajusta si la
; longitud es impar (ultimo indice impar no se perderia).
; Escribe en cadena_salida via DS:DI (no STOSB, porque
; ES apunta a video y no a datos).
; ============================================================
ProcesarCadena PROC NEAR
        MOV  CX, tam_in
        CMP  CX, 2
        JB   cad_vacia

        MOV  SI, OFFSET cadena_entrada
        INC  SI                         ; saltar indice 0 (par)
        MOV  DI, OFFSET cadena_salida
        MOV  BX, 0

        SHR  CX, 1
        ADC  CX, 0
        JCXZ cad_vacia

bucle2:
        LODSB                           ; lee indice impar, SI++
        MOV  [DI], AL                   ; guarda en cadena_salida
        INC  DI
        INC  SI                         ; salta el indice par
        INC  BX
        LOOP bucle2

        MOV  tam_out, BX
        RET

cad_vacia:
        MOV  tam_out, 0
        RET
ProcesarCadena ENDP

codigo  ENDS
        END program