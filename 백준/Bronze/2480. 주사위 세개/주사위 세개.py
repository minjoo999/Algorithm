a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
li = [a, b, c]
li = sorted(li)
if (li[0] == li[1]) & (li[1] == li[2]) & (li[2] == li[0]):
    print(10000 + a * 1000)
elif (li[0] < li[1] < li[2]):
    print(li[2] * 100)
else:
    print(1000 + li[1] * 100)