for i in range(int(input())):
    a,b,c = map(float, input().split())
    media = (a*2 + b*3 + c*5) / 10
    print(f'{media:.1f}')