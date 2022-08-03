#include <iostream>
using namespace std;
 
int main() {
    int x;
    while(scanf("%d", &x) != EOF){
        if(x == 0){
            printf("vai ter copa!\n");
        }else{
            printf("vai ter duas!\n");
        }
    }
}
