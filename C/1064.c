#include <stdio.h>
 
int main() {
    int quant = 0;
    float total = 0.0;
    float media = 0.0;
    for(int i = 1; i <= 6; i++){
        float val;
        scanf("%f", &val);
        if(val >= 0){
            total = total + val;
            quant ++;
        }
    }
    media = total / quant;
    printf("%d valores positivos\n", quant);
    printf("%.1f\n", media);
}
