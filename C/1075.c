#include <stdio.h>
 
int main() {
 
    int num;
    scanf("%d", &num);
    for(int i = 1; i<=10000;i++){
        if(i%num == 2){
            printf("%d\n", i);
        }
    }
}
