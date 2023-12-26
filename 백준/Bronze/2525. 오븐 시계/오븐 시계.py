H, m = map(int, input().split())
t = int(input())
p = m + t
if p >= 60:
    m = p%60
    H = (H+(p//60))%24
else:
    m = p
print(H, m)
    