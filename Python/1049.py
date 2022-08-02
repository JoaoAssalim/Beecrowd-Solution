especie = input()
subespecie = input()
alimentacao = input()


if especie == 'vertebrado':
    if subespecie == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        elif alimentacao == 'onivoro':
            print('pomba')
    elif subespecie == 'mamifero':
        if alimentacao == 'onivoro':
            print('homem')
        elif alimentacao == 'herbivoro':
            print('vaca')

elif especie == 'invertebrado':
    if subespecie == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        elif alimentacao == 'herbivoro':
            print('lagarta')
    elif subespecie == 'anelideo':
        if alimentacao == 'hematofago':
            print('sanguessuga')
        elif alimentacao == 'onivoro':
            print('minhoca')