        page    65,132
title   TITULO DEL inicio
;--------------------Segmento de pila-----------------
;                    ----------------
pila    segment para stack 'stack'
        dw      32   dup(?)
pila    ends
;-------------------Segmento de datos-----------------
;                   -----------------
datos  segment para 'data'
menu   db "File       $Edit       $View       $"
       db "Run        $Breakpoints$Data       $"
       db "Options    $Windows    $Help       $"

       db "F1-Help $F2-Bkpt $F3-Mod  $F4-Here $"
       db "F5-Zoom $F6-Next $F7-Trace$F8-Step $"
       db "F9-Run  $F10-Menu$"

posMen dw 0002h,0008h,000Eh,0014h,0019h,0026h,002Ch
       dw 0035h,003Eh,1800h,1808h,1810h,1817h,181Fh
       dw 1827h,182Fh,1838h,1840h,1847h
datos  ends
;------------------Segmento de codigo-----------------
;                  ------------------
codigo segment para 'code'
inicio proc    far
       assume  ss:pila,ds:datos,cs:codigo,es:datos
       push    ds
       sub     ax,ax
       push    ax
       mov     ax,datos
       mov     ds,ax

       mov     bh,70h     ;-+
       mov     cx,0000h   ; |> Menu screen
       mov     dx,004Fh   ;-+
       call    bopan
       mov     bh,3Fh     ;-+
       mov     cx,0100h   ; |> Work screen
       mov     dx,184Fh   ;-+
       call    bopan
       mov     bh,70h     ;-+ 
       mov     cx,1800h   ; |> Tools screen
       mov     dx,184Fh   ;-+
       call    bopan
       mov     cx,9            ;-------+
       lea     si,menu         ;       |
       mov     bx,0            ;       |
otro:  mov     dx,posMen[bx]   ;       |
       call    pocur           ;       |
       call    esCad           ;       |> Menu
       call    pocur   ;-+             |
       mov     al,[si] ; |1s Char red  |
       call    esChar  ;-+             |
       add     si,12           ;       |
       add     bx,2            ;       |
       loop    otro            ;-------+
       mov     cx,10           ;---------------+
       lea     si,menu+108     ;               |
       mov     bx,18           ;               |
otro1: mov     dx,posMen[bx]   ;               |
       call    pocur           ;               |
       call    esCad           ;               |
       call    pocur           ;               |
       mov     al,[si]         ;               |>Tools
       call    esChar          ;               |>Tools
       mov     dx,posMen[bx]   ;-+             |
       inc     dl              ; |Segundo      |
       call    pocur           ; |caracter rojo|
       mov     al,[si+1]       ;-+             |
       call    esChar          ;               |
       add     si,9            ;               |
       add     bx,2            ;               |
       loop    otro1           ;---------------+
       mov     dx,posMen[bx-2] ;-+
       add     dl,2            ; |
       call    pocur           ; |> Tercer
       sub     si,9            ; |> caracter rojo
       mov     al,[si+2]       ; |
       call    esChar          ;-+
       mov     dx,0100h
       call    pocur
       ret
inicio endp
;-------------------Borra la pantalla-----------------
;                   -----------------
bopan  proc
       mov     ah,06    ; o mov ah,07
       mov     al,0     ; Si AL=0 se borra la pantalla
       int     10h
       ret
bopan  endp
;--------------------Pone el cursor-------------------
;                    --------------
pocur  proc
       push    bx
       mov     ah,02
       mov     bh,00      ; Pagina
       int     10h
       pop     bx
       ret
pocur  endp
;-----------------Escribe un caracter-----------------
;                 -------------------
esChar proc
       push    cx
       push    bx
       mov     ah,09h     ; o mov ah,0Ah
       mov     bh,0
       mov     bl,74h
       mov     cx,1
       int     10h
       pop     bx
       pop     cx
       ret
esChar endp
;------------------Escribe una cadena-----------------
;                  ------------------
esCad  proc
       push    dx
       mov     dx,si
       mov     ah,09
       int     21h
       pop     dx
       ret
esCad  endp
;-----------------------------------------------------
codigo ends
       end     inicio
