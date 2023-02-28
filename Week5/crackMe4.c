#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void oil(uint *A, uint *D){
    *D = *D ^ 4;
    *A = *A | 0x2e39f3;
    return;
}

int main(){

    uint A;
    char *B;
    uint C;
    uint D;
    char E [360];
    int i;
    char Piece2 [360];
    size_t sVar2;
    int iVar1;
    FILE *__stream;

    //Input PID
    printf("Please enter your PID: ");
    scanf("%d", &C);

    A = 0x35478;
    B = "7030726e";
    for(i = 0; i < 7; i = i + 1){
        A = C ^ A;
        D = A + B[i] + 0x5c;
        oil(&A, &D);
        sprintf(E, "%d", (ulong)D);
        sVar2 = strlen(E);
        strncat((char *)&Piece2,E,sVar2);
        A = A << 7;
    }

    printf("Final code is: %s\n",Piece2);
    return 0;
}

