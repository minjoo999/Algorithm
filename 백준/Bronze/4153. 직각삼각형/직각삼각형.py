while True:
    a, b, c = sorted(map(int, input().split()))
    if (a != 0) & (b != 0) & (c != 0):
        if c**2 == a**2 + b**2:
            print("right")
        else:
            print("wrong")
    else:
        break