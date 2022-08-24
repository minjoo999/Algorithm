N = int(input())
case_num = 0
while True:
    num = []
    shapes = list(input())
    if shapes[0] == 'O':
        num.append(1)
    else:
        num.append(0)
    for i in range(1, len(shapes)):
        if shapes[i] == 'O':
            if shapes[i-1] == 'O':
                num.append(num[i-1] + 1)
            else:
                num.append(1)
        else:
            num.append(0)
    print(sum(num))
    case_num += 1
    if case_num >= N:
        break