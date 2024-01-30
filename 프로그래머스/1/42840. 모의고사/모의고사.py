def solution(answers):
    answer = []
    person = [0] * 3
    list_one = [1,2,3,4,5]
    list_two = [2,1,2,3,2,4,2,5]
    list_three = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == list_one[i%5]:
            person[0] += 1
        if answers[i] == list_two[i%8]:
            person[1] += 1
        if answers[i] == list_three[i%10]:
            person[2] += 1
    winner = max(person)
    for i in range(len(person)):
        if person[i] == winner:
            answer.append(i+1)
    answer.sort()
    return answer
print(solution([1,2,3,4,5]))