N = int(input())
P = list(map(int, input().split()))
P.insert(0,0)
DP = [0] * (N+1)
for i in range(1, N+1):
    for j in range(1, i+1):
        DP[i] = max(DP[i], DP[i-j] + P[j])
print(DP[N])