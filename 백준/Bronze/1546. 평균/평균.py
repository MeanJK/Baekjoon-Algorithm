import sys
import statistics

N = int(sys.stdin.readline())
m_list = sys.stdin.readline().split()
score = list(map(int, m_list))
M = max(score)
for i in range(N):
    score[i] = score[i]/M*100
result = sum(score)
print(result / len(score))