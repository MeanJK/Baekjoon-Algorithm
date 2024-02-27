# 1.combinations 써서 순열 조합
# 2. 큐 이용
from collections import deque
while True:
    try:
        s, m = map(str, input().split())
        q = deque(list(s))  
        for c in m:
            if q and c == q[0]:
                q.popleft()
        if q:
            print('No')
        else:
            print('Yes')
    except:
        break
    