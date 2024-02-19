N = int(input())
P = list(map(int, input().split()))
time = []
dp = 0
result = 0
P.sort() # 12334
#1 12 123 1233 12334
for i in range(len(P)): #0,1,2,3,4
    for j in range(i+1): #0, 01 012 0123 01234 
        dp += P[j]
    time.append(dp)
    dp = 0
print(sum(time))