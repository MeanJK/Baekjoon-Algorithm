N = int(input())
def fiv(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiv(n-1)+fiv(n-2)
print(fiv(N))    