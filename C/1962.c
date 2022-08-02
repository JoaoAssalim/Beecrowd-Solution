#include <stdio.h>
 
int main() {
 
    int n, antigo = 2015, atual =0;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        int ano;
        scanf("%d", &ano);
        if(ano >= antigo){
            printf("%d A.C.\n", ano-antigo+1);
        }else{
            printf("%d D.C.\n", antigo-ano);
        }
    }
}
