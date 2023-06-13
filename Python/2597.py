from math import floor
def calc(x):
    y = int(floor(x**0.5))
    return x-y

for i in range(int(input())):
    n = int(input())
    print(calc(n))