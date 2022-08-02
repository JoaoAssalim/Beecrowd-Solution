criancas = []

while True:
    try:
        nome = input()
        criancas.append(nome)
    except EOFError:
        break

criancas = sorted(criancas, key=str.lower)
print(criancas[-1])