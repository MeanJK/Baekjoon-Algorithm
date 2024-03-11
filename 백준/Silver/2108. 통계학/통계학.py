import sys
input = sys.stdin.readline
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))
print(round(sum(num)/n))
num.sort()
median = len(num)//2
print(num[median])
dic = dict()
for i in num:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
mx = max(dic.values())
mx_dic = []
for i in dic:
    if mx == dic[i]:
        mx_dic.append(i)
if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])
print(max(num) - min(num))    