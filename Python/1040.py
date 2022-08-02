notas = input().split()
n1, n2, n3, n4 = float(notas[0]), float(notas[1]), float(notas[2]), float(notas[3])

media = (n1*2 + n2*3 + n3*4 +n4*1)/10

if media >= 7.0:
    print(f'Media: {media:.1f}')
    print("Aluno aprovado.")
elif media < 5.0:
    print(f'Media: {media:.1f}')
    print("Aluno reprovado.")
else:
    print(f'Media: {media:.1f}')
    print("Aluno em exame.")
    exame = float(input())
    print(f'Nota do exame: {exame}')
    media_final = (media + exame) / 2
    if media_final >= 5:
        print("Aluno aprovado.")
        print(f'Media final: {media_final}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {media_final}')