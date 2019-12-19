# 图灵机模型 by Yixiao Lan
## Introduce
图灵机模型，修改源码中硬编码的'test.el'为自己的脚本文件即可运行，即可在控制台看到输出。
''.el'是定义的为该模型的脚本语言的后缀。
## Operation Set
指令集定义如下：（内存地址前面要加@，立即数前不用加，程序指针前不用加）
1. MOV @1,2    @1<-2
2. ADD @1,2    @1<-@1+2
3. DEC @1,2    @1<-@1-2
4. MUL @1,2    @1<-@1*2
5. DIV @1,2    @1<-@1/2
6. EQU 1,2,4    1=2?pc<-4:pc<-pc+1
7. NEQ 1,1,4    1!=2?pc<-4:pc<-pc+1
8. BGT 1,2,4    1>2?pc<-4:pc<-pc+1
9. SMT 1,2,4    1<2?pc<-4:pc<-pc+1
10. ANB 1,2,4    1&2?pc<-4:pc<-pc+1
11. ORB 1,2,4    1|2?pc<-4:pc<-pc+1
12. DEL @1    @1<-NULL
13. PRT @1    PRINT TO TERMINAL<-@1
14. PRTM    PRINT COMPLETE MEMORY TO TERMINAL
15. END    QUIT PROCESS
##Note
每行末尾都要有';'。
值与','中间没有空格。
##Sample
```EL
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


