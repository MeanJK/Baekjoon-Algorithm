n, m = map(int, input().split())
castle = []
for _ in range(n):
    castle.append(input())
row, col = 0,0
for i in range(n):
    if 'X' not in castle[i]:
        row += 1
for j in range(m):
    if 'X' not in [castle[i][j] for i in range(n)]:
        col += 1
print(max(row, col))