pila    segment stack
        dw 100 dup(0)
pila    ends
;----------------------------------------
datos   segment
a       db   1
b       db   2
c       db   0
datos   ends
;----------------------------------------
codigo  segment
program proc far
        assume ss:pila,ds:datos,cs:codigo
        push ds          ; 1)
        sub  ax,ax
        push ax          ; 2)
        mov  ax,datos
        mov  ds,ax

        mov  al,a
        push ax          ; 3)
        mov  bl,b
        push bx          ; 4)
        call sumar       ; 5)
        mov  c,al
        retf
program endp
;----------------------------------------
sumar   proc
	push bp          ; 6)
        mov  ax,sp
        mov  bp,ax
        mov  ax,[bp+6]
        mov  bx,[bp+4]
        add  al,bl
        pop  bp
        ret  2	; Se descartan dos
		; operandos
sumar   endp
;----------------------------------------
codigo  ends
        end  program
