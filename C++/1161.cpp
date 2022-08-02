#include <bits/stdc++.h>

using namespace std;

int main() {
    int a,b;
    while(scanf("%d%d", &a, &b) != EOF){
        long long int totalA = 1, totalB = 1, total = 0;
        
        for(int i = 1; i <= a; i++){
            totalA *= i;
        }
        for(int y = 1; y <= b; y++){
            totalB *= y;
        }
        total = totalA + totalB;
        cout << total << "\n";
    }
    return 0; 
}
