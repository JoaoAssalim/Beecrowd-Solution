c = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(f"Teste {c}")
    c += 1
    print(pow(2, n) -1)
    print()