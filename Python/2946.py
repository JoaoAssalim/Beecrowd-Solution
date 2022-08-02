n = input()
inteiro = int(n, 2)
numeross_digitados = []
numereos_divisieis = []

for i in range(int(input())):
    num = int(input())
    if(inteiro % num == 0):
        numereos_divisieis.append(num)
        
if len(numereos_divisieis) > 0:
    nova = ''
    for x in sorted(numereos_divisieis):
        nova += f'{x} '
    print(nova[:-1])
else:
    print('Nenhum')