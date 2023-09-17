es = 2
ant = -1

def dfs(x):
    global es, ant, anter
    marked[x] = True

    for w in graph[x]:
        if not marked[w]:
            if f'{x}-{w}' in extra:
                extra.remove(f'{x}-{w}')
            st = f'{x}-{w} pathR(G,{w})'
            if ant == 0:
                print((" " * es) + st)
            elif ant == x:
                es += 2
                print((" " * es) + st)
            else:
                id = anter.index(x)
                es = (id + 1) * 2
                print((" " * es) + st)

            ant = w

            if ant not in anter:
                anter.append(ant)
            dfs(w)
        else:
            if f'{x}-{w}' in extra:
                if ant == x:
                    print((" " * (es+2)) + f'{x}-{w}')
                else:
                    id = anter.index(x)
                    es = (id + 1) * 2
                    print((" " * (es)) + f'{x}-{w}')
                extra.remove(f'{x}-{w}')



for p in range(int(input())):
    print(f"Caso {p+1}:")
    n, m = list(map(int, input().split()))
    graph = [[] for i in range(n)]
    marked = [False for i in range(n)]
    
    min = 999999999999
    
    extra = set()

    for i in range(m):
        a, b = list(map(int, input().split()))
        if a < min:
            min = a
        if b < min:
            min = b
        graph[a].append(b)
        extra.add(f'{a}-{b}')
        
    for i in range(n):
        graph[i] = sorted(graph[i])
    
    extra = list(extra)
    
    while False in marked:
        idx = marked.index(False)
        anter = [idx]
        
        if not marked[idx] and graph[idx] and marked[min]:
            print()
        dfs(idx)
    
    
    print()
