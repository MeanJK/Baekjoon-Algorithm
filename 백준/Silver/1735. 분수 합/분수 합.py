n, m = map(int, input().split())
a, b = map(int, input().split())
numerator = n*b + a*m
denominator = b*m

def gcd(x,y):
    while(x):
        y, x = x, y%x
    return y
result = gcd(numerator, denominator)
if result == 1:
    print(numerator, denominator)
else:
    print(numerator//result, denominator // result)