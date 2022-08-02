#include <stdio.h>
 
int main() {
    int n;
    scanf("%d", &n);
    
    for(int i = 1; i <= n;i++){
        float a,b,c, total;
        scanf("%f%f%f", &a,&b,&c);
        total = (a * 2 + b * 3 + c * 5) / 10;
        printf("%.1f\n", total);
    }
}
