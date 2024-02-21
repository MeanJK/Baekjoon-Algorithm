import sys
import math
N = int(input())
min_num = sys.maxsize
def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

#def pelindrom(x):
#    count = 0
#    x = list(str(x))
#    for i in range((len(x)+1)//2):
#        if x[i] == x[(len(x)-1)-i]:
#            count += 1
#    if count == (len(x)+1)//2:
#        return True
#    else:
#        return False

for i in range(N, 10000001):
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if isPrime(i) == True:
            print(i)
            break