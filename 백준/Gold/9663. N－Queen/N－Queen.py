N = int(input())
cnt = 0
isused1 = [0 for _ in range(40)]
isused2 = [0 for _ in range(40)]
isused3 = [0 for _ in range(40)]
def queen(cur):
    global cnt
    if cur == N:
        cnt += 1
        return
    for i in range(N):
        if isused1[i] == 1 or isused2[cur+i] == 1 or isused3[cur-i+N-1] == 1:
            continue
        isused1[i] = 1
        isused2[cur+i] = 1
        isused3[cur-i+N-1] = 1
        queen(cur+1)
        isused1[i] = 0
        isused2[cur+i] = 0
        isused3[cur-i+N-1] = 0
queen(0)
print(cnt)