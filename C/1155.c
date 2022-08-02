#include <stdio.h>
 
int main() {
 
    float s = 1.0;
    for(float i = 2; i <= 100; i++){
        s += 1/i;
    }
    printf("%.2f\n", s);
}
