import heapq

def dijkstra(G,start):  
    INF = 999999999

    dis = dict((key,INF) for key in G)
    dis[start] = 0
    vis = dict((key,False) for key in G)
    pq = []
    heapq.heappush(pq,[dis[start],start])

    path = dict((key,[start]) for key in G)
    while len(pq)>0:
        v_dis,v = heapq.heappop(pq)
        if vis[v] == True:
            continue
        vis[v] = True
        p = path[v].copy()
        for node in G[v]:
            new_dis = dis[v] + float(G[v][node])
            if new_dis < dis[node] and (not vis[node]):
                dis[node] = new_dis
                heapq.heappush(pq,[dis[node],node])
                temp = p.copy()
                temp.append(node)
                path[node] = temp

    return dis,path
    
while True:
    try:
        V, A = list(map(int, input().split()))
        aviao = {}
        oni = {}
        for i in range(1, V+1):
            aviao[i] = {i:0}
            oni[i] = {i:0}
            
        for i in range(A):
            a,b,t,r = list(map(int, input().split()))
            if t == 0:
                aviao[a].update({b:r})
            else:
                oni[a].update({b:r})
        
        distance1,path1 = dijkstra(aviao,1)
        distance2,path2 = dijkstra(oni,1)
        
        if distance1[V] < distance2[V] and distance1[V] != 0:
            print(int(distance1[V]))
        else:
            print(int(distance2[V]))
            
    except EOFError:
        break
