#include <stdio.h>
 
int main() {
 
    int a,b;
    scanf("%d", &a);
    scanf("%d", &b);
    int soma = 0;
    if(a <= b){
        for(int i = a+1; i < b; i++){
            if(i%2){
                soma = soma + i;
            }
        }
    }else{
        for(int i = b+1; i < a; i++){
            if(i%2){
                soma = soma + i;
            }
        }
    }
    printf("%d\n", soma);
}
