a,b = map(int, input().split())
total = b-a

if total >= 3:
    print('Muito bem! Apresenta antes do Natal!')
elif total > 0 and total <= 2:
    if b < 23:
        print('Parece o trabalho do meu filho!')
        print('TCC Apresentado!')
    else:
        print('Parece o trabalho do meu filho!')
        print('Fail! Entao eh nataaaaal!')
else:
    print('Eu odeio a professora!')