N = float(input())
N1 = str(N)
if N1[0] == '-':
    print(f'{N:.4E}')
else:
    print(f'+{N:.4E}')
