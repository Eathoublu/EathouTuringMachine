# 图灵机模型 by Yixiao Lan
Email:yixiaolan@foxmail.com
## Introduce
A Turing Machine instance with assembler-like syntax and instruction set.
The script file name is hard coded in script is 'tape.trl', allowing you you change it to yours.Run it, and you will see output in the terminal.
We called the language for this model is 'trl'.
## Operation Set
Now the operation set is allow operate as follow:
For the following item, the first code is the operate code, followed by two arguments.The first argument is a memory cursor refer to a memory space(0<cursor<1024),the second argument is the immediate value or a memory cursor to add to the address value, result will storage in the memory space refer by the first argument. Remember to add an '@' symbol before the cursor's value like '@23'.
1. MOV @1,2    @1<-2
2. ADD @1,2    @1<-@1+2
3. DEC @1,2    @1<-@1-2
4. MUL @1,2    @1<-@1*2
5. DIV @1,2    @1<-@1/2
For the following item, the first code is the operate code, followed by three arguments.The first and second argument are immediate values or cursors.The third value is a process cursor (pc) to jump to if the bool value is true.
6. EQU 1,2,4    1=2?pc<-4:pc<-pc+1
7. NEQ 1,1,4    1!=2?pc<-4:pc<-pc+1
8. BGT 1,2,4    1>2?pc<-4:pc<-pc+1
9. SMT 1,2,4    1<2?pc<-4:pc<-pc+1
10. ANB 1,2,4    1&2?pc<-4:pc<-pc+1
11. ORB 1,2,4    1|2?pc<-4:pc<-pc+1
For the following item, the second argument is an memory cursor.
12. DEL @1    @1<-NULL
13. PRT @1    PRINT TO TERMINAL<-@1
For the following item, no second argument is needed.
14. PRTM    PRINT COMPLETE MEMORY TO TERMINAL
15. END    QUIT PROCESS
##Note
Remember to add ';' on every end of line.
There's no white space between value and ','.
##Sample
```TRL
MOV @1,2;
MUL @1,2;
PRT @1;
DEL @1;
PRT @1;
END;
------------
output:
4
0
```


