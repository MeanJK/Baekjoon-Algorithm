N = int(input())
def pec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * pec(n-1)
print(pec(N))    