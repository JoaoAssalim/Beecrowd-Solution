def bfs(x):
    queue = [x]
    
    while queue:
        w = queue.pop(0)
        if not visited[w]:
            visited[w] = True
            for i in graph[w]:
                if not visited[i]:
                    queue.append(i)

a, b = list(map(int, input().split()))
graph = [[] for i in range(a)]
visited = [False for i in range(a)]

for i in range(b):
    u, v = list(map(int, input().split()))
    u, v = u-1, v-1
    graph[u].append(v)
    graph[v].append(u)

bfs(0)

if all(i for i in visited):
    print("COMPLETO")
else:
    print("INCOMPLETO")
