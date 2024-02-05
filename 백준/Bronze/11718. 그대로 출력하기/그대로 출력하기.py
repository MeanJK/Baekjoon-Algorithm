alpha_list = []
while True:
    try:
        alpha = input()
        if alpha == '':
            break
        alpha_list.append(alpha)
        if len(alpha_list) >= 100:
            break
    except EOFError:
        break
for alpha in alpha_list:
    print(alpha)