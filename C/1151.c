#include <stdio.h>
 
int main() {
 
    int anterior = 0, proximo = 1, aux = 0;
    int comp, total = 2;
    
    scanf("%d", &comp);
    
    printf("%d %d ", anterior, proximo);
    while (total < comp-1){
        aux = anterior + proximo;
        anterior = proximo;
        proximo = aux;
        total += 1;
        printf("%d ", proximo);
    }
    printf("%d\n", proximo+anterior);
    
}
