graph = []
DP = [0] * 82
max_value = 0
for i in range(9):
    graph.append(list(map(int, input().split())))
max_value = max(max(row) for row in graph)

for i in range(9):
    for j in range(9):
        if graph[i][j] == max_value:
            print(max_value)
            print(i+1, j+1)
            break