import sys

input = sys.stdin.readline

N, X = map(int, input().split())

people = list(map(int, input().split()))


def most_visited(li):
    result = []

    r = 0
    for s in range(X):
        r += li[s]
    result.append(r)

    for start in range(1, N):
        end = start + X - 1
        if end >= N:
            break

        else:
            rs = result[-1] - li[start-1] + li[end]
            result.append(rs)

    return result


res = most_visited(people)

ans = max(res)

if ans == 0:
    print("SAD")
else:
    print(ans)
    print(res.count(ans))
