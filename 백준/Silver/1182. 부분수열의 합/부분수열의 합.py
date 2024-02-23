n,s = map(int, input().split())
total = 0
s_list = list(map(int, input().split()))

def rec(idx, tot):
    global total
    if idx >= n:
        return
    tot += s_list[idx]
    if tot == s:
        total += 1
    rec(idx+1, tot - s_list[idx])
    rec(idx+1, tot)
rec(0,0)    
print(total)