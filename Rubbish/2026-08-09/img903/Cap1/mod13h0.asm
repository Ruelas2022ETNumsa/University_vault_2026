pila    segment stack
        dw 100 dup(0)
pila    ends
;----------------------------------------------------------
datos   segment
posx    dw   0
posy    dw   0
color   db   14       ; Amarillo
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
        mov  ax,0a000h
        mov  es,ax

	mov  ah,0fh	; Obtener modo de video
	int  10h
	mov  vian,ax
        mov  al,13h	; Pone modo 13h
	mov  ah,0	; 320x200x256
        int  10h

	call pixel     ; ESI
	mov  posx,319  ; 
	call pixel     ; ESD
	mov  posy,199  ; 
	call pixel     ; EID
	mov  posx,0    ; 
	call pixel     ; EII
        mov  ah,07     ; Espera una tecla
        int  21h
        mov  ax,vian   ; Repone
        mov  ah,0	; modo texto
        int  10h
        ret
program endp
;----------------------------------------------------------
pixel   proc
	push cx
	mov  bx,posy
	mov  di,bx
        mov  cl,8           ; posy*256
        shl  bx,cl
        mov  cl,6           ; posy*64
        shl  di,cl
        add  di,posx        ; posy*(256+64)+posx
        mov  al,color
        mov  es:[bx+di],al  ; 0a000+posy*(320)+posx
	pop  cx
        ret
pixel   endp
;----------------------------------------------------------
codigo  ends
        end  program
