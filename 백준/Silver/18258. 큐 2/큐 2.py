from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    m = input().strip()
    if 'push' in m:
        name, integer = map(str, m.split())
        q.append(int(integer))
    elif m == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            answer = q.popleft()
            print(answer)
    elif m == 'size':
        print(len(q))
    elif m == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif m == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])  
    elif m == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])