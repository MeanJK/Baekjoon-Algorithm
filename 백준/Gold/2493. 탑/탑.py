N = int(input())
castle = list(map(int, input().split())) # 6 9 5 7 4
dp = [0] * N # 0 0 0 0 0
stack = []
for i in range(len(castle)):
    while stack:
        if castle[stack[-1][0]] < castle[i]:
            stack.pop()
        else:
            dp[i] = stack[-1][0] + 1
            break
    stack.append((i, castle[i]))
print(*dp)