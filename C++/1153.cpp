#include <bits/stdc++.h>
using namespace std;
int main() {
    int comp, total = 1;
    cin >> comp;
    for(int i = 1; i <=comp; i++){
        total *= i;
    }
    cout << total << endl;
}
