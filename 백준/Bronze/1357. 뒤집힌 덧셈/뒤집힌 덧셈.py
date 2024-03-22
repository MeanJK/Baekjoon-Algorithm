import sys
input = sys.stdin.readline
x, y = map(int, input().split())
strX = str(x)
strY = str(y)
newX = ''
newY = ''
for i in range(len(strX)-1, -1, -1):
    newX += strX[i]
for i in range(len(strY)-1, -1, -1):
    newY += strY[i]
answer = int(newX) + int(newY)
answer = str(answer)
result = ''
for i in range(len(answer)-1, -1, -1):
    result += answer[i]
print(int(result))