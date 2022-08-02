#include <stdio.h>
 
int main() {
 
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n;i++){
        int start, quant, soma = 0;
        scanf("%d%d", &start, &quant);
        while(1){
            if (quant == 0){
                break;
            }
            if(start % 2){
                soma += start;
                quant -= 1;
                start += 2;
            }else{
                start += 1;
            }
        }
        printf("%d\n", soma);
        
    }
}
