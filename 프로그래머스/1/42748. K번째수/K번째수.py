def solution(array, commands):
    split_list = []
    for i in range(len(commands)):
        split_array = array[commands[i][0]-1:commands[i][1]]
        split_array.sort()
        split_list.append(split_array[commands[i][2]-1])
    return split_list
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))