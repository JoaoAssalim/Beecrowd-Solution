#include <bits/stdc++.h>

using namespace std;

int main() {
    int n; cin >> n;
    for(int i = 0; i < n; i++){
        int x; cin >> x;
        float bx, by; cin >> bx >> by;
        int near = 0;
        float dist = 999999999999999999999.0;
        for(int j = 0; j < x; j++){
            float x, y; cin >> x >> y;
            float euc = sqrt((pow(abs(bx-x), 2) + pow(abs(by-y), 2)));
            if(euc < dist){
                dist = euc;
                near = j + 1;
            }
        }
        cout << near << endl;
    }
}
