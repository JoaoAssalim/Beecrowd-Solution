#include <stdio.h>
 
int main() {
 
    int n;
    scanf("%d", &n);
    int in = 0;
    for(int i = 1; i <= n; i++){
        int num;
        scanf("%d", &num);
        if(num >= 10 && num <= 20){
            in = in + 1;
        }
    }
    
    printf("%d in\n", in);
    printf("%d out\n", n-in);
}
