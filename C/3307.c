#include<stdio.h>
#include <math.h>

int main() {
    int n; scanf("%d", &n);
    for(int i = 0; i < n; i++){
        int x; scanf("%d", &x);
        double r = sqrt(x/(4*3.14));
        if(r < 12)
            printf("vermelho = R$ %.2lf\n", x*0.09);
        else if(r <= 15)
            printf("azul = R$ %.2lf\n", x*0.07);
        else
            printf("amarelo = R$ %.2lf\n", x*0.05);
    }
    
}
