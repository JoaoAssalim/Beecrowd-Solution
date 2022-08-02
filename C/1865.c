#include <stdio.h>
#include <string.h>
int main() {
 
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        char str[100];
        int forca;
        scanf("%s%d", &str, &forca);
        if(strcmp(str, "Thor")==0){
            printf("Y\n");
        }else{
            printf("N\n");
    
        }
    }
}
