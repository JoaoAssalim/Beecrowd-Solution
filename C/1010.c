#include <stdio.h>
 
int main() {
 
    int cod, quant;
    float valor, total;
    scanf("%d%d%f", &cod,&quant,&valor);
    total = quant * valor;
    scanf("%d%d%f", &cod,&quant,&valor);
    total = total + quant * valor;
    printf("VALOR A PAGAR: R$ %.2f\n", total);
}
