#include <stdio.h>
 
int main() {
    float c = 0;
    int n; scanf("%d", &n);
    for(int i = 0; i < n; i++){
        double a, b; scanf("%lf %lf", &a, &b);
        c += a/b;
    }
    if(c <= 1)
        printf("OK\n");
    else
        printf("FAIL\n");
}
