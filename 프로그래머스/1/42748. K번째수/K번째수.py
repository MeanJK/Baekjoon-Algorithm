def solution(array, commands):
    all_list = []
    for i in range(len(commands)):
        start_idx = commands[i][0] - 1
        end_idx = commands[i][1]
        k_idx = commands[i][2]
        
        com_list = array[start_idx:end_idx]
        com_list.sort()
        all_list.append(com_list[k_idx-1])
    return all_list
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))