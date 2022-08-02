#include <stdio.h>
#include <math.h>

int main() {

    float x1,y1,x2,y2,d1,d2,dT;
    scanf("%f%f", &x1,&y1);
    scanf("%f%f", &x2,&y2);

    d1 = x2 - x1;
    d1 = d1 * d1;
    d2 = y2 - y1;
    d2 = d2 * d2;
    dT = d1 + d2;
    dT = sqrt(dT);

    printf("%.4f\n", dT);
}
