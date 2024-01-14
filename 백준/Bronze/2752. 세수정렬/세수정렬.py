m = list(map(int, input().split()))
for i in range(len(m)):
    for j in range(i, len(m)):
        if m[i] > m[j]:
            m[i], m[j] = m[j], m[i]
for _ in m:
    print(_)
