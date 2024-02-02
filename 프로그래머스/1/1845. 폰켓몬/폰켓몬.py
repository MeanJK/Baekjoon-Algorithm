def solution(nums):
    pick = len(nums)/2
    count = 0
    pick_list = []
    for i in range(len(nums)):
        if count < pick and nums[i] not in pick_list:
            pick_list.append(nums[i])
            count += 1
    return count
print(solution([3,1,2,3]))