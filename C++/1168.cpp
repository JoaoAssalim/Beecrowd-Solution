#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    for(int i = 0; i < n; i++){
        char num[101];
        cin >> num;
        int leds = 0;
        for(int p = 0; p < strlen(num); p++){
            if(num[p] == '1'){
                leds += 2;
            }else if(num[p] == '2' || num[p] == '3' || num[p] == '5'){
                leds += 5;
            }else if(num[p] == '4'){
                leds += 4;
            }else if(num[p] == '6' || num[p] == '9' || num[p] == '0'){
                leds += 6;
            }else if(num[p] == '7'){
                leds += 3;
            }else if(num[p] == '8'){
                leds += 7;
            }
        }
        cout << leds << " leds" << endl;
    }
}
