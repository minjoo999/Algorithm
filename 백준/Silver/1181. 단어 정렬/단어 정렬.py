N = int(input())
li = []

for i in range(N):
    a = input()
    li.append(a)

li2 = sorted(li)
li3 = sorted(li2, key=len)
result = []
for j in li3:
    if j not in result:
        result.append(j)

for word in result:
    print(word)
