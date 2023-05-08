#include <bits/stdc++.h>

using namespace std;

int main() {
    int a,b;
    while(cin >> a >> b){
        int x1 = b*2, x2 = b * 3;
        
        if(x1 > a || x2 > a)
            cout << "Raios! Raios Duplos! Raios Triplos!\n";
        else{
            int sqr = sqrt(a), dir = 1, x = 0, y = 0, n = a, aux = a, maxlen = to_string(a).length();
            string mat[sqr][sqr];
            
            for(int i = a; i > 0; i--){
                string s = to_string(i);
                if(i == x1)
                    s = "*";
                else if(i == x2)
                    s = "!";
                
                
                while(s.length() < maxlen){
                    s = " " + s;
                }
                
                mat[x][y] = s;
                
                if (dir == 1){
                    if (y < sqr-1){
                        if (mat[x][y+1] == "\0")
                            y += 1;
                        else{
                            x += 1;
                            dir = 2;
                        }
                    }else{
                        x += 1;
                        dir = 2;
                    }
                }else if (dir == 2){
                    if (x < sqr-1){
                        if (mat[x+1][y] == "\0"){
                            x += 1;
                        }else{
                            y -= 1;
                            dir = 3;
                        }
                    }else{
                        y -= 1;
                        dir = 3;
                    }

                }else if (dir == 3){
                    if (y >= 0){
                        if (mat[x][y-1] == "\0")
                            y -= 1;
                        else{
                            x -= 1;
                            dir = 4;
                        }
                    }else{
                        x -= 1;
                        dir = 2;
                    }
                }else if (dir == 4){
                    if (x >= 0){
                        if (mat[x-1][y] == "\0"){
                            x -= 1;
                        }else{
                            y += 1;
                            dir = 1;
                        }
                    }else{
                        y += 1;
                        dir = 1;
                    }
                }
            }
            
            for(int i = 0; i < sqr; i++){
                for(int j = 0; j < sqr; j++){
                    if(i == sqr-1 && j == sqr-1)
                        cout << mat[i][j];
                    else
                        cout << mat[i][j] << " ";
                }
                cout << endl;
            }
        }
    }
}
