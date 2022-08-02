#include <stdio.h>
 
int main() {
 
    float a, reajuste;
    scanf("%f", &a);
    
    if(a <= 400.00){
        reajuste = (a * 15) / 100;
        printf("Novo salario: %.2f\n", a+reajuste);
        printf("Reajuste ganho: %.2f\n", reajuste);
        printf("Em percentual: 15 %\n");
    }else if(a > 400.00 && a <= 800.00){
        reajuste = (a * 12) / 100;
        printf("Novo salario: %.2f\n", a+reajuste);
        printf("Reajuste ganho: %.2f\n", reajuste);
        printf("Em percentual: 12 %\n");
    }else if(a > 800.00 && a <= 1200.00){
        reajuste = (a * 10) / 100;
        printf("Novo salario: %.2f\n", a+reajuste);
        printf("Reajuste ganho: %.2f\n", reajuste);
        printf("Em percentual: 10 %\n");
    }else if(a > 1200.00 && a <= 2000.00){
        reajuste = (a * 7) / 100;
        printf("Novo salario: %.2f\n", a+reajuste);
        printf("Reajuste ganho: %.2f\n", reajuste);
        printf("Em percentual: 7 %\n");
    }else{
        reajuste = (a * 4) / 100;
        printf("Novo salario: %.2f\n", a+reajuste);
        printf("Reajuste ganho: %.2f\n", reajuste);
        printf("Em percentual: 4 %\n");
    }
}
