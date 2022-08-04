#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    double a,b;
    cin >> a >> b;
    printf("%.6lf\n", ((((1.0 + a/100.00) * (1.0 + b/100.00)) - 1.0) * 100.0));
}
