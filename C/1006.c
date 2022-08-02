#include <stdio.h>
 
int main() {
 
    float a,b,c, media;
    scanf("%f", &a);
    scanf("%f", &b);
    scanf("%f", &c);
    media = a * 2;
    media = media + b * 3;
    media = media + c * 5;
    media = media / 10;
    printf("MEDIA = %.1f\n", media);
}
