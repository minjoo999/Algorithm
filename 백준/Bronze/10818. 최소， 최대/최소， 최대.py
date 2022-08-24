N = int(input())
a = list(map(int, input().split(' ')))
if len(a) == N:
    print(min(a), max(a))