#include <stdio.h>
 
int main() {
    char *mes[12] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
    int a;
    scanf("%d", &a);
    printf("%s\n", mes[a-1]);
}
