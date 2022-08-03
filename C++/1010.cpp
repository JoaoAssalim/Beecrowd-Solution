#include <bits/stdc++.h>

using namespace std;

int main() {
    float total = 0;
    for(int i = 0; i < 2; i++){
        float a,b,c;
        cin >> a >> b >> c;
        total += b*c;
    }
    printf("VALOR A PAGAR: R$ %.2f\n", total);
}
