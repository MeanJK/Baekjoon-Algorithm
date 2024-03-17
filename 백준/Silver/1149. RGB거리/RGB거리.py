import sys
input = sys.stdin.readline
N = int(input())

d = [[0] * 3 for i in range(1001)]
rgb = [[0] * 3 for i in range(1001)]

for i in range(1, N+1):
    rgb[i] = list(map(int, input().strip().split()))

for i in range(1, N+1):
    for j in range(3):
        d[i][0] = min(d[i-1][1], d[i-1][2]) + rgb[i][0]
        d[i][1] = min(d[i-1][0], d[i-1][2]) + rgb[i][1]
        d[i][2] = min(d[i-1][0], d[i-1][1]) + rgb[i][2]

print(min(d[N]))        