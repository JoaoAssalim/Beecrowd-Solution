#include <stdio.h>
 
int main() {
 
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        int num, soma = 0;
        scanf("%d", &num);
        for(int y = 1; y < num; y++){
            if(num%y == 0){
                soma += y;
            }
        }
        if(num == soma){
            printf("%d eh perfeito\n", num);
        }else{
            printf("%d nao eh perfeito\n", num);
        }
    }
}
