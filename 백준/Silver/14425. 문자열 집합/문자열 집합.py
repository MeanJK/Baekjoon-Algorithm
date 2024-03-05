n, m = map(int, input().split())
S = []
check = []
count = 0
for _ in range(n):
    S.append(input())
for _ in range(m):
    check.append(input())
for word in check:
    if word in S:
        count += 1
print(count)