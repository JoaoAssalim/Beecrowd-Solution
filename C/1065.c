#include <stdio.h>
 
int main() {
 
   int total = 0;
   
   for(int i = 0; i < 5; i++){
       int n;
       scanf("%d", &n);
       if(n%2 == 0){
           total+=1;
       }
   }
   printf("%d valores pares\n", total);
}
