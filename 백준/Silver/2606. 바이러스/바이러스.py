import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(x):
    visited[x] = 1
    for nx in graph[x]:
        if visited[nx] == 0:
            dfs(nx)
dfs(1)
print(sum(visited) - 1)