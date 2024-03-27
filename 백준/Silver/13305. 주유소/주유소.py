import sys

input = sys.stdin.readline

n = int(input())  #도시의 개수 4
km = list(map(int, input().split()))
# 인접한 두 도시를 연결하는  거리2, 3, 1
price = list(map(int, input().split()))  # 도시마다 주유소의 리터당 가격 # 5 2 4 1
dp = [0] * (n-1)  #마지막 신경 x
dp[0] = km[0] * price[0]  # 10
nowPrice = price[0]
for i in range(1, n-1):
    if nowPrice > price[i]:
        nowPrice = price[i]
    dp[i] = dp[i-1] + nowPrice * km[i]    
print(dp[-1])