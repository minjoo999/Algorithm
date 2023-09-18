letters = input().rstrip()

d = 0
max_n = ''
min_n = ''


for l in letters:
    if l == 'M':
        d += 1
    else:
        if d > 0:
            max_n += str((10 ** d) * 5)
            min_n += str((10 ** d) + 5)

        else:
            max_n += '5'
            min_n += '5'
        d = 0

if d > 0:
    min_n += str(10 ** (d - 1))
    max_n += '1'*d

print(max_n)
print(min_n)
