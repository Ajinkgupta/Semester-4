assume cs:code,ds:data
data segment

a db 'DATTA MEGHE'
slen equ ($ - a)

msg1 db 'THE CHARACTER IS FOUND $'
msg2 db 'THE CHARACTER IS NOT FOUND $'
msg3 db 'NUMBER OF TIMES "E" FOUND: $'

data ends

code segment

start:
mov ax,data
mov ds,ax
mov es,ax

lea si,a
mov cx,slen

mov al,'E'
xor bx,bx

cld
repne scasb
jcxz exit

inc bx
loop start

lea dx,msg1
mov ah,09H
int 21H

jmp output_count

exit:
lea dx,msg2
mov ah,09H
int 21h

output_count:
lea dx,msg3
mov ah,09H
int 21h

mov al,bh
add al,30h
mov ah,02h
int 21h

mov ah,4ch
int 21H

code ends
end start
