def floodFill(img, row, col, p):
    start = img[row][col]
    queue = [(row, col)]
    visited = set()

    while len(queue) > 0:
        row, col = queue.pop(0)
        visited.add((row, col))
        vis[row][col] = True
        img[row][col] = p

        for row, col in neighbors(img, row, col, start):
            if (row, col) not in visited:
                queue.append((row, col))
    
    return img

def neighbors(img, row, col, start):
    indices = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    return [(row, col) for row, col in indices if isValid(img, row, col) and img[row][col] == start]

def isValid(img, row, col):
    return row >= 0 and col >= 0 and row < len(img) and col < len(img[0])

for i in range(int(input())):
    graph = []
    
    i = 0
    while i < 5:
        l = list(map(int, input().split()))
        if len(l) > 0:
            graph.append(l)
            i += 1
        
    vis = [[False for i in range(5)] for j in range(5)]
    
    if graph[0][0] != 1:
        floodFill(graph, 0, 0, 3)
        
        if graph[0][0] == graph[4][4]:
            print("COPS")
        else:
            print("ROBBERS")
    else:
        print("ROBBERS")
