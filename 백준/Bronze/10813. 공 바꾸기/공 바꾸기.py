import sys

N, M = map(int, sys.stdin.readline().split())
m_list = [k for k in range(1, N+1)]
for l in range(M):
    i, j = map(int, sys.stdin.readline().split())
    m_list[i-1], m_list[j-1] = m_list[j-1], m_list[i-1]
for b in range(N):
    print(m_list[b], end=' ')