from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    a = input().rstrip()
    if a[0] == '1':
        q.appendleft(a[2:])
    elif a[0] == '2':
        q.append(a[2:])
    elif a == '3':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif a == '4':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif a == '5':
        print(len(q))
    elif a == '6':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif a == '7':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif a == '8':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])