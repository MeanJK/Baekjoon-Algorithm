import sys
input = sys.stdin.readline
while True:
    sentence = input().rstrip()
    if len(sentence) == 1 and sentence == '.':
        break
    else:
        stack = []
        for char in sentence:
            if char in ['[', '(']:
                stack.append(char)
            elif char == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                elif len(stack) == 0:
                    stack.append(-1)
                    break
                else:
                    break
            elif char == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                elif len(stack) == 0:
                    stack.append(-1)
                    break
                else:
                    break
        if len(stack) == 0:
            print('yes')
        else:
            print('no')         