count = int(input())
n1 = list(map(int, input().split()))
n1.sort()
if len(n1) == 1:
    print(n1[0]**2)
else:
    print(n1[0] * n1[-1])
   