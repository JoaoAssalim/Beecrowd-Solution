saida, tempo, fuso = list(map(int, input().split()))

if saida == 0:
    saida = 24

horario = saida + tempo + fuso
if horario >= 24:
    horario -= 24
print(horario)
