bonecos = 0
arquitetos = 0
musicos = 0
desenhistas = 0

total = 0
for i in range(int(input())):
    nome, brinquedo, tempo = list(map(str, input().split()))
    if brinquedo == 'bonecos': bonecos += int(tempo)
    elif brinquedo == 'arquitetos': arquitetos += int(tempo)
    elif brinquedo == 'musicos': musicos += int(tempo)
    elif brinquedo == 'desenhistas': desenhistas += int(tempo)
    
total += bonecos // 8
total += arquitetos // 4
total += musicos // 6
total += desenhistas // 12

print(total)
