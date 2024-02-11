X, Y, W, Z = map(int, input().split())
print(min(X, Y, W-X, Z-Y))