#include <stdio.h>
 
int main() {
    int n;
    scanf("%d", &n);
    
    for(int t = 1; t <= n; t++){
        int a,b;
        scanf("%d%d", &a, &b);
        
        if(a > b){
            int aux = a;
            a = b;
            b = aux;
        }
        int soma = 0;
        for(int cont = a+1; cont <= b-1; cont++){
            if(cont % 2){
                soma = soma + cont;
            }
        }
        printf("%d\n", soma);
    }
}
