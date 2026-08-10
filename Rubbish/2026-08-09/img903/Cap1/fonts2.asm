pila    segment stack
        dw 100 dup(0)
pila    ends
;----------------------------------------------------------
datos   segment
carA    db    38h,38h,28h,6ch,6ch,6ch,44h,44h,0feh,0feh,0c6h,0c6h
x       db    0		; Para controlar las posiciones de bit
fil     dw    5		; Para controlar posiciones de pantalla
col     dw    40
k       dw    0		; Si k=0 caracter, si k=1 atributo
atrib   db    02h
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
        mov  ax,0b800h		; Parrafo del segmento*16
        mov  es,ax

        call bopan
        mov  si,0
fo1:
        mov  x,8
        mov  col,40
        mov  al,carA[si]
fo2:
        shl  al,1
        jnc  fo3
        call punto
fo3:
        inc  col
        dec  x
        cmp  x,0
        jne  fo2
        inc  fil
        inc  si
        cmp  si,12
        jne  fo1
        ret
program endp
;----------------------------------------------------------
pomem   proc
        mov  ax,fil		; Nro.fila*(Ancho de fila)*2
        mov  bx,160
        mul  bx
        mov  bx,ax
        mov  di,col		; Nro.Columna*2
        shl  di,1
        add  di,k		; Mas K
        ret
pomem   endp
;----------------------------------------------------------
punto   proc
        push ax
        mov  k,0		; Caracter
        call pomem
        mov  al,'o'
        mov  es:[bx+di],al
        mov  k,1		; Atributo
        call pomem
        mov  al,atrib
        mov  es:[bx+di],al
        pop  ax
        ret
punto   endp
;----------------------------------------------------------
bopan   proc
        mov  ax,0720h
        mov  cx,80*25
        mov  di,0
        rep  stosw
        ret
bopan   endp
;----------------------------------------------------------
codigo  ends
        end  program