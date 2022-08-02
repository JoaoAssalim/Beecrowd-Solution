#include <stdio.h>
 
int main() {
 
    int n, hour;
    float salary;
    
    scanf("%d", &n);
    scanf("%d", &hour);
    scanf("%F", &salary);
    
    printf("NUMBER = %d\n", n);
    printf("SALARY = U$ %.2f\n", salary*hour);
}
