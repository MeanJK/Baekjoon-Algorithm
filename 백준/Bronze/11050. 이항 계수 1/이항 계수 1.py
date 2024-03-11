n, k = map(int, input().split())
result = 1
division = 1
for i in range(n, n-k, -1):
    result *= i
for i in range(k, 0, -1):
    division *= i
print(result // division)