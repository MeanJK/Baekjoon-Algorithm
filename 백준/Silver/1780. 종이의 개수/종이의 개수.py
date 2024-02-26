import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
m_count, z_count, o_count = 0,0,0

def paper(r, c, n):
    global m_count, z_count, o_count
    color = graph[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if color != graph[i][j]:
                paper(r, c, n//3)
                paper(r+n//3, c, n//3)
                paper(r+n//3, c+n//3, n//3)
                paper(r+2*n//3, c, n//3)
                paper(r+2*n//3, c+n//3, n//3)
                paper(r, c+n//3, n//3)
                paper(r, c+2*n//3, n//3)
                paper(r+n//3, c+2*n//3, n//3)
                paper(r+2*n//3, c+2*n//3, n//3)
                return
    if color == -1:
        m_count += 1
    elif color == 0:
        z_count += 1
    else:
        o_count += 1
paper(0,0,N)
print(m_count)
print(z_count)
print(o_count)