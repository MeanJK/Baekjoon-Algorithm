import sys
input = sys.stdin.readline
N = int(input())
num = [0] * (N+1)
dp = [0] * (N+1)
for i in range(1, N+1):
    num[i] = int(input())
if N == 1:
    print(num[1])
    exit()
elif N == 2:
    print(num[1] + num[2])
    exit()
dp[1] = num[1]    
dp[2] = num[1] + num[2]
for i in range(3, N+1):
    dp[i] = max(dp[i-1], dp[i-2] + num[i], dp[i-3]+num[i-1]+num[i])
print(dp[-1])    