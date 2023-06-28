#include <iostream>

using namespace std;

int main() {
    float c = 0;
    int n; cin >> n;
    for(int i = 0; i < n; i++){
        double a, b; cin >> a >> b;
        c += a/b;
    }
    if(c <= 1)
        cout << "OK\n";
    else
        cout << "FAIL\n";
}
