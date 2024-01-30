def solution(n, computers):
    answer = 0
    def dfs(x):
        visited[x] = True
        for i in range(n):
            if computers[x][i] == 1 and not visited[i]:
                dfs(i)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1   
    return answer
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))