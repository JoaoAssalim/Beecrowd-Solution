from math import floor
def hp(iv, bs, ev, lvl):
    return floor((((iv + bs + (ev**0.5/8) + 50) * lvl)/50)+10)

def s(iv, bs, ev, lvl):
    return floor((((iv + bs + (ev**0.5/8)) * lvl)/50)+5)

for i in range(int(input())):
    nome, lvl = input().split()
    lvl = int(lvl)
    act = ["HP: ", "AT: ", "DF: ", "SP: "]
    print(f'Caso #{i+1}: {nome} nivel {lvl}')
    
    for j in range(4):
        bs, iv, ev = list(map(int, input().split()))
        if j == 0:
            print(f"{act[j]}{hp(iv, bs, ev, lvl):.0f}")
        else:
            print(f"{act[j]}{s(iv, bs, ev, lvl):.0f}")
    
