#include <bits/stdc++.h>

using namespace std;

int main() {
    int a,b,c;
    while(cin >> a >> b >> c){
        vector<int> l = {a,b,c};
        sort(l.begin(), l.end());
        
        if ((pow(l[2], 2) == pow(l[1], 2) + pow(l[0], 2)) && gcd(l[0], gcd(l[1], l[2])) == 1)
            cout << "tripla pitagorica primitiva\n";
        else if ((pow(l[2], 2) == pow(l[1], 2) + pow(l[0], 2)))
            cout << "tripla pitagorica\n";
        else
            cout << "tripla\n";
    }
}