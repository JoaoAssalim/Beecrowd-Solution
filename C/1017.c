#include <stdio.h>
 
int main() {
 
    int a,b;
    float litros;
    scanf("%d", &a);
    scanf("%d", &b);
    litros = a * b;
    litros = litros / 12;
    printf("%.3f\n", litros);
}
