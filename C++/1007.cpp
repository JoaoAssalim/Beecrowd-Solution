#include <bits/stdc++.h>

using namespace std;

int main() {
    int a,b,c,d;
    cin >> a >> b >> c >> d;
    int dif = a * b - c * d;
    if(dif == 0){
        printf("DIFERENCA = 0\n");
    }else{
        printf("DIFERENCA = %.d\n", dif);
    }
}
