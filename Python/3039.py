menino = 0
menina = 0
 
for i in range(int(input())):
    nome, sexo = list(map(str, input().split()))
    if sexo == 'F': menina += 1
    else: menino += 1

print(f'{menino} carrinhos')
print(f'{menina} bonecas')
