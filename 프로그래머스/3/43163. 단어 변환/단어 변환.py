from collections import deque
def solution(begin, target, words):
    count = 0
    q = deque()
    q.append([begin, 0])
    visited = [False for i in range(len(words))]
    while q:
        word, cnt = q.popleft() #hit, 0
        if word == target:
            return cnt
        for i in range(len(words)):
            temp = 0
            if not visited[i]:
                for j in range(len(word)):
                    if words[i][j] != word[j]:
                        temp += 1
                if temp == 1:
                    q.append([words[i], cnt + 1])
                    visited[i] = True
    return count

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
visited = [False] * len(words)

print(solution(begin, target, words))