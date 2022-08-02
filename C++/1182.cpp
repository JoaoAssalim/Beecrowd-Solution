#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    int linha;
    cin >> linha;
    char oper[2];
    cin >> oper;
    float matriz[12][12];
    
    for(int i = 0; i < 12; i++){
        for(int y = 0; y < 12; y++){
            float num;
            cin >> num;
            matriz[i][y] = num;
        }
    }
    float total;
    for(int n = 0; n < 12; n++){
        total += matriz[n][linha];
    }
    
    if(oper == "S"){
        printf("%.1f\n", total);
    }else{
        printf("%.1f\n", total/12.0);
    }
}
