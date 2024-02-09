N, K = map(int, input().split())
S_list = []
def S(N):
    for i in range(1,N+1):
        if N % i == 0:
            S_list.append(i)
    if len(S_list) < K:
      return 0
    else:
      return S_list[K-1]
print(S(N))