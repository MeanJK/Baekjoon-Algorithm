DP = [i for i in range(1,21)]
for _ in range(10):
    a, b = map(int, input().split()) # 9,13
    if a != b:
        for i in range((b-a)//2 + 1):
            DP[a-1+i], DP[b-1-i] = DP[b-1-i], DP[a-1+i]
for i in DP:
    print(i, end=' ')