import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
num_list = []
for i in range(N):
    A_min = min(A)
    B_max = max(B)
    num_list.append(B_max*A_min)
    A.remove(A_min)
    B.remove(B_max)
print(sum(num_list))    