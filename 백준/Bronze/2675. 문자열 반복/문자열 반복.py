T = int(input())
for num in range(0, T):
    R, S = map(str, input().split(' '))
    S2 = list(S)
    for i in S2:
        P= ''.join(i*int(R))
        print(P, end='')
    print()