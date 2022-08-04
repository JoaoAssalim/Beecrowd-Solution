#include <bits/stdc++.h>
 
using namespace std;

int main() {

    int a,b,c;
    cin >> a >> b >> c;
    if(a > b && a < c){
        printf("huguinho\n");
    }else if(a < b && a > c){
        printf("huguinho\n");
    }else if(b > a && b < c){
        printf("zezinho\n");
    }else if(b < a && b > c){
        printf("zezinho\n");
    }else{
        printf("luisinho\n");
    }
}
