import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
dp = [0] * (N+1)
count = 0
dp[1] = num[0]
for n in num:
    if n < 0:
        count += 1
        
if count == N:
    print(max(num))
elif count == 0:
    print(sum(num))
else:
    for i in range(2, N+1):
        if num[i-1] + dp[i-1] < 0:
            dp[i] = 0
        else:
            dp[i] = num[i-1] + dp[i-1]
    print(max(dp))            