#include <iostream>
 
using namespace std;
 
int main() {
 
    string palavra;
    cin >> palavra;
    if(palavra.length() >= 10){
        cout << "palavrao\n";
    }else{
        cout << "palavrinha\n";
    }
}
