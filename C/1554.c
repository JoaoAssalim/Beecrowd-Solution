#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n; scanf("%d", &n);
    for(int i = 0; i < n; i++){
        int x; scanf("%d", &x);
        float bx, by; scanf("%f%f", &bx, &by);
        int near = 0;
        float dist = 999999999999999999999.0;
        for(int j = 0; j < x; j++){
            float x, y; scanf("%f%f", &x, &y);;
            float euc = sqrt((pow(abs(bx-x), 2) + pow(abs(by-y), 2)));
            if(euc < dist){
                dist = euc;
                near = j + 1;
            }
        }
        printf("%d\n", near);
    }
}
