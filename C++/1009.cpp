#include <bits/stdc++.h>

using namespace std;

int main() {
    char name[101];
    float b,c;
    cin >> name >> b >> c;
    printf("TOTAL = R$ %.2f\n", b + (c*15/100));
}
