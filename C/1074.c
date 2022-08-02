#include <stdio.h>
 
int main() {
 
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n;i++){
        int num;
        scanf("%d", &num);
        if(num == 0){
            printf("NULL\n");
        }else if(num%2){
            if(num > 0){
                printf("ODD POSITIVE\n");
            }else{
                printf("ODD NEGATIVE\n");
            }
        }else{
            if(num > 0){
                printf("EVEN POSITIVE\n");
            }else{
                printf("EVEN NEGATIVE\n");
            }
        }
    }
}
