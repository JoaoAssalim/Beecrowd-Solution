#include <bits/stdc++.h>

int calc(int x){
    int y = sqrt(x);
    return x - y;
}

using namespace std;

int main() {
    int x; cin >> x;
    for(int i = 0; i < x; i++){
        int n; cin >> n;
        cout << calc(n) << endl;
    }
}