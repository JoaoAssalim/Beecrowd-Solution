alunos = []
notas = 8
maior = 0

for i in range(int(input())):
    aluno, nota = map(float, input().split())
    if nota >= notas:
        if nota > maior:
            maior = nota
            alunos.append(aluno)
        
if maior == 0:
    print('Minimum note not reached')
else:
    print(int(alunos[-1]))