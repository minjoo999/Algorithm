X = int(input())
N = int(input())
li = []
while True:
    a, b = map(int, input().split(' '))
    li.append(a*b)
    if len(li) == N:
        if sum(li) == X:
            print("Yes")
            break
        else:
            print("No")
            break