#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
 
    int n, in = 0, out = 0;
    cin >> n;
    for(int i = 0; i < n; i++){
        int num;
        cin >> num;
        if(num >= 10 and num <= 20){in += 1;}
        else{out += 1;}
    }
    cout << in << " in\n";
    cout << out << " out\n";
}
