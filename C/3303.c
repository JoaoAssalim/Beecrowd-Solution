#include <stdio.h>
#include <string.h>
int main() {

    char a[20];
    scanf("%s", &a);
    if(strlen(a) >= 10){
        printf("palavrao\n");
    }else{
        printf("palavrinha\n");
    }
}
