#include <bits/stdc++.h>

using namespace std;

int main() {
    int n; cin >> n;
    int aux = 0;
    cin.ignore();
    for(int i = 0; i < n; i++){
        string s; cin >> s;
        if(s.find("CD") != string::npos){
            aux++;
        }
    }
    cout << n-aux << endl;

}
