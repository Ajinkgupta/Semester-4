DATA SEGMENT 
NO1 DB "9036"
D2 DB ?
D1 DB 16 DUP(?)
DATA ENDS

CODE SEGMENT 
ASSUME CS:CODE,DS:DATA
START:
MOV AX,DATA
MOV DS,AX
LEA SI,NO1
LEA DI,D1
MOV CX,04H

TOP:
MOV AL,[SI]
MOV DX,0CH

UP1:
ROL AX,1
DEC DX
JNZ UP1
AND AX,1111000000000000B
MOV DX,04H 

UP2:
ROL AX,1
JNC DN
MOV BX,1
MOV [DI] ,BX
JMP DN2

DN:
MOV BX,0
MOV [DI],BX

DN2:
INC DI
DEC DX
JNZ UP2
INC SI
DEC CX
JNZ TOP
INT 3



CODE ENDS 
END START