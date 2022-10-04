N = input()
li = sorted(N, reverse=True)
li2 = list(map(int, li))
for i in range(len(li2)):
    print(li2[i], end='')