#include <stdio.h>
 
int main() {
 
    int h1,m1,h2,m2,start,end,dif,h,m;
    scanf("%d%d%d%d",&h1,&m1,&h2,&m2);
    start = h1*60+m1;
    end = h2*60+m2;
    dif = end-start;
    if (dif <= 0){
        dif = dif+24*60;
    }
    h = dif / 60;
    m = dif%60;
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", h, m);
}
