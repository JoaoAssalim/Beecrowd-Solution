#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
 
    int i = 1, j = 7;
    
    int aux = j;
    while(i <= 9){
        int aux = j;
        for(int c = 0; c < 3; c++){
            cout << "I=" << i << " J=" << aux << endl;
            aux -= 1;
        }
        i += 2;
    }
}
