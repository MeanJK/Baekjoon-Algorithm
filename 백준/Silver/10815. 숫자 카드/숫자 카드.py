N = int(input())
card = list(map(int, input().split()))
M = int(input())
checkCard = list(map(int, input().split()))
checkList = []
dict = {card[i] : 0 for i in range(N)};
for i in range(M):
    if checkCard[i] not in dict:
        print(0, end=' ')
    else:
        print(1, end=' ')