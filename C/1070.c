#include <stdio.h>
 
int main() {
 
    int quant, n;
    quant = 0;
    scanf("%d", &n);
    
    while(1){
        if (quant == 6){
            break;
        }
        if(n % 2 == 1){
            printf("%d\n", n);
            n = n + 2;
            quant ++;
        }else{
            n = n + 1;
        }
    }
}
