#include <stdio.h>
 
int main() {
 
    int x,a, resp = 1, menor = 0;
    scanf("%d", &x);
    
    for(int i = 0; i < x; i++){
        scanf("%d", &a);
        if(i == 0){
            menor = a;
        }
        if(a < menor){
            menor = a;
            resp = i+1;
        }
    }
    printf("%d\n", resp);
}
