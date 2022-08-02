m=input().split()
h1,m1,h2,m2 = int(m[0]), int(m[1]), int(m[2]), int(m[3])
start=h1*60+m1
end=h2*60+m2
dif=end-start

if dif<=0:
    dif+=24*60

h=dif//60
m=dif%60

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')