from string import ascii_lowercase
S = input()
alpha_list = list(ascii_lowercase)
for i in alpha_list:
    if i in S:
        print(S.find(i), end=' ')
    else:
        print(-1, end=' ')