import sys
graph = []
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
blank = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i,j))
def row(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def col(y, b):
    for i in range(9):
        if b == graph[i][y]:
            return False
    return True
def checkRect(x, y, c):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if c == graph[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)
        
    for i in range(1,10):
        x = blank[idx][0]
        y = blank[idx][1]
        if row(x,i) and col(y,i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0
dfs(0)                                   