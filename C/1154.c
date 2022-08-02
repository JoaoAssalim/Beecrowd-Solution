#include <stdio.h>
 
int main() {

    float media = 0, idade = 0, quant = 0;
    
    while(1){
        int i;
        scanf("%d", &i);
        
        if(i < 0){
            break;
        }else{
            idade += i;
            quant += 1;
        }
    }
    media = idade/quant;
    printf("%.2f\n", media);
}
