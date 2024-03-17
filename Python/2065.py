n, m = list(map(int, input().split()))
func_tempo = [0 for i in range(n)]
temp = list(map(int, input().split()))
clients = list(map(int, input().split()))

for i in clients:
    idx = func_tempo.index(min(func_tempo))
    func_tempo[idx] += i * temp[idx]

print(max(func_tempo))
