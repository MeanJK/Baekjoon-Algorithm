N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]
for i in range(N):
    x, y = list(map(int, input().split()))
    for row in range(x, x+10):
        for val in range(y, y+10):
            arr[row][val] = 1
result = 0
for i in arr:
    result += i.count(1)
print(result)