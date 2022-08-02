#include <stdio.h>
 
int main() {
 
    float s = 1;
    float a = 3, b = 2;
    
    while(a <= 39){
        s += a/b;
        a += 2;
        b *= 2;
    }
    printf("%.2f\n", s);
}
