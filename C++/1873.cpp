#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    int n;
    cin >> n;
    
    for(int i = 0; i < n; i++){
        string a, b;
        cin >> a >> b;
        
        if(a == b){
            cout << "empate";
        }else{
            if(a == "tesoura" && b == "papel"){cout << "rajesh";}
            else if(b == "tesoura" && a == "papel"){cout << "sheldon";}
            
            else if(a == "papel" && b == "pedra"){cout << "rajesh";}
            else if(b == "papel" && a == "pedra"){cout << "sheldon";}
            
            else if(a == "pedra" && b == "lagarto"){cout << "rajesh";}
            else if(b == "pedra" && a == "lagarto"){cout << "sheldon";}
            
            else if(a == "lagarto" && b == "spock"){cout << "rajesh";}
            else if(b == "lagarto" && a == "spock"){cout << "sheldon";}
            
            else if(a == "spock" && b == "tesoura"){cout << "rajesh";}
            else if(b == "spock" && a == "tesoura"){cout << "sheldon";}
            
            else if(a == "tesoura" && b == "lagarto"){cout << "rajesh";}
            else if(b == "tesoura" && a == "lagarto"){cout << "sheldon";}
            
            else if(a == "lagarto" && b == "papel"){cout << "rajesh";}
            else if(b == "lagarto" && a == "papel"){cout << "sheldon";}
            
            else if(a == "papel" && b == "spock"){cout << "rajesh";}
            else if(b == "papel" && a == "spock"){cout << "sheldon";}
            
            else if(a == "spock" && b == "pedra"){cout << "rajesh";}
            else if(b == "spock" && a == "pedra"){cout << "sheldon";}
            
            else if(a == "pedra" && b == "tesoura"){cout << "rajesh";}
            else if(b == "pedra" && a == "tesoura"){cout << "sheldon";}
        }
        cout << endl;
    }
}
