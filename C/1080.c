#include <stdio.h>
 
int main() {
 
    int maior = 0, posicao = 0;
    
    for(int i = 1; i < 101; i++){
        int num;
        scanf("%d", &num);
        if(num > maior){
            maior = num;
            posicao = i;
        }
    }
    printf("%d\n%d\n", maior, posicao);
}
