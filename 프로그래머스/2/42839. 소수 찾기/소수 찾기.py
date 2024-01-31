from itertools import permutations
def is_prime(x): #-> 7
        if x <= 1:
            return False
        for i in range(2,x): #7을 2부터 6까지 나눴을때 나머지가 0이 아니면
            if x%i == 0:
                return False
        return True
def solution(numbers):
    count = 0
    num = []
    for i in range(1, len(numbers)+1):
        num.append(list(set(map(''.join, permutations(numbers, i)))))
        per = list(set(map(int ,set(sum(num, [])))))
    for i in per:
        if is_prime(i) == True:
            count+=1
    return count
print(solution("17"))