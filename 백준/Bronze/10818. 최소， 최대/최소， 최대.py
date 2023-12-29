import sys

N = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
print(min(m_list), max(m_list))