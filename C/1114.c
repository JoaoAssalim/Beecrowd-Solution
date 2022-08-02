#include <stdio.h>
 
int main() {
    while(1){
        int ano;
        scanf("%d", &ano);
        if(ano == 2002){
            printf("Acesso Permitido\n");
            break;
        }else{
            printf("Senha Invalida\n");
        }
    }
}
