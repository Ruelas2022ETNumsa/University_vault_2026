pila    segment stack
        dw 100 dup(0)
pila    ends
;----------------------------------------------------------
datos   segment
cadena  db    'Javier'
largo   dw    6
fil     dw    12
col     dw    40
k       dw    0
atrib   db    67h
datos   ends
;----------------------------------------------------------
codigo  segment
program proc far
        assume ss:pila,ds:datos,cs:codigo
        push ds
        sub  ax,ax
        push ax
        mov  ax,datos
        mov  ds,ax

        mov  ax,0b800h
        mov  es,ax

        lea  si,cadena
        mov  cx,largo
otro:
        mov  al,[si]
        call posxy
        inc  si
        inc  col
        loop otro
        ret
program endp
;----------------------------------------------------------
pomem   proc
        push ax
        mov  ax,fil
        mov  bx,160
        mul  bx
        mov  bx,ax
        mov  di,col
        shl  di,1
        add  di,k
        pop  ax
        ret
pomem   endp
;----------------------------------------------------------
posxy   proc
        mov  k,0		; Caracter
        call pomem
        mov  es:[bx+di],al
        mov  k,1		; Atributo
        call pomem
        mov  al,atrib
        mov  es:[bx+di],al
        ret
posxy   endp
;----------------------------------------------------------
codigo  ends
        end  program