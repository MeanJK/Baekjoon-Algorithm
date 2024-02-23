N, r, c = map(int, input().split())

def func1(n, r, c):
    if n == 0:
        return 0
    half = 1 << (n-1)
    if half > r and half > c:
        return func1(n-1, r, c)
    
    elif half > r and half <= c:
        return half * half + func1(n-1, r, c-half)
    
    elif half <= r and half > c:
        return 2 * half * half + func1(n-1, r-half, c)
    
    else:
        return 3 * half * half + func1(n-1, r-half, c-half)

result = func1(N, r, c)
print(result)