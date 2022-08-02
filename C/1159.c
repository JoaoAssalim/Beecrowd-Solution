#include <stdio.h>

int main() {

    while(1){
        int start, quant = 5, soma = 0;
        scanf("%d", &start);
        if(start == 0){
            break;
        }
        while(1){
            if (quant == 0){
            break;
            }
            if(start % 2 == 0){
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
