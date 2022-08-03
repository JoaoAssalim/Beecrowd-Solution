#include <bits/stdc++.h>
using namespace std;
int main() {
    int comp, ant = 0, prox = 1;
    cin >> comp;
    cout << ant << " " << prox << " ";
    for(int i = 0; i < comp-2; i++){
        int aux = prox;
        prox += ant;
        ant = aux;
        cout << prox;
        if(i < comp-3){
            cout << " ";
        }
    }
    cout << endl;
}
