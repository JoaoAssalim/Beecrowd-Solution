#include <stdio.h>

int main() {
 
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        int num;
        scanf("%d", &num);
        if(num%2){
            printf("1\n");
        }else{
            printf("0\n");
    
        }
    }
}
