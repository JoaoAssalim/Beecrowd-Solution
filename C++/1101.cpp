#include <bits/stdc++.h>

using namespace std;

int main() {

    while(1){
        int m,n, total = 0;
        cin >> m >> n;
        if(m <= 0 || n <= 0){
            break;
        }
        if(m < n){
            int aux = m;
            m = n;
            n = aux;
        }
        for(int i = n; i <= m; i++){
            cout << i << " ";
            total += i;
        }
        cout << "Sum=" << total << endl;
    }
}
