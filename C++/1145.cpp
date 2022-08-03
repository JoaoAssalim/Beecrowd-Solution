#include <bits/stdc++.h>
 
int main() {
 
    int jump, num, count = 1;
    scanf("%d%d", &jump, &num);
    
    while(count <= num){
        for(int i = 1; i < jump+1; i++){
            if(i == jump){
                printf("%d", count);
            }else{
                printf("%d ", count);
            }
            count += 1;
        }
        printf("\n");
        
    }
}
