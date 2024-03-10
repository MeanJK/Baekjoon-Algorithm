import math
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True
for i in range(n,m+1):
    if isPrime(i) == True:
        print(i)