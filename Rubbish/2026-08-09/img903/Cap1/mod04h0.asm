pila    segment stack
        dw 100 dup(0)
pila    ends
;----------------------------------------------------------
datos   segment
posx    dw   0
posy    dw   0
color   db   01010101b       ; Cuatro colores
vian	dw   0
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
        mov  ax,0B800h
        mov  es,ax

        mov  ah,0fh    ; Obtener modo de video
        int  10h
        mov  vian,ax
        mov  al,04h    ; Pone modo 13h
        mov  ah,0      ; 320x200x256
        int  10h

        call pixel     ; ESI
        mov  posx,79         ; 319/4
        call pixel     ; ESD
        mov  posy,99         ; 199/2
        call pixel     ; EID
        mov  posx,0
        call pixel     ; EII

        mov  posy,1    ; Una recta en posy = 1
        mov  cx,80     ; CX = 320/4
otro:   call pixel
        inc  posx
	loop otro      ; 
        mov  ah,07     ; Espera una tecla
        int  21h
        mov  ax,vian   ; Repone
        mov  ah,0      ; modo texto
        int  10h
        ret
program endp
;----------------------------------------------------------
pixel   proc
        push cx
        mov  ax,80
        mul  posy
        mov  bx,ax
        mov  di,posx
        mov  al,color
        mov  es:[di+bx],al  ; 0B800+posy*(320/4)+posx
        pop  cx
        ret
pixel   endp
;----------------------------------------------------------
codigo  ends
        end  program
