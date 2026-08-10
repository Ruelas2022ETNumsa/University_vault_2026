              page    65,132
title         TITULO DEL inicio
;------------------------------------------------------------------
;                           Segmento de pila
;                           ----------------
pila	segment para stack 'stack'
	dw      32   dup(?)
pila	ends
;------------------------------------------------------------------
;                           Segmento de datos
;                           -----------------
datos	segment para 'data'
datos	ends
;------------------------------------------------------------------
codigo	segment para 'code'
inicio	proc	far
	assume  ss:pila,ds:datos,cs:codigo,es:datos
	push    ds
	sub     ax,ax
	push    ax
	mov     ax,datos
	mov     ds,ax
	call	bopan
	call    pocur
	call	esChar
	ret
inicio	endp
;------------------------------------------------------------------
bopan	proc
	mov ah,06    ; o mov ah,07
	mov al,0     ; Si AL=0 se borra la pantalla
	mov bh,07
	mov cx,0000  ; ESI
	mov dx,184Fh ; EID
	int 10h
	ret
bopan	endp
;------------------------------------------------------------------
pocur	proc
	mov ah,02
	mov bh,00      ; Pagina
	mov dh,12      ; fila
	mov dl,40      ; columna
	int 10h
	ret
pocur	endp
;------------------------------------------------------------------
esChar	proc
	mov ah,09h     ; o mov ah,0Ah
	mov al,'J'
	mov bh,0
	mov bl,07
	mov cx,1
	int 10h
	ret
esChar	endp
;------------------------------------------------------------------
codigo	ends
	end     inicio
