import math
S = int(input())
n = 0
m = 0
while True:
    if S > n:
        n += 1
        S = S-n
        m += 1
    else:
        print(m)
        break