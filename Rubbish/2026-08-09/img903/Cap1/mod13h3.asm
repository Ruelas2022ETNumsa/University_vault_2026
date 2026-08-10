pila    segment stack
        dw 100 dup(0)
pila    ends
;----------------------------------------------------------
datos   segment
posx    dw   ?
posy    dw   ?
color   db   14
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
        mov  cx,10      ; CX lineas
        mov  posx,0	; posx,posy        
        mov  posy,2	; Un pixel es ubicado por
otro:	call linea
	add  posx,1    ; Espacio entre lineas
;	inc  color
	loop otro
        mov  ah,07	; Espera una tecla
        int  21h
        mov  ax,vian
        mov  ah,0	; Pone modo 13h
        int  10h
        ret
program endp
;----------------------------------------------------------
linea	proc
	push cx
	push posy
	mov  cx,10     ; linea de CX pixels
li1:	call pixel
	inc  posy
	loop li1
	pop  posy
	pop  cx
	ret
linea	endp
;----------------------------------------------------------
pixel   proc
	push cx
	mov  bx,posy
	mov  di,bx
        mov  cl,8		; posy*256
        shl  bx,cl
        mov  cl,6		; posy*64
        shl  di,cl
        add  di,posx		; posy*(256+64)+posx
        mov  al,color
        mov  es:[bx+di],al	; 0a000+posy*(320)+posx
	pop  cx
        ret
pixel   endp
;----------------------------------------------------------
codigo  ends
        end  program
