#include <bits/stdc++.h>

using namespace std;

int main() {
    int n = 1;
    while(1){
        int num; cin >> num;
        if(num == 0)
            break;
        cout << "Teste " << n << endl;
        n++;
        long long int movimentos = (pow(2, num)) - 1;
        cout << movimentos << endl << endl;
    }
}
