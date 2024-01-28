def solution(nums):
    answer = 0
    result = len(set(nums))
    getP = int(len(nums) / 2)
    
    if result < getP:
        answer = result
    else:
        answer = getP
    return answer
print(solution([3,1,2,3]))