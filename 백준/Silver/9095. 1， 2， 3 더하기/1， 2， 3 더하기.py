import sys
dp = [0] * 11
T = int(input())
dp[1] = 1
dp[2] = 2
dp[3] = 4
result = []
for _ in range(T):
    N = int(input())
    for i in range(4, 11):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    result.append(dp[N])
for r in result:
    print(r)