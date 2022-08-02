#include <stdio.h>

int main() {
 
    int n,n1,n2,n3, total;
    scanf("%d%d%d%d", &n,&n1,&n2,&n3);
    
    total = (n+n1+n2+n3) - 3;
    printf("%d\n", total);
}
