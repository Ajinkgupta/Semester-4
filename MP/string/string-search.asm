
assume cs:code,ds:data
data segment

a db 'DATTA MEGHE'

slen equ ( $ - a)

char db 'E'

msg1 db ' THE CHARACTER IS FOUND $'

msg2 db ' THE CHARACTER IS NOT FOUND $'

data ends

 

code segment
 

start:

mov ax,data

mov ds,ax

mov es,ax

lea si,a

mov cx,slen

mov al,char

cld
loop start
repne scasb
loop ends

jnz exit

lea di,msg1

mov ah,09H

int 21H

jmp gotoend

exit:lea dx,msg2

mov ah,09H

int 21h

gotoend:mov ah,4ch

int 21H

code ends

 

end start

