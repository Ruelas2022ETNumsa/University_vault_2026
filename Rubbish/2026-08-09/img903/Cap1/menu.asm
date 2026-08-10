	page    65,132
title	TITULO DEL inicio
;---------------------------Segmento de pila-----------------------
;                           ----------------
pila	segment para stack 'stack'
	dw      32   dup(?)
pila	ends
;---------------------------Segmento de datos----------------------
;                           -----------------
datos	segment para 'data'
menu	db	"Archivo        $Editar         $Ver            $"
	db	"Correr         $Punto de parada$"
poMen	db 0,8,15,19,26
datos	ends
;---------------------------Segmento de codigo---------------------
;                           ------------------
codigo	segment para 'code'
inicio	proc	far
	assume  ss:pila,ds:datos,cs:codigo,es:datos
	push    ds
	sub     ax,ax
	push    ax
	mov     ax,datos
	mov     ds,ax
	call	bopan
	mov	cx,5
	lea	si,menu
	lea	bx,poMen
	mov     dx,0000h
otro:	mov	dl,[bx]
	call    pocur
	call	esCad
	call	pocur
	mov	al,[si]
	call	esChar
	add	si,16
	inc	bx
	loop	otro
	ret
inicio	endp
;-----------------------Borra la pantalla--------------------------
;                       -----------------
bopan	proc
	mov	ah,06    ; o mov ah,07
	mov	al,0     ; Si AL=0 se borra la pantalla
	mov	bh,07
	mov	cx,0000  ; ESI
	mov	dx,184Fh ; EID
	int	10h
	ret
bopan	endp
;--------------------------Pone el cursor--------------------------
;                          --------------
pocur	proc
	push	bx
	mov	ah,02
	mov	bh,00      ; Pagina
	int	10h
	pop	bx
	ret
pocur	endp
;-------------------------Escribe un caracter----------------------
;                         -------------------
esChar	proc
	push	cx
	push	bx
	mov	ah,09h     ; o mov ah,0Ah
	mov	bh,0
	mov	bl,0Ah
	mov	cx,1
	int	10h
	pop	bx
	pop	cx
	ret
esChar	endp
;---------------------------Escribe una cadena---------------------
;                           ------------------
esCad	proc
	push	dx
	mov	dx,si
	mov	ah,09
	int	21h
	pop	dx
	ret
esCad	endp
;------------------------------------------------------------------
codigo	ends
	end     inicio
