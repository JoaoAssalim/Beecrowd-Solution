#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    int notas[10] = {100, 50, 20, 10, 5, 2, 1};
    int val;
    cin >> val;
    
    cout << val << endl;
    for(int i = 0; i < 7; i++){
        int qnt = 0;
        if(val >= notas[i]){
            qnt = val / notas[i];
            val -= notas[i] * qnt;
        }
        cout << qnt << " nota(s) de R$ " << notas[i] << ",00\n";
    }
}
