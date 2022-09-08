A, B = map(int, input().split(' '))
A1 = [A//100, (A % 100)//10, A % 10]
B1 = [B//100, (B % 100)//10, B % 10]
a = A1[2] * 100 + A1[1] * 10 + A1[0]
b = B1[2] * 100 + B1[1] * 10 + B1[0]
if a > b:
    print(a)
else:
    print(b)