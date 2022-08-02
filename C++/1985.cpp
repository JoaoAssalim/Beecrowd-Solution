#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
 
    int a;
    float total = 0;
    cin >> a;
    for(int i = 0; i<a; i++){
        int cod, qnt;
        cin >> cod >> qnt;
        if(cod == 1001){ total += 1.50 * qnt;}
        else if(cod == 1002){ total += 2.50 * qnt;}
        else if(cod == 1003){ total += 3.50 * qnt;}
        else if(cod == 1004){ total += 4.50 * qnt;}
        else if(cod == 1005){ total += 5.50 * qnt;}
    }
    printf("%.2f\n", total);
}
