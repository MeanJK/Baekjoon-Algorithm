N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
result = ''

def recursive(r, c, n):
    global result
    color = graph[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if color != graph[i][j]:
                result += '('
                recursive(r, c, n//2)
                recursive(r, c+n//2, n//2)
                recursive(r+n//2, c, n//2)
                recursive(r+n//2, c+n//2, n//2)
                result += ')'
                return
    if color == 1:
        result += '1'
    else:
        result += '0'
recursive(0,0,N)
print(result)