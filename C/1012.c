#include <stdio.h>
 
int main() {
 
    float a,b,c, total;
    scanf("%f%f%f", &a,&b,&c);
    total = a*c;
    printf("TRIANGULO: %.3f\n", total/2);
    total = c*c;
    printf("CIRCULO: %.3f\n", total*3.14159);
    total = a+b;
    printf("TRAPEZIO: %.3f\n", total*c/2);
    total = b*b;
    printf("QUADRADO: %.3f\n", total);
    total = a*b;
    printf("RETANGULO: %.3f\n", total);
}
