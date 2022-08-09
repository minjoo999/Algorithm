H, M = input().split(' ')
H = int(H)
M = int(M)
if M >= 45:
    print(H, M-45)
elif (M < 45) & (H != 0):
    print(H-1, 15+M)
else:
    print(23, 15+M)