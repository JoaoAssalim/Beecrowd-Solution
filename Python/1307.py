from math import gcd
for i in range(int(input())):
    a = int(input(), 2)
    b = int(input(), 2)
    print(f"Pair #{i+1}: Love is not all you need!" if gcd(a, b) == 1 else f"Pair #{i+1}: All you need is love!")