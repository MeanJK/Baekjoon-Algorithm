N = int(input())
m = 0
for i in range(N):
    if int(input()) == 1:
        m += 1  
if m > N // 2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')