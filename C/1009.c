#include <stdio.h>
 
int main() {
 
    char nome;
    double salario, vendas, salarioFinal;
    
    scanf("%s", &nome);
    scanf("%lf", &salario);
    scanf("%lf", &vendas);
    salarioFinal = vendas * 15 / 100;
    printf("TOTAL = R$ %.2lf\n", salarioFinal +  salario);
}
