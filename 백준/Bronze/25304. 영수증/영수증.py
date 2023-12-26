AllPrice = int(input())
AllNum = int(input())
Dnum = 0
for i in range(AllNum):
    Anum, Bnum = map(int, input().split())
    Dnum += Anum * Bnum
if Dnum == AllPrice:
    print("Yes")
else:
    print("No")