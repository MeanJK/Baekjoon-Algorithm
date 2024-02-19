N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
group = 0
num = []
def dfs(x,y):
    global count
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0       
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)            
        return True
    return False
for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            num.append(count)
            group += 1
            count = 0
num.sort()
print(group)
for i in num:
    print(i)