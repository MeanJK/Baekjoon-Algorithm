import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
prefix = [0] * m
result = 0
for i in range(n):
    result += num[i]
    prefix[result % m] += 1
answer = prefix[0]
for i in prefix:
    answer += i * (i-1) // 2
print(answer)    