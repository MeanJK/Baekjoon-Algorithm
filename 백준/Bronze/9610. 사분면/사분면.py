N = int(input())
Q1 = Q2 = Q3 = Q4 = AXIS = 0
for i in range(N):
    A, B = map(int, input().split())
    if A > 0 and B > 0:
        Q1 += 1
    elif A < 0 and B > 0:
        Q2 += 1
    elif A < 0 and B < 0:
        Q3 += 1
    elif A > 0 and B < 0:
        Q4 += 1
    else:
        AXIS += 1
print(f"Q1: {Q1}\nQ2: {Q2}\nQ3: {Q3}\nQ4: {Q4}\nAXIS: {AXIS}")