alpha, x = map(str, input().split())
alpha_num = []
for i in range(len(alpha)):
    if alpha[i].isdigit():
        alpha_num.append(int(alpha[i]))
    else:
        alpha_num.append(int(ord(alpha[i]))-55)
sum_num = 0   
base = int(x)
for i in range(len(alpha_num)):
    sum_num += alpha_num[i] * (base**(len(alpha_num) - (i+1)))
print(sum_num)