#include <stdio.h>
 
int main() {
 
    char palavra[50] = "LIFE IS NOT A PROBLEM TO BE SOLVED";
    int x;
    scanf("%d", &x);
    
    for(int i = 0; i < x; i++){
        printf("%c", palavra[i]);
    }
    printf("\n");
}
