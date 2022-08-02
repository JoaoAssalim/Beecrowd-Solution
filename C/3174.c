#include <stdio.h>
#include <string.h>
int main() {
 
    int bonecos = 0;
    int arquitetos = 0;
    int musicos = 0;
    int desenhistas = 0;
    int total = 0;
    int n;
    
    scanf("%d", &n);
    for(int i = 1; i <= n; i++){
        char nome[100], brinquedo[100];
        int tempo = 0;
        
        scanf("%s%s%d", &nome, &brinquedo, &tempo);
        if(strcmp(brinquedo, "bonecos") == 0){
            bonecos = bonecos + tempo; 
        }else if(strcmp(brinquedo, "arquitetos") == 0){
            arquitetos = arquitetos + tempo;
        }else if(strcmp(brinquedo, "musicos") == 0){
            musicos = musicos + tempo;
        }else if(strcmp(brinquedo, "desenhistas") == 0){
            desenhistas = desenhistas + tempo;
        }
    }
    total = total + bonecos / 8;
    total = total + arquitetos / 4;
    total = total + musicos / 6;
    total = total + desenhistas / 12;
    
    printf("%d\n", total);
}
