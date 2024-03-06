n, m = map(int, input().split())
def gcd(x,y):
    if x > y:
        while(y):
            x, y = y, x%y
        return x
    elif x < y:
        while(x):
            y, x = x, y%x
        return y
def lcm(x,y):
    result = (x*y) // gcd(x,y)
    return result
if n == m:
    print(n)
else:
    print(lcm(n,m))