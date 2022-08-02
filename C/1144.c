#include <stdio.h>
 
int main() {
 
    int n;
    scanf("%d", &n);
    
    for(int i = 1; i < n+1; i++){
        printf("%d %d %d\n", i, i*i, i*i*i);
        printf("%d %d %d\n", i, i*i + 1, i*i*i + 1);
    }
}
