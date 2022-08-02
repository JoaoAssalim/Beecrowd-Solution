#include<stdio.h>

int main() {
    int T;
    scanf("%d", &T);
    for(int T1 = 1; T1 <= T; T1++){
        int B;
        int Ai, Di, Li, Ay, Dy, Ly;
        scanf("%d", &B);
        scanf("%d%d%d", &Ai, &Di, &Li);
        scanf("%d%d%d", &Ay, &Dy, &Ly);
        int golpe1, golpe2 = 0;
        golpe1 = (Ai + Di) / 2;
        golpe2 = (Ay + Dy) / 2;
        
        if(Li % 2 == 0){
            golpe1 = golpe1 + B;
        }
        if(Ly % 2 == 0){
            golpe2 = golpe2 + B;
        }
        
        if(golpe1 > golpe2){
            printf("Dabriel\n");
        }else if(golpe2 > golpe1){
            printf("Guarte\n");
        }else{
            printf("Empate\n");
        }
    }
    
    
}
