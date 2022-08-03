#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    int n, p = 3;
    cin >> n;
    
    for(int i =0; i < n; i++){
        cout << p-2 << " " << p-1 << " " << p << " PUM\n";
        p += 4;
    }
    
}
