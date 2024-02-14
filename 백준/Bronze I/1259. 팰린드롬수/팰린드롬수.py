while True:
    N = int(input())
    if N == 0:
        break
    else:
        sorted = []
        reversed = []
        N = str(N)
        for i in range(len(N)):
            sorted.append(N[i])
        for i in range(len(N)-1, -1, -1):
            reversed.append(N[i])
        if sorted == reversed:
            print('yes')
        else:
            print('no')