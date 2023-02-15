data segment
a dw 0001
b dw 0002
c dw 5003
d dw 9004
r1 dd ?
r2 dd ?
data ends
 
code segment
assume cs:code,ds:data
start:
mov ax,data
mov ds,ax
mov ax,a
mov bx,b
mov cx,c
mov dx,d 
adc ax,bx
adc cx,dx
mov r1,ax
mov r2,bx
int 3
code ends
end start
