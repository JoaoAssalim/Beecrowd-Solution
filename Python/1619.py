from datetime import datetime

for i in range(int(input())):
    d1, d2 = list(map(str, input().split()))
    d2 = datetime.strptime(d2, '%Y-%m-%d')
    d1 = datetime.strptime(d1, '%Y-%m-%d')
    quantidade_dias = abs((d2 - d1).days)
    print(quantidade_dias)
