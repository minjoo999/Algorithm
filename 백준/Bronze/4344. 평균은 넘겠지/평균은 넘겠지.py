C = int(input())
case_num = 0
while True:
    N_li = list(map(int, input().split(' ')))
    N = N_li[0]
    average = (sum(N_li)-N) / N
    student_num = []
    for i in range(1, N+1):
        if N_li[i] > average:
            student_num.append(N_li[i])
    ratio = 100*(len(student_num) / N)
    print(format(ratio, ".3f"), "%", sep='')
    case_num += 1
    if case_num >= C:
        break