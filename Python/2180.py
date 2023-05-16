from math import floor
def isPrime(x):
    primes = []
    
    while len(primes) < 10:
        ver = True
        for i in range(2, int(x**0.5)):
            if x % i == 0:
                ver = False
                break
        if ver:
            primes.append(x)
        x += 1
    return primes
    
n = int(input())
soma = sum(isPrime(n))
print(f'{soma} km/h')
h = int(floor(60000000 / soma))
d = int(floor(h/24))

print(f'{h} h / {d} d')
            
