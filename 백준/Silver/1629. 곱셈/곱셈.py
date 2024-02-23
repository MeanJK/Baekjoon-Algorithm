a, b, c = map(int,input().split())
def func1(a,b,c):
    if b == 1:
        return a % c
    val = pow(a, b//2, c)
    val = val * val % c
    if b % 2 == 0:
        return val
    else:
        val = val * a % c
        return val
print(func1(a,b,c))
    
    
    