for i in range(int(input())):
    graos = 1
    casas = int(input())
    for c in range(casas):
        graos = graos * 2
    
    peso = (graos / 12) * 0.001
    print(f'{int(peso)} kg')
