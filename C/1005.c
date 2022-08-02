#include <stdio.h>
 
int main() {
 
    float a,b, media;
    scanf("%f", &a);
    scanf("%f", &b);
    media = a * 3.5;
    media = media + b * 7.5;
    media = media / 11;
    printf("MEDIA = %.5f\n", media);
}
