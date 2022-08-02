for i in range(int(input())):
    dados = input().split()
    alunos = int(dados[0])
    alunos_acima = 0
    media = 0
    for aluno in dados[1:]:
        media += int(aluno)
    media = media / (len(dados) - 1)
            
    for nota in dados[1:]:
        if int(nota) > media:
            alunos_acima += 1
    media_aluno = alunos_acima / alunos
    print(f'{media_aluno*100:.3f}%')