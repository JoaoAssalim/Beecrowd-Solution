for _ in range(int(input())):
    n = int(input())
    fibo = [0,1]

    for i in range(n-1):
        soma = fibo[-2] + fibo[-1]
        fibo.append(soma)

    print(f'Fib({n}) = {fibo[n]}')