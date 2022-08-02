#include <stdio.h>
 
int main() {
    int total = 0;
    for(int i = 0; i < 6; i++){
        float a;
        scanf("%f", &a);
        if(a >= 0){
            total += 1;
        }
    }
    printf("%d valores positivos\n", total);
}
