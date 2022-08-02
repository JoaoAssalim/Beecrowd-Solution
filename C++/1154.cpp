#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
 
    float idades = 0, quantidade = 0;
    while(1){
        int idade;
        cin >> idade;
        if(idade < 0){
            break;
        }
        idades += idade;
        quantidade += 1;
    }
    printf("%.2f\n", idades/quantidade);
}
