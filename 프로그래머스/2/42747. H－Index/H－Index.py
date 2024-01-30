def solution(citations):           #1,2,3,4,5
    citations.sort(reverse = True) #6,5,3,1,0
    for i in range(len(citations)):
        if i+1 > citations[i]:
            return i
    return len(citations)
print(solution([3,0,6,1,5]))