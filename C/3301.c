#include <stdio.h>
int main() {

    int a,b,c;
    scanf("%d%d%d", &a,&b,&c);
    if(a > b && a < c){
        printf("huguinho\n");
    }else if(a < b && a > c){
        printf("huguinho\n");
    }else if(b > a && b < c){
        printf("zezinho\n");
    }else if(b < a && b > c){
        printf("zezinho\n");
    }else{
        printf("luisinho\n");
    }
}
