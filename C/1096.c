#include <stdio.h>
 
int main() {
    int i,j;
    i = 1;
    
    while(i <= 9){
        j = 7;
        for(int t = 1; t <= 3; t++){
            printf("I=%d J=%d\n",i, j);
            j = j - 1;
        }
        i = i + 2;
    }
}
