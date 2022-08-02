#include <stdio.h>

int main(){
    int i;
    scanf("%d", &i);

    for(int n = 1; n <= i; n++){
        char nome[100];
        scanf("%s", &nome);
        printf("Y\n");
    }
}
