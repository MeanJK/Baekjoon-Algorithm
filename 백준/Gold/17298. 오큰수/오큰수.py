N = int(input())
num = list(map(int, input().split()))
NGE = [-1] * N
stack = []

for i in range(N):
    while stack and num[i] > num[stack[-1]]:
        NGE[stack[-1]] = num[i]
        stack.pop()
    stack.append(i)
print(*NGE)
