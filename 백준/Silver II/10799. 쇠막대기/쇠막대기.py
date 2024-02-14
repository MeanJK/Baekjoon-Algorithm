lazer = input()
stack = []
answer = 0
for i in range(len(lazer)):
    if lazer[i] == '(':
        stack.append(lazer[i])
    else:
        if lazer[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            answer += 1
            stack.pop()
print(answer)