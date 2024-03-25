import sys
input = sys.stdin.readline
n, k = map(int, input().split())
t = list(map(int, input().split()))
result = []
result.append(sum(t[:k]))
for i in range(n-k):
    result.append(result[i] -t[i] + t[k+i])
print(max(result))