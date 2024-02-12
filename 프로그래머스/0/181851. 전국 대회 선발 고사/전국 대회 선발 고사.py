def solution(rank, attendance):
    answer = 0
    num_list = []
    for i in range(len(rank)):
        if attendance[i] == True:
            num_list.append(rank[i])
    num_list.sort()
    for j in range(len(rank)):
        if rank[j] == num_list[0]:
            answer += (10000 * j)
        elif rank[j] == num_list[1]:
            answer += (100*j)
        elif rank[j] == num_list[2]:
            answer += 1*j         
    return answer
print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))