#include <bits/stdc++.h>

using namespace std;

int main() {

    int i;
    cin >> i;
    
    for(int n =0; n < i; n++){
        int a,b, total=0;
        cin >> a >> b;
        
        if(a > b){
            int aux = a;
            a = b;
            b = aux;
        }
        for(int y = a+1; y < b; y++){
            if(y%2){total += y;}
        }
        cout << total << endl;
    }
}
