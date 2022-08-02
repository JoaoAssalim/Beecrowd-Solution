pokemons = 151
lista_pokemons = []

for i in range(int(input())):
    pok = input()
    if not pok in lista_pokemons:
        pokemons -= 1
        lista_pokemons.append(pok)
print(f'Falta(m) {pokemons} pomekon(s).')