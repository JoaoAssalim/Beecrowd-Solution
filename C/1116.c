#include <stdio.h>
 
int main() {
 
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        float a,b;
        float result = 0;
        scanf("%f%f", &a, &b);
        
        if(b == 0){
            printf("divisao impossivel\n");
        }else{
            result = a / b;
            printf("%.1f\n", result);
        }
    }
}
