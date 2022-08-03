#include <bits/stdc++.h>
using namespace std;
int main() {
 
    int n;
    cin >> n;
    for(int i = 0; i < n;i++){
        int start, quant, soma = 0;
        cin >> start >> quant;
        while(1){
            if (quant == 0){
                break;
            }
            if(start % 2){
                soma += start;
                quant -= 1;
                start += 2;
            }else{
                start += 1;
            }
        }
        cout << soma << endl;
        
    }
}
