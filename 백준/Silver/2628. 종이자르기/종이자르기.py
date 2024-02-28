import sys
input = sys.stdin.readline
n, m = map(int, input().split())
T = int(input())
height = [0, m]
width = [0,n]
for _ in range(T):
    a, b = map(int, input().split())
    if a == 0:
        height.append(b)
    else:
        width.append(b)
height.sort()
width.sort()
result = 0
for i in range(len(width)-1):
    for j in range(len(height)-1):
        x = width[i+1] - width[i]
        y = height[j+1] - height[j]
        result = max(result, x*y)
print(result)        