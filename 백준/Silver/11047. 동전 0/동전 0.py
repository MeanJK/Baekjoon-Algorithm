N, K = map(int, input().split())
coin = []
result = 0
for _ in range(N):
    coin.append(int(input()))
coin.sort(reverse = True)
for c in coin:
    if K == 0:
        break
    if K // c >= 1:
        result += K // c
        K %= c
print(result)