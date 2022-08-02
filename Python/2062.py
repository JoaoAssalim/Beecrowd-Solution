n = int(input())
palavras = input().split()

for i in range(len(palavras)):
    if 'OB' in palavras[i] and len(palavras[i]) <=3:
        palavras[i] = 'OBI'
    if 'UR' in palavras[i] and len(palavras[i]) <=3:
        palavras[i] = 'URI'
        
nova = ' '.join(palavras)
print(nova)