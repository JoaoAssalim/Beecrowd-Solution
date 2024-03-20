n, m = list(map(int, input().split()))
maze = [input() for i in range(n)]

c = 0

for i in range(n):
    for j in range(m):
        if maze[i][j] == "#":
            if i == 0 or j == 0 or i == len(maze) - 1 or j == len(maze[0]) - 1:
                c += 1
            elif (i-1 >= 0 and maze[i-1][j] == '.') or (i+1 < len(maze) and maze[i+1][j] == '.') or (j-1 >= 0 and maze[i][j-1] == ".") or (j+1 < len(maze[0]) and maze[i][j+1] == "."):
                c += 1

print(c)
