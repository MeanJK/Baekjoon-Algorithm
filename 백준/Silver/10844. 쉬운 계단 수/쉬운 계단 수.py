N = int(input())
dp = [[0] * 101 for _ in range(101)]
mod = 1000000000
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        dp[i][j] %= mod
result = 0
for i in range(10):
    result = (result + dp[N][i]) % mod
print(result)