#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    int hora, h = 0, m = 0;
    cin >> hora;
    
    if(hora >= 3600){
        h = hora / 3600;
        hora -= h * 3600;
    }if(hora >= 60){
        m = hora / 60;
        hora -= m * 60;
    }
    cout << h << ":" << m << ":" << hora << endl;
    
}
