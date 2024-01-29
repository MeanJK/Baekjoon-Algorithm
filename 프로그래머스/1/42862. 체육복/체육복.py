def solution(n, lost, reserve):
    del_reserve = set(reserve) - set(lost)
    del_lost = set(lost) - set(reserve)
    for i in del_reserve:
        if i-1 in del_lost:
            del_lost.remove(i-1)
        elif i+1 in del_lost:
            del_lost.remove(i+1)
    return n - len(del_lost)
print(solution(5, [2,4], [1,3,5]))