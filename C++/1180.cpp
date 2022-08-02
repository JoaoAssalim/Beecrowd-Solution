#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
 
    int n;
    cin >> n;
    int menor = 0, pos = 0;
    for(int i = 0; i < n; i++){
        int num;
        cin >> num;
        if(i == 0){
            menor = num;
        }
        if(num < menor){
            menor = num;
            pos = i;
        }
        
    }
    cout << "Menor valor: " << menor << "\n";
    cout << "Posicao: " << pos << "\n";
}
