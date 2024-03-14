import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
prefix_sum = [0]
temp = 0
for i in num:
    temp += i
    prefix_sum.append(temp)
for _ in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])