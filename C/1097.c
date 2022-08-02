#include <stdio.h>
 
int main() {
    int i,j,j1;
    i = 1;
    j = 7;
    j1 = j;
    
    while(i <= 9){
        j1 = j;
        for(int t = 1; t <= 3; t++){
            printf("I=%d J=%d\n",i, j1);
            j1 = j1 - 1;
        }
        j = j + 2;
        i = i + 2;
    }
}
