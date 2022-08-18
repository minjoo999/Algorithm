N = int(input())
for i in range(1, N+1):
    if N == 1:
        print("*")
    else:
        print(" "*(N-i), end='')
        print("*"*i)