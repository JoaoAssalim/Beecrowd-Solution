#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    int n;
    cin >> n;
    
    for(int i =0; i < n; i++){
        float a,b;
        cin >> a >> b;
        
        if(b == 0){
            cout << "divisao impossivel\n";
        }else{
            printf("%.1f\n", a/b);
        }
    }
    
}
