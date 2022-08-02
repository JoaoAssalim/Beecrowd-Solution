#include <stdio.h>
 
int main(){
    int a, b, c, d;
    
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%d", &d);
    
    int diferenca = a*b - c*d;
    printf("DIFERENCA = %d\n", diferenca);
}
