T = int(input())
cent = [25, 10, 5, 1]
for i in range(T):
    DP = [0] * 4
    C = int(input())
    for j in range(4):
        if C // cent[j] != 0:
            DP[j] = C // cent[j]
            C %= cent[j]
        elif cent[j] == 1:
            DP[j] = C
        print(DP[j])
  