#include <stdio.h>
#include <string.h>
int main() {

    int a;
    scanf("%d", &a);
    for (int contador = 1; contador <= a; contador++) {
        int result;
        scanf("%d", &result);
        printf("resposta %d: %d\n", contador, result);
    }
}
