#include <bits/stdc++.h>
using namespace std;
int main() {
    while(1){
        int n;
        cin >> n;
        if(n == 0){
            break;
        }
        for(int i = 1; i <= n; i++){
            if(i < n){
                cout << i << " ";
            }else{
                cout << i << endl;
            }
        }
    }
}
