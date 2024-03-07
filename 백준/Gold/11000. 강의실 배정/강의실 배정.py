import heapq
import sys
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    q.append(list(map(int, input().split())))
room = []
q.sort(key = lambda x : (x[0], x[1]))
heapq.heappush(room, q[0][1])
for i in range(1, n):
    if q[i][0] >= room[0]:
        heapq.heappop(room)
    heapq.heappush(room, q[i][1])
print(len(room))        