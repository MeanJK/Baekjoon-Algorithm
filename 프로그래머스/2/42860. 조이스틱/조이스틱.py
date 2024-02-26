def solution(name):
    answer = 0
    min_cursor = len(name) - 1
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char)+1)
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        min_cursor = min(min_cursor, i*2+len(name) - next, i+2*(len(name) - next))
    answer += min_cursor            
    return answer
print(solution('JAN'))
#26
#a b c d e f g h i j k l m(오 12번) n(13번) o(왼 12번) p q r s t u v w x y z