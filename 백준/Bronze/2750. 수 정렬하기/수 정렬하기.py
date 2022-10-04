N = int(input())
li = []
for i in range(N):
    a = int(input())
    li.append(a)
li = sorted(li)
for j in range(N):
    print(li[j])