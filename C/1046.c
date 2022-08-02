#include <stdio.h>
 
int main() {
 
    int a,b;
    scanf("%d%d", &a,&b);
    if(a>=b){
        a = a-b;
        a = 24 - a;
    }else{
        a = b - a;
    }
    printf("O JOGO DUROU %d HORA(S)\n", a);
}
