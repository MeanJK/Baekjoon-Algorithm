N = int(input())
for i in range(N):
    T = int(input())
    max = 0
    mname = ""
    for j in range(T):
        name, num = input().split()
        num = int(num)
        if num > max:
            max = num
            mname = name
    print(mname)