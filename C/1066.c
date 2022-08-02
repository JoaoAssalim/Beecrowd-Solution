#include <stdio.h>
 
int main() {
 
    int par = 0, impar = 0, positivo = 0, negativo = 0;
    
    for(int i = 0; i < 5; i++){
        int num;
        scanf("%d", &num);
        
        if(num % 2){
            impar += 1;
        }else{
            par += 1;
        }
        if(num < 0){
            negativo += 1;
        }else if(num > 0){
            positivo += 1;
        }
    }
    
    printf("%d valor(es) par(es)\n", par);
    printf("%d valor(es) impar(es)\n",impar);
    printf("%d valor(es) positivo(s)\n", positivo);
    printf("%d valor(es) negativo(s)\n",negativo); 
} 
