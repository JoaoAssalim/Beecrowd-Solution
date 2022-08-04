#include <bits/stdc++.h>

using namespace std;

int main() {
    int a, menor = 0, pos = 1;
    cin >> a;
    for(int i = 1; i <= a; i++){
        int n;
        cin >> n;
        if(i == 1){
            menor = n;
        }
        if(n < menor){
            menor = n;
            pos = i;
        }
    }
    cout << pos << endl;
}
