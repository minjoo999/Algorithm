a = []
numbers = []
for i in range(0, 10):
    num = int(input())
    numbers.append(num)
for n in numbers:
    a.append(n % 42)
a = set(a)
a = list(a)
print(len(a))