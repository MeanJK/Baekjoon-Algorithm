from math import gcd
n = int(input())
a = int(input())
dist_list = []
for i in range(n-1):
    num = int(input())
    dist_list.append(num - a)
    a = num
g = dist_list[0]
for i in range(1, len(dist_list)):
    g = gcd(g, dist_list[i])

result = 0    
for i in dist_list:
    result += (i // g) - 1
print(result)    