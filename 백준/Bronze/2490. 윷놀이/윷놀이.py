throw_y = []
for i in range(3):
    throw_y.append(list(map(int, input().split())))
for y in throw_y:
    zero = 0
    for t in y:
        if t == 0:
            zero += 1
    if zero == 0:
        print('E')
    elif zero == 1:
        print('A')
    elif zero == 2:
        print('B')
    elif zero == 3:
        print('C')
    elif zero == 4:
        print('D')